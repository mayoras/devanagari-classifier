<script lang="ts">
	import { onMount } from 'svelte';
	import { exportToImage } from '$lib/utils/image';

	let canvas: HTMLCanvasElement;
	let ctx: CanvasRenderingContext2D | null;
	let isDrawing = false;

	export let dims: devan.component.canvas.Dimensions;

	export function clear() {
		ctx?.clearRect(0, 0, canvas.width, canvas.height);
	}

	export async function exportCanvas() {
		return await exportToImage(canvas);
	}

	onMount(() => {
		// set dimensions
		canvas.width = dims.width * dims.size;
		canvas.height = dims.height * dims.size;

		// get context
		ctx = canvas.getContext('2d');

		if (!ctx) {
			throw new Error('Context 2d is null');
		}

		ctx.fillStyle = 'white';
		ctx.strokeStyle = 'white';
		ctx.lineWidth = dims.size;
	});

	// Canvas Handlers //
	function startDrawing(e: PointerEvent) {
		const { offsetX, offsetY } = e;

		isDrawing = true;
		ctx?.beginPath();
		ctx?.moveTo(offsetX, offsetY);
	}

	function stopDrawing() {
		isDrawing = false;
		ctx?.closePath();
	}

	function draw(e: PointerEvent) {
		const { offsetX, offsetY } = e;

		if (!isDrawing || !ctx) {
			return;
		}

		ctx.lineWidth = 30;

		ctx.lineTo(offsetX, offsetY);
		ctx.stroke();
	}
</script>

<canvas
	bind:this={canvas}
	on:pointerdown={startDrawing}
	on:pointerup={stopDrawing}
	on:pointermove={draw}
/>

<style>
	canvas {
		border-radius: 5px;
		background-color: black;
		box-shadow: 0 0 3px 3px black;
	}
</style>
