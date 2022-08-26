# etc

- [1. Functional Endpoints](#1-functional-endpoints)
  - [1.1. HandlerFunction](#11-handlerfunction)
  - [1.2. RouterFunction](#12-routerfunction)
- [2. URI Links](#2-uri-links)
  - [2.1. UriComponents](#21-uricomponents)
  - [2.2. URI Encoding](#22-uri-encoding)
  - [2.3. Relative Servlet Requests](#23-relative-servlet-requests)
  - [2.4. Links to Controllers](#24-links-to-controllers)
- [3. Asynchronous Requests](#3-asynchronous-requests)
- [4. CORS](#4-cors)
  - [4.1. Processing](#41-processing)
  - [4.2. @CrossOrigin](#42-crossorigin)
  - [4.3. Global Configuration](#43-global-configuration)
  - [4.4. CORS Filter](#44-cors-filter)
- [5. Web Security](#5-web-security)
- [6. HTTP Caching](#6-http-caching)
  - [6.1. CacheControl](#61-cachecontrol)
  - [6.2. Controllers](#62-controllers)
  - [6.3. Static Resources](#63-static-resources)
  - [6.4. ETag Filter](#64-etag-filter)
- [7. View Technologies](#7-view-technologies)
  - [7.1. Thymeleaf](#71-thymeleaf)
- [8. HTTP/2](#8-http2)
- [출처](#출처)

## 1. Functional Endpoints

- `HandlerFunction` is the equivalent of **the body** of a `@RequestMapping` method in the annotation-based programming model.
  - (컨트롤러 로직?)
- `RouterFunction` is the equivalent of a `@RequestMapping` annotation, but with the major difference that router functions provide not just data, but also behavior.
  - (URL 맵핑, HTTP 메서드 맵핑?)

### 1.1. HandlerFunction

- `ServerRequest` and `ServerResponse` are immutable interfaces that offer JDK 8-friendly access to the HTTP request and response, including headers, body, method, and status code.

### 1.2. RouterFunction

- Router functions are used to route the requests to the corresponding `HandlerFunction`.

## 2. URI Links

### 2.1. UriComponents

- URI 템플릿으로 URI 생성을 도움.

```java
UriComponents uriComponents = UriComponentsBuilder
        .fromUriString("https://example.com/hotels/{hotel}")  // Staitc factory method와 URI 템플릿
        .queryParam("q", "{q}")  // URI 컴포넌트 추가 및 변경.
        .encode() // URI 템플릿과 URI 변수를 Request로 인코딩.
        .build(); // 빌드

// 변수를 확장하고, URI를 얻음.
URI uri = uriComponents.expand("Westin", "123").toUri();
```

```java
URI uri = UriComponentsBuilder
        .fromUriString("https://example.com/hotels/{hotel}")
        .queryParam("q", "{q}")
        .encode()
        .buildAndExpand("Westin", "123")
        .toUri();
```

```java
URI uri = UriComponentsBuilder
        .fromUriString("https://example.com/hotels/{hotel}?q={q}")
        .build("Westin", "123");
```

### 2.2. URI Encoding

- UriComponentsBuilder#encode(): Pre-encodes the URI template first and then strictly encodes URI variables when expanded.
- UriComponents#encode(): Encodes URI components after URI variables are expanded.

### 2.3. Relative Servlet Requests

- 서블릿의 URI 활용

```java
HttpServletRequest request = ...

// Re-uses scheme, host, port, path, and query string...
URI uri = ServletUriComponentsBuilder.fromRequest(request)
        .replaceQueryParam("accountId", "{id}")
        .build("123");
```

### 2.4. Links to Controllers

- 컨트롤러의 URI 활용

```java
@Controller
@RequestMapping("/hotels/{hotel}")
public class BookingController {
    @GetMapping("/bookings/{booking}")
    public ModelAndView getBooking(@PathVariable Long booking) {
        // ...
    }
}
```

```java
UriComponents uriComponents = MvcUriComponentsBuilder
    .fromMethodName(BookingController.class, "getBooking", 21).buildAndExpand(42);
URI uri = uriComponents.encode().toUri();
```

- /hotels/42/bookings/21
- buildAndExpand - 남은 변수에 채워짐.

## 3. Asynchronous Requests

- (비동기는 WebFlux로 해야 하지 않을까? 일단 패스)
- 비동기로 리퀘스트에 응답.

## 4. CORS

- Cross-Origin Resource Sharing - 교차 출처 리소스 공유
- eg. https://domain-a.com의 프런트 엔드 JavaScript 코드가 XMLHttpRequest를 사용하여 https://domain-b.com/data.json을 요청하는 경우.

- 현재 출처 외부의 리소스에 대한 AJAX 호출을 금지
  - 예를 들어 한 탭에는 은행 계좌가 있고 다른 탭에는 evil.com이 있을 수 있습니다. evil.com의 스크립트는 귀하의 자격 증명으로 은행 API에 AJAX 요청을 할 수 없어야 합니다.

### 4.1. Processing

- Spring MVC `HandlerMapping` 구현은 CORS에 대한 내장 지원을 제공
- 교차 출처 요청(즉, Origin 헤더가 있고 요청 호스트와 다름)을 활성화하려면 명시적으로 선언된 일부 CORS 구성이 필요
  - 일치하는 CORS 구성이 없으면 실행 전 요청이 거부됨.

### 4.2. @CrossOrigin

- 교차 출처 요청을 활성화
- 메서드, 클래스 수준의 어노테이션

```java
@CrossOrigin(origins = "https://domain2.com", maxAge = 3600)
@RestController
@RequestMapping("/account")
public class AccountController {

    @GetMapping("/{id}")
    public Account retrieve(@PathVariable Long id) {
        // ...
    }

    @DeleteMapping("/{id}")
    public void remove(@PathVariable Long id) {
        // ...
    }
}
```

- https://domain2.com로부터 온 30분 이내의 요청을 허용.

- @CrossOrigin의 인자가 비어있으면 모든 요청을 허용
  - All origins.
  - All headers.
  - All HTTP methods to which the controller method is mapped.

### 4.3. Global Configuration

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
            .allowedOrigins("https://domain2.com")
            .allowedMethods("PUT", "DELETE")
            .allowedHeaders("header1", "header2", "header3")
            .exposedHeaders("header1", "header2")
            .allowCredentials(true).maxAge(3600);
    }
}
```

### 4.4. CORS Filter

- 스프링 시큐리티 참조.

## 5. Web Security

- 스프링 시큐리티 참조.

## 6. HTTP Caching

- HTTP caching revolves around the `Cache-Control` response header and, subsequently, conditional request headers (such as `Last-Modified` and `ETag`).

### 6.1. CacheControl

```java
CacheControl ccCustom = CacheControl.maxAge(10, TimeUnit.DAYS).noTransform().cachePublic();
```

- private - eg. browser 캐시
- public - eg. proxy 캐시

### 6.2. Controllers

```java
@GetMapping("/book/{id}")
public ResponseEntity<Book> showBook(@PathVariable Long id) {

    Book book = findBook(id);
    String version = book.getVersion();

    return ResponseEntity
            .ok()
            .cacheControl(CacheControl.maxAge(30, TimeUnit.DAYS))
            .eTag(version) // lastModified is also available
            .body(book);
}
```

- 콘텐츠가 변경되지 않았음을 나타내는 경우 빈 본문과 함께 304(NOT_MODIFIED) 응답

### 6.3. Static Resources

- 최적의 성능을 위해 Cache-Control 및 조건부 응답 헤더와 함께 정적 리소스를 제공해야 함.

### 6.4. ETag Filter

- `ShallowEtagHeaderFilter` to add “shallow” eTag values that are computed from the response content
- 대역폭을 절약하고 cpu를 더 씀.

## 7. View Technologies

- The use of view technologies in Spring MVC is pluggable
  > Views have access to all the beans of your application context

### 7.1. Thymeleaf

- [템플릿 엔진과 타임리프](../../../web101/thymeleaf.md) 참조.

## 8. HTTP/2

- Servlet 4를 지원하는 컨테이너와 Spring Framework 5를 사용하면 별다른 애플리케이션 조작 없이 HTTP/2가 사용됨.

---

## 출처

- [스프링 Web Servlet 공식문서 읽기]1. Spring MVC (4) - Functional Endpoints - <https://velog.io/@ybw903/스프링-공식문서-읽기1.-Spring-MVC-4-Functional-Endpoints>
- 교차 출처 리소스 공유 (CORS) - <https://developer.mozilla.org/ko/docs/Web/HTTP/CORS>
