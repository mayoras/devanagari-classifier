import os

DEVAN_API_PORT = int(os.getenv("DEVAN_API_PORT") or 8888)
DEVAN_API_HOSTNAME = os.getenv("DEVAN_API_HOSTNAME") or "locahost"
DEVAN_PROD_ENV = True if os.getenv("DEVAN_PROD_ENV") == "1" else False