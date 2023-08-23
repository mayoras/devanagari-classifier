import { writable } from 'svelte/store';

// how to make a store that changes localStorage:
// https://gist.github.com/JHethDev/7cdd180a941df0168af6e8799c406bd0
function createLocalStorage(key: string, startValue = false) {
	const { subscribe, set, update } = writable(startValue);

	return {
		subscribe,
		set,
		update,
		useLocalStorage: () => {
			const isDark = localStorage.getItem(key);

			if (isDark) {
				set(JSON.parse(isDark));
			}

			subscribe(val => {
				localStorage.setItem(key, JSON.stringify(val));
			});
		}
	};
}

export const darkTheme = createLocalStorage('isDark', false);
