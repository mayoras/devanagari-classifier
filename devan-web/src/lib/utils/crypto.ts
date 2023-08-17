import { randomUUID } from 'crypto';

export function generateIDs(numIDs: number): string[] {
	const ids: string[] = [];

	for (let i = 0; i < numIDs; ++i) {
		ids.push(randomUUID());
	}

	return ids;
}
