type IDGenerator = (() => string) | null;

export function generateIDs(numIDs: number, generator: IDGenerator = null): string[] {
	const ids: string[] = [];

	// select generator
	const genID = generator ? generator : crypto.randomUUID;

	for (let i = 0; i < numIDs; ++i) {
		ids.push(genID());
	}

	return ids;
}
