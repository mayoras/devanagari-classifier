import { RGBA_PIXEL_SIZE } from '$lib/constants/image';
import * as fs from 'fs';

const DATA_FILENAME = 'tests/mocks/data.txt';

/**
 * Get a predefined mocked canvas drawing. Useful for checking the drawing integrity after potencial preprocessing.
 * @return {Promise<Uint8ClampedArray | null>} a Promise that resolves with an 8-bit array corresponding to the image
 */
export async function getMockDrawnCanvas(): Promise<Uint8ClampedArray | null> {
	let pixels: number[];

	let mockDrawnCanvas: Uint8ClampedArray;

	// read and store data
	try {
		const data: string = fs.readFileSync(DATA_FILENAME, 'utf-8');

		pixels = data.split(',').map(val => Number(val));

		mockDrawnCanvas = new Uint8ClampedArray(pixels);

		return mockDrawnCanvas;
	} catch (err) {
		console.error('error on readFileSync: ', err);
		return null;
	}
}

/**
 * Get a blank canvas for a given number of pixels
 * @param {number} numPixels Number of pixels (4-tuple RGBA element) to be mocked
 * @return {Promise<Uint8ClampedArray | null>} a Promise that resolves with an 8-bit array
 * corresponding to the image that mock the canvas.
 */
export async function getBlankCanvas(numPixels: number): Promise<Uint8ClampedArray | null> {
	return new Uint8ClampedArray(numPixels * RGBA_PIXEL_SIZE).fill(0);
}

/**
 * Get a random drawn canvas for a given number of pixels
 * @param {number} numPixels Number of pixels (4-tuple RGBA element) to be mocked
 * @return {Promise<Uint8ClampedArray | null>} a Promise that resolves with an 8-bit array
 * corresponding to the image that mock the canvas.
 */
export async function getMockRandomCanvas(numPixels: number): Promise<Uint8ClampedArray | null> {
	const pixels: number[] = [];

	// generate random 8-bit pixels
	for (let i = 0; i < numPixels; i += 4) {
		pixels.push(getRandomNumberInRange(0, 255)); // red
		pixels.push(getRandomNumberInRange(0, 255)); // green
		pixels.push(getRandomNumberInRange(0, 255)); // blue
		pixels.push(getRandomNumberInRange(0, 255)); // alpha
	}

	return new Uint8ClampedArray(pixels);
}

/**
 * Generates a random integer within a specified range.
 * @param {number} min - The minimum value of the range (inclusive).
 * @param {number} max - The maximum value of the range (inclusive).
 * @returns {number} A random integer within the specified range.
 */
function getRandomNumberInRange(min: number, max: number): number {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
