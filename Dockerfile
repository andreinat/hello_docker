FROM ubuntu:xenial
RUN apt-get update -y
RUN apt-get install -y python3-pip 
COPY . /hello_docker
WORKDIR /hello_docker
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["hello_docker.py"]