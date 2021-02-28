FROM python:3.6

ADD . /app

WORKDIR app

RUN apt-get update && apt-get install -y \
  g++ \
  musl-dev \
  libffi-dev \
  curl

COPY requirements.txt ./

RUN pip3 install -r requirements.txt \
  && rm requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "--log-level", "DEBUG", "app:app"]

