# properties

## secret

- 별도의 properties파일을 생성.
- 이 파일은 git에서 관리하지 않음.
- 메인 properties에 `spring.profiles.include=파일구분자` 추가
  - `application-secret.yml`의 경우
  - `spring.profiles.include=secret` 추가

---

## 출처

- [FIFA Online TMI] Properties 를 통해 API KEY 숨기고 가져오기
- <https://nam-ki-bok.github.io/spring/HideAPI/>
