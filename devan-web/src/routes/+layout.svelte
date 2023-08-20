<script lang="ts">
	import { onMount } from 'svelte';
	import { darkTheme } from '../stores/theme';
	import { waitForElement } from '$lib/utils/dom';

	onMount(async () => {
		const body = await waitForElement('body');
		if (body) {
			darkTheme.set((body as HTMLBodyElement).classList.contains('dark'));
		}
	});
</script>

<header>
	<div class="container">
		<h1 class="title">Devanagari Character Classifier</h1>
	</div>
</header>

<slot />

<footer><span>By Cesar A. Mayora</span></footer>

<style>
	.container {
		display: flex;
		justify-content: center;
		align-items: center;
		padding: 1em;
	}
	.title {
		margin: 0;
		padding: 0;
		width: auto;
		font-size: 2.5em;
		font-weight: lighter;
	}
	footer {
		display: flex;
		justify-content: end;
	}
	span {
		padding: 1em;
		font-size: larger;
		font-weight: lighter;
		color: var(--gray-text);
	}
</style>
