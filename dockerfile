FROM ubuntu:16.04

MAINTAINER Thakur Akash akashthakur.iqbal@gmail.com

RUN apt-get update -y 
RUN apt-get install -y python3 python3-pip 

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3","main.py"]
