ethereum - Docker
---

## 環境のビルド
```
$ sudo su
# ./geth_init.sh
# docker-compose build --no-cache
```

## geth起動
```
# docker-compose up -d
```

## geth停止&削除
```
# docker-compose down
```

## ログの表示
```
# docker logs -f geth
```

## geth consoleへのアクセス
```
# docker exec -it geth geth /root/.ethereum/geth.ipc
```

## 環境の初期化
```
$ sudo rm ./geth/.ethereum
```


※ $ <- normal user
※ # <- super user