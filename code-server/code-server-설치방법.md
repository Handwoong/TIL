### 서론

Code-server는 웹 환경에서 VSCode를 사용할 수 있습니다. 즉, 모든 장치에서 코드를 작성할 수 있습니다!
아이패드를 사려고 마음먹고 어떻게 활용할까 찾아보다 알게되었고, 설치하면서 여러가지 문제로 재설치를 여러번 하면서 했던 삽질들을 다시 하지않기 위해 기록을 남기게 되었습니다.
~~모두 아이패드를 사기 위한 자기합리화 읍읍..~~

> Code-server: https://github.com/coder/code-server

## 설치 환경

- VM: Oracle Cloud Free Tier
- OS: Ubuntu 20.04 LTS

code-server의 최소요구사항은 1GB RAM, 2 CPU cores입니다.
제가 설치해본 환경은 우분투, 라즈비안인데 다른 OS도 설치하시는데 문제없을거라 생각이 됩니다.

## 1. 설치

설치방법으로는 설치스크립트, npm, brew등 여러 방법이 있지만 저는 간편한 설치스크립트를 사용하였습니다.
다른 방법으로 설치하는건 공식문서에서 확인하실 수 있습니다.

> https://coder.com/docs/code-server/latest/install

우선 기본 패키지 업데이트를 진행해 줍니다.

```bash
sudo apt-get update
sudo apt-get upgrade
```

업데이트가 완료되면 code-server를 설치합니다.

```bash
curl -fsSL https://code-server.dev/install.sh | sh
```

간단하게 code-server 설치가 완료되었습니다!

## 2. 방화벽 설정

언제, 어디서나 접속이 가능해야 함으로 포트를 열어줄 필요가 있습니다.
VM환경에서 설치하신다면 꼭! 해주셔야하며, 그게 아닌 집에있는 라즈베리파이와 같은 머신을 사용하신다면 로컬환경에선 접속이 가능하나 집 밖에서 접속하기위해선 필수로 해주셔야합니다.

```bash
sudo iptables -I INPUT 5 -i ens3 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -I INPUT 5 -i ens3 -p tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -I INPUT 5 -i ens3 -p tcp --dport 8080 -m state --state NEW,ESTABLISHED -j ACCEPT
```

기본적으로 HTTP(80), HTTPS(443)포트와 code-server에서 사용할 포트(default 8080)를 열어줍니다.

## 3. code-server 설정

code-server를 서비스로 실행하기 위해 systemctl로 enable시켜줍니다.

```bash
sudo systemctl enable --now code-server@$USER
```

외부접속을 위해 `.config/code-server`경로의 config.yaml을 수정해줘야합니다.

```bash
vim .config/code-server/config.yaml
```

`bind-addr`을 0.0.0.0:포트번호로 설정합니다.

```yaml
bind-addr: 0.0.0.0:8080
auth: password
password: 비밀번호
cert: false
```

이후 설정을 변경하였음으로 서비스를 재시작하게되면 `아이피:포트번호`로 접속이 가능해집니다.

```bash
sudo systemctl restart --now code-server@$USER
```

![login_code-server](https://user-images.githubusercontent.com/95131477/167278360-5bc3d809-a6a2-4db7-b7af-655dfdafc5b2.png)

## 4. Nginx 설치하기

우리가 목표했던 언제 어디서나 접속하기는 성공했습니다.
하지만 HTTP환경에선 안그래도 한정적인 VSCode extension들이 더욱 더 한정적이게 됩니다.
원활한 extension 사용을 위해 Certbot으로 인증서를 발급받고, HTTPS 연결을 하겠습니다.

아래의 명령어로 nginx를 설치합니다.

```bash
sudo apt install nginx
```

설치 후 nginx 서비스를 시작해줍니다.

```bash
sudo service nginx start
```

이제 자신의 아이피주소로 접속하게 되면 아래와 같은 nginx 기본 화면이 보여야 합니다.

![nginx](https://user-images.githubusercontent.com/95131477/167278513-f380cbf4-044b-4caa-ba8d-763ada8c29e7.png)

## 5. 인증서 발급받기

인증서를 발급받기 위해서 **도메인**이 필요합니다.
[Let's Encrypt](https://letsencrypt.org/)를 통해 무료 TLS 인증서를 발급 받을 수 있으며, 인증서 발급에 [Certbot](https://certbot.eff.org/)을 사용하고, standalone 방법으로 인증서를 발급 받겠습니다.

standalone 방법

- 80번포트가 개방되어야함 -> 이미 실행중인 서비스가 존재하면 중단해야함
- 자동 갱신 가능
- 와일드카드 서브도매인 사용불가 (\*.example.com)
- 와일드카드 서브도메인 인증서가 필요하지 않다면 권장

아래 명령으로 certbot을 설치합니다.

```bash
sudo snap install certbot --classic
```

code-server와 nginx 서비스를 중지합니다.

```bash
sudo nginx -s stop
sudo systemctl stop code-server@$USER
```

그 후 아래 명령으로 인증을 진행합니다.

```bash
sudo certbot certonly --standalone
```

몇가지 질문이 나오게되고, 아래를 보시고 입력해주시면 됩니다.

```bash
Enter email address (used for urgent renewal and security notices)
 (Enter 'c' to cancel): # 이메일 주소
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
agree in order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y # 약관동의, N 선택 시 진행 불가
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: N # Let's Encrypt 프로젝트 정보 이메일 수신동의
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please enter the domain name(s) you would like on your certificate (comma and/or
space separated) (Enter 'c' to cancel): # 도메인주소
```

성공하였다면 아래와 같이 인증서의 경로가 나오게됩니다.

```bash
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/example.handwoong.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/example.handwoong.com/privkey.pem
```

## 6. Nginx 설정

위에서 발급받은 인증서를 적용하고 code-server를 띄워봅시다!

우선 Nginx의 기본 설정들을 제거합니다.

```bash
cd /etc/nginx
sudo rm ./sites-enabled/default
sudo rm ./sites-avilable/default
```

code-server의 설정을 만들어줍니다.

```bash
sudo vim /etc/nginx/sites-available/code-server.conf
```

다음과 같이 입력합니다.

```conf
server {
    listen [::]:443 ssl;
    listen 443 ssl;
    ssl_certificate # 인증서 경로;
    ssl_certificate_key # 인증서 키 경로;
    server_name mydomain.com; # 발급받은 도메인

    location / {
      proxy_pass http://localhost:8080/; # config.yaml로 설정한 서버의 주소
      proxy_set_header Host $host;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection upgrade;
      proxy_set_header Accept-Encoding gzip;
    }
}
server {
        if ($host = mydomain.com) { # 발급받은 도메인
            return 301 https://$host$request_uri;
        }
    listen 80;
	listen [::]:80;
	server_name mydomain.com; # 발급받은 도메인
    return 404;
}
```

위처럼 설정하게 되면 크롬으로는 접속이 가능하나 사파리에서 접속이 안되는 **문제**가 있습니다.
이는 TLS버전을 1.3에서 1.2로 다운그레이드하여 해결 할 수 있었고, 애플에서 아직 웹 소켓 TLS 1.3을 지원하지 않는것 같다고 합니다.

server {} 내에 아래의 내용을 추가합니다.

```conf
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384';
```

> Issue3850 : https://github.com/coder/code-server/issues/3850

심볼릭링크를 생성하여 작업한 설정을 활성화 해줍니다.

```bash
sudo ln -s /etc/nginx/sites-available/code-server.conf /etc/nginx/sites-enabled/code-server.conf
```

nginx 및 code-server를 다시 실행시켜줍니다.

```bash
sudo nginx
sudo systemctl start code-server@$USER
```

이제 도메인주소로 접속하면 HTTPS 연결이 완료된 것을 확인할 수 있습니다!
![finish_code-server](https://user-images.githubusercontent.com/95131477/167280316-0b3551f6-0a27-47f9-95fd-9d894dbeef74.png)

### 마치며

Code-server를 설치하면서 VM 생성부터 Nginx, 인증서발급 등 처음 해보는것이 많았는데 문제가 생길 때마다 이리저리 찾으러 다닌게 좋은 경험이었다고 생각하고, 그래도 역시 아이패드보단 컴퓨터가 편하다는 걸 한번 더 느끼고 있습니다.
