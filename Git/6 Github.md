# 4. GitHub

- [1. 계정 만들고 설정하기](#1-계정-만들고-설정하기)
  - [SSH 사용하기](#ssh-사용하기)
  - [SSH 공개키 만들기](#ssh-공개키-만들기)
  - [아바타](#아바타)
  - [사용자 이메일 주소](#사용자-이메일-주소)
  - [투팩터(2FA) 인증](#투팩터2fa-인증)
- [2. GitHub 프로젝트에 기여하기](#2-github-프로젝트에-기여하기)
  - [프로젝트 Fork 하기](#프로젝트-fork-하기)
  - [GitHub 플로우](#github-플로우)
    - [Pull Request 만들기](#pull-request-만들기)
    - [Pull Request 놓고 감 놓고 배 놓기](#pull-request-놓고-감-놓고-배-놓기)
  - [Pull Request 팁](#pull-request-팁)
    - [Patch를 Pull Request로 보내기](#patch를-pull-request로-보내기)
    - [Pull Request를 최신으로 업데이트하기](#pull-request를-최신으로-업데이트하기)
  - [Pull Request 만들기](#pull-request-만들기-1)
  - [Pull Request 놓고 감 놓고 배 놓기](#pull-request-놓고-감-놓고-배-놓기-1)
  - [GitHub Flavored Markdown](#github-flavored-markdown)
    - [GitHub Flavored Markdown](#github-flavored-markdown-1)
    - [타스크 리스트](#타스크-리스트)
    - [코드 조각](#코드-조각)
    - [인용](#인용)
    - [참조](#참조)
    - [Emoji](#emoji)
    - [이미지](#이미지)
- [3. GitHub 프로젝트 관리하기](#3-github-프로젝트-관리하기)
- [4. Organization 관리하기](#4-organization-관리하기)
- [5. GitHub 스크립팅](#5-github-스크립팅)

## 1. 계정 만들고 설정하기

- Github - <https://github.com>

  - 가장 큰 Git 저장소 호스트
  - Git 호스팅, 이슈 트래킹, 코드 리뷰, 등등

- 계정 만들기 - Sign up for GitHub

### SSH 사용하기

- https:// 프로토콜

  - Git 저장소를 사용하는 데 부족함이 없음.
  - 사용자이름과 암호로 인증.

- SSH 리모트
  - SSH 공개키 필요.
  - 계정 설정 -> SSH Keys 메뉴에서 등록
  - Add an SSH key -> ~/.ssh/id_rsa.pub 파일 내용 복사 -> Add key

### SSH 공개키 만들기

- 많은 Git 서버들은 SSH 공개키 인증을 사용.

- 공개키 확인

  - ~/.shh에 사용자 SSH키가 들어 있음.
  - .pub - 공개키
  - 나머지는 개인키

  ```shell
  $ cd ~/.ssh
  $ ls
  authorized_keys2  id_dsa       known_hosts
  config            id_dsa.pub
  ```

- SSH 공개키 만들기

  - ssh-keygen - Linux, Mac.
  - Git for Windows - windows.
  - .ssh/id_rsa 키를 저장하고 싶은 디렉토리를 입력하고 암호를 두 번 입력.

  ```shell
  $ ssh-keygen
  Generating public/private rsa key pair.
  Enter file in which to save the key (/home/schacon/.ssh/id_rsa):
  Created directory '/home/schacon/.ssh'.
  Enter passphrase (empty for no passphrase):
  Enter same passphrase again:
  Your identification has been saved in /home/schacon/.ssh/id_rsa.
  Your public key has been saved in /home/schacon/.ssh/id_rsa.pub.
  The key fingerprint is:
  d0:82:24:8e:d7:f1:bb:9b:33:53:96:93:49:da:9b:e3 schacon@mylaptop.local
  ```

  - 사용자가 자신의 공개키를 Git 서버 관리자에게 보냄.
  - 사용자는 .pub 파일의 내용을 복사하여 이메일을 보냄.

### 아바타

- Github 사이트에서 사용자 이름 옆의 그림.
- Profile -> Upload new picture 메뉴에서 변경.

### 사용자 이메일 주소

- Git 커밋에 있는 이메일 주소로 사용자를 식별.
- 사용자가 이메일 주소를 여러 개 사용해서 커밋해도 Github는 그 이메일을 모두 등록하기만 했으면 처리.
- Emails 메뉴에서 등록

### 투팩터(2FA) 인증

- 비밀번호 인증 후 TOTP(Time based One-Time Password)나 sms 인증코드로 로그인.
- Security 메뉴에서 Set up two-factor authentication 설정.

## 2. GitHub 프로젝트에 기여하기

### 프로젝트 Fork 하기

- 원래 프로젝트에 Push할 권한이 없음.
- Fork해서 통째로 복사. - Fork 버튼을 누르기면 됨.
- 내 스페이스에서 Push가능, 기능 개선.
- Push한 내용을 원래 저장소로 보내기. - Pull Request
  - 토론 스레드를 만들고, 코드 리뷰 후, 원 소유자가 마음에 들면 Merge.

### GitHub 플로우

- Github 워크플로 - Integration-Manager 워크플로와 같음.

  - Pull Request가 중심인 협업 워크플로를 위주로 설계.
  - Fork 해서 프로젝트에 기여
  - 단일 저장소만 사용하는 작은 팀
  - 전 세계에서 흩어져서 일하는 회사
  - 한 번도 본 적 없는 사람들 사이에서도 유용

- 순서

  1. 프로젝트를 Fork 한다.
  2. master 기반으로 토픽 브랜치를 만든다.
  3. 뭔가 수정해서 커밋한다.
  4. 자신의 GitHub 프로젝트에 브랜치를 Push 한다.
  5. GitHub에 Pull Request를 생성한다.
  6. 토론하면서 그에 따라 계속 커밋한다.
  7. 프로젝트 소유자는 Pull Request를 Merge 하고 닫는다.

#### Pull Request 만들기

- 기여하고자 하는 프로젝트 찾기.
- Fork 버튼으로 프로젝트 복사.
- git clone으로 내려받음.
- 토픽 브랜치를 만들고 코드 수정 후 다시 Push.

- Fork 한 내 저장소에 가면 GitHub은 토픽 브랜치가 하나 Push 됐다는 것을 알려주고  
  원 저장소에 Pull Request를 보낼 수 있는 큰 녹색 버튼을 보여준다.
- 원 프로젝트 소유자가 판단 할 수 있게 제목과 설명을 상세히 적음.

#### Pull Request 놓고 감 놓고 배 놓기

- Pull Request가 오면 프로젝트 소유자는 변경점을 확인 후,  
  Merge하거나 거절하거나 코멘트를 달 수 있음.
- 관리자가 코멘트를 달면 Pull Request를 만든 사람과  
  저장소를 'Watch’하는 사람 모두에게 알림이 감.

- 누구나 Pull Request에 코멘트를 달 수 있음. 토론.

  - 토론을 기반으로 기여자는 코드를 수정.
  - 해당 토픽 브랜치에 이어서 커밋하고 Push.
  - 기존 Pull Request에 Push하면 알림이 가지 않음. 직접 코멘트를 남겨야 함.

- Files Changed 탭에서 차이점을 볼 수 있음.

  - git diff master \<branch>와 같은 내용.

- 프로젝트 소유주는 Merge 버튼으로 머지가능. 무조건 non-fast-forward Merge.
  - Merge 커밋이 남음.
  - 머지하면 Github의 Pull Request는 자동으로 닫힘.

### Pull Request 팁

#### Patch를 Pull Request로 보내기

- Patch처럼 완벽하고 꼭 순서대로 적용 되는 것이 아님.
- Pull Requset는 주제를 두로 논의를 하는 곳.
- 커뮤니티의 힘으로 더욱 좋은 답을 찾음.
- Merge버튼을 누르면 Merge 커밋을 일부러 남기겠다는 뜻도 됨.
- 나중에 Pull Request를 보고 왜 이렇게 결정하게 되었는지 확인 할 수 있음.

#### Pull Request를 최신으로 업데이트하기

-

### Pull Request 만들기

### Pull Request 놓고 감 놓고 배 놓기

### GitHub Flavored Markdown

#### GitHub Flavored Markdown

#### 타스크 리스트

#### 코드 조각

#### 인용

#### 참조

#### Emoji

#### 이미지

## 3. GitHub 프로젝트 관리하기

## 4. Organization 관리하기

## 5. GitHub 스크립팅
