FROM ubuntu:latest

RUN apt-get update ; apt-get -y install fortune
ADD 1.sh /bin/1.sh

ENTRYPOINT /bin/1.sh
