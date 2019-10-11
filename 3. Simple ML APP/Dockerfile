FROM ubuntu:latest
RUN apt update -y
RUN apt install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]