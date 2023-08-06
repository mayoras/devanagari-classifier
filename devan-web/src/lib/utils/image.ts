import { Buffer } from 'buffer';
import {
	IMG_WIDTH,
	IMG_HEIGHT,
	RED_GRAY_PROPORTION,
	GREEN_GRAY_PROPORTION,
	BLUE_GRAY_PROPORTION,
	RGBA_PIXEL_SIZE
} from '../constants/image';

// TODO: fix resize strategy
/**
 * Exports the drawing contained in the canvas to the corresponding Base64 encoding of the image
 * contained.
 * @param canvas `canvas` HTML element containing the user drawing
 * @returns a Promise for the Base64 encoded image
 */
export async function exportToImage(canvas: HTMLCanvasElement): Promise<string | null> {
	if (isBlank(canvas)) {
		console.log('WARNING: canvas is blank. Not exporting');
	}

	// create a new bitmap resized to 32x32 resolution
	const bitmap = await createImageBitmap(canvas, {
		resizeWidth: IMG_WIDTH,
		resizeHeight: IMG_HEIGHT
	});

	// create a new canvas
	const canvasResized = document.createElement('canvas');
	const ctxResized = canvasResized.getContext('2d');

	if (!ctxResized) {
		throw new Error('Context 2d is null');
	}

	canvasResized.width = bitmap.width;
	canvasResized.height = bitmap.height;

	// paste bitmap to the new canvas
	ctxResized.drawImage(bitmap, 0, 0);

	// get the new ImageData object from the new canvas
	const imageData = ctxResized.getImageData(0, 0, canvasResized.width, canvasResized.height);

	const bmp = toGrayScale(imageData.data).toString();

	return Buffer.from(bmp, 'binary').toString('base64');
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
 * Checks if `canvas` DOM element is blank.
 * @param canvas HTML Canvas element
 * @returns `true` if canvas is blank (no drawing by the user), `false` otherwise
 */
export function isBlank(canvas: HTMLCanvasElement): boolean {
	const ctx = canvas.getContext('2d');
	if (!ctx) {
		throw new Error('Context 2d is null');
	}
	const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
	const data = imageData.data;

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
