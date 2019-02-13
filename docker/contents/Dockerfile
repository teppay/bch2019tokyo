FROM ubuntu

RUN apt update
RUN apt install -y python3-pip python3-dev libfuzzy-dev vim
RUN pip3 install flask ssdeep requests

VOLUME ["/root/workdir"]