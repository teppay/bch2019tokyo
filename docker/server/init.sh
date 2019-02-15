#!/usr/bin/env bash

docker-compose build
docker-compose up -t
docker exec -it ubuntu-server nginx
