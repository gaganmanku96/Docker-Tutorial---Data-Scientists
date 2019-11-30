# Docker Examples for just starters

### What is a docker and why to use it?
#### Docker makes machine learning model deployment easy. For example- while building your model you setup production environment on your local system with all the dependencies. Now, you have to replace exact same steps on server and consider there are 4 servers. It will become a tedious task to replace and there also changes that might screw a step. With DOCKER you can create a Dockerfile which will be do all our tasks on as much machines as we want.

## Medium Article [link](https://towardsdatascience.com/docker-made-easy-for-data-scientists-b32efbc23165)

### So, let's get started.

### 1. Simple Flask APP
This is very simple app which prints 'hello world' on browser screen.
Let's also understand each line of Dockerfile one by one.
```
FROM ubuntu:latest
```
So, we are downloading the latest image from the DockerHub (where you find multiple images). You could also download python3 direct but to keep things simple i've choosen ubuntu. You can also specify the extact version of the image you want to download.

```
RUN apt update -y
```
Now, this command will be familiar to you if you are on linux based OS. It basically updates all the packages and pulls latest version info of them. Flag -y makes sure it doesn't ask for yes to start updating.

```
RUN apt install -y python3-pip
```
This command installs python3-pip. After that you could easily install any python package. If you want to install python 2 try python-pip.

```
COPY . /app
```
Now, we are copying all files from the same directory to /app(this will be created inside the docker container that will run). It's syntax is COPY src dst.

```
WORKDIR /app
```
This command sets the working directory inside the docker container. For our case it will be app since all our files are copied inside it.

```
RUN pip3 install -r requirements.txt
```
Now, since we are inside the app dir in Docker container we can install packages. The requirement file is already present here because we copied it.

```
CMD ["python3","app.py"]
```
The file that you want to run

### Now, you may wanna know the difference between RUN, ENTRYPOINT and CMD. Since, this is the first tutorial, let's try to keep things simple and discuss their difference after some time.

#### To build docker image, type
```
$ docker build -t simpleflask .
```
##### Make sure your Dockerfile is in the same directory.

#### To run the docker image, type
```
$ docker run -d -p 5000:5000 simpleflask
```

#### Calling API
TO check if your docker container is running or not. Type
```
$ docker ps -a
```
You'll see a docker container there.
You can also see it by opening localhost:5000 in web browser


### Few best practices for creating Dockerfile
1. The part or lines that will be least updated should be placed at Top and the lines which will be modified most should be placed at the bottom. Why? Everytime you make an update to Dockerfile, all the lines after that will run again.
2. After any change you'll have to build the Dockerfile again and delete the old one.
3. In case when there are more frequent operations then do all compulsory step in one image and then use it as base image to reduce overall container size and build time.