FROM python:3.7 AS build-env

ADD . /app
WORKDIR /app

RUN apt-get update
#RUN apt-get install -y build-essential libssl-dev uuid-dev cmake libcurl4-openssl-dev pkg-config python3-dev python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

#FROM gcr.io/distroless/python3
#COPY --from=build-env /app /app
#COPY --from=build-env /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages

WORKDIR /app
ENV PYTHONPATH=/usr/local/lib/python3.7/site-packages

CMD ["/usr/local/bin/python3", "bot.py"]