FROM ubuntu:latest
RUN apt update -y &&\
    apt install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt \
    && python3 train.py
CMD ["python3","app.py"]