type IDGenerator = (() => string) | null;

export function generateIDs(numIDs: number, generator: IDGenerator = null): string[] {
	const ids: string[] = [];

	// select generator
	if (generator) {
		for (let i = 0; i < numIDs; ++i) {
			ids.push(generator());
		}
	} else {
		for (let i = 0; i < numIDs; ++i) {
			ids.push(crypto.randomUUID());
		}
	}

	return ids;
}
