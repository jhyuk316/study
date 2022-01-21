# 2. Git 기초

- [1. Git 저장소](#1-git-저장소)
- [2. 수정하고 저장소에 저장](#2-수정하고-저장소에-저장)
  - [2.1. 파일 상태 확인](#21-파일-상태-확인)
  - [2.2. 파일을 새로 추적하기(Staged)](#22-파일을-새로-추적하기staged)
  - [2.3. Modified 상태의 파일을 Stage 하기](#23-modified-상태의-파일을-stage-하기)
  - [2.4. 파일 상태 간략하게 확인하기](#24-파일-상태-간략하게-확인하기)
  - [2.5. 파일 무시하기(.gitignore)](#25-파일-무시하기gitignore)
  - [2.6. Staged와 Unstaged 상태의 변경 내용을 보기](#26-staged와-unstaged-상태의-변경-내용을-보기)
  - [2.7. 변경사항 커밋하기](#27-변경사항-커밋하기)
  - [2.8. Staging Area 생략하기](#28-staging-area-생략하기)
  - [2.9. 파일 삭제하기](#29-파일-삭제하기)
  - [2.10. 파일 이름 변경하기](#210-파일-이름-변경하기)
- [3. 커밋 히스토리 조회하기](#3-커밋-히스토리-조회하기)
- [4. 되돌리기](#4-되돌리기)
  - [4.1. 커밋 수정](#41-커밋-수정)
  - [4.2. 파일 상태를 Unstage로 변경](#42-파일-상태를-unstage로-변경)
  - [4.3. Modified 파일 되돌리기](#43-modified-파일-되돌리기)
- [5. 리모트 저장소](#5-리모트-저장소)
  - [5.1. 리모트 저장소 확인하기](#51-리모트-저장소-확인하기)
  - [5.2. 리모트 저장소 추가하기](#52-리모트-저장소-추가하기)
  - [5.3. 리모트 저장소를 Pull 하거나 Fetch 하기](#53-리모트-저장소를-pull-하거나-fetch-하기)
  - [5.4. 리모트 저장소에 Push 하기](#54-리모트-저장소에-push-하기)
  - [5.5. 리모트 저장소 살펴보기](#55-리모트-저장소-살펴보기)
  - [5.6. 리모트 저장소 이름을 바꾸거나 리모트 저장소를 삭제하기](#56-리모트-저장소-이름을-바꾸거나-리모트-저장소를-삭제하기)
- [6. 태그](#6-태그)
  - [6.1. 태그 조회하기](#61-태그-조회하기)
  - [6.2. 태그 붙이기](#62-태그-붙이기)
  - [6.3. 나중에 태그하기](#63-나중에-태그하기)
  - [6.4. 태그 공유하기](#64-태그-공유하기)
  - [6.5. 태그를 Checkout 하기](#65-태그를-checkout-하기)
- [7. Git Alias](#7-git-alias)

## 1. Git 저장소

- 기존 디렉터리를 Git 저장소로 만들기
  - 디렉터리로 이동.
  - `git init` - .git 디렉터리 생성.
- Git 저장소를 Clone 하기
  - `git clone <url>` - 저장소의 모든 데이터를 복제
  - `git clone <url> <디렉터리명>` - 새로운 디렉터리에 저장소의 모든 데이터를 복제

## 2. 수정하고 저장소에 저장

![files lifecycle](images/Git%20사용법_files_lifecycle.png)

파일 상태

- Tracked
  - Unmodified - 수정하지 않음.
  - Modified - 수정함.
  - Staged - 커밋으로 저장소에 기록 예정.
- Untracked - 관리 대상이 아님.

### 2.1. 파일 상태 확인

- `git status`

- 하나도 파일을 수정하지 않은 상태 예시

  ```shell
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  nothing to commit, working directory clean
  ```

- README라는 파일을 만들었을 때 - Untracked에 파일이 추가된 것을 확인할 수 있음.

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

### 2.2. 파일을 새로 추적하기(Staged)

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

### 2.3. Modified 상태의 파일을 Stage 하기

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

### 2.4. 파일 상태 간략하게 확인하기

- `git status -s` or `git status --short`

  ```shell
  $ git status -s
   M README             // 변경 O, 스테이징 X
  MM Rakefile           // 변경 후 스테이징 후 다시 변경.
  A  lib/git.rb         // 변경 X, 스테이징 X, 새 파일
  M  lib/simplegit.rb   // 변경 O, 스테이징 O
  ?? LICENSE.txt        // Untracked
  ```

- 왼쪽은 Staging Area, 오른쪽은 Working Tree
- ?? - Untracked
- A - Add 새로 생성한 파일
- M - Modified 수정한 파일

### 2.5. 파일 무시하기(.gitignore)

- git 관리가 필요 없는 파일 목록.
- .gitignore 파일을 만들고 패턴을 작성.

  - \#로 시작 - 주석
  - 표준 Glob 패턴 사용. 프로젝트 전체에 적용.

    - \* - 모든 문자
    - [abc] - abc
    - [0-9] - 0123456789
    - \*\* - 디렉터리 안의 디렉터리 포함 eg. a/\*\*/z - a/b/z, a/b/c/z

  - /로 시작 - 하위 디렉터리에 적용 안됨. Not Recursive
  - /로 끝 - 디렉터리.
  - !로 시작 - 해당 패턴은 무시하지 않음.

- 자주 쓰는 .gitignore 모음 <https://github.com/github/gitignore>

```txt
# 확장자가 .a인 파일 무시
*.a

# 윗 라인에서 확장자가 .a인 파일은 무시하게 했지만 lib.a는 무시하지 않음
!lib.a

# 현재 디렉터리에 있는 TODO파일은 무시하고 subdir/TODO처럼 하위 디렉터리에 있는 파일은 무시하지 않음
/TODO

# build/ 디렉터리에 있는 모든 파일은 무시
build/

# doc/notes.txt 파일은 무시하고 doc/server/arch.txt 파일은 무시하지 않음
doc/*.txt

# doc 디렉터리 아래의 모든 .pdf 파일을 무시
doc/**/*.pdf
```

### 2.6. Staged와 Unstaged 상태의 변경 내용을 보기

- 어떤 내용이 변경되었는지 확인.
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

### 2.7. 변경사항 커밋하기

- `git commit`

  - Staging Area에 추가된 파일을 커밋함.
  - 편집기가 실행되고, 텍스트가 자동으로 포함됨.
  - 첫 줄은 비어있고, 둘째 줄부터 git status의 결과가 채워짐.

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

### 2.8. Staging Area 생략하기

- `git commit -a` - Tracked 상태의 파일 모두를 자동으로 스테이징해서 커밋.

### 2.9. 파일 삭제하기

- `git rm` 명령으로 Tracked 상태의 파일을 삭제한 후 스테이징 후 커밋

  - rm으로 하면 삭제되는 되지만 스테이징은 안된 상태
  - git rm을 명령하면 삭제 후 스테이징 상태가 됨.
  - 커밋을 하면 파일은 삭제되고 Git은 이 파일을 더 이상 추적하지 않음.
  - 이미 파일을 수정하거나 Staging Area에 추가했으면 -f 옵션으로 강제로 삭제해야 함.

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
  - .gitignore에 추가하는 것을 잊었거나, 불필요한 파일이 추적됐을 경우.

- 예시 `git rm log/\*.log` - log 폴더의 모든 .log파일 삭제하는 예시
  - \* 앞에 \을 넣어야 함.

### 2.10. 파일 이름 변경하기

- Git은 파일 이름의 변경이나 파일의 이동을 명시적으로 관리하지 않음.
- 자동으로 파일명 변경이나 파일의 이동을 추적함.
- `git mv file_from file_to` - 하지만 파일명 변경 명령어는 있음.???

## 3. 커밋 히스토리 조회하기

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

## 4. 되돌리기

- 되돌린 것은 복구할 수 없음.

### 4.1. 커밋 수정

- `git commit --amend`

  - 마지막 커밋 수정.
  - 메시지를 잘못 적은 경우 - 메시지를 재설정 후 실행
  - 파일을 빼먹었을 경우 - Staging Area에 추가 후 실행

  ```shell
  $ git commit -m 'initial commit'  // 실수한 커밋
  $ git add forgotten_file          // 빠진 파일 스테이징
  $ git commit --amend              // 커밋 수정
  ```

### 4.2. 파일 상태를 Unstage로 변경

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

### 4.3. Modified 파일 되돌리기

- `git checkout -- <file>` - 파일을 커밋 시점으로 되돌리기.

  ```shell
  $ git checkout -- CONTRIBUTING.md
  $ git status
  On branch master
  Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

      renamed:    README.md -> README
  ```

## 5. 리모트 저장소

- 인터넷이나 네트워크 어딘가에 있는 저장소

### 5.1. 리모트 저장소 확인하기

- `git remote`
  - 현재 프로젝트에 등록된 리모트 저장소 확인.
  - Clone하면 origin이라는 리모트 저장소가 등록됨.
- `git remote -v` - 리모트 저장소의 URL을 확인.

### 5.2. 리모트 저장소 추가하기

- `git remote add <단축 이름> <url>`

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

### 5.3. 리모트 저장소를 Pull 하거나 Fetch 하기

- `git fetch <remote>`

  - 리모트의 저장소의 데이터를 모두 가져옴.
  - Merge는 하지 않음.
  - 로컬의 작업 파일을 정리하고 수동으로 merge해야 함.

- `git pull` - 데이터를 가져오고 로컬 브랜치와 Merge함.

### 5.4. 리모트 저장소에 Push 하기

- `git push <리모트 저장소 이름> <브랜치 이름>`
  - git push origin master
  - master 브랜치를 origin 서버에 Push
  - 다른 사람이 작업을 했으면 Merge 후에 Push 가능.

### 5.5. 리모트 저장소 살펴보기

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

### 5.6. 리모트 저장소 이름을 바꾸거나 리모트 저장소를 삭제하기

- `git remote rename pb paul` - 원격 저장소 이름을 pb에서 paul로 변경.
- `git remote remove paul` - 원격 저장소 paul을 삭제

## 6. 태그

- 보통 릴리즈 할 때 사용.

### 6.1. 태그 조회하기

- `git tag`
- `git tag -l "검색 패턴"` - 검색 패턴의 태그들 표시

  ```shell
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

### 6.2. 태그 붙이기

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

### 6.3. 나중에 태그하기

- `git tag -a v1.2 9fceb02` - 체크섬 번호를 쓰면 커밋에 태그를 설정 가능.

### 6.4. 태그 공유하기

- git push는 태그를 원격 저장소로 보내지 않음.
- `git push origin <태그 이름>` - 태그 이름 푸시
- `git push origin --tags' - 모든 태그 이름 푸시

### 6.5. 태그를 Checkout 하기

- `git checkout 2.0.0` - 2.0.0 태그를 체크아웃
  - detached HEAD(HEAD에서 떨어짐) 상태가 되어 브랜치에서 작업하는 것과 다르게 동작할 수 있음.

## 7. Git Alias

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
