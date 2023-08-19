type ResponseImageProps = devan.image.ResponseImageProps;

export function isResponse(res: unknown): res is ResponseImageProps {
	return res instanceof Object && 'success' in res && 'labels' in res;
}
