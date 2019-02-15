FROM ubuntu:18.04
ADD default /etc/nginx/sites-enabled/default
ADD initialize.sh /
RUN /bin/bash -c \
    'apt-get --yes update;\
     apt-get --yes install nginx;\
     apt-get --yes install curl; \
     apt-get --yes install lsof; \
     apt-get --yes install vim;  \
     apt-get --yes install python3;\
     apt-get --yes install python3-pip;\
     pip3 install flask'
EXPOSE 80
CMD ["tail", "-f", "dev/null"]
