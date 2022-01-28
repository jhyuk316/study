# 1. Git

- [1. Git이란?](#1-git이란)
  - [1.1. 버전 관리](#11-버전-관리)
  - [1.2. Git의 특징](#12-git의-특징)
- [2. Git 설치](#2-git-설치)
  - [2.1. Git 최초 설정](#21-git-최초-설정)

## 1. Git이란?

분산 버전 관리 시스템(DVCS)

### 1.1. 버전 관리

- 로컬 버전 관리

  - 디렉터리 별로 관리.
  - 파일의 변경되는 부분(델타)을 링크 리스트로 관리.

- 중앙집중 버전 관리 시스템 (CVCS : Centralized Version Control System)

  ![CVCS](images/Git%20사용법_CVCS.png)

  - Subversion
  - 파일을 관리하는 서버가 별도로 존재.
  - 중앙 서버에서 사용할 파일을 Checkout해서 사용
  - 장점 : 관리지가 관리하기 편함.
  - 단점 : 서버가 안되면 아무 작업도 할 수 없음.

- 분산 버전 관리 시스템(DVCS : Distributed Version Control System)

  ![DVCS](images/Git%20사용법_DVCS.png)

  - **Git**, Mecurial
  - 저장소를 통째로 복제(Clone)
  - 장점 :
    - 서버가 없어도 작업을 할 수 있음. - 저장소를 복제한 것이므로.
    - 속도가 빠름. - 거의 모든 명령을 로컬에서 실행.
  - 단점 :
    - 복잡함. - 분산된 시스템을 통합하기 위한 명령들이 많음.

### 1.2. Git의 특징

- 델타 기반이 아니라 특정 시점의 파일들의 링크(스냅샷)으로 관리

  ![snapshots](images/Git%20사용법_snapshots.png)

- 거의 모든 명령을 로컬에서 실행
- Git의 무결성 - 항상 체크섬(SHA-1)을 관리.
- Git은 데이터를 추가할 뿐 - 되돌리거나 삭제는 없음. 삭제 또한 새로운 스냅샷

- 세 가지 상태

  - Modified - 수정한 파일 아직 커밋되지 않은 상태.
  - Staged - 수정한 파일을 곧 커밋할 것이라고 표시한 상태.
  - Committed - 로컬 데이터베이스에 저장 완료.

  ![Three States](images/Git%20사용법_Three_States.png)

  - .git directory - 프로젝트의 메타데이터와 객체 데이터베이스를 저장한 곳.
  - Working Tree - 프로젝트의 특정 버전을 Checkout한 것.
  - Staging Area - Index, Git 디렉터리에 있음. 곧 커밋할 파일에 대한 정보 저장.

## 2. Git 설치

- Windows
  - <http://git-scm.com/download/win>에서 다운로드 후 설치
- Linux
  - $ sudo apt install git-all
  - $ sudo dnf install git-all
- Mac
  - $ git --version

### 2.1. Git 최초 설정

- git config

  - /etc/gitconfig 파일

    - 시스템의 모든 사용자와 모든 저장소에 적용되는 설정.
    - `git config --system` 옵션으로 변경 가능. (관리자 권한이 필요.)

  - ~/.gitconfig, ~/.config/git/config 파일

    - 특정 사용자(즉 현재 사용자)에게만 적용되는 설정.
    - `git config --global` 옵션으로 변경 가능.
    - 특정 사용자의 모든 저장소 설정에 적용.

  - .git/config 파일

    - 디렉터리에 있고 특정 저장소(혹은 현재 작업 중인 프로젝트)에만 적용.
    - `git config --local` 옵션으로 변경 가능.

  - 우선순위는 로컬 > 사용자 > 시스템 순

- 사용자 정보 등록

  ```shell
  git config --global user.name "John Doe"
  git config --global user.email johndoe@example.com
  ```

  > Git은 사용자를 메일 주소로 구분함.

- 설정 확인

  - `git config --list` - 모든 설정 보기

  ```shell
  $ git config --list
  user.name=John Doe
  user.email=johndoe@example.com
  color.status=auto
  color.branch=auto
  color.interactive=auto
  color.diff=auto
  ```

  - `git config <key>` - 특정 key의 설정 보기

  ```shell
  $ git config user.name
  John Doe
  ```
