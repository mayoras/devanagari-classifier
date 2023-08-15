import unittest
import numpy as np

from devan.pipeline import (
    Pipeline,
    TransformList,
    TestInputNotDefined,
    PipelineInputNotDefined,
    PipelineModelNotDefined,
)
from devan.preproc import min_max_scaling, get_hog_desc
from devan.character import Character
from devan.constants.image import NORM_IMG_WIDTH

from test.mocks.character import get_blank_char_mock, get_ra_example, get_random_chars
from test.mocks.model import MockMLPClassifier


def fill_main_diagonal(arr: np.ndarray, val: int) -> np.ndarray:
    # for each char array
    for i, c in enumerate(arr):
        # convert c in matrix
        n = int(np.sqrt(c.size))
        mat = c.reshape((n, n))

        # fill diagonal
        np.fill_diagonal(mat, val)
        arr[i] = mat.flatten()

    return arr


def fill_anti_diagonal(arr: np.ndarray, val: int) -> np.ndarray:
    # for each char array
    for i, c in enumerate(arr):
        # convert c in matrix
        n = int(np.sqrt(c.size))
        mat = c.reshape((n, n))

        # fill diagonal
        np.fill_diagonal(np.fliplr(mat), val)
        arr[i] = mat.flatten()

    return arr


class TestPipeline(unittest.TestCase):
    def test_char_transform(self):
        # simple blank 5x5 character
        N = 5
        mock_char = get_blank_char_mock(n=N)

        pipeline = Pipeline(chars=[mock_char])

        # add transforms
        pipeline.add_multi_transform(
            [
                (fill_main_diagonal, {"val": 1}),
                (fill_anti_diagonal, {"val": 2}),
            ]
        )

        # apply transforms
        transformed_chars = pipeline.transform()
        char_trans = transformed_chars[0].reshape(N, N)

        # check main diagonal
        self.assertListEqual(np.diag(char_trans).tolist(), [1, 1, 2, 1, 1])

        # check anti diagonal
        self.assertListEqual(np.diag(np.fliplr(char_trans)).tolist(), [2] * N)

        empty_char_pipeline = Pipeline(chars=[])
        empty_char_pipeline.add_multi_transform(
            [
                (fill_main_diagonal, {"val": 1}),
                (fill_anti_diagonal, {"val": 2}),
            ]
        )

        # check transform no chars
        self.assertRaises(PipelineInputNotDefined, empty_char_pipeline.transform)

    def test_transform_order(self):
        # simple blank 5x5 character
        N = 5
        mock_char = get_blank_char_mock(n=N)

        pipeline = Pipeline(chars=[mock_char])

        # add transforms
        pipeline.add_multi_transform(
            [
                (fill_main_diagonal, {"val": 1}),
                (fill_main_diagonal, {"val": 2}),
            ]
        )

        # apply transforms
        transformed_chars = pipeline.transform()
        char_trans = transformed_chars[0].reshape(N, N)

        # check the second transform was the last applied
        self.assertListEqual(np.diag(char_trans).tolist(), [2] * N)

    def test_single_predict(self):
        # Instance a character
        img, label = get_ra_example()
        char = Character(pil_img=img)

        # Create the Pipeline
        transforms: TransformList = [(min_max_scaling, {}), (get_hog_desc, {})]
        pipeline = Pipeline(
            chars=[char], trans=transforms, model=MockMLPClassifier(labels=[label])
        )

        # Transform input chars
        _X_test = pipeline.transform()

        # Predict the class of that character
        pred = pipeline.predict()

        # check is a function
        self.assertTrue(callable(pipeline.predict))

        # predictions are a list of integers
        self.assertTrue(type(pred) == list)
        self.assertTrue(all(isinstance(n, int) and n >= 0 for n in pred))

        # check label integrity
        self.assertEqual(pred[0], label)

    def test_multiple_predict(self):
        NUM_CHARS = 3
        # get three random characters
        chars = get_random_chars(num_chars=NUM_CHARS, dim=NORM_IMG_WIDTH)
        labels = [1, 2, 3]

        # create pipeline
        pipeline = Pipeline(
            chars=chars, trans=[], model=MockMLPClassifier(labels=labels)
        )

        pipeline.transform()

        # get predictions
        pred = pipeline.predict()

        # check is a function
        self.assertTrue(callable(pipeline.predict))

        # predictions are a list of integers
        self.assertTrue(type(pred) == list)
        self.assertTrue(all(isinstance(n, int) and n >= 0 for n in pred))

        # check labels returned
        self.assertListEqual(pred, labels)

    def test_predict_edgecases(self):
        # empty pipeline
        empty_pipeline = Pipeline(chars=[])

        # non-empty pipeline with no model defined
        img, _label = get_ra_example()
        no_model_pipeline = Pipeline(chars=[Character(pil_img=img)])
        no_model_pipeline.transform()

        # empty pipeline input has undefined test input
        self.assertRaises(TestInputNotDefined, empty_pipeline.predict)

        # pipeline with no model should raise
        self.assertRaises(PipelineModelNotDefined, no_model_pipeline.predict)
