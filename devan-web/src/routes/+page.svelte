<script lang="ts">
	import Canvas from '$lib/components/Canvas.svelte';
</script>

<div class="container">
	<Canvas resolution={{ width: 32, height: 32 }} />
</div>

<style>
	.container {
		display: flex;
		height: 100vh;
		justify-content: center;
		align-items: center;
	}
</style>
