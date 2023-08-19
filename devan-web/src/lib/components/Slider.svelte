<script lang="ts">
	import { DEFAULT_PENCIL_THICKNESS } from '$lib/constants/canvas';

	export let numMarkers = 3;
	export let min: number;
	export let max: number;
	export let value = DEFAULT_PENCIL_THICKNESS;

	let markers = Array.from({ length: numMarkers }, (_, i) => min + i - 1);
</script>

<input type="range" {min} {max} bind:value list="markers" />

<datalist id="markers">
	{#each markers as mark (mark)}
		<option value={`${mark > 0 ? (mark * max) / (numMarkers - 1) : min}`} />
	{/each}
</datalist>

<style>
	input {
		width: 100%;
		height: 100%;
	}
</style>
