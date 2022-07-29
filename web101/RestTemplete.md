# RestTemplete

## RestTemplate란?

- deprecated 될 예정
- 블럭킹

## WebClient

- Spring 5에 등장
- 논블럭킹
- 의존성

  ```groovy
  implementation 'org.springframework.boot:spring-boot-starter-webflux'
  ```

- immutable

```java
WebClient webClient = WebClient.create(String baseUrl);
```

```java
String NaverApiUrl = "https://naveropenapi.apigw.ntruss.com";
WebClient webClient = WebClient.create(NaverApiUrl);
Mono<String> mono = webClient.get()
        .uri(uriBuilder -> uriBuilder.path("/map-geocode/v2/geocode")
                .queryParam("query", street)
                .build())
        .header("X-NCP-APIGW-API-KEY-ID", apiKey.getNaverClientId())
        .header("X-NCP-APIGW-API-KEY", apiKey.getNaverClientSecret())
        .exchangeToMono(clientResponse -> clientResponse.bodyToMono(String.class));
String block = mono.block();
```

---

## 출처

- 스프링 RestTemplate - <https://blog.naver.com/hj_kim97/222295259904>
- Spring WebClient 사용법 - <https://medium.com/@odysseymoon/spring-webclient-%EC%82%AC%EC%9A%A9%EB%B2%95-5f92d295edc0>
- [Spring Web Reactive] 2. WebClient - 2.1. 구성 - <https://araikuma.tistory.com/831>
- 토리맘의 한글라이즈 프로젝트 - <https://godekdls.github.io/Reactive%20Spring/webclient/#21-configuration>
