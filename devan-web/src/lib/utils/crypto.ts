type IDGenerator = (() => string) | null;

let defaultUUIDGenerator: () => string;

if (typeof crypto === 'undefined' || !crypto.randomUUID) {
	defaultUUIDGenerator = function () {
		return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
			const r = (Math.random() * 16) | 0;
			const v = c === 'x' ? r : (r & 0x3) | 0x8;
			return v.toString(16);
		});
	};
} else {
	defaultUUIDGenerator = crypto.randomUUID;
}

export function generateIDs(numIDs: number, generator: IDGenerator = null): string[] {
	const ids: string[] = [];

	// select generator
	if (generator) {
		for (let i = 0; i < numIDs; ++i) {
			ids.push(generator());
		}
	} else {
		for (let i = 0; i < numIDs; ++i) {
			ids.push(defaultUUIDGenerator());
		}
	}

	return ids;
}
