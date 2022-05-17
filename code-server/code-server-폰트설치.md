### 서론

Code-server를 설치하고 사용하던 중 폰트가 거슬리기 시작했다.
평소에 네이버의 D2Coding-ligature폰트를 사용하는데 code-server에서 기본폰트만 사용하려니 심적인 불편함과 zsh테마도 쓸 수 없는 상황이 발생했다.
code-server에서 새로운 폰트를 사용하려면 code-server에 접속하는 장치에 사용하고자 하는 폰트가 설치되어 있으면 된다. 데스크톱같은 경우 간단히 설치하면 되니 문제가 없지만 아이패드의 경우에 폰트를 마음대로 설치할 수 없다. 내 목적은 언제 어디서나 같은 개발환경을 세팅하는 것이다.
이에 대한 해결 방법은 code-server를 호스팅하면서 폰트를 같이 호스팅시켜주면 된다.

> 관련 이슈 : https://github.com/coder/code-server/issues/1374

## 설치

설치에 앞서 설치하고자 하는 폰트를 다운로드 해야한다. 본 포스팅에선 [D2Coding-ligature 웹 폰트](https://github.com/Joungkyun/font-d2coding-ligature)를 사용할 예정이다. 설치하고자 하는 폰트를 다운로드를 하였다면 code-server가 설치되어 있는 경로를 확인해준다.

code-server를 설치 스크립트를 통해 설치하였다면 보통 `/usr/lib/code-server`에 설치되어 있을 것이다. 혹시나 설치 경로가 다를 수 있기 때문에 설치 경로를 먼저 확인해주고, 우리가 수정하고자 하는 `workbench.html`이 있는지 확인해주자. `workbench.html`은 다음 경로에 있다.

```bash
cd /usr/lib/code-server/lib/vscode/out/vs/code/browser/workbench
```

code-server나 nano 또는 vim을 사용해서 `workbench.html`을 열고 아래 코드를 넣어주고 저장한다.

```html
<link
  rel="stylesheet"
  type="text/css"
  href="{{VS_BASE}}/static/out/vs/code/browser/fonts.css"
/>
```

> code-server의 버전이 **3.x.x**라면 `workbench.html`이 아닌 `vscode.html`를 찾아야합니다. 또한 경로지정에 `VS_BASE`가 아닌 `CS_STATIC_BASE`를 사용해야 한다.

다음으로 `/usr/lib/code-server/lib/vscode/out/vs/code/browser`경로에 다운로드 했던 폰트를 넣어주고, `fonts.css`를 생성한다. `fonts.css`의 내용은 다음과 같다.

```css
@font-face {
  font-family: "D2Coding ligature";
  src: url("./D2Coding-ligature.woff2") format("woff2"), url("./D2Coding-ligature.woff")
      format("woff");
  font-weight: 400;
  font-style: normal;
}
```

마지막으로 code-server를 재시작 해준 후 접속하게 되면 끝이다.

```bash
sudo systemctl restart code-server@$USER
```

아래 사진과 같이 아이패드에서도 폰트와 zsh테마 적용이 정상적으로 동작하는 것을 확인 할 수 있다.

![finish](https://velog.velcdn.com/images/handwoong/post/904653a1-9770-4859-9266-8d2d32c49fa2/image.jpeg)

## 문제점

이 방법에는 하나의 문제가 있는데 code-server 버전을 업데이트하게 되면 설치해둔 폰트가 풀리게 된다.
찾아보니 지금으로썬 해당 문제를 해결 할 방법이 없는 것 같고 추후에 방법이 나온다면 글을 업데이트하도록 하겠다.

## 참고자료

[code-server - Issue1374](https://github.com/coder/code-server/issues/1374)
[코드 서버에 커스텀 폰트 적용하기 - 정훈님 블로그](https://jeonghun-ban.github.io/posts/development-environment/how-to-add-custom-fonts-on-code-server/)
