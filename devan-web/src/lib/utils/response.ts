type ResponseImageProps = {
	success: boolean;
	labels: [
		{
			id: string;
			label: string;
		}
	];
};

export function isResponse(res: unknown): res is ResponseImageProps {
	return res instanceof Object && 'success' in res && 'labels' in res;
}
