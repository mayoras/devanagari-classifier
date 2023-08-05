import { Buffer } from 'buffer';
import {
	IMG_WIDTH,
	IMG_HEIGHT,
	RED_GRAY_PROPORTION,
	GREEN_GRAY_PROPORTION,
	BLUE_GRAY_PROPORTION
} from './constants';

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

function toGrayScale(data: Uint8ClampedArray): Uint8Array {
	const grayScaled = new Uint8Array(IMG_WIDTH * IMG_HEIGHT);

	for (let i = 0; i < data.length; i += 4) {
		const red = data[i];
		const green = data[i + 1];
		const blue = data[i + 2];

		const grayValue =
			(red * RED_GRAY_PROPORTION + green * GREEN_GRAY_PROPORTION + blue * BLUE_GRAY_PROPORTION) *
			(255 / (RED_GRAY_PROPORTION + GREEN_GRAY_PROPORTION + BLUE_GRAY_PROPORTION));

		grayScaled[i / 4] = grayValue;
	}

	return grayScaled;
}

function isBlank(canvas: HTMLCanvasElement): boolean {
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
