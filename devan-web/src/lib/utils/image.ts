import { Buffer } from 'buffer';
import {
	RED_GRAY_PROPORTION,
	GREEN_GRAY_PROPORTION,
	BLUE_GRAY_PROPORTION,
	RGBA_PIXEL_SIZE,
	DRAW_POINTER_SIZE
} from '../constants/image';

/**
 * Exports the drawing contained in the canvas to the corresponding Base64 encoding of the image
 * contained.
 * @param canvas `canvas` HTML element containing the user drawing
 * @returns a Promise for the Base64 encoded image
 */
export async function exportToImage(canvas: HTMLCanvasElement): Promise<string | null> {
	const ctx = canvas.getContext('2d');

	if (!ctx) {
		throw new Error('Context 2d is null');
	}

	// console.log('>>', canvas.width, canvas.height);

	const originalImageData = ctx.getImageData(0, 0, canvas.width, canvas.height);

	if (isBlank(originalImageData.data)) {
		console.warn('canvas is blank. Not exporting');
		return null;
	}

	// convert to gray-scaled image
	const origData = toGrayScale(originalImageData.data);

	// convert to 2D matrix
	const origImage = arrayToMatrix(origData, canvas.width, canvas.height);

	// resize image to 32x32 pixels
	const resizedImage = scaleDownImage(origImage, DRAW_POINTER_SIZE);

	// convert to Uint8Array
	const arr = new Uint8Array(resizedImage.reduce((flat, subArray) => flat.concat(subArray), []));

	// return encoded array data
	return Buffer.from(arr.toString(), 'binary').toString('base64');
}

/**
 * Scale down a given source gray-scaled image by a scaling factor.
 * @param srcImage Gray-scaled image to be scaled down
 * @param factor Scaling factor
 * @returns The scaled down image
 */
export function scaleDownImage(srcImage: number[][], factor: number): number[][] {
	if (!Number.isInteger(factor)) {
		throw new Error('factor should be positive integer');
	}
	if (factor <= 0) {
		throw new Error('factor should be greater than 0');
	}

	const numRows = srcImage.length;
	const numCols = srcImage[0].length;

	const dstImage: number[][] = [];

	let value: number;
	for (let iSrc = 0, iDst = 0; iSrc < numRows; iSrc += factor, ++iDst) {
		dstImage.push([]);
		for (let jSrc = 0, jDst = 0; jSrc < numCols; jSrc += factor, ++jDst) {
			value = Math.round(mean(srcImage, iSrc, jSrc, factor, factor));
			dstImage[iDst][jDst] = value;
		}
	}

	return dstImage;
}

/**
 * Changes the mode of a canvas DOM element from RGBA to Gray-Scale.
 * @param data byte array containing the RGBA pixel values from a canvas
 * @returns byte array containing the gray (8-bit) pixel values from canvas
 */
export function toGrayScale(data: Uint8ClampedArray): Uint8Array {
	const grayScaled = new Uint8Array(data.length / RGBA_PIXEL_SIZE);

	for (let i = 0; i < data.length; i += RGBA_PIXEL_SIZE) {
		const red = data[i];
		const green = data[i + 1];
		const blue = data[i + 2];

		const grayValue = Math.round(
			red * RED_GRAY_PROPORTION + green * GREEN_GRAY_PROPORTION + blue * BLUE_GRAY_PROPORTION
		);

		if (grayValue > 255 || grayValue < 0) throw new Error('Uint8 Overflow');

		grayScaled[i / RGBA_PIXEL_SIZE] = grayValue;
	}

	return grayScaled;
}

/**
 * Checks if the image data array of the user `canvas` DOM element is blank.
 * @param data unsigned integer clamped array of RGBA pixel values
 * @returns `true` if array is blank (zeroed array), `false` otherwise
 */
export function isBlank(data: Uint8ClampedArray): boolean {
	for (let i = 0; i < data.length; i += 4) {
		const red = data[i];
		const green = data[i + 1];
		const blue = data[i + 2];

		if (red !== 0 || green !== 0 || blue !== 0) {
			return false;
		}
	}

	return true;
}

function arrayToMatrix(arr: Uint8Array, rows: number, cols: number): number[][] {
	const mat: number[][] = [];

	for (let i = 0; i < rows; ++i) {
		mat.push([]);
		for (let j = 0; j < cols; ++j) {
			mat[i].push(arr[i * cols + j]);
		}
	}

	return mat;
}

function mean(img: number[][], row: number, col: number, height: number, width: number): number {
	let sum = 0;

	for (let i = row; i - row < height; ++i) {
		for (let j = col; j - col < width; ++j) {
			sum += img[i][j];
		}
	}

	return sum / (height * width);
}
