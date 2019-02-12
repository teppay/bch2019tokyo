FROM ubuntu:19.04
ADD default /etc/nginx/sites-enabled/default
RUN /bin/bash -c \
    'apt-get --yes update;\
     apt-get --yes install nginx;\
     apt-get --yes install curl; \
     apt-get --yes install lsof; \
     service nginx start'
EXPOSE 80
CMD ["tail", "-f", "dev/null"]
