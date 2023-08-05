<script lang="ts">
	import Canvas from '$lib/components/Canvas.svelte';
	import { DEVAN_API_URL } from '$lib/contants';
	import type { Image } from '../types';

	let canvas: Canvas;

	async function sendPayload(payload: Image.ImagePayloadProps) {
		try {
			const response = await fetch(DEVAN_API_URL, {
				method: 'POST',
				mode: 'cors',
				headers: {
					'Content-Type': 'application/json',
					Accept: 'application/json'
				},
				body: JSON.stringify(payload)
			});

			const json = await response.json();

			console.log(json);
		} catch (e) {
			console.error('Error on FETCH:', e);
			return null;
		}
	}

	async function handleExport() {
		const bitmapEncoded = await canvas.exportCanvas();

		if (!bitmapEncoded) {
			throw new Error('image could not be encoded (null).');
		}

		const payload: Image.ImagePayloadProps = {
			file: 'image',
			mode: 'gray',
			alpha: true,
			data: bitmapEncoded
		};

		sendPayload(payload);
	}
</script>

<div class="container">
	<div>
		<Canvas bind:this={canvas} dims={{ width: 32, height: 32, size: 13 }} />
		<div class="controls">
			<button type="button" on:click={handleExport}>Export</button>
			<button on:click={() => canvas.clear()}>Clear</button>
		</div>
	</div>
</div>

<style>
	.container {
		display: flex;
		height: 100vh;
		justify-content: center;
		align-items: center;
	}

	.controls {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-top: 2em;
	}

	button {
		width: 45%;
		height: 3em;
		font-size: large;
		border: 2px solid purple;
		background: transparent;
		cursor: pointer;
		transition: 0.5s ease-out;
		box-shadow: 0 0 3px 3px skyblue;
		font-weight: bold;
		color: purple;
	}

	button:hover {
		background-color: cyan;
		box-shadow: 0 0 4px 4px skyblue;
		transition: 0.5s linear;
	}
</style>
