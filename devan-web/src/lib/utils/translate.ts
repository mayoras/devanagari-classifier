import { DEVANAGARI_CHARACTERS } from '$lib/constants/character';

export function labelToCharacter(label: string) {
	const char = DEVANAGARI_CHARACTERS.get(label);

	if (char === undefined) {
		return 'undefined character';
	}

	return char;
}
