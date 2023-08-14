import os

DEVAN_API_HOSTNAME = os.getenv("DEVAN_API_HOSTNAME") or "localhost"
DEVAN_API_PORT = int(os.getenv("DEVAN_API_PORT") or 8080)
DEVAN_PROD_ENV = True if os.getenv("DEVAN_PROD_ENV") == "1" else False
