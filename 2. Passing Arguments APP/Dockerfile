FROM python:3.6-slim-buster
LABEL maintainer "Gagandeep Singh"
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3","app.py"]