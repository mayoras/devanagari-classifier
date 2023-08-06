import * as fs from 'fs';

const DATA_FILENAME = 'tests/mocks/data.txt';

export function getMockDrawnCanvas(): Uint8ClampedArray | null {
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
