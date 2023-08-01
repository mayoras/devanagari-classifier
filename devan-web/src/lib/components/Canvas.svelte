<script lang="ts">
	import { onMount } from 'svelte';
	import type { CANVAS_RESOLUTION_PROPS } from './types';

	export let resolution: CANVAS_RESOLUTION_PROPS = {
		width: 32,
		height: 32
	};

	let canvas: HTMLCanvasElement;
	let ctx: CanvasRenderingContext2D | null;

	let drawing = false;

	onMount(() => {
		// set resolution
		canvas.width = resolution.width;
		canvas.height = resolution.height;

		// get context
		ctx = canvas.getContext('2d');

		if (!ctx) {
			throw new Error('Context 2d is null');
		}
	});

	// Canvas Handlers //
	function startDrawing() {
		drawing = true;
		console.log('started drawing...');
	}

	function stopDrawing() {
		drawing = false;
		console.log('stopped drawing...');
	}

	function draw() {
		if (drawing) console.log('drawing...');
	}
</script>

<canvas
	bind:this={canvas}
	on:pointerdown={startDrawing}
	on:pointerup={stopDrawing}
	on:pointermove={draw}
	class="canvas"
/>

<style>
	.canvas {
		/* width: 30em;
		height: 30em; */
		border-radius: 5px;
		background-color: black;
	}
</style>
