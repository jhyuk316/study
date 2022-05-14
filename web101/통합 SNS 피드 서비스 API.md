# 통합 SNS 피드 서비스 API

- 통합 SNS 피드 서비스 개발
- 일반 사용자가 소셜 로그인을 통해 페이스북, 트위터, 인스타그램 등의 개인 피드를 받아오면 통합 피드를 보여주는 서비스.

## 시연과 설명

### 페이스북 소셜 로그인 기능(OAuth2)

- index페이지에서 가능.

### 사용자 인증을 위한 토큰 발행(JWT)

- 소셜 로그인 시 발행된 token이 바로 보임.

### 사용자의 최신 피드를 통합해 보여주는 API

### 피드 정보를 강제 풀링 요청 API

- /posts

## IndexController

- Web page 관련 controller
- / - index페이지 반환, index 페이지에서 로그인요구
- /login - 스프링 시큐리티 권환 요구시 /login으로 반환 되므로 이페이지를 index로 연결
- /test/login - 로그인 되었을테 인증 결과를 확인 하기 위한 것.

## ApiController

- /posts
  - 연결된 Facebook의 post를 가져옴.

## DTO

- API통신을 하기위한 클래스

- UserDTO - User의 정보를 담기 위한 DTO

  - provider - 페이스북 같은 프로바이더를 기록
  - providerId - 각 프로바이더에서 쓰이는 ID값(user의id가 아님)을 저장.

- FacebookDTO - 페이스북 응답을 받기 위한 DTO

  - PostDTO의 리스트를 가짐

- PostDTO - 페이스북 응답의 포스트 정보를 받기 위한 DTO
  - created_time - 생성일자
  - message - 메시지
  - object_id - 이미지의 id를 받아옴

## Model

- UserEntity - user정보 저장

  - id - DB식별자
  - Email - 유저 식별자, email이 같으면 통합 SNS의 유저가 같은 것으로 판단.
  - name
  - FacebookID - 페이스북의 식별자. post을 가져올 때 사용.
  - FacebookAccessToken - Oauth2를 통해서 발급받은 AccessToken을 가지고 있음.
  - InstagramID - 인스타그램의 식별자. post을 가져올 때 사용.

- PostEntity - 피드 정보 저장.

## config

## OAuth2

- spring-boot-starter-oauth2-client를 활용해 OAuth2인증
- 리소스 서버에 웹사이트, 개발자 등록을 해야함.
- 발급받은 client-id, client-secret을 입력.
- 필요한 권한을 scope에 설정.
- redirect-uri를 설정.

### CustomOAuth2UserService

- 인증 서버가 보내주는 OAuth2 인증데이터가 모두 다르므로 통합해서 인증할 서비스.
- OAuth2User데이터를 받아서 공통된 OAuthAttributesDTO를 생성하고 이후 이를 사용.
- 유저의 Email정보를 확인해서 이미 있는 email이면 갱신하고 없는 emil이면 추가(회원가입)
- DefalutOAuth2User로 반환.

#### OAuthAttributesDTO

- OAuth2user정보를 저장할 DTO
- 각 인증서버 마다 다른 정보를 실제로 매핑해주는 기능을 가짐.

### OAuth2SuccessHandler

- 인증이 성공하면 호출 되는 헨들러.
- 인증정보를 받아서 JWT토큰을 발행함.
- JWT를 Response에 반환.

## JWT

- JSON Web Token

  - HEADER
  - PAYLOAD
  - VERIFY SIGNATURE

- UsernamePasswordAuthenticationFilter 필터 전에 JwtAuthFilter 삽입

### JwtAuthFilter

- 발급한 JWT 토큰을 검증하여 인증하는 서비스.
- TokenService에게 Token발행과 검증을 요청

### TokenService

- `Token generateToken(String uid)`- uid(email)을 받아서 페이로드에 저장하고 토큰 발행
- `boolean verifyToken(Token token)` - 받은 토큰을 검증.

### Token

- AccessToken과 RefreshToken을 가지고 있는 DTO.

---

## 대략적인 필터 순서

1. HeaderWriterFilter - 헤더 검사

2. CorsFilter - 허가된 사이트나 클라이언트인가?

3. CsrfFilter - 리소스 변경요청시 내가 보냈던 리소스인가?

4. LogoutFilter - 로그아웃하겠다는 것인가?

5. OAuth2AuthorizationRequestRedirectFilter - Oauth2인증

6. OAuth2LoginAuthenticationFilter

7. UsernamePasswordAuthenticationFilter

8. DefaultLoginPageGeneratingFilter

9. DefaultLogoutPageGeneratingFilter

10. BearerTokenAuthenticationFilter

11. BasicAuthenticationFilter

12. SecurityContextHolderAwareRequestFilter

13. RememberMeAuthenticationFilter

14. AnonymousAuthenticationFilter

15. OAuth2AuthorizationCodeGrantFilter

16. SessionManagementFilter

17. ExceptionTranslationFilter

18. FilterSecurityInterceptor
