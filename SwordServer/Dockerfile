FROM python:3-alpine as base

FROM base as builder

ADD . /app

WORKDIR app

RUN apk add --update \
    gcc \
    g++ \
    make \
    musl-dev \
    python3-dev \
    libc6-compat \
    && rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt

# RUN python -m grpc_tools.protoc --proto_path=. ./sword.proto --python_out=. --grpc_python_out=.

ADD entrypoint.sh /usr/local/bin/

RUN ["chmod", "+x", "/usr/local/bin/entrypoint.sh"]

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

EXPOSE 50051

CMD ["python3", "sword_server.py"]