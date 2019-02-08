#!/usr/bin/env bash
echo "[*] docker build -t geth_init geth_init"
docker build -t geth_init geth_init
echo "[*] docker run -d --name geth_init -v $PWD/geth:/tmp geth_init"
docker run -d --name geth_init -v $PWD/geth:/tmp geth_init

echo "[*] docker exec -it geth_init rsync -a /root/.ethereum /tmp/"
docker exec -it geth_init rsync -a /root/.ethereum /tmp/

echo "[*] docker kill geth_init"
docker kill geth_init

echo "[*] docker rm geth_init"
docker rm geth_init

echo "[*] docker rmi geth_init"
docker rmi geth_init