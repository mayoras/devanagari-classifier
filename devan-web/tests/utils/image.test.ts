/* eslint-disable @typescript-eslint/no-non-null-assertion */
import { describe, expect, it, beforeEach, assert, test } from 'vitest';
import { isBlank, toGrayScale } from '$lib/utils/image';
import { getBlankCanvas, getMockDrawnCanvas, getMockRandomCanvas } from '../mocks/canvas';
import { IMG_HEIGHT, IMG_WIDTH } from '$lib/constants/image';

describe('toGrayScale', () => {
	// canvas is a Uint8ClampedArray array of RGBA pixels
	let canvasData: Uint8ClampedArray | null;
	let grayCanvas: Uint8Array;

	beforeEach(async () => {
		// fresh new canvas
		canvasData = await getMockDrawnCanvas();

		assert(canvasData, 'canvas mock is null');

		grayCanvas = toGrayScale(canvasData);
	});

	it('should be a function', () => {
		expect(typeof toGrayScale).toBe('function');
	});

	it('should be a Uint8Array object instance', () => {
		expect(typeof grayCanvas, 'type of returned object to be object').toBe('object');

		expect(grayCanvas instanceof Uint8Array, 'instance of Uint8Array').toBeTruthy();
	});

	test('all elements of returned object are numbers', () => {
		expect(
			grayCanvas.every(num => typeof num === 'number'),
			'are all numbers'
		).toBeTruthy();
	});

	test('pixels are 8-bit scaled', () => {
		expect(
			grayCanvas.every(num => num >= 0 && num <= 255),
			'are byte values'
		).toBeTruthy();
	});

	it('should not be empty', () => {
		expect(grayCanvas, 'not to be null').not.toBeNull();

		expect(grayCanvas.length).not.toEqual(0);
	});

	it(`should have length ${IMG_WIDTH * IMG_HEIGHT}`, () => {
		expect(grayCanvas.length).toEqual(IMG_HEIGHT * IMG_WIDTH);
	});

	it('should have length 0', async () => {
		const zeroCanvas = await getMockRandomCanvas(0 * IMG_WIDTH);

		assert(zeroCanvas, 'canvas mock is null');

		const zeroGrayCanvas = toGrayScale(zeroCanvas);

		expect(zeroGrayCanvas.length, 'canvas length of zero elements is not zero').toEqual(0);
	});
});

describe('isBlank', () => {
	let blankCanvas: Uint8ClampedArray | null;
	let fullyFilledCanvas: Uint8ClampedArray | null;
	let onePixelCanvas: Uint8ClampedArray | null;
	let randomFilledCanvas: Uint8ClampedArray | null;

	beforeEach(async () => {
		blankCanvas = await getBlankCanvas(IMG_HEIGHT * IMG_WIDTH);
		fullyFilledCanvas = await getBlankCanvas(IMG_HEIGHT * IMG_WIDTH);
		onePixelCanvas = await getBlankCanvas(IMG_HEIGHT * IMG_WIDTH);
		randomFilledCanvas = await getMockRandomCanvas(IMG_HEIGHT * IMG_WIDTH);

		assert(blankCanvas);
		assert(fullyFilledCanvas);
		assert(onePixelCanvas);
		assert(randomFilledCanvas);

		// red pixel in corner canvas
		onePixelCanvas[0] = 255;

		// completely gray canvas
		fullyFilledCanvas.fill(180);
	});

	test('zeroed canvas is a blank canvas', () => {
		expect(isBlank(blankCanvas!)).toBeTruthy();
	});

	test('drawn canvas is NOT a blank canvas', () => {
		expect(isBlank(fullyFilledCanvas!), 'fully filled canvas cannot be blank').toBeFalsy();
		expect(isBlank(onePixelCanvas!), 'single-pixel-drawn canvas cannot be blank').toBeFalsy();
		expect(isBlank(randomFilledCanvas!), 'randomly filled canvas cannot be blank').toBeFalsy();
	});
});
/* eslint-enable @typescript-eslint/no-non-null-assertion */
