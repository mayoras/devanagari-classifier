<script lang="ts">
	import Canvas from '$lib/components/Canvas.svelte';
	import { DEVAN_API_URL } from '$lib/constants/api';
	import { IMG_WIDTH, IMG_HEIGHT, DRAW_POINTER_SIZE } from '$lib/constants/image';
	import {
		DEFAULT_PENCIL_THICKNESS,
		MIN_PENCIL_THICKNESS,
		MAX_PENCIL_THICKNESS
	} from '$lib/constants/canvas';
	import { generateIDs } from '$lib/utils/crypto';

	type PayloadImageProps = devan.image.PayloadImageProps;

	const NUM_THICKNESS_MARKERS = 4;

	let markers = Array.from(
		{ length: NUM_THICKNESS_MARKERS + 1 },
		(_, i) => MIN_PENCIL_THICKNESS + i - 1
	);

	let canvas: Canvas;
	let pencilThickness = DEFAULT_PENCIL_THICKNESS;
	let numCanvases = 1;

	async function sendPayload(payload: PayloadImageProps[]) {
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

		const ids = generateIDs(numCanvases);

		const payload: PayloadImageProps[] = [];
		for (const id of ids) {
			payload.push({
				id,
				file: 'image',
				mode: 'gray',
				alpha: false,
				// WARN: this has to be edited for supporting more canvases.
				// 		 this is an ad-hoc approach
				data: bitmapEncoded
			} satisfies PayloadImageProps);
		}

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
			bind:value={pencilThickness}
			list="markers"
		/>

		<datalist id="markers">
			{#each markers as mark (mark)}
				<option
					value={`${
						mark > 0 ? (mark * MAX_PENCIL_THICKNESS) / NUM_THICKNESS_MARKERS : MIN_PENCIL_THICKNESS
					}`}
				/>
			{/each}
		</datalist>
	</div>
	<div>
		<Canvas
			bind:this={canvas}
			dims={{ width: IMG_WIDTH, height: IMG_HEIGHT, size: DRAW_POINTER_SIZE }}
			thickness={pencilThickness}
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
