echo -n "[*] docker stop nginx\t: "
docker stop nginx
echo -n "[*] docker stop uwsgi\t: "
docker stop uwsgi

echo -n "[*] docker rm nginx\t: "
docker rm   nginx
echo -n "[*] docker rm uwsgi\t: "
docker rm   uwsgi
