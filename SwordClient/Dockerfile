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

EXPOSE 5000

CMD ["python3", "app.py"]

