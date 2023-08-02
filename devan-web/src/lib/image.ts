export async function exportToPNG(canvas: HTMLCanvasElement): Promise<ImageData | null> {
	if (isBlank(canvas)) {
		console.log('WARNING: canvas is blank. Not exporting');
	}

	// create a new bitmap resized to 32x32 resolution
	const bitmap = await createImageBitmap(canvas, { resizeWidth: 32, resizeHeight: 32 });

	// create a new canvas
	const canvas_resized = document.createElement('canvas');
	const ctx_resized = canvas_resized.getContext('2d');

	if (!ctx_resized) {
		throw new Error('Context 2d is null');
	}

	canvas_resized.width = bitmap.width;
	canvas_resized.height = bitmap.height;

	// paste bitmap to the new canvas
	ctx_resized.drawImage(bitmap, 0, 0);

	// get the new ImageData object from the new canvas
	const imageData = ctx_resized.getImageData(0, 0, canvas_resized.width, canvas_resized.height);

	return imageData;
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
