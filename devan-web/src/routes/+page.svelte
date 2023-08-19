<script lang="ts">
	import { fade } from 'svelte/transition';
	import Canvas from '$lib/components/Canvas.svelte';
	import Slider from '$lib/components/Slider.svelte';
	import Button from '$lib/components/Button.svelte';
	import { DEVAN_API_URL } from '$lib/constants/api';
	import { IMG_WIDTH, IMG_HEIGHT, DRAW_POINTER_SIZE } from '$lib/constants/image';
	import {
		DEFAULT_PENCIL_THICKNESS,
		MIN_PENCIL_THICKNESS,
		MAX_PENCIL_THICKNESS
	} from '$lib/constants/canvas';
	import { generateIDs } from '$lib/utils/crypto';
	import { isResponse } from '$lib/utils/response';

	type PayloadImageProps = devan.image.PayloadImageProps;

	const NUM_THICKNESS_MARKERS = 3;

	let canvas: Canvas;
	let pencilThickness = DEFAULT_PENCIL_THICKNESS;
	let numCanvases = 1;
	let predicted = false;
	let currentID: string;
	let promise: Promise<string>;

	async function handleResponse(res: Response) {
		const json: unknown = await res.json();

		if (!isResponse(json)) {
			throw new Error(`${json} does not satisfies Response interface.`);
		}

		if (!json.success) {
			throw new Error('Request was not accepted by the server.');
		}

		if (json.labels.length > 1) {
			console.warn(
				'Multiple character prediction is not supported yet.\nJust showing the current character'
			);
		}

		let pred = json.labels.find(el => el.id === currentID);

		if (pred === undefined) {
			throw new Error('current image ID does not match any response ID.');
		}

		return pred.label;
	}

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

			predicted = true;

			promise = handleResponse(response);
		} catch (e) {
			console.error('Error on FETCH:', e);
			return null;
		}
	}

	async function handleExport() {
		const bitmapEncoded = await canvas.exportCanvas();

		if (bitmapEncoded === null) {
			throw new Error('image could not be encoded (null).');
		}

		if (bitmapEncoded === '') {
			return;
		}

		const ids = generateIDs(numCanvases);

		currentID = ids[0];

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

<main class="main-container">
	<div class="canvas-container">
		<div>
			<div>
				<div class="pencil-ctls">
					<div class="thk-icons">
						<img src="/svg/Thin.svg" alt="Thin pencil" />
						<img src="/svg/Medium.svg" alt="Medium pencil" />
						<img src="/svg/Bold.svg" alt="Bold pencil" />
					</div>

					<Slider
						bind:value={pencilThickness}
						min={MIN_PENCIL_THICKNESS}
						max={MAX_PENCIL_THICKNESS}
						numMarkers={NUM_THICKNESS_MARKERS}
					/>
				</div>
				<Canvas
					bind:this={canvas}
					dims={{ width: IMG_WIDTH, height: IMG_HEIGHT, size: DRAW_POINTER_SIZE }}
					thickness={pencilThickness}
				/>
			</div>
			<div class="actions">
				<Button type="button" label="Classify" on:click={handleExport} />
				<Button
					type="button"
					label="Clear"
					on:click={() => {
						predicted = false;
						canvas.clear();
					}}
				/>
			</div>
		</div>
	</div>

	<div
		class="pred-container"
		style="width: {IMG_WIDTH * DRAW_POINTER_SIZE}px; height: {IMG_HEIGHT * DRAW_POINTER_SIZE}px;"
	>
		<div class="card">
			<div class="card-content">
				{#if predicted}
					{#await promise}
						<strong>Resolving...</strong>
					{:then label}
						<h2 class="pred-title">Your character is:</h2>
						<img src="" alt="" transition:fade={{ duration: 1000 }} />
						<strong class="pred-character-name"><i>"{label}"</i></strong>
					{:catch error}
						<p style="color: red">Error on server response: {error.message}</p>
					{/await}
				{:else}
					<h2 class="pred-title">You have not made a character prediction.</h2>
					<img src="/svg/Brain.svg" alt="Gray Brain Icon" />
					<span class="pred-no-character"
						>Draw a character and click <code>Predict</code> to show prediction.</span
					>
				{/if}
			</div>
		</div>
	</div>
</main>

<style>
	.pred-container {
		margin-top: 1em;
		z-index: -1;
	}

	.card {
		display: flex;
		justify-content: center;

		width: 100%;
		height: 100%;
		background-color: white;
		border-radius: 2.5% 5% 5% 2.5%;

		box-shadow: 0 0 7px 3px teal;
	}

	.card-content {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		text-align: center;

		color: gray;
		font-weight: 500;
	}

	.pred-title {
		font-size: larger;
		font-weight: bolder;
		margin-bottom: 15px;
	}

	.card-content > img {
		width: 150px;
		height: 150px;
		padding: 2em;
	}

	.main-container {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.canvas-container {
		display: flex;
		height: 90vh;
		justify-content: center;
		align-items: center;
	}

	.actions {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-top: 2em;
	}

	.pencil-ctls {
		display: flex;
		flex-direction: column;
		padding: 1em;
	}

	.thk-icons {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.thk-icons > img {
		width: 2rem;
		height: 3rem;
	}

	.pred-character-name {
		font-size: larger;
		font-weight: bolder;
		margin-top: 1em;
	}
</style>
