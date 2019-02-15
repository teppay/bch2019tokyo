FROM python:3.6

RUN mkdir /var/www
WORKDIR /var/www


RUN pip install Flask
RUN pip install uwsgi


WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
