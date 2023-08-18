<script lang="ts">
	export let numMarkers = 3;
	export let minValue: number;
	export let maxValue: number;
	export let slideValue: number;

	let markers = Array.from({ length: numMarkers }, (_, i) => minValue + i - 1);
</script>

<input type="range" min={minValue} max={maxValue} bind:value={slideValue} list="markers" />

<datalist id="markers">
	{#each markers as mark (mark)}
		<option value={`${mark > 0 ? (mark * maxValue) / (numMarkers - 1) : minValue}`} />
	{/each}
</datalist>

<style>
	input {
		width: 100%;
		height: 100%;
	}
</style>
