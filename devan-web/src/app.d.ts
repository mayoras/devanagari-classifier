// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		namespace Image {
			interface ImagePayloadProps {
				file: string;
				mode: 'gray' | 'rgb';
				alpha?: boolean;
				data: string;
			}
		}

		namespace Component {
			namespace Canvas {
				interface IDimensions {
					width: number;
					height: number;
					size: number;
				}
			}
		}
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}
}

export {};
