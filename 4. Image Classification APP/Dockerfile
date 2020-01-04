FROM python:3.6-slim-buster
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python3 train.py
CMD ["python3","app.py"]