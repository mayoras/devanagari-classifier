FROM python:3.10.12

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy app files
COPY ./devan /app/devan

EXPOSE 8080

CMD uvicorn devan.main:app --host $DEVAN_API_HOSTNAME --port $DEVAN_API_PORT
