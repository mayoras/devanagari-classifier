<script lang="ts">
	import Canvas from '$lib/components/Canvas.svelte';

	let canvas: Canvas;
</script>

<div class="container">
	<div>
		<Canvas bind:this={canvas} dims={{ width: 32, height: 32, size: 13 }} />
		<div class="controls">
			<button
				type="button"
				on:click={async () => {
					const bitmap = await canvas.exportCanvas();
					console.log(bitmap);
				}}>Export</button
			>
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
	}

	button:hover {
		background-color: aqua;
		box-shadow: 0 0 5px 2px skyblue;
		transition: 0.5s ease;
	}
</style>
