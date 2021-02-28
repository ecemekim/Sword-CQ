FROM python:3.6

ADD . /app

WORKDIR app

RUN apt-get update && apt-get install -y \
  g++ \
  musl-dev \
  libffi-dev

COPY requirements.txt ./

RUN pip3 install -r requirements.txt \
  && rm requirements.txt

# RUN python -m grpc_tools.protoc --proto_path=. ./sword.proto --python_out=. --grpc_python_out=.

EXPOSE 50051

CMD ["python3", "sword_server.py"]
