# Windows Subsystem for Linux (WSL)

## 1. WSL

## 2. zsh와 oh my-zsh

1. zsh

   - `sudo apt-get install zsh` - Z쉘 설치
   - `chsh -s /usr/bin/zsh` - 기본 쉘 변경
   - `echo $SHELL` - 현재 쉘 확인.

2. ## oh my zsh - <https://ohmyz.sh/>

   - `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` - curl을 이용한 설치
   - `sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"` - wget을 이용한 설치
   - theme 설정
     - `vi ~/.zshrc`
     - ZSH_THEME="agnoster"로 수정.

3. 글꼴 변경

   - ubuntu 창에서 우클릭 -> 속성 -> 글꼴 -> 글꼴 D2coding

4. 색상 변경
   - https://github.com/microsoft/terminal/releases/tag/1810.02002
   - CMD 창에서 `colortool -b <테마명>`
   - 추천 테마 - OneHalfDark, solarized_dark
   - -b - 현재 창과 기본값 모두(both) 변경

---

## 출처

- 윈도우10 Frontend 개발환경 세팅(2) <https://medium.com/@boystyou82/%EC%9C%88%EB%8F%84%EC%9A%B010-frontend-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD-%EC%84%B8%ED%8C%85-2-d82b47136e63>
- 개발환경 WSL2 + zsh로 갈아타기 <https://mulder21c.github.io/2021/01/28/setting-up-wsl-2-dev-env-and-zsh-on-windws-10/>
