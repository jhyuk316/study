# REST Clients

- [1. RestTemplate](#1-resttemplate)
  - [1.1. Initialization](#11-initialization)
  - [1.2. Body](#12-body)
  - [1.3. Message Conversion](#13-message-conversion)
  - [1.4. Jackson JSON Views](#14-jackson-json-views)
- [2. WebClient](#2-webclient)
  - [2.1. Reactor](#21-reactor)
  - [2.2. tutorial](#22-tutorial)
    - [2.2.1. Dependencies](#221-dependencies)
    - [2.2.2. Working with the WebClient](#222-working-with-the-webclient)
- [출처](#출처)

## 1. RestTemplate

- synchronous client
- RestTemplate은 요청당 스레드 모델을 기반으로 하는 Java Servlet API를 사용
- 웹 클라이언트가 응답을 받을 때까지 스레드가 차단
- 애플리케이션은 많은 스레드를 생성하게 되고 스레드 풀이 가득 차고 콘텍스트 스위칭 등으로 성능이 저하됨.

### 1.1. Initialization

```java
RestTemplate template = new RestTemplate(new HttpComponentsClientHttpRequestFactory());
```

```java
String uriTemplate = "https://example.com/hotels/{hotel}";
URI uri = UriComponentsBuilder.fromUriString(uriTemplate).build(42);

RequestEntity<Void> requestEntity = RequestEntity.get(uri)
        .header("MyRequestHeader", "MyValue")
        .build();

ResponseEntity<String> response = template.exchange(requestEntity, String.class);

String responseHeader = response.getHeaders().getFirst("MyResponseHeader");
String body = response.getBody();
```

### 1.2. Body

- RestTemplate에 의해 반환된 Object는 HttpMessageConverter에 의해 변환됨.

```java
Person person = restTemplate.getForObject("https://example.com/people/{id}", Person.class, 42);
```

### 1.3. Message Conversion

- The `spring-web` module contains the `HttpMessageConverter` contract for reading and writing the body of HTTP requests and responses through `InputStream` and `OutputStream`.

### 1.4. Jackson JSON Views

## 2. WebClient

- non-blocking, reactive client

- Reactive
  - 이벤트에 즉각적으로 반응하는 것.
  - non-blocking is reactive
  - Reactive 프레임워크는 이벤트 기반 아키텍처를 사용
  - 반응적 접근 방식은 동기/차단 방식에 비해 더 적은 스레드와 시스템 리소스를 사용하면서 더 많은 논리를 처리

### 2.1. Reactor

- The reactive library of choice for Spring WebFlux.

- Mono - API types to work on data sequences of 0..1
- Flux - API types to work on data sequences of 0..N

### 2.2. tutorial

#### 2.2.1. Dependencies

```groovy
dependencies {
    compile 'org.springframework.boot:spring-boot-starter-webflux'
}
```

#### 2.2.2. Working with the WebClient

1. Creating a WebClient Instance

   ```java
   WebClient client = WebClient.builder()
        .baseUrl("http://localhost:8080")
        .defaultCookie("cookieKey", "cookieValue")
        .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
        .defaultUriVariables(Collections.singletonMap("url", "http://localhost:8080"))
        .build();
   ```

2. make a request

   ```java
   UriSpec<RequestBodySpec> uriSpec = client.post();
   ```

   ```java
   RequestBodySpec bodySpec = uriSpec.uri(
        uriBuilder -> uriBuilder.pathSegment("/resource").build());
   ```

   ```java
   RequestHeadersSpec<?> headersSpec = bodySpec.bodyValue("data");
   ```

   ```java
   ResponseSpec responseSpec = headersSpec.header(
       HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
    .accept(MediaType.APPLICATION_JSON, MediaType.APPLICATION_XML)
    .acceptCharset(StandardCharsets.UTF_8)
    .ifNoneMatch("*")
    .ifModifiedSince(ZonedDateTime.now())
    .retrieve();
   ```

3. handle the response

   ```java
   Mono<String> response = headersSpec.exchangeToMono(response -> {
        if (response.statusCode().equals(HttpStatus.OK)) {
            return response.bodyToMono(String.class);
        } else if (response.statusCode().is4xxClientError()) {
            return Mono.just("Error response");
        } else {
            return response.createException()
                .flatMap(Mono::error);
        }
   });
   ```

   ```java
   Mono<String> response = headersSpec.retrieve()
        .bodyToMono(String.class);
   ```

---

## 출처

- Spring WebClient vs. RestTemplate - <https://www.baeldung.com/spring-webclient-resttemplate>
- Spring 5 WebClient - <https://www.baeldung.com/spring-5-webclient>
