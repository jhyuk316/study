# 3. Git 브랜치

- [1. 브랜치란 무엇인가?](#1-브랜치란-무엇인가)
  - [1.1. 새 브랜치 생성하기](#11-새-브랜치-생성하기)
  - [1.2. 브랜치 이동하기](#12-브랜치-이동하기)
- [2. 브랜치와 Merge의 기초](#2-브랜치와-merge의-기초)
  - [2.1. 브랜치의 기초](#21-브랜치의-기초)
  - [2.2. 머지의 기초](#22-머지의-기초)
  - [2.3. 충돌(Conflict)의 기초](#23-충돌conflict의-기초)
- [3. 브랜치 관리](#3-브랜치-관리)
- [4. 브랜치 워크플로](#4-브랜치-워크플로)
  - [Long-Running 브랜치](#long-running-브랜치)
  - [토픽 브랜치](#토픽-브랜치)
- [5. 리모트 브랜치](#5-리모트-브랜치)
  - [리모트 브랜치 예제](#리모트-브랜치-예제)
  - [PUSH 하기](#push-하기)
  - [브랜치 추적](#브랜치-추적)
  - [Pull 하기](#pull-하기)
  - [리모트 브랜치 삭제](#리모트-브랜치-삭제)
- [6. Rebase 하기](#6-rebase-하기)
  - [Rebase의 기초](#rebase의-기초)
  - [Rebase 활용](#rebase-활용)
  - [Rebase의 위험성](#rebase의-위험성)
  - [Rebase한 것을 다시 Rebase 하기](#rebase한-것을-다시-rebase-하기)
  - [Rebase vs. Merge](#rebase-vs-merge)

## 1. 브랜치란 무엇인가?

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

### 1.1. 새 브랜치 생성하기

- `git branch <이름>`

  ```shell
  $ git branch testing
  ```

  한 커밋 히스토리를 가리키는 두 브랜치

  ![two-branches](images/Git%20사용법_two-branches.png)

  - HEAD - 현재 작업 중인 로컬 브랜치를 가리키는 포인터.
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

### 1.2. 브랜치 이동하기

- `git checkout <브랜치 이름>` - 브랜치 이동.

1. testing 브랜치로 이동.

   ```shell
   git checkout testing
   ```

   ![head-to-testing](images/Git%20사용법_head-to-testing.png)

2. 커밋해보기

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

## 2. 브랜치와 Merge의 기초

- 실제 개발 시나리오

1. 웹사이트가 있고 뭔가 작업을 진행하고 있다.

   1. 새로운 이슈를 처리할 새 Branch를 하나 생성한다.
   2. 새로 만든 Branch에서 작업을 진행한다.

2. 이때 중요한 문제가 생겨서 그것을 해결하는 Hotfix를 먼저 만들어야 한다.

   1. 새로운 이슈를 처리하기 이전의 운영(Production) 브랜치로 이동한다.
   2. Hotfix 브랜치를 새로 하나 생성한다.
   3. 수정한 Hotfix 테스트를 마치고 운영 브랜치로 Merge 한다.

3. 다시 작업하던 브랜치로 옮겨가서 하던 일 진행한다.

### 2.1. 브랜치의 기초

- 53번 이슈를 처리하는 상황

  - `git checkout -b iss53` - 브랜치를 만들면서 체크아웃.

  ```shell
  $ git checkout -b iss53
  Switched to a new branch "iss53"
  ```

  - 위의 명령을 풀어쓴 것.

  ```shell
  $ git branch iss53
  $ git checkout iss53
  ```

  ![basic-branching-2](images/Git%20사용법_basic-branching-2.png)

  - 작업 중인 iss53 브랜치

  ```shell
  $ vim index.html
  $ git commit -a -m 'added a new footer [issue 53]'
  ```

  basic-branching-3
  ![basic-branching-3](images/Git%20사용법_basic-branching-3.png)

- Hotfix를 해결해야 하는 상황

  - iss53을 어딘가 저장하고 운영환경으로 복귀해야 함.
  - 브랜치를 변경할 때는 워킹 디렉터리를 정리하는 것이 좋음.

    - 커밋하지 않은 파일이 checkout할 브랜치와 충돌할 수 있음.

  - master 브랜치로 이동.

  ```shell
  $ git checkout master
  Switched to branch 'master'
  ```

  - hotfix 브랜치를 만들고, 이슈를 해결

  ```shell
  $ git checkout -b hotfix
  Switched to a new branch 'hotfix'
  $ vim index.html
  $ git commit -a -m 'fixed the broken email address'
  [hotfix 1fb7853] fixed the broken email address
  1 file changed, 2 insertions(+)
  ```

  ![basic-branching-4](images/Git%20사용법_basic-branching-4.png)

  - hotfix를 master에 merge

  ```shell
  $ git checkout master
  $ git merge hotfix
  Updating f42c576..3a0874c
  Fast-forward
  index.html | 2 ++
  1 file changed, 2 insertions(+)
  ```

  - Fast-forward - C4가 C2에 기반한 브랜치 이므로 별도의 Merge과정 없이 커밋됨.

  ![basic-branching-5](images/Git%20사용법_basic-branching-5.png)

  - hotfix 브랜치 제거
    - 아무런 문제가 없으면 hotfix 브랜치는 더 이상 필요 없음.

  ```shell
  $ git branch -d hotfix
  Deleted branch hotfix (3a0874c).
  ```

- iss53으로 가서 하던 일을 계속함.

  ```shell
  $ git checkout iss53
  Switched to branch "iss53"
  $ vim index.html
  $ git commit -a -m 'finished the new footer [issue 53]'
  [iss53 ad82d7a] finished the new footer [issue 53]
  1 file changed, 1 insertion(+)
  ```

  ![basic-branching-6](images/Git%20사용법_basic-branching-6.png)

  - 이 상태로는 hotfix는 iss53에 적용되지 않은 상태.

### 2.2. 머지의 기초

- iss53의 개발이 끝남. 이제 merge.

  ```shell
  $ git checkout master
  Switched to branch 'master'
  $ git merge iss53
  Merge made by the 'recursive' strategy.
  index.html |    1 +
  1 file changed, 1 insertion(+)
  ```

  ![basic-merging-1](images/Git%20사용법_basic-merging-1.png)

  - master는 iss53의 조상이 아니므로 Fast-forward가 되지 않음.

- 3-way Merge

  - 공통 조상 1개와 각 브랜치의 커밋 두 개를 사용하여 머지.
  - 3-way Merge의 결과를 별도의 커밋으로 만듦.
  - 해당 브랜치가 그 커밋을 가리킴.

  ![basic-merging-2](images/Git%20사용법_basic-merging-2.png)

  - 필요 없어진 iss53 브랜치 제거
    - `git branch -d iss53`

### 2.3. 충돌(Conflict)의 기초

- 충돌 발생

  - 두 브랜치가 같은 부분을 수정했다면 3-way merge가 실패함.

  ```shell
  $ git merge iss53
  Auto-merging index.html
  CONFLICT (content): Merge conflict in index.html
  Automatic merge failed; fix conflicts and then commit the result.
  ```

  - 충돌이 발생하면 새 커밋이 생기지 않음.

- 충돌이 일어난 파일은 Unmerged상태로 표기.

  - 개발자가 충돌을 해결해줘야 함.

  ```shell
  $ git status
  On branch master
  You have unmerged paths.
    (fix conflicts and run "git commit")

  Unmerged paths:
    (use "git add <file>..." to mark resolution)

      both modified:      index.html

  no changes added to commit (use "git add" and/or "git commit -a")
  ```

  - 충돌이 난 부분 표시
    - 위가 HEAD(master 브랜치)의 내용
    - 아래가 iss53 브랜치의 내용.

  ```shell
  <<<<<<< HEAD:index.html
  <div id="footer">contact : email.support@github.com</div>
  =======
  <div id="footer">
  please contact us at support@github.com
  </div>
  >>>>>>> iss53:index.html
  ```

  - 개발자는 양쪽을 보고 적당하게 수정.

  ```shell
  <div id="footer">
  please contact us at email.support@github.com
  </div>
  ```

  - git add를 실행
  - git commit을 실행
  - Merge한 커밋 메시지

  ```shell
  Merge branch 'iss53'

  Conflicts:
      index.html
  #
  # It looks like you may be committing a merge.
  # If this is not correct, please remove the file
  # .git/MERGE_HEAD
  # and try again.


  # Please enter the commit message for your changes. Lines starting
  # with '#' will be ignored, and an empty message aborts the commit.
  # On branch master
  # All conflicts fixed but you are still merging.
  #
  # Changes to be committed:
  # modified:   index.html
  #
  ```

## 3. 브랜치 관리

- `git branch` - 브랜치 목록 보기

  - \* - 현재 브랜치

  ```shell
  $ git branch
    iss53
  * master
    testing
  ```

  - `git branch -v` - 브랜치 목록과 마지막 커밋 보기

  ```shell
  $ git branch -v
    iss53   93b412c fix javascript issue
  * master  7a98805 Merge branch 'iss53'
    testing 782fd34 add scott to the author list in the readmes
  ```

  - `git branch --merged` - 현재 브랜치와 merged된 브랜치 목록
    - git branch -d로 \* 없는 브랜치 삭제 가능

  ```shell
  $ git branch --merged
    iss53
  * master
  ```

  - `git branch --no-merged` - merged 되지 않은 브랜치
    - git branch -d로 삭제 불가능.
    - `git branch -D` - 브랜치 강제 삭제.

  ```shell
  $ git branch --no-merged
    testing
  ```

## 4. 브랜치 워크플로

### Long-Running 브랜치

- master - 배포할 코드, 안정 버전의 브랜치.
- develop - 개발을 진행하고 안정화하는 브랜치. 안정화가 되면 master와 merge.
- topic - 이슈를 처리하기 위한 짧은 호흡의 브랜치.

  안정적인 브랜치일수록 커밋 히스토리가 뒤쳐짐.

  ![lr-branches-1](images/3%20Git%20브랜치_lr-branches-1.png)

  각 브랜치를 하나의 실험실로 생각.

  ![lr-branches-2](images/3%20Git%20브랜치_lr-branches-2.png)

### 토픽 브랜치

- 어떤 한 가지 주제나 작업을 위해 만든 짧은 호흡의 브랜치.
- master 브랜치에 Merge 할 시점이 되면 순서에 관계없이 그때 Merge 하면 됨.

- 시나리오

  - iss91 브랜치를 만들고 해당 작업.
  - iss91v2 브랜치를 만들고 다른 방법을 시도해보기.
  - master 브랜치로 되돌아가서 dumbidea 브랜치를 만들고 아이디어를 적용해보기.

  ![topic-branches-1](images/3%20Git%20브랜치_topic-branches-1.png)

  - dumbidea와 iss91v2를 채택, Merge 하기

  ![topic-branches-2](images/3%20Git%20브랜치_topic-branches-2.png)

## 5. 리모트 브랜치

- 리모트 Refs - 리모트 저장소에 있는 포인터인 레퍼런스. 즉, 브랜치, 태그 등등.

  - `git ls-remote [remote]` - 모든 리모트 Refs 조회.

- 리모트 트래킹 브랜치 - 리모트 브랜치를 추적하는 레퍼런스이며 브랜치.

  - 리모트 서버에 연결할 때마다 리모트의 브랜치 업데이트 내용에 따라서 자동 갱신.
  - 리모트 저장소에 마지막으로 연결했던 순간에 브랜치가 무슨 커밋을 가리키고 있는지 나타냄.
  - \<remote>/\<branch> - origin의 master브랜치는 origin/master로 표기

> origin - git clone이 자동으로 만들어 주는 리모트 저장소 이름.

### 리모트 브랜치 예제

1. git.ourcompany.com을 Clone 이후 서버와 로컬의 master 브랜치

   - git clone git.ourcompany.com
   - origin/master - 리모트 브랜치
   - master - 로컬 브랜치

   ![Clone 이후 서버와 로컬의 master 브랜치](images/3%20Git%20브랜치_remote-branches-1.png)

2. 다른 팀원이 git.ourcompany.com 서버에 Push 하고 master 브랜치를 업데이트

   ![로컬과 서버의 커밋 히스토리는 독립적임](images/3%20Git%20브랜치_remote-branches-2.png)

3. 리모트 서버로부터 저장소 정보를 동기화

   - `git fetch origin`
   - 로컬 저장소가 갖고 있지 않은 새로운 정보가 있으면 모두 내려받음.
   - 받은 데이터를 로컬 저장소에 업데이트하고 나서, origin/master 포인터의 위치를 옮김.
     ![git fetch 명령은 리모트 브랜치 정보를 업데이트](images/3%20Git%20브랜치_remote-branches-3.png)

4. 팀내의 다른 저장소가 git.team1.ourcompany.com을 추가.

   - `git remote add teamone git://git.team1.ourcompany.com`

   ![서버를 리모트 저장소로 추가](images/3%20Git%20브랜치_remote-branches-4.png)

5. teamone 서버의 데이터 받기.

   - `git fetch teamone`
   - origin 서버에 있는 데이터이므로 아무것도 내려받지 않음.
   - teamone/master의 리모트 트래킹 브랜치가 추가됨.

   ![teamone/master 의 리모트 트래킹 브랜치](images/3%20Git%20브랜치_remote-branches-5.png)

### PUSH 하기

- `git push <remote> <branch>`

  - 로컬의 브랜치를 쓰기 권한이 있는 리모트 저장소로 전송.
  - 로컬 저장소의 브랜치는 자동으로 리모트 저장소로 전송되지 않음.
  - 로컬 브랜치에만 두는 비공개 브랜치를 만들 수 있음.

  ```shell
  $ git push origin serverfix
  Counting objects: 24, done.
  Delta compression using up to 8 threads.
  Compressing objects: 100% (15/15), done.
  Writing objects: 100% (24/24), 1.91 KiB | 0 bytes/s, done.
  Total 24 (delta 2), reused 0 (delta 0)
  To https://github.com/schacon/simplegit
   * [new branch]      serverfix -> serverfix
  ```

  - git은 위의 명령을 git push refs/heads/serverfix:refs/heads/serverfix로 확장 해석.
  - git push serverfix:serverfix와 동일.
  - git push origin serverfix:awesomebranch
    - 로컬 serverfix를 리모트 저장소 awesomebranch에 저장하라는 의미.

- 누군가 Fetch 명령으로 리모트 트래킹 브랜치를 내려받음.

  - 로컬 저장소에 serverfix 브랜치가 생기는 것이 아님.
  - origin/serverfix브랜치 포인트가 생김.

  ```shell
  $ git fetch origin
  remote: Counting objects: 7, done.
  remote: Compressing objects: 100% (2/2), done.
  remote: Total 3 (delta 0), reused 3 (delta 0)
  Unpacking objects: 100% (3/3), done.
  From https://github.com/schacon/simplegit
   * [new branch]      serverfix    -> origin/serverfix
  ```

  - 새로 받은 브랜치의 내용을 Merge
    - `git merge origin/serverfix`

- Merge 하지 않고 리모트 트래킹 브랜치에서 시작하는 새 브랜치를 만들기

  - `git checkout -b serverfix origin/serverfix`
  - origin/serverfix에서 시작하고 수정할 수 있는 serverfix 로컬 브랜치 생성.

  ```shell
  $ git checkout -b serverfix origin/serverfix
  Branch serverfix set up to track remote branch serverfix from origin.
  Switched to a new branch 'serverfix'
  ```

### 브랜치 추적

- 트래킹(Tracking) 브랜치

  - `git checkout -b <branch> <remote>/<branch>`
  - 리모트 트래킹 브랜치를 로컬 브랜치로 Checkout해서 생성.
  - 리모트 브랜치와 직접적인 연결고리가 있는 로컬 브랜치.
  - `git pull` - 리모트 저장소로부터 데이터를 내려받아 연결된 리모트 브랜치와 자동으로 Merge.
  - Clone하면 자동으로 master 브랜치를 origin/master 브랜치의 트래킹 브랜치로 만듦.
  - `--track` - 로컬 브랜치 이름 자동 생성.

  ```shell
  $ git checkout --track origin/serverfix
  Branch serverfix set up to track remote branch serverfix from origin.
  Switched to a new branch 'serverfix'
  ```

  - `git checkout serverfix`로 생략 가능.
    - 입력한 브랜치가 있는 리모트가 딱 한 개 있고, 로컬에 없으면 생략 가능.

  ```shell
  $ git checkout serverfix
  Branch serverfix set up to track remote branch serverfix from origin.
  Switched to a new branch 'serverfix'
  ```

  - 로컬에 존재하는 브랜치를 트래킹 브랜치로 만들기.
    - `git branch -u` 또는 `git branch --set-upstream-to`
    - 현재 로컬 브랜치가 트래킹 브랜치가 됨.

  ```shell
  $ git branch -u origin/serverfix
  Branch serverfix set up to track remote branch serverfix from origin.
  ```

- 추적 브랜치 설정 확인

  - `git branch -vv`
  - 로컬 브랜치 목록과 로컬 브랜치가 추적하고 있는 리모트 브랜치를 보여줌.

  ```shell
  $ git branch -vv
    iss53     7e424c3 [origin/iss53: ahead 2] forgot the brackets
    master    1ae2a45 [origin/master] deploying index fix
  * serverfix f8674d9 [teamone/server-fix-good: ahead 3, behind 1] this should do it
    testing   5ea463a trying something new
  ```

  - serverfix는 teamone/server-fix-good을 트래킹
    - ahead 3 - 커밋 3개가 앞서 있음.
    - behind 1 - 커밋 1개가 뒤쳐짐.
    - 서버로 보내지 않은 커밋이 3개, 서버의 브랜치에서 머지하지 않은 커밋이 1개라는 뜻.
  - testing - 트래킹 중인 브랜치가 없음.

  - `명령을 실행했을 때 나타나는 결과는 모두 마지막으로 서버에서 데이터를 가져온(fetch) 시점을 바탕으로 계산`

    - 서버의 최신 데이터가 아님.
    - 최신 데이터와 비교하려면 fetch 후 확인해야 함.
      - `git fetch --all`
      - `git branch -vv`

### Pull 하기

- `git pull`
  - 추적 브랜치를 git fetch 후 git merge를 수행
  - fetch는 로컬에 없는 데이터를 받아와 저장만 함.
  - 워킹 디렉터리의 파일 내용은 변경되지 않음.
  - Merge를 해야 합쳐짐.

> 일반적으로 fetch, merge를 따로 쓰는 게 나음.

### 리모트 브랜치 삭제

- `git push --delete <branch>`

  - 리모트 브랜치가 필요 없을 때
  - 서버의 브랜치가 사라짐.

  ```shell
  $ git push origin --delete serverfix
  To https://github.com/schacon/simplegit
  - [deleted]         serverfix
  ```

## 6. Rebase 하기

### Rebase의 기초

### Rebase 활용

### Rebase의 위험성

### Rebase한 것을 다시 Rebase 하기

### Rebase vs. Merge

히스토리를 보는 관점

1. 작업한 내용의 기록

   - 커밋 히스토리 변경 - 거짓말
   - Merge

2. 프로젝트가 어떻게 진행되었는지 이야기

   - 커밋을 다듬어서 필요한 정보로 만듦.
   - Rebase

> 로컬 브랜치의 히스토리 정리를 위해 Rebase 할 수 있지만, Push한 커밋은 절대 Rebase하지 말 것.
