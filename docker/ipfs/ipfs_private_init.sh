#!/usr/bin/env bash

echo "[*] docker build -t ipfs_private_init ipfs_private_init --no-cache"
docker build -t ipfs_private_init ipfs_private_init --no-cache

echo "[*] docker run -d --name ipfs_private_init -v $PWD/ipfs_dir:/tmp ipfs_private_init"
docker run -d --name ipfs_private_init -v $PWD/ipfs_dir:/tmp ipfs_private_init

echo "[*] docker exec -it ipfs_private_init cp -r /root/.ipfs /tmp/"
docker exec -it ipfs_private_init cp -r /root/.ipfs /tmp/

echo "[*] docker kill ipfs_private_init"
docker kill ipfs_private_init

echo "[*] docker rm ipfs_private_init"
docker rm ipfs_private_init

echo "[*] docker rmi ipfs_private_init"
docker rmi ipfs_private_init