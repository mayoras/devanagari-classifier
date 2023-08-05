// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}
}

export interface ImagePayloadProps {
	file: string;
	mode: 'gray' | 'rgb';
	alpha?: boolean;
	data: string;
}

export {};
