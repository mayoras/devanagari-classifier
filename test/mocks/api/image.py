from api.model import ImageBody

DATA_FILENAME = "./test/mocks/api/data.txt"


def get_mock_image_body() -> ImageBody:
    fake_payload = {
        "file": "image",
        "mode": "gray",
        "alpha": False,
    }

    with open(DATA_FILENAME, "r") as file:
        fake_payload["data"] = file.read()

    return ImageBody(**fake_payload)
