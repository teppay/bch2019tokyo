FROM ethereum/client-go:v1.8.12

RUN apk add --update bash

COPY ./genesis.json /root/.ethereum/

RUN geth --datadir /root/.ethereum init /root/.ethereum/genesis.json

VOLUME ["/root/.ethereum"]

EXPOSE 8545
EXPOSE 8546
EXPOSE 30303