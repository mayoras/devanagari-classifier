<div class="card">
	<slot />
</div>

<style>
	.card {
		display: flex;
		justify-content: center;

		width: 100%;
		height: 100%;
		background-color: var(--card-bg);
		border-radius: 2.5% 5% 5% 2.5%;

		box-shadow: 0 0 7px 3px var(--box-shadow);
	}
</style>
