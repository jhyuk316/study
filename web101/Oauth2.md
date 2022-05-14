# Oauth2

## 1. Oauth란?

### 1.1. Role

- Resource Server & Authorization Server

  - google, facebook, twitter 등.

- Resource Owner

  - user

- Client
  - 제3의 서비스, 내가 개발할 서비스

### 1.2. 등록

- Client가 Resource Server에 사용 권한을 얻는 것.

  - Client-ID - 애플리케이션 식별자
  - Client-Secret - 애플케이션 비밀번호(노출되면 안됨.)
  - Authorized redirect URLs - authorization code를 요청하고 전달받을 주소.
  - scope - 사용할 기능 지정.

- 등록 과정 - 각 사이트마다 다름.
  1. 개발자 계정등록
  2. 앱 생성
  3. Redirect URI 등록
  4. Client-ID, Client-Secret 복사

### 1.3. Resource Owner의 승인

- 구글로 페이스북으로 로그인하기 등을 보여주는 것.
- 리소스 owner가 정보 사용을 허락하는 것.

- 과정
  - 리소스 서버의 주소
  - 리소스 서버에 로그인 요청.
  - Resource Owner가 로그인.
  - Client-ID를 보고 필요한 Scope을 체크
  - Resource Owner에게 Scope을 알려줌. user가 허용하면.
  - Client-ID를 보고 토큰을 Authorized redirect URLs을 전달.

### 1.4. Resource Server의 승인

- redirect URLs과 authorization code를 Owner에게 제공
- user는 redirect url로 접속하게되고 클라이언트는 authorization code를 얻게 됨.
- 클라이언트는 authorization code와 client-id,client-secret을 Resource Server 인증을 요청.
- Resource Server는 클라이언트가 전송한 authorization code와 client-id,client-secret이 모두 일치하는 지 검사.

### 1.5. Access Token 발행

- authorization code를 제거
- access Token 발행
- client에게 access token제공
- access Token은 Resource Owner의 정보를 제공.

### 1.6. API 호출

- Resource Server의 API에 access token을 넣어 요청.
- access token 전달 방법 두가지
  - header에 Authorization: Bearer로 access_token 전달 - 보단 안전하고 주로 사용.
  - get prameter로 access_token 전달 - 쓰지 말자.

### 1.7. refresh token

- access Token - 보안을 위해서 수명이 짧다.
- refresh token - access token을 재발행 받기 위한 토큰.
  - 수명이 길다.
  - 매번 유저가 로그인 해서 재발행 받는 것을 방지.

```text
  +--------+                                           +---------------+
  |        |--(A)------- Authorization Grant --------->|               |
  |        |                                           |               |
  |        |<-(B)----------- Access Token -------------|               |
  |        |               & Refresh Token             |               |
  |        |                                           |               |
  |        |                            +----------+   |               |
  |        |--(C)---- Access Token ---->|          |   |               |
  |        |                            |          |   |               |
  |        |<-(D)- Protected Resource --| Resource |   | Authorization |
  | Client |                            |  Server  |   |     Server    |
  |        |--(E)---- Access Token ---->|          |   |               |
  |        |                            |          |   |               |
  |        |<-(F)- Invalid Token Error -|          |   |               |
  |        |                            +----------+   |               |
  |        |                                           |               |
  |        |--(G)----------- Refresh Token ----------->|               |
  |        |                                           |               |
  |        |<-(H)----------- Access Token -------------|               |
  +--------+           & Optional Refresh Token        +---------------+
```

---

- WEB2-OAuth - <https://www.youtube.com/playlist?list=PLuHgQVnccGMA4guyznDlykFJh28_R08Q->
- Spring OAuth2 Provider 정리 - <https://cheese10yun.github.io/spring-oauth2-provider/>

- 12. OAuth2 - <https://docs.spring.io/spring-security/site/docs/5.2.12.RELEASE/reference/html/oauth2.html>

## 2. google

## 3. naver

## 4. facebook

- 스프링 부트로 OAuth2 구현(페이스북, 구글, 카카오, 네이버) - <https://xzio.tistory.com/1049>

## 5. twitter

- How to implement OAuth Social Login (Single Sign-On)Using Twitter & Spring Boot (Java)— Part 2 - <https://rohankadam965.medium.com/how-to-implement-oauth-social-login-using-twitter-spring-boot-java-part-2-acff7f4b255a>

## 6. instargram

- https://docs.oceanwp.org/article/487-how-to-get-instagram-access-token

## 7. kakao

- [Spring] 스프링으로 OAuth2 로그인 구현하기3 - 카카오 - <https://loosie.tistory.com/302?category=932704>

---

## 출처

- OAuth2.0 + JWT를 사용한 토큰 기반 서버 인증 구현하기 - <https://zkdlu.tistory.com/12>
- [Spring Boot] OAuth2 + JWT + React 적용해보리기 - <https://velog.io/@jkijki12/Spring-Boot-OAuth2-JWT-%EC%A0%81%EC%9A%A9%ED%95%B4%EB%B3%B4%EB%A6%AC%EA%B8%B0>
