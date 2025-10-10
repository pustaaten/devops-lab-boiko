University: [ITMO University](https://itmo.ru/ru/)

Faculty: [FICT](https://fict.itmo.ru)

Course: [Введение в веб технологии](https://itmo-ict-faculty.github.io/introduction-in-web-tech/)

Year: 2025/2026

Author: Boyko Ekaterina Olegovna

Lab: Lab0

Date of create: 08.10.2025

Date of finished: 10.10.2025

---

## Отчет

1. Установила Docker Desktop AMD 64 с сайта https://www.docker.com/products/docker-desktop/

2. С помощью Windows PowerShell проверила установку докера командой "PS C:\Users\Boyko> docker --version
Docker version 28.4.0, build d8eb465"

3. Запустила тестовый контейнер С помощью Windows PowerShell 
PS C:\Users\Boyko> docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete
Digest: sha256:54e66cc1dd1fcb1c3c58bd8017914dbed8701e2d8c74d9262e26bd9cc1642d31
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
 <img width="1311" height="688" alt="image" src="https://github.com/user-attachments/assets/f3544816-18b0-426d-92a0-647fa10ee908" />

4. Зашла в созданный контейнер в приложении docker.desktop, появился контейнер hopeful_pasteur - перешла в раздел Exec, но не смогла написать команду 
<img width="1536" height="184" alt="image" src="https://github.com/user-attachments/assets/f7c1e2ca-89a2-4c09-940e-a1715e064ba7" />



Изучила базовые команды: 

5. 
PS C:\Users\Boyko> docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    54e66cc1dd1f   2 months ago   20.3kB

6. 
PS C:\Users\Boyko> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

6. 
PS C:\Users\Boyko> docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                          PORTS     NAMES
0c4d283ef5ba   hello-world   "/hello"   6 minutes ago   Exited (0) About a minute ago             hopeful_pasteur

<img width="1404" height="195" alt="image" src="https://github.com/user-attachments/assets/bc481576-ab6e-47ed-b356-488e6e12a156" />


Работа с готовыми образами


7. Скачала образ Ubunt
PS C:\Users\Boyko> docker pull ubuntu:latest
latest: Pulling from library/ubuntu
a1a21c96bc16: Pull complete
Digest: sha256:728785b59223d755e3e5c5af178fab1be7031f3522c5ccd7a0b32b80d8248123
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest

8. Установила докер образ 
PS C:\Users\Boyko> docker run -it ubuntu bash
root@f0ccd0bb0963:/# apt update && apt install -y curl

<img width="904" height="187" alt="image" src="https://github.com/user-attachments/assets/1ec1c4c1-250d-4d95-b1ad-1333e626719d" />

9. Проверила установку curl
root@ce5628550dfd:/# curl --version
curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.7
Release-Date: 2023-12-06, security patched: 8.5.0-2ubuntu10.6
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd

10. Посмотрела файлы командой ls и закыла контейнер 
root@f0ccd0bb0963:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@f0ccd0bb0963:/# exit
exit

<img width="1292" height="144" alt="image" src="https://github.com/user-attachments/assets/860b6524-1adc-4f72-8f3a-b56e53f195bb" />


Запуск веб-сервера:


11. Запустила контейнер с nginx: 
PS C:\Users\Boyko> docker run -d -p 8080:80 --name web-server nginx:alpine
Unable to find image 'nginx:alpine' locally
alpine: Pulling from library/nginx
e2d0ea5d3690: Pull complete
76c9bcaa4163: Pull complete
03e63548f209: Pull complete
621a51978ed7: Pull complete
83ce83cd9960: Pull complete
7fb80c2f28bc: Pull complete
2d35ebdb57d9: Pull complete
f80aba050ead: Pull complete
Digest: sha256:7c1b9a91514d1eb5288d7cd6e91d9f451707911bfaea9307a3acbc811d4aa82e
Status: Downloaded newer image for nginx:alpine

13. Зашла по ссылке в браузере http://localhost:8080/
Вылезло окно "Welcome to nginx!
If you see this page, the nginx web server is successfully installed and working. Further configuration is required.

For online documentation and support please refer to nginx.org.
Commercial support is available at nginx.com.

Thank you for using nginx."

13. Посмотрела логи: 
"172.17.0.1 - - [10/Oct/2025:13:30:06 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 YaBrowser/25.8.0.0 Safari/537.36" "-"
172.17.0.1 - - [10/Oct/2025:13:30:06 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8080/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 YaBrowser/25.8.0.0 Safari/537.36" "-"
2025/10/10 13:30:06 [error] 32#32: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"

14. Подключилась к контейнеру, увидела, что у меня лежит на веб-сервере 
PS C:\Users\Boyko> docker exec -it web-server sh
/ # ls
bin                   etc                   mnt                   run                   tmp
dev                   home                  opt                   sbin                  usr
docker-entrypoint.d   lib                   proc                  srv                   var
docker-entrypoint.sh  media                 root                  sys

<img width="1133" height="349" alt="image" src="https://github.com/user-attachments/assets/fc8e7e13-23ac-489e-a854-830e43554edb" />


Управление контейнерами:

15. Посмотрела какие у меня есть контейнеры: 
PS C:\Users\Boyko> docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                         PORTS                                     NAMES
87197e1d5160   nginx:alpine   "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes                  0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-server
ce5628550dfd   ubuntu         "bash"                   15 minutes ago   Exited (0) 12 minutes ago                                                stupefied_gates
f0ccd0bb0963   ubuntu         "bash"                   18 hours ago     Exited (0) 53 minutes ago                                                happy_hellman
0c4d283ef5ba   hello-world    "/hello"                 18 hours ago     Exited (0) About an hour ago                                             hopeful_pasteur

16. Останавливаю веб-сервер: 
PS C:\Users\Boyko> docker stop web-server
web-server

17. Запустила остановленный сервер: 
PS C:\Users\Boyko> docker start web-server
web-server

18. Попыталась удалить контейнер, но не смогла тк он запущен 
PS C:\Users\Boyko> docker rm web-server
Error response from daemon: cannot remove container "web-server": container is running: stop the container before removing or force remove
Остановила контейнер и удалила
PS C:\Users\Boyko> docker rm web-server
web-server

19. Удалила образ
PS C:\Users\Boyko> docker rmi nginx:alpine
Untagged: nginx:alpine
Deleted: sha256:7c1b9a91514d1eb5288d7cd6e91d9f451707911bfaea9307a3acbc811d4aa82e
<img width="1915" height="512" alt="image" src="https://github.com/user-attachments/assets/ad2288bd-acb3-4b05-8006-1ea9da67bdc5" />



Работа с томами (volumes):


20. Создала том
PS C:\Users\Boyko> docker volume create my-volume
my-volume

21. Запустила контейнер с томом: 
PS C:\Users\Boyko> docker run -it --name volume-test -d -v my-volume:/data ubuntu bash
1e6066d3588ae271d44c8382d6a16b6a1bace89238f7790043c4ce35dae88bcb

22. Остановила контейнер и удалила его: 
PS C:\Users\Boyko> docker stop volume-test
volume-test
PS C:\Users\Boyko> docker rm volume-test
volume-test

<img width="1683" height="365" alt="image" src="https://github.com/user-attachments/assets/82001397-7233-4b68-aca1-38f3b583d4f2" />


24. Создала контейнер develop-test с тем же томом 
PS C:\Users\Boyko> docker run -it --name develop-test -d -v my-volume:/data ubuntu bash
194c77aaa68f1d129a35a3fcbbabff76ac2be1cb7fbde11cffa61929efc37056

<img width="1248" height="45" alt="image" src="https://github.com/user-attachments/assets/a09b5bcf-0f4c-4a6f-8e94-435ffa993173" />

26. Посмотрела, что файл существует теперь в этом контейнере: 
PS C:\Users\Boyko> docker exec -it 194c77aaa68f bash
root@194c77aaa68f:/# ls
bin  boot  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@194c77aaa68f:/# ls data
test.txt

<img width="1507" height="189" alt="image" src="https://github.com/user-attachments/assets/15a35dc8-b8ab-44a3-92dc-cdb911b905f4" />

Как это выглядит сейчас в ЛК Докера: 
<img width="1574" height="537" alt="image" src="https://github.com/user-attachments/assets/ed966078-a615-4b89-b54f-bb53d3b6a51d" />
<img width="1574" height="246" alt="image" src="https://github.com/user-attachments/assets/4c36a0e9-03c5-4491-8b15-5535d7e7b5bd" />


