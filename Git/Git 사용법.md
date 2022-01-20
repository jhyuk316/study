# Git

- [1. Git](#1-git)
  - [1.1. Git이란?](#11-git이란)
    - [1.1.1. 버전 관리](#111-버전-관리)
    - [1.1.2. Git의 특징](#112-git의-특징)
  - [1.2. Git 설치](#12-git-설치)
    - [1.2.1. Git 최초 설정](#121-git-최초-설정)
- [2. Git 기초](#2-git-기초)
  - [2.1. Git 저장소](#21-git-저장소)
  - [2.2. 수정하고 저장소에 저장](#22-수정하고-저장소에-저장)
    - [2.2.1. 파일 상태 확인](#221-파일-상태-확인)
    - [2.2.2. 파일을 새로 추적하기(Staged)](#222-파일을-새로-추적하기staged)
    - [2.2.3. Modified 상태의 파일을 Stage 하기](#223-modified-상태의-파일을-stage-하기)
    - [2.2.4. 파일 상태 간략하게 확인하기](#224-파일-상태-간략하게-확인하기)
    - [2.2.5. 파일 무시하기(.gitignore)](#225-파일-무시하기gitignore)
    - [2.2.6. Staged와 Unstaged 상태의 변경 내용을 보기](#226-staged와-unstaged-상태의-변경-내용을-보기)
    - [2.2.7. 변경사항 커밋하기](#227-변경사항-커밋하기)
    - [2.2.8. Staging Area 생략하기](#228-staging-area-생략하기)
    - [2.2.9. 파일 삭제하기](#229-파일-삭제하기)
    - [2.2.10. 파일 이름 변경하기](#2210-파일-이름-변경하기)
  - [2.3. 커밋 히스토리 조회하기](#23-커밋-히스토리-조회하기)
  - [2.4. 되돌리기](#24-되돌리기)
    - [커밋 수정](#커밋-수정)
    - [파일 상태를 Unstage로 변경](#파일-상태를-unstage로-변경)
    - [Modified 파일 되돌리기](#modified-파일-되돌리기)
  - [2.5. 리모트 저장소](#25-리모트-저장소)
    - [리모트 저장소 확인하기](#리모트-저장소-확인하기)
    - [리모트 저장소 추가하기](#리모트-저장소-추가하기)
    - [리모트 저장소를 Pull 하거나 Fetch 하기](#리모트-저장소를-pull-하거나-fetch-하기)
    - [리모트 저장소에 Push 하기](#리모트-저장소에-push-하기)
    - [리모트 저장소 살펴보기](#리모트-저장소-살펴보기)
    - [리모트 저장소 이름을 바꾸거나 리모트 저장소를 삭제하기](#리모트-저장소-이름을-바꾸거나-리모트-저장소를-삭제하기)
  - [2.6. 태그](#26-태그)
    - [태그 조회하기](#태그-조회하기)
  - [태그 붙이기](#태그-붙이기)
    - [나중에 태그하기](#나중에-태그하기)
    - [태그 공유하기](#태그-공유하기)
    - [태그를 Checkout 하기](#태그를-checkout-하기)
  - [2.7. Git Alias](#27-git-alias)
  - [Git 브랜치](#git-브랜치)
    - [브랜치란 무엇인가?](#브랜치란-무엇인가)
    - [새 브랜치 생성하기](#새-브랜치-생성하기)
    - [브랜치 이동하기](#브랜치-이동하기)
    - [브랜치와 Merge 의 기초](#브랜치와-merge-의-기초)
  - [2.8. Git 명령어](#28-git-명령어)
  - [2.9. 실용편](#29-실용편)
    - [2.9.1. amend](#291-amend)
    - [2.9.2. undo commit](#292-undo-commit)
- [3. Github](#3-github)
- [4. 출처](#4-출처)

## 1. Git

### 1.1. Git이란?

분산 버전 관리 시스템(DVCS)

#### 1.1.1. 버전 관리

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

#### 1.1.2. Git의 특징

- 델타 기반이 아니라 특정 시점의 파일들의 링크(스냅샷)으로 관리

  ![snapshots](images/Git%20사용법_snapshots.png)

- 거의 모든 명령을 로컬에서 실행
- Git의 무결성 - 항상 체크섬(SHA-1)을 관리.
- Git은 데이터를 추가할 뿐 - 되돌리거나 삭제는 없음. 삭제 또한 새로운 스냅샷
- 세 가지 상태

  - Modified - 수정한 파일 아직 커밋 되지 않은 상태.
  - Staged - 수정한 파일을 곧 커밋할 것이라고 표시한 상태.
  - Committed - 로컬 데이터베이스에 저장 완료.

  ![Three States](images/Git%20사용법_Three_States.png)

  - .git directory - 프로젝트의 메타데이터와 객체 데이터베이스를 저장한 곳.
  - Working Tree - 프로젝트의 특정 버전을 Checkout한 것.
  - Staging Area - Index, Git 디렉터리에 있음. 곧 커밋할 파일에 대한 정보 저장.

### 1.2. Git 설치

- Windows
  - <http://git-scm.com/download/win>에서 다운로드 후 설치
- Linux
  - $ sudo apt install git-all
  - $ sudo dnf install git-all
- Mac
  - $ git --version

#### 1.2.1. Git 최초 설정

- git config

  - /etc/gitconfig 파일

    - 시스템의 모든 사용자와 모든 저장소에 적용되는 설정.
    - `git config --system` 옵션으로 변경 가능. (관리자 권한이 필요.)

  - ~/.gitconfig, ~/.config/git/config 파일

    - 특정 사용자(즉 현재 사용자)에게만 적용되는 설정.
    - `git config --global` 옵션으로 변경 가능.
    - 특정 사용자의 모든 저장소 설정에 적용.

  - .git/config 파일

    - 디렉토리에 있고 특정 저장소(혹은 현재 작업 중인 프로젝트)에만 적용.
    - `git config --local` 옵션으로 변경 가능.

  - 우선 순위는 로컬 > 사용자 > 시스템 순

- 사용자 정보 등록

  ```shell
  git config --global user.name "John Doe"
  git config --global user.email johndoe@example.com
  ```

  > Git은 사용자를 메일 주소로 구분 함.

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

## 2. Git 기초

### 2.1. Git 저장소

- 기존 디렉터리를 Git 저장소로 만들기
  - 디렉터리로 이동.
  - `git init` - .git 디렉터리 생성.
- Git 저장소를 Clone하기
  - `git clone <url>` - 저장소의 모든 데이터를 복제
  - `git clone <url> <디렉터리명>` - 새로운 디렉터리에 저장소의 모든 데이터를 복제

### 2.2. 수정하고 저장소에 저장

![files lifecycle](images/Git%20사용법_files_lifecycle.png)

파일 상태

- Tracked
  - Unmodified - 수정하지 않음.
  - Modified - 수정함.
  - Staged - 커밋으로 저장소에 기록 예정.
- Untracked - 관리 대상이 아님.

#### 2.2.1. 파일 상태 확인

- `git status`

- 하나도 파일을 수정하지 않은 상태 예시

  ```shell
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  nothing to commit, working directory clean
  ```

- README라는 파일을 만들었을 때 - Untracked에 파일이 추가된 것을 확인 할 수 있음.

  ```shell
  $ echo 'My Project' > README
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Untracked files:
  (use "git add <file>..." to include in what will be committed)

      README

  nothing added to commit but untracked files present (use "git add" to track
  ```

#### 2.2.2. 파일을 새로 추적하기(Staged)

- `git add <filename>` - 파일 Staged 하기

  - Changes to be committed에 있으면 Staged 상태라는 의미.

  ```shell
  $ git add README
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

      new file:   README
  ```

#### 2.2.3. Modified 상태의 파일을 Stage 하기

- CONTRIBUTING.md라는 파일을 수정한 예시

  - Changes not staged for commit
    - Tracked 파일이지만 Staged는 아니라는 의미.

  ```shell
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

      new file:   README

  Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   CONTRIBUTING.md
  ```

- add로 스테이징한 예시.

  ```shell
  $ git add CONTRIBUTING.md
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

      new file:   README
      modified:   CONTRIBUTING.md
  ```

- 이후 다시 CONTRIBUTING.md을 수정하면

  ```shell
  $ vim CONTRIBUTING.md
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

      new file:   README
      modified:   CONTRIBUTING.md

  Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   CONTRIBUTING.md
  ```

  - 예전 CONTRIBUTING.md가 스테이징된 것이지 현재 CONTRIBUTING.md이 스테이징 된 것이 아님.

#### 2.2.4. 파일 상태 간략하게 확인하기

- `git status -s` or `git status --short`

  ```shell
  $ git status -s
   M README             // 변경 O, 스테이징 X
  MM Rakefile           // 변경 후 스테이징 후 다시 변경.
  A  lib/git.rb         // 변경 X, 스테이징 X, 새파일
  M  lib/simplegit.rb   // 변경 O, 스테이징 O
  ?? LICENSE.txt        // Untracked
  ```

- 왼쪽은 Staging Area, 오른쪽은 Working Tree
- ?? - Untracked
- A - Add 새로 생성한 파일
- M - Modified 수정한 파일

#### 2.2.5. 파일 무시하기(.gitignore)

- git 관리가 필요 없는 파일 목록.
- .gitignore 파일을 만들고 패턴을 작성.

  - \#로 시작 - 주석
  - 표준 Glob 패턴 사용. 프로젝트 전체에 적용.

    - \* - 모든 문자
    - [abc] - abc
    - [0-9] - 0123456789
    - \*\* - 디렉터리 안의 디렉터리포함 eg. a/\*\*/z - a/b/z, a/b/c/z

  - /로 시작 - 하위 디렉터리에 적용 안됨. Not Recursive
  - /로 끝 - 디렉터리.
  - !로 시작 - 해당 패턴은 무시하지 않음.

- 자주 쓰는 .gitignore 모음 <https://github.com/github/gitignore>

```txt
# 확장자가 .a인 파일 무시
*.a

# 윗 라인에서 확장자가 .a인 파일은 무시하게 했지만 lib.a는 무시하지 않음
!lib.a

# 현재 디렉토리에 있는 TODO파일은 무시하고 subdir/TODO처럼 하위디렉토리에 있는 파일은 무시하지 않음
/TODO

# build/ 디렉토리에 있는 모든 파일은 무시
build/

# doc/notes.txt 파일은 무시하고 doc/server/arch.txt 파일은 무시하지 않음
doc/*.txt

# doc 디렉토리 아래의 모든 .pdf 파일을 무시
doc/**/*.pdf
```

#### 2.2.6. Staged와 Unstaged 상태의 변경 내용을 보기

- 어떤 내용이 변경 되었는지 확인.
- `$ git diff`

  - 수정했지만 아직 staged가 아닌 파일을 비교
  - 워킹 디렉터리와 Staging Area를 비교
  - _마지막 커밋으로부터 변경된 것을 보여주는 명령어가 아님_
  - @@ -?,? +?,? @@ - 삭제된 라인 번호, 추가된 라인 번호.
  - \- - 삭제된 라인
  - \+ - 추가된 라인

  ```shell
  $ git diff
  diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
  index 8ebb991..643e24f 100644
  --- a/CONTRIBUTING.md
  +++ b/CONTRIBUTING.md
  @@ -65,7 +65,8 @@ branch directly, things can get messy.
  Please include a nice description of your changes when you submit your PR;
  if we have to read the whole diff to figure out why you're contributing
  in the first place, you're less likely to get feedback and have your change
  -merged in.
  +merged in. Also, split your changes into comprehensive chunks if your patch is
  +longer than a dozen lines.

  If you are starting to work on a particular area, feel free to submit a PR
  that highlights your work in progress (and note in the PR title that it's
  ```

- `$ git diff --staged` - 마지막 커밋과 Staging Area를 비교

#### 2.2.7. 변경사항 커밋하기

- `git commit`

  - Staging Area에 추가된 파일을 커밋함.
  - 편집기가 실행되고, 텍스트가 자동으로 포함됨.
  - 첫줄은 비어있고, 둘째줄부터 git status의 결과가 채워짐.

  ```txt
  # Please enter the commit message for your changes. Lines starting
  # with '#' will be ignored, and an empty message aborts the commit.
  # On branch master
  # Your branch is up-to-date with 'origin/master'.
  #
  # Changes to be committed:
  #   new file:   README
  #   modified:   CONTRIBUTING.md
  #
  ~
  ~
  ~
  ".git/COMMIT_EDITMSG" 9L, 283C
  ```

- `git commit -v` - 편집기에 diff 메시지도 추가됨.
- `git commit -m "message"` - 메시지를 첨부

  ```shell
  $ git commit -m "Story 182: Fix benchmarks for speed"
  [master 463dc4f] Story 182: Fix benchmarks for speed
  2 files changed, 2 insertions(+)
  create mode 100644 README
  ```

  - master 브랜치에 커밋
  - 463dc4f 체크섬

#### 2.2.8. Staging Area 생략하기

- `git commit -a` - Tracked 상태의 파일 모두를 자동으로 스테이징해서 커밋.

#### 2.2.9. 파일 삭제하기

- `git rm` 명령으로 Tracked 상태의 파일을 삭제한 후 스테이징 후 커밋

  - rm으로 하면 삭제되는 되지만 스테이징은 안된 상태
  - git rm을 명령하면 삭제 후 스테이징 상태가 됨.
  - 커밋을 하면 파일은 삭제되고 Git은 이 파일을 더 이상 추적하지 않음.
  - 이미 파일을 수정하거나 Staging Area에 추가 했으면 -f 옵션으로 강제로 삭제해야 함.

  ```shell
  $ git rm PROJECTS.md
  rm 'PROJECTS.md'
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

      deleted:    PROJECTS.md
  ```

- `git rm --cached`

  - 파일을 지우지 않고 Git에서 추적만 하지 않게 하기.
  - .gitignore에 추가하는 것을 잊었거나, 불필요한 파일이 추적 됐을 경우.

- 예시 `git rm log/\*.log` - log 폴더의 모든 .log파일 삭제하는 예시
  - \* 앞에 \을 넣어야 함.

#### 2.2.10. 파일 이름 변경하기

- Git은 파일 이름의 변경이나 파일의 이동을 명시적으로 관리하지 않음.
- 자동으로 파일명 변경이나 파일의 이동을 추적함.
- `git mv file_from file_to` - 하지만 파일명 변경 명령어는 있음.???

### 2.3. 커밋 히스토리 조회하기

- `git log`

  - 최신 내역이 위에 나옴.
  - SHA-1 체크섬, 저자 이름, 메일, 커밋한 날짜, 메시지

  ```shell
  $ git log
  commit ca82a6dff817ec66f44342007202690a93763949
  Author: Scott Chacon <schacon@gee-mail.com>
  Date:   Mon Mar 17 21:52:11 2008 -0700

      changed the version number

  commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
  Author: Scott Chacon <schacon@gee-mail.com>
  Date:   Sat Mar 15 16:40:33 2008 -0700

      removed unnecessary test

  commit a11bef06a3f659402fe7563abf99ad00de2209e6
  Author: Scott Chacon <schacon@gee-mail.com>
  Date:   Sat Mar 15 10:31:28 2008 -0700

      first commit
  ```

- `git log -p` or `git log -patch` - 각 커밋의 diff를 보여줌.
- `git log -2` - 최근 두 개의 결과만 보여줌.
- `git log -stat` - 각 커밋의 통계 정보 조회.
- `git log --pretty` - 로그 출력 형식 변경
  - `git log --pretty=oneline`
  - `git log --pretty=format:"%h %s" --graph`
    - 브랜치와 머치 히스토리를 아스키 그래프로 출력.
    - %h 짧은 해시, %s 요약

### 2.4. 되돌리기

- 되돌린 것은 복구 할 수 없음.

#### 커밋 수정

- `git commit --amend`

  - 마지막 커밋 수정.
  - 메시지를 잘못 적은 경우 - 메시지를 재설정 후 실행
  - 파일을 빼먹었을 경우 - Staging Area에 추가 후 실행

  ```shell
  $ git commit -m 'initial commit'  // 실수한 커밋
  $ git add forgotten_file          // 빠진 파일 스테이징
  $ git commit --amend              // 커밋 수정
  ```

#### 파일 상태를 Unstage로 변경

- 모든 파일을 스테이징 한 상황

  ```shell
  $ git add *
  $ git status
  On branch master
  Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

      renamed:    README.md -> README
      modified:   CONTRIBUTING.md
  ```

- `git reset HEAD <file>` - file을 Unstage

  ```shell
  $ git reset HEAD CONTRIBUTING.md
  Unstaged changes after reset:
  M CONTRIBUTING.md
  $ git status
  On branch master
  Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

      renamed:    README.md -> README

  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   CONTRIBUTING.md
  ```

#### Modified 파일 되돌리기

- `git checkout -- <file>` - 파일을 커밋 시점으로 되돌리기.

  ```shell
  $ git checkout -- CONTRIBUTING.md
  $ git status
  On branch master
  Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

      renamed:    README.md -> README
  ```

### 2.5. 리모트 저장소

- 인터넷이나 네트워크 어딘가에 있는 저장소

#### 리모트 저장소 확인하기

- `git remote`
  - 현재 프로젝트에 등록된 리모트 저장소 확인.
  - Clone하면 origin이라는 리모트 저장소가 등록됨.
- `git remote -v` - 리모트 저장소의 URL을 확인.

#### 리모트 저장소 추가하기

- `git remote add <단축이름> <url>`

  ```shell
  $ git remote
  origin
  $ git remote add pb https://github.com/paulboone/ticgit
  $ git remote -v
  origin  https://github.com/schacon/ticgit (fetch)
  origin  https://github.com/schacon/ticgit (push)
  pb  https://github.com/paulboone/ticgit (fetch)
  pb  https://github.com/paulboone/ticgit (push)
  ```

#### 리모트 저장소를 Pull 하거나 Fetch 하기

- `git fetch <remote>`

  - 리모트의 저장소의 데이터를 모두 가져옴.
  - Merge는 하지 않음.
  - 로컬의 작업 파일을 정리하고 수동으로 merge해야 함.

- `git pull` - 데이터를 가져오고 로컬 브랜치와 Merge함.

#### 리모트 저장소에 Push 하기

- `git push <리모트 저장소 이름> <브랜치 이름>`
  - git push origin master
  - master 브랜치를 origin 서버에 Push
  - 다른 사람이 작업을 했으면 Merge 후에 Push 가능.

#### 리모트 저장소 살펴보기

- `git remote show <리모트 저장소 이름>` - 리모트 저장소의 구체적인 정보 확인.

  - Pull시 master 브랜치와 머지할 브랜치를 알려줌.

  ```shell
  $ git remote show origin
  * remote origin
    Fetch URL: https://github.com/schacon/ticgit
    Push  URL: https://github.com/schacon/ticgit
    HEAD branch: master
    Remote branches:
      master                               tracked
      dev-branch                           tracked
    Local branch configured for 'git pull':
      master merges with remote master
    Local ref configured for 'git push':
      master pushes to master (up to date)
  ```

#### 리모트 저장소 이름을 바꾸거나 리모트 저장소를 삭제하기

- ` git remote rename pb paul` - 원격 저장소 이름을 pb에서 paul로 변경.
- `git remote remove paul` - 원격 저장소 paul을 삭제

### 2.6. 태그

- 보통 릴리즈 할 때 사용.

#### 태그 조회하기

- `git tag`
- `git tag -l "검색 패턴"` - 검색 패턴의 태그들 표시

  ```
  $ git tag -l "v1.8.5*"
  v1.8.5
  v1.8.5-rc0
  v1.8.5-rc1
  v1.8.5-rc2
  v1.8.5-rc3
  v1.8.5.1
  v1.8.5.2
  v1.8.5.3
  v1.8.5.4
  v1.8.5.5
  ```

### 태그 붙이기

- Lightweight 태그 - 특정 커밋에 대한 포인터
- Annotated 태그 - 태그를 만든 사람의 이름, 이메일, 만든 날짜, 메시지도 저장.

- Annotated 태그

  - `git tag -a v1.4 -m "my version 1.4"` - -a 옵션

  ```shell
  $ git tag -a v1.4 -m "my version 1.4"
  $ git tag
  v0.1
  v1.3
  v1.4
  ```

  - `git show v1.4` - 태그 정보와 커밋 정보 확인

```shell
$ git show v1.4
tag v1.4
Tagger: Ben Straub <ben@straub.cc>
Date:   Sat May 3 20:19:12 2014 -0700

my version 1.4

commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number
```

- Lightweight 태그
  - `$ git tag v1.4-lw`

#### 나중에 태그하기

- `git tag -a v1.2 9fceb02` - 체크섬 번호를 쓰면 커밋에 태그를 설정 가능.

#### 태그 공유하기

- git push는 태그를 원격 저장소로 보내지 않음.
- `git push origin <태그 이름>` - 태그 이름 푸시
- `git push origin --tags' - 모든 태그 이름 푸시

#### 태그를 Checkout 하기

- `git checkout 2.0.0` - 2.0.0 태그를 체크아웃
  - detached HEAD(HEAD에서 떨어짐) 상태가 되어 브랜치에서 작업하는 것과 다르게 동작할 수 있음.

### 2.7. Git Alias

- Git의 단축키
- Alias 예시

  ```shell
  $ git config --global alias.co checkout
  $ git config --global alias.br branch
  $ git config --global alias.ci commit
  $ git config --global alias.st status
  ```

  - git commit 대신 git ci로 커밋 가능.

- 활용 : unstage 명령어 만들기

  ```shell
  $ git config --global alias.unstage 'reset HEAD --'
  $ git unstage fileA
  //$ git reset HEAD -- fileA와 동일
  ```

### Git 브랜치

#### 브랜치란 무엇인가?

- 브랜치 - 코드를 통째로 복사하고 나서 원래 코드와는 상관없이 독립적으로 개발을 진행

- Git이 데이터를 저장하는 법

  - 일련의 스냅샷으로 기록
  - 커밋 Object
    - 현 Staging Area에 있는 데이터의 스냅샷에 대한 포인터.
    - 저자나 커밋 메시지 같은 메타데이터.
    - 이전 커밋에 대한 포인터 등.
  - Blob - 파일을 Stage해서 Git 저장소에 파일, 체크섬을 저장한 것.

  ```shell
  $ git add README test.rb LICENSE
  $ git commit -m 'The initial commit of my project'
  ```

  commit and tree

  ![commit-and-tree](images/Git%20사용법_commit-and-tree.png)

  - 루트 디렉터리와 각 하위 디렉터리의 트리 개체를 체크섬과 함께 저장소에 저장.
  - 커밋 객체를 만들고 메타데이터와 루트 디렉터리 트리 개체를 가리키는 포인터 정보를 커밋 개체에 저장.

  commits and parents

  ![commits-and-parents](images/Git%20사용법_commits-and-parents.png)

  - 파일을 수정하고 커밋하면 이전 커밋이 무엇인지도 저장.

  branch and history

  ![branch-and-history](images/Git%20사용법_branch-and-history.png)

  - 브랜치는 커밋 사이를 가볍게 이동할 수 있는 포인터.
  - master/main - git을 처음 만들면 만들어지는 기본 브랜치.

#### 새 브랜치 생성하기

- `git branch <이름>`

  ```shell
  $ git branch testing
  ```

  한 커밋 히스토리를 가리키는 두 브랜치

  ![two-branches](images/Git%20사용법_two-branches.png)

  - HEAD - 현재 작업중인 로컬 브랜치를 가리키는 포인터.
  - 새 브랜치를 만들었지만 HEAD를 옮기지는 않음.

- 현재 브랜치를 확인하기

  - `git log --decorate`

  ```shell
  $ git log --oneline --decorate
  f30ab (HEAD -> master, testing) add feature #32 - ability to add new formats to the central interface
  34ac2 Fixed bug #1328 - stack overflow under certain conditions
  98ca9 The initial commit of my project
  ```

  - master, testing 브랜치가 f30ab 커밋을 가리킴.
  - HEAD는 master를 가리킴.

#### 브랜치 이동하기

- `git checkout <브랜치 이름>` - 브랜치 이동.

1. testing 브랜치로 이동.

```shell
git checkout testing
```

![head-to-testing](images/Git%20사용법_head-to-testing.png)

2. 커밋 해보기

```shell
$ vim test.rb
$ git commit -a -m 'made a change'
```

![advance-testing](images/Git%20사용법_advance-testing.png)

3. master로 이동

```shell
$ git checkout master
```

![checkout-master](images/Git%20사용법_checkout-master.png)

4. 파일을 수정하고 다시 커밋

```shell
$ vim test.rb
$ git commit -a -m 'made other changes'
```

![advance-master](images/Git%20사용법_advance-master.png)

#### 브랜치와 Merge 의 기초

- 실제 개발 시나리오

1. 웹사이트가 있고 뭔가 작업을 진행중.

   1. 새로운 이슈를 처리할 새 Branch를 하나 생성한다.
   2. 새로 만든 Branch에서 작업을 진행한다.

2. 이때 중요한 문제가 생겨서 그것을 해결하는 Hotfix를 먼저 만들어야 한다. 그러면 아래와 같이 할 수 있다.

   1. 새로운 이슈를 처리하기 이전의 운영(Production) 브랜치로 이동한다.
   2. Hotfix 브랜치를 새로 하나 생성한다.
   3. 수정한 Hotfix 테스트를 마치고 운영 브랜치로 Merge 한다.

3. 다시 작업하던 브랜치로 옮겨가서 하던 일 진행한다.

### 2.8. Git 명령어

git init : git 초기화  
git remote add origin 레파지토리 : 로컬 저장소와 원격 저장소의 연결  
git status : 현재 깃의 상태  
git add : 변경된 파일들 모두 트랙  
git commit -m "커밋메시지" :커밋메시지 설정  
git push origin master : 로컬 저장소를 원격에 업로드
git pull origin master : 원격 저장소를 로컬에 다운로드

### 2.9. 실용편

#### 2.9.1. amend

#### 2.9.2. undo commit

reset

## 3. Github

---

## 4. 출처

- ProGit <https://git-scm.com/book/ko/v2>
