export function waitForElement(el: string) {
	return new Promise(res => {
		if (document.querySelector(el)) {
			return res(document.querySelector(el));
		}

		const observer = new MutationObserver(_mutations => {
			_mutations;
			if (document.querySelector(el)) {
				res(document.querySelector(el));
				observer.disconnect();
			}
		});

		observer.observe(document.body, {
			childList: true,
			subtree: true
		});
	});
}

export function syncBodyStoreTheme(body: HTMLBodyElement, darkTheme: boolean) {
	body.classList.remove('light', 'dark');
	body.classList.add(darkTheme ? 'dark' : 'light');
}
