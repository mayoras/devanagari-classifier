<script lang="ts">
	import { onMount } from 'svelte';
	import type { Component } from '../../types';
	import { drawBlurredRect } from '$lib/draw';
	import { exportToImage } from '$lib/image';

	let canvas: HTMLCanvasElement;
	let ctx: CanvasRenderingContext2D | null;
	let isDrawing = false;

	export let dims: Component.Canvas.IDimensions;

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

		if (!isDrawing) {
			return;
		}

		drawBlurredRect(ctx, offsetX, offsetY, dims.size * 2);
	}
</script>

<div>
	<canvas
		bind:this={canvas}
		on:pointerdown={startDrawing}
		on:pointerup={stopDrawing}
		on:pointermove={draw}
	/>
</div>

<style>
	canvas {
		border-radius: 5px;
		background-color: black;
		box-shadow: 0 0 3px 3px black;
	}

	div {
		display: flex;
		justify-content: center;
		align-items: center;
	}
</style>
