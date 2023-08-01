<script lang="ts">
	import Canvas from '$lib/components/Canvas.svelte';

	let canvas: Canvas;
</script>

<div class="container">
	<div>
		<Canvas bind:this={canvas} dims={{ width: 32, height: 32, size: 13 }} />
		<button on:click={() => canvas.clear()}>Clear</button>
	</div>
</div>

<style>
	.container {
		display: flex;
		height: 100vh;
		justify-content: center;
		align-items: center;
	}

	button {
		margin-top: 2em;
		width: 100%;
		height: 3em;
		font-size: large;
		border: 2px solid purple;
		background: transparent;
		cursor: pointer;
		transition: 0.5s ease-out;
	}

	button:hover {
		background-color: aqua;
		box-shadow: 0 0 5px 2px skyblue;
		transition: 0.5s ease;
	}
</style>
