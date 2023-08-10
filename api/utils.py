import base64


def binary_to_string(bin: bytes) -> str:
    return bin.decode("utf-8")


def decode_image(enc: str) -> str:
    return binary_to_string(base64.b64decode(enc))
