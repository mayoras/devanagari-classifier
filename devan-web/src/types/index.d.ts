declare namespace devan {
	namespace image {
		interface ImagePayloadProps {
			file: string;
			mode: 'gray' | 'rgb';
			alpha?: boolean;
			data: string;
		}
	}
	namespace component {
		namespace canvas {
			interface IDimensions {
				width: number;
				height: number;
				size: number;
			}
		}
	}
}
