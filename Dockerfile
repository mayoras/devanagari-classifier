FROM python:3.10.12

# default env variables
ENV DEVAN_API_HOSTNAME=0.0.0.0
ENV DEVAN_API_PORT=8080
ENV DEVAN_CORS_ORIGIN=localhost

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy app files
COPY ./devan /app/devan

EXPOSE 8080

CMD uvicorn devan.main:app --proxy-headers --host $DEVAN_API_HOSTNAME --port $DEVAN_API_PORT
