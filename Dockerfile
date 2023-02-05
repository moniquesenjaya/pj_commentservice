FROM python:3.10-slim

WORKDIR /pj-commentservice

COPY requirements.txt /pj-commentservice/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /pj-commentservice/requirements.txt

COPY . /pj-commentservice/src

WORKDIR /pj-commentservice/src

ARG MONGO_URI="mongodb://host.docker.internal:27017/"
ARG MONGO_DB_NAME="CommentService"
ARG BASE_PATH="/service/comment"
ARG VERSION_1="/v1"
ARG FE_URL="http://localhost:3000"

ENV MONGO_URI=${MONGO_URI}
ENV MONGO_DB_NAME=${MONGO_DB_NAME}
ENV BASE_PATH=${BASE_PATH}
ENV VERSION_1=${VERSION_1}
ENV FE_URL=${FE_URL}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--proxy-headers"]