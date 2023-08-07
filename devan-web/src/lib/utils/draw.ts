/**
 * Draws a white rectangle into the canvas with blurred effect.
 * @param ctx rendering 2D context of the canvas containing the drawing
 * @param x canvas X-coordinate of the rectangle to be drawn
 * @param y canvas Y-coordinate of the rectangle to be drawn
 * @param size side length of the rectangle to be drawn
 */
export function drawBlurredRect(
	ctx: CanvasRenderingContext2D | null,
	x: number,
	y: number,
	size: number
): void {
	const numPasses = 3;
	const blurIntensity = 10;

	if (ctx) {
		ctx.globalAlpha = 1 / numPasses;
	}

	for (let i = 0; i < numPasses; ++i) {
		ctx?.fillRect(
			x - blurIntensity / 2,
			y - blurIntensity / 2,
			size + blurIntensity,
			size + blurIntensity
		);
	}
}

export function drawGridSquare(
	ctx: CanvasRenderingContext2D,
	x: number,
	y: number,
	size: number
): void {
	const gridXPosition = Math.floor(x / size);
	const gridYPosition = Math.floor(y / size);

	for (let i = 0; i < 2; ++i) {
		for (let j = 0; j < 2; ++j) {
			ctx.fillRect((gridXPosition + i) * size, (gridYPosition + j) * size, size, size);
		}
	}
}
