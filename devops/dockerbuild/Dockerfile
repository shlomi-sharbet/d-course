### TO PACK THE CODE INTO A DOCKER IMAGE

# Pull the base image - python already installed on ubuntu
FROM python:3.9-slim

#set the working directory in the container
#the container is like a "ubuntu" virtual machine
#WORKDIR - the container will be created AND RUN in /app directory
#mkdir /app && cd /app
WORKDIR /app

#COPY is like cp in linux - from where to where will copy to /app
COPY requirements.txt .

#copy the content of the current directory to the container
# . means to the current directory
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]