/* eslint-disable @typescript-eslint/no-non-null-assertion */
import { describe, expect, it, test } from 'vitest';
import { generateIDs } from '$lib/utils/crypto';

function isUUID(uuid: string): boolean {
	const pattern = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
	return pattern.test(uuid);
}

describe('generatedIDs', () => {
	const NUM_NO_IDS = 0;
	const NUM_FEW_IDS = 5;
	const NUM_MANY_IDS = 50;

	it('should be a function', () => {
		expect(typeof generateIDs).toBe('function');
	});

	it('should return an array of string IDs for each image', () => {
		const ids = generateIDs(NUM_FEW_IDS);

		// is array
		expect(Array.isArray(ids), 'return type is not array').toBeTruthy();

		// there are the correct number of IDs requested
		expect(ids.length, 'incorrect returned array length').toEqual(NUM_FEW_IDS);

		// is array of string
		expect(
			ids.every(id => typeof id === 'string'),
			`not all IDs are of type 'string'`
		).toBeTruthy();
	});

	test('IDs are UUID', () => {
		const ids = generateIDs(NUM_FEW_IDS);

		// are uuids every id generated
		expect(
			ids.every(id => isUUID(id)),
			'not all IDs generated are UUID.'
		).toBeTruthy();
	});

	test('IDs are all unique', () => {
		const idsFew = generateIDs(NUM_FEW_IDS);
		const idsMany = generateIDs(NUM_MANY_IDS);

		// for few IDs
		const uniqueFew = new Set<string>(idsFew);
		expect(uniqueFew.size, 'there are repeated IDs').toEqual(idsFew.length);

		// for many IDs
		const uniqueMany = new Set<string>(idsMany);
		expect(uniqueMany.size, 'there are repeated IDs').toEqual(idsMany.length);
	});

	it('should return empty array if no images are given', () => {
		const noID = generateIDs(NUM_NO_IDS);

		expect(noID, 'returns non-empty array for 0 requested IDs').toHaveLength(0);
	});
});
