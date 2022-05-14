# JWT 토큰

## Json Web Token

### 세션

1. 클라이언트가 서버에 접속.
2. 서버는 세션id 목록을 만듬.(로그인한다면 유저정보도 함께 저장.)
   1. 클라이언트가 세션id를 가지고 있고, 목록에 있으면 그냥 진행.
   2. 클라이언트가 세션ID가 없거나 목록에 없는 세션ID면 생성.
3. 서버가 header에 세션ID를 담아서 전달.
4. 클라이언트는 쿠키에 세션ID를 저장.
5. 세션ID로 로그인 상태 유지.
6. 클라이언트 브라우저를 닫으면 세션을 지움.
7. 서버는 일정 시간이 지나면 세션ID를 지움.

#### 단점

- 로드배런싱 - 사용자가 많아서 분산 서버 만듬.
  - 이때, 세션ID 검증 문제가 발생.
    - 해결책 1 - 세션DB는 하나의 서버이므로 부하 분산이 재대로 되지 않음.
    - 해결책 2 - 각각의 서버가 세션 DB를 가지고 있으면 한 사용자는 무조건 같은 서버에 접속 되야함.

### CIA

- C - 기밀성
- I - 무결성
- A - 가용성

- alice가 bob에게 문서를 보낼 때 지켜져야 할 것들.
- 암호화

  - 탈취당해도 알아 볼 수 없으니 기밀성이 유지됨.
  - 변조 한것을 알 수 있으니 무결성.
  - 암화키를 이용해 가용할 수 있음.

- 암호화키도 전달 과정에도 CIA문제를 겪음.
  - 전달 되는 데이터 탈취, 변조.
  - 응답하는 ACK 변조.

### RSA

- 공개키로 암호화하면 개인키로 복호화 할 수 있고,
- 개인키로 암호화하면 공개키로 복호화 할 수 있다.

- Public Key, 공개키 - 공개 되어있는 나의 키.
- Private Key, 개인키 - 나만 가지고 있는 키.

- 인증기관 - 공개키를 관리하는 기관.

- 서명, 인증

  - 서명 - 개인키로 암호화
  - 암호화 - 공개키로 암호화.
  - `A개인키:B공개키:데이터` - A가 B로 메시지를 보낼 때.
    - A공개키로 복호화 되면 보낸 사람을 알 수 있음.
    - B개인키로 복호화 되면 나에게 보낸 메세지임을 알 수 있음.

- RSA로 대칭키를 전달하는데 주로 사용.

### RFC 7519

- RFC - RFC(Request for Comments) 문서는 비평을 기다리는 문서라는 의미로, 컴퓨터 네트워크 공학 등에서 **인터넷 기술에 적용 가능한 새로운 연구, 혁신, 기법 등을 아우르는 메모**
- 네트워크 프로토콜 정의?

- RFC 7519 - JWT에 대해 기술된 문서.

### 왜 쓰는가?

- HMAC 서명 또는 RSA, ECDSA로 공개/개인키 쌍으로 서명
- `서명된 토큰` - 암호화용이 아님.

### 구조

- `Header.Payload.Signiure`
- header
  - 알고리즘 - HS256, RSA
  - 타입 - JWT
- payload
  - 등록된 클레임 - 발행자, 만료시간, 주제 등등
  - 개인 클레임 - User ID
- Signiure
  - HS256(HMAC)으로 암호화된 해더
  - \+ HS256으로 암호화된 페이로더
  - \+ HS256으로 암호화된 비밀키(서버만 알고 있는 값)
- 각 값은 Base64로 인코딩 되어 있음.

```TEXT
BASE64(Header).
BASE64(Payload).
BASE64(HS256(Header+Payload+비밀키))
```

- HMAC - 시크릿키를 포함한 암호화.
- HS256 - HMAC으로 암호화된 SHA256값.

- 웹브라우저 저장소에 저장됨.
- 클라이언트는 저장된 JWT를 서버에 보냄.
- 서버는 유효한 토큰인지 확인.

  - header, payload, 비밀키를 암호화를 해보고 받은 값과 같으면 유효한 토큰

- 토큰값 검증만 하면 되므로 세션을 사용할 필요가 없음.

### Bearer Token

- httpBasic() - header의 Authorization:ID,PASSWORD를 담음,
- Bearer Token - header의 Authorization:Token을 담음.
  - token은 유효시간이 있어서 탈취당해도 비교적 안전.

### 어디에 쓰는가?

### gradle

```groovy
    implementation 'io.jsonwebtoken:jjwt:0.9.1'
    //
    implementation 'io.jsonwebtoken:jjwt-api:0.11.2'
    implementation 'io.jsonwebtoken:jjwt-impl:0.11.2'
    implementation 'io.jsonwebtoken:jjwt-jackson:0.11.2'
```

---

## 출처

- JWT 토큰이란?? - <https://velog.io/@syoung125/JWT-%ED%86%A0%ED%81%B0%EC%9D%B4%EB%9E%80>
- Spring Boot에서 JWT 사용하기 - <https://shinsunyoung.tistory.com/110>
- [Spring] Spring Security + JWT 로그인 - <https://velog.io/@shinmj1207/Spring-Spring-Security-JWT-%EB%A1%9C%EA%B7%B8%EC%9D%B8>
- https://ko.wikipedia.org/wiki/RFC - <https://ko.wikipedia.org/wiki/RFC>
- OAuth2.0 + JWT를 사용한 토큰 기반 서버 인증 구현하기 - <https://zkdlu.tistory.com/12>
- Spring Boot Security + JWT + MySQL Hello World Example -
  <https://www.javainuse.com/spring/boot-jwt>
- Spring boot jwt 로그인 구현 - <https://samtao.tistory.com/49>
