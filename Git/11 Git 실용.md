# 5. Git 실용

- [마지막 커밋 수정하기(amend)](#마지막-커밋-수정하기amend)
- [undo commit](#undo-commit)
- [Git repository 분리하기 feat.Github](#git-repository-분리하기-featgithub)
- [변경사항 단위로 staging하기](#변경사항-단위로-staging하기)
  - [vscode](#vscode)
  - [커밋한 파일 더 이상 추적하지 않기](#커밋한-파일-더-이상-추적하지-않기)
- [출처](#출처)

## 마지막 커밋 수정하기(amend)

- `git commit --amend`

  - 자동으로 텍스트 편집기를 실행.
  - 마지막 커밋 메시지를 열어줌.
  - 커밋 메시지를 변경하고 닫기.

- 파일 추가하기

  - `git add`명령으로 파일 스테이징.
  - `git commit --amend`으로 마지막 커밋이 수정됨.
  - 커밋 메시지 닫기.

- SHA-1 값은 변경됨.

## undo commit

> 로컬 저장소에서만 사용할 것. Push 했을 경우 사용하지 말 것.

- 마지막 커밋을 취소. 파일은 유지.
- `git reset HEAD^` - HEAD에서 한 커밋 전으로 이동시키라는 것.

  - Staging에서 제거됨.
  - 변경한 파일은 유지됨.
  - GUI에는 대부분 undo commit으로 있음.

- `git reset <commit>`

  - 옵션

  |                   | --soft      | --mixed(default)      | --hard          |
  | ----------------- | ----------- | --------------------- | --------------- |
  | HEAD              |             | 지정한 커밋으로 이동  |                 |
  | Staging Area      | 변화 X      | Commit의 내용으로     | Commit 내용으로 |
  | Working Directory | 변화 X      | 변화 X                | Commit 내용으로 |
  | 용도              | Branch 이동 | Staging Area에서 빼기 | 변경사항 취소   |

## Git repository 분리하기 feat.Github

1. 분리할 디렉터리만 새로운 브랜치 만들기.
   - `git subtree split -P <분리하려는 서브 디렉터리 이름> -b <임시 브랜치 이름>`
   - eg. git subtree split -P Leetcode -b split_leetcode - 대소문자 주의
2. 새로운 레포지토리 만들고 clone.
   - Github에 새로운 레포지토리를 만듦.
   - `git clone <새 레포지토리 명>`
   - eg. git clone https://github.com/jhyuk316/Leetcode.git
3. 새 디렉터리에서 그 브랜치를 받기.
   - cd <새 레포지토리 명> - 새 레포지토리로 이동.
   - `git pull <분리하려는 큰 프로젝트의 경로> <아까 만든 브랜치 이름>`
   - eg. git pull ..\study split_leetcode
4. 새로운 레포지토리에 올리기.
   - `git push -u origin main` or `git push` - main push
5. 원 프로젝트에서 분리 디렉터리 삭제 후 커밋.
   - `git rm -rf <삭제 디렉터리>`
   - `git commit -m "메시지"`
   - `git push - u origin main` or `git push`
6. 임시 브랜치 삭제
   - `git branch -D <임시 브랜치 이름>` - Merge하지 않기 때문에 강제 삭제

## 변경사항 단위로 staging하기

- hunk - 파일 안의 변경 사항 단위
- `git add -p` - hunk 단위로 상호작용하며 스테이징하기
  - 변경사항(hunk) 내용이 쭉 보임.
  - y - 이 hunk를 스테이징.
  - n - 이 hunk를 스테이징 하지 않음.
  - a - 이 hunk와 남은 hunk 스테이징.
  - d - 이 hunk와 남은 hunk 스테이징 하지 않음.
  - g - 이동할 hunk 선택.
  - / - regex에 매칭되는 hunk 찾기.
  - j - 이 hunk는 보류하고 다음 보류 중인 hunk로.
  - J - 이 hunk는 보류하고 다음 hunk로.
  - k - 이 hunk는 보류하고 이전 보류 중인 hunk로.
  - K - 이 hunk는 보류하고 이전 hunk로.
  - s - 이 hunk를 더 작은 hunk로 쪼개기. hunk 단위가 원하는 것보다 클 때 사용.
  - e - 이 hunk를 수동으로 수정.

### vscode

- 원하는 부분을 스테이징

  - source control의 Changes에서 원하는 파일 선택
  - 원하는 부분을 블럭 후 우클릭
  - Stage Selected Ranges 클릭

- 필요 없는 부분 스테이징에서 빼기

  - source control에서 Staged Changes에서 원하는 파일 선택
  - 원하는 부분 블럭 후 우클릭
  - Unstage Selected Ranges 클릭

### 커밋한 파일 더 이상 추적하지 않기

1. 추적된 파일을 Index, Github에서 지우기

   - .gitignore에 추적하지 않을 파일 작성
   - index에서 파일 삭제
     - `git rm -r --cached <file>` - file 생략 하면 모든 파일.
   - 전체 스테이징
     - `git add .`
   - 변경 사항 커밋.
     - `git commit -m 'Remove all files that are in the .gitignore'`
   - 원격 저장소 업데이트
     - `git push origin main`

2. 로컬에서만 변경할 파일.

   - `git update-index --skip-worktree <file>`
     - 로컬에서만 변경되는 설정의 경우.
     - 개발자가 파일을 변경 해야 하므로 git에게 특정 파일을 건드리지 않도록 지시할 때 유용
   - 다시 추적
     - `git update-index --no-skip-worktree <file>`

3. 윈격저장소와 로컬에서 변하지 않을 파일.

   - `git update-index --assume-unchanged <file>`
     - 개발자가 파일을 변경 해서는 안 된다고 가정.
     - 이 플래그는 SDK와 같이 변경되지 않는 폴더의 `성능을 개선 하기 위한 것`.
   - 다시 추적
     - `git update-index --no-assume-unchanged <file>`

---

## 출처

- 레포지토리의 하위폴더를 분리해서 새로운 레포지토리로 만들기 <https://sustainable-dev.tistory.com/119>
- 7.2 Git 도구 - 대화형 명령 <https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EB%8C%80%ED%99%94%ED%98%95-%EB%AA%85%EB%A0%B9>
