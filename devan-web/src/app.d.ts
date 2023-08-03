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
	colortype: 'gray' | 'rgb';
	alpha?: boolean;
	data: string;
}

export {};
