FROM python:3.10.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Set env variables
ENV DEVAN_API_HOSTNAME="0.0.0.0"
ENV DEVAN_API_PORT=80
ENV DEVAN_MODEL_V1_FILENAME="/code/models/Devanagari_model.joblib"

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy app files
COPY ./devan /code/devan

# Copy model file
COPY ./models/Devanagari_model.joblib ${DEVAN_MODEL_V1_FILENAME}

CMD uvicorn devan.main:app --proxy-headers --host "$DEVAN_API_HOSTNAME" --port "$DEVAN_API_PORT"
