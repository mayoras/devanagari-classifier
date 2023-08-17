<script lang="ts">
	import Canvas from '$lib/components/Canvas.svelte';
	import { DEVAN_API_URL } from '$lib/constants/api';
	import { IMG_WIDTH, IMG_HEIGHT, DRAW_POINTER_SIZE } from '$lib/constants/image';
	import {
		DEFAULT_PENCIL_THICKNESS,
		MIN_PENCIL_THICKNESS,
		MAX_PENCIL_THICKNESS
	} from '$lib/constants/canvas';

	type ImagePayloadProps = devan.image.ImagePayloadProps;

	let canvas: Canvas;
	let pencil_thickness = DEFAULT_PENCIL_THICKNESS;

	async function sendPayload(payload: ImagePayloadProps) {
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

		const payload = {
			file: 'image',
			mode: 'gray',
			alpha: false,
			data: bitmapEncoded
		} satisfies ImagePayloadProps;

		sendPayload(payload);
	}
</script>

<div class="container">
	<div class="pencil-ctls">
		<input
			class="thk-ctl"
			type="range"
			min={`${MIN_PENCIL_THICKNESS}`}
			max={`${MAX_PENCIL_THICKNESS}`}
			bind:value={pencil_thickness}
			list="markers"
		/>

		<datalist id="markers">
			<option value={`${MIN_PENCIL_THICKNESS}`} />
			<option value={`${MAX_PENCIL_THICKNESS / 4}`} />
			<option value={`${(2 * MAX_PENCIL_THICKNESS) / 4}`} />
			<option value={`${(3 * MAX_PENCIL_THICKNESS) / 4}`} />
			<option value={`${MAX_PENCIL_THICKNESS}`} />
		</datalist>
	</div>
	<div>
		<Canvas
			bind:this={canvas}
			dims={{ width: IMG_WIDTH, height: IMG_HEIGHT, size: DRAW_POINTER_SIZE }}
			thickness={pencil_thickness}
		/>
		<div class="actions">
			<button type="button" on:click={handleExport}>Classify</button>
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

	.actions {
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
