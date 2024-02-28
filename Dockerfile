# FROM anibali/pytorch:2.0.1-cuda11.8-ubuntu22.04

FROM python:3.9

WORKDIR /app

LABEL maintainer="nguyentn"

COPY ./main.py /app/

COPY ./requirements.txt /app/

COPY ./model_storage /app/model_storage

COPY ./model /app/model

COPY ./preprocess /app/preprocess

COPY ./phobert-base-v2 /app/phobert-base-v2

EXPOSE 30000

RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "30000"]
