FROM python:3.8.7-alpine3.12

ADD . /app

WORKDIR app

RUN apk add --no-cache \
  g++ \
  musl-dev \
  libffi-dev

COPY requirements.txt ./

RUN pip install -r requirements.txt \
  && rm requirements.txt \
  && apk del \
  g++ \
  musl-dev \
  libffi-dev
# RUN python -m grpc_tools.protoc --proto_path=. ./sword.proto --python_out=. --grpc_python_out=.

EXPOSE 50051

CMD ["python3", "sword_server.py"]
