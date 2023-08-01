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
