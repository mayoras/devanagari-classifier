<script lang="ts">
	import type { HTMLButtonAttributes } from 'svelte/elements';

	export let label: string;
	export let type: HTMLButtonAttributes['type'] = 'button';
	export let disabled = false;
</script>

<button {type} {disabled} on:click>{label}</button>

<style>
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
