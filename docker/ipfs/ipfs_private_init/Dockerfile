FROM golang:1.11-stretch

ENV PATH=$PATH:/usr/local/go/bin
ENV PATH=$PATH:$GOPATH/bin

RUN go get -u -d github.com/ipfs/go-ipfs

WORKDIR $GOPATH/src/github.com/ipfs/go-ipfs
RUN make install

# Swarm TCP; should be exposed to the public
EXPOSE 4001
# Daemon API; must not be exposed publicly but to client services under you control
EXPOSE 5001
# Web Gateway; can be exposed publicly with a proxy, e.g. as https://ipfs.example.org
EXPOSE 8080
# Swarm Websockets; must be exposed publicly when the node is listening using the websocket transport (/ipX/.../tcp/8081/ws).
EXPOSE 8081

RUN ipfs init
RUN ipfs bootstrap rm --all

ENTRYPOINT [ "ipfs", "daemon" ]

VOLUME ["/tmp"]