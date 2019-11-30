FROM ubuntu:latest
LABEL maintainer "Gagandeep Singh"
RUN apt update -y &&\
    apt install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3","app.py"]