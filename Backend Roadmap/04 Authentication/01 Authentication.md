# 1. Authentication

- [1. Authentication vs Authorization](#1-authentication-vs-authorization)
- [2. Basic Authentication](#2-basic-authentication)
- [3. Session Based Authentication](#3-session-based-authentication)
- [4. Token Authentication](#4-token-authentication)
- [5. JWT](#5-jwt)
- [6. oAuth](#6-oauth)
- [출처](#출처)

## 1. Authentication vs Authorization

![Authentication_Authorization](images/06%20Authentication_Authentication_Authorization.png)

- Authentication

  - 인증
  - 누구인가?
  - 인증 방법
    - 비밀번호 - UserName, 비밀번호 가장 흔한 방식.
    - 일회용 핀 - 단일 세션, 트랜잭션에 한하여 액세스 허용.
    - 인증 앱 - 액세스를 허용하는 외부 기관을 통해 보안 코드 생성.
    - 생체인식 - 시스템에 지문이나 망막 스캔을 제출.

- Authorization

  - 인가, 허가
  - 뭘 할 수 있는가?
  - 사용자에게 특정 **리소스**나 **기능**에 액세스할 수 있는 권한을 부여하는 프로세스
  - 인가는 보안 환경에서 항상 인증 이후에 진행되어야 함.

|                                 |       인증 (Authentication)       |      인가 (Authorization)      |
| :-----------------------------: | :-------------------------------: | :----------------------------: |
|              기능               |          자격 증명 확인           |         권한 허가/거부         |
|            진행 방식            | 비밀번호, 생체인식, 일회용 핀, 앱 | 보안 팀에서 관리하는 설정 사용 |
|     사용자가 볼 수 있는가?      |                예                 |             아니오             |
| 사용자가 직접 변경할 수 있는가? |          부분적으로 가능          |             불가능             |
|           데이터 전송           |           ID 토큰 사용            |        액세스 토큰 사용        |

## 2. Basic Authentication

> - RFC(Request for Comments)
>
> 문서는 비평을 기다리는 문서라는 의미로, 컴퓨터 네트워크 공학 등에서 **인터넷 기술에 적용 가능한 새로운 연구, 혁신, 기법 등을 아우르는 메모**

![Basic_Authentication](images/06%20Authentication_Basic_Authentication.png)

- HTTP 인증
- RFC 7235

- 절차

  1. 클라이언트가 서버에 요청
  2. 인증이 필요한 요청일때 서버는 401 Unauthorized 응답과 함께 WWW-Authenticate 헤더를 기술해서 인증 방법을 설명
     - `WWW-Authenticate: Basic realm="User Visible Realm"`
  3. 클라이언트가 서버로 인증, 인코딩된 비밀번호와 그 외 인증 파라미터들을 Authorization 헤더에 담아서 요청.
     - `Authorization: Basic base64(id:passward)`
  4. 인증이 완료되면 정상적인 상태 코드를 반환.

- Base64로 인코딩.
- 암호화 되지 않음.
- HTTPS(TLS) 연결 위에서 사용해야 안전.
- 사용자를 로그아웃 시킬 수 없음.

## 3. Session Based Authentication

![Session_Authentication](images/01%20Authentication_Session_Authentication.png)

- 세션 - 고유 ID, 로그인 시간 및 만료 시간 등을 저장한 작은 파일(JSON)

- 절차

  1. 클라이언트가 서버에 로그인 요청.
  2. 서버는 로그인 요청을 인증하고 세션을 데이터베이스에 저장, 세션 ID가 포함된 쿠키를 클라이언트에 반환.
  3. 클라이언트는 요청과 함께 쿠키를 보냄.
  4. 서버는 쿠키 안의 ID를 확인하고 DB에 있으면 응답을 보냄.

- 장점
  - 관리자가 세션에 대한 권한을 가짐.
- 단점
  - 쿠키 위조, 중간자 공격에 노출됨.
  - 로드배런싱 - 사용자가 많아서 분산 서버 만듬.
    - 이때, 세션ID 검증 문제가 발생.
      - 해결책 1 - 세션DB는 하나의 서버이므로 부하 분산이 재대로 되지 않음.
      - 해결책 2 - 각각의 서버가 세션 DB를 가지고 있으면 한 사용자는 무조건 같은 서버에 접속 되야함.

## 4. Token Authentication

- Bearer Authentication

![Token_Authentication](images/01%20Authentication_Token_Authentication.png)

- 절차

  1. 클라이언트가 서버에 로그인 요청.
  2. 서버는 로그인을 승인하고 클라이언트에 토큰을 보냄.
  3. 클라이언트는 요청과 함께 헤드에 토큰을 넣어 보냄.
  4. 서버는 토크이 유효하면 응답을 보냄.

- 장점
  - 확장성이 높음.
- 단점
  - 인증 내용이 클라이언트에 저장되므로 서버에서 관리가 어려움.

## 5. JWT

- Json Web Token
- RFC 7519 - JWT에 대해 기술된 문서.

## 6. oAuth

- Authorization
- 인터넷 사용자들이 비밀번호를 제공하지 않고 다른 웹사이트 상의 자신들의 정보에 대해 웹사이트나 애플리케이션의 접근 권한을 부여할 수 있는 공통적인 수단으로서 사용되는, 접근 위임을 위한 개방형 표준

---

## 출처

- 인증과 인가 (권한 부여) 비교 – 특징 및 차이점 - <https://www.okta.com/kr/identity-101/authentication-vs-authorization/>
- RFC 7235 - HTTP/1.1 : Authentication 번역 - <https://roka88.dev/110>
- Session vs Token Based Authentication - <https://sherryhsu.medium.com/session-vs-token-based-authentication-11a6c5ac45e4>
- Basic access authentication - <https://en.wikipedia.org/wiki/Basic_access_authentication>
- Basic Authentication in ASP.NET Web API - <https://docs.microsoft.com/en-us/aspnet/web-api/overview/security/basic-authentication>
- OAuth - <https://ko.wikipedia.org/wiki/OAuth>
