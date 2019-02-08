FROM ethereum/client-go:v1.8.12

RUN apk add --update bash
RUN apk add rsync

COPY ./.ethereum /root/.ethereum

RUN geth account import --password /root/.ethereum/passwd /root/.ethereum/privkey
RUN geth --datadir /root/.ethereum init /root/.ethereum/genesis.json

VOLUME [ "/tmp" ]