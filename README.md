# Docker Examples for just starters

### What is a docker and why to use it?
Docker makes machine learning model deployment easy. For example- while building your model you setup production environment on your local system with all the dependencies. Now, you have to replace exact same steps on server and consider there are 4 servers. It will become a tedious task to replace and there also changes that might screw a step. With DOCKER you can create a Dockerfile which will be do all our tasks on as much machines as we want.

## Medium Article [link](https://towardsdatascience.com/docker-made-easy-for-data-scientists-b32efbc23165)

### How to write Dockerfile
#### Elements
1. FROM
```
The image that you want to use. This is the base image. Example- ubuntu, redis, nginx.
You can also specify the version that you want to pull.
Example FROM ubuntu:18.04
```
2. COPY
```
All the files that are required to run the project need to be copied inside docker container.
Copy each file or individually or use '.' to copy all files to app direcotry inside container( COPY . /app). Use dockerignore file to remove redundant files.
Example COPY . /app
```
3. WORKDIR
```
This command is used to set the working directory. After you have copied the files inside container. Set that directory as working directory.
Example WORKDIR /app
```
4. RUN
```
Any step that is required before running the main file is done here. Example- running apt update, installing a particular package, etc.
Example RUN apt update & apt install redis

```
```
Each run statement creates a new layer. The goal is to minimise number of layers. Hence, try to merge all RUN statements into one.
```
5. CMD
```
Enter the command here that you want to execute as soon as the docker build process completes.
There can be only one CMD.
Example CMD ["python", "app.py"]
```
### Example Dockerfile
```
FROM ubuntu:latest
RUN apt update &&\
  apt install python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python", "app.py"]
```

### NOTE
The commands should be in order of least updating to most updating. Why? Everytime you make a change a new docker image will be build.
Cache files will be used for the commands that remain unchanged.

### To build docker image, type
```
$ docker build -t simpleflask .
```
or
```
$ docker build .
```
##### Make sure your Dockerfile is in the same directory.

### To view the build docker image
```
$ docker images
```

#### To run the docker image, type
```
$ docker run -d -p 5000:5000 simpleflask
```
##### -d means running in deamon mode (background) or detached mode.
##### -p means the port

#### To check if docker container is running
```
$ docker ps
```
You'll see a docker container there.

#### To start or stop container
```
$ docker start/stop continaer_name or id
```

#### Calling flask API inside Docker container
1. To pass data inside it
```
import requests
import json

data = {'f1': 5,
        'f2': 3,
        'f3': 4}
URL = 'http://127.0.0.1:5000/predict'

output = requests.post(URL, json.dumps(data))

print(f"Status = {output.status}\nResult = {output.text}")
```
Just convert the data into JSON form and send a POST request

### Few best practices for creating Dockerfile
1. The part or lines that will be least updated should be placed at Top and the lines which will be modified most should be placed at the bottom. Why? Everytime you make an update to Dockerfile, all the lines after that will run again.
2. After any change you'll have to build the Dockerfile again and delete the old one.
3. In case when there are more frequent operations then do all compulsory step in one image and then use it as base image to reduce overall container size and build time.
