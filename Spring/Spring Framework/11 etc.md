# ETC

## Resources

- 리소스 인터페이스
- java.net.URL을 스프링 프레임워크에 맞게 추상화 한 것

- 주요 메서드

  - InputStream getInputStream() - 리소스츨 찾아 열고 스트림 반환.
  - boolean exists()
  - boolean isOpen()
  - String getDescription() - 리소스 설명(파일 이름, 리소스 URL)

- 주요 구현체
  - UrlResource
    - java.net.URL 을 참고.
    - http, https, ftp, file, jar 지원
  - ClassPathResource
    - classpath를 통해 가져온 리소스
    - 지원하는 접두어가 classpath: 임
  - FileSystemResource
    - 파일 시스템 경로를 통해 가져온 리소스
  - ServletContextResource
    - 웹 애플리케이션 루트 경로를 통해 가져온 리소스

### 리소스 읽어오기

- Resource의 타입은 **resource 문자열**과 **ApplicationContext의 타입**에 따라 결정

- ApplicationContext

  - `var ctx = new ClassPathXmlApplicationContext("app.xml");`
    - classpath 기준으로 리소스(app.xml)를 찾음.
  - `var ctx = new FileSystemXmlApplicationContext("app.xml");`
    - 파일 시스템 기준으로 리소스(app.xml)를 찾음.

> 스프링부트는 기본적으로 WebApplicationContext. 아마도?

- Resource strings

  | Prefix     | Example                        | Explanation                                                               |
  | ---------- | ------------------------------ | ------------------------------------------------------------------------- |
  | classpath: | classpath:com/myapp/config.xml | Loaded from the classpath.                                                |
  | file:      | file:///data/config.xml        | Loaded as a URL from the filesystem. See also FileSystemResource Caveats. |
  | https:     | https://myserver/logo.png      | Loaded as a URL.                                                          |
  | (none)     | /data/config.xml               | **Depends on the underlying ApplicationContext.**                         |

- 예시

  ```java
  @Autowired
  ResourceLoader resourceLoader;

  @Override
  public void run(ApplicationArguments args) throws Exception {
      Resource resource = resourceLoader.getResource("test.txt");
      System.out.println(resource.exists());
      System.out.println(Files.readString(Path.of(resource.getURI())));
  }
  ```

  - ResourceLoader는 ApplicationContext 상위 인터페이스임.
  - 자동 주입이 가능.

## Validation

- org.springframework.Validation.Validator
- 애플리케이션에서 사용하는 객체를 검증하기 위한 인터페이스

- Validator

```java
public class Person {
    private String name;
    private int age;
}
```

```java
public class PersonValidator implements Validator {
    public boolean supports(Class clazz) {
        return Person.class.equals(clazz);
    }

    public void validate(Object obj, Errors e) {
        ValidationUtils.rejectIfEmpty(e, "name", "name.empty");
        Person p = (Person) obj;
        if (p.getAge() < 0) {
            e.rejectValue("age", "negativevalue");
        } else if (p.getAge() > 110) {
            e.rejectValue("age", "too.darn.old");
        }
    }
}
```

- boolean supports(Class clazz)
  - Class를 Validator가 검증할 수 있는가?
  - 검증의 대상인지 확인하는 메서드.
- void validator(Object obj, org.springframework.validation.Errors e)
  - 오브젝트를 검증
  - 검증 오류시 에러 등록.
  - ValidationUtils로 편리하게 검증 가능.
- rejectValue(검증 필드, 에러 문구)

  - 에러 등록.

- 예시 코드

```java
personValidator.validate(person, errors);

errors.getAllErrors().forEach(e -> {
    Arrays.stream(e.getCodes()).forEach(System.out::println);
    System.out.println(e.getDefaultMessage());
});
```

### Java Bean Validation

- 어노테이션 방식의 Bean Validation
- Java EE 표준 스펙
- <https://beanvalidation.org/>

  ```java
  public class PersonForm {

      @NotNull
      @Size(max=64)
      private String name;

      @Min(0)
      private int age;
  }
  ```

- Configuring a Bean Validation Provider

  - 스프링 부트 2.0.5부터는 자동.

  ```java
  import org.springframework.validation.beanvalidation.LocalValidatorFactoryBean;

  @Configuration
  public class AppConfig {

      @Bean
      public LocalValidatorFactoryBean validator() {
          return new LocalValidatorFactoryBean();
      }
  }
  ```

- Injecting a Validator

```java
import org.springframework.validation.Validator;

@Service
public class MyService {

    @Autowired
    private Validator validator;
}
```

```java
validator.validate(personForm, errors);
```

## Spring Expression Language (SpEL)

- 런타임에 오프젝트 그래프를 조작 및 쿼리하는 표현 언어.
- 스프링 3.0

```java
ExpressionParser parser = new SpelExpressionParser();
// invokes 'getBytes().length'
Expression exp = parser.parseExpression("'Hello World'.bytes.length");
int length = (Integer) exp.getValue();
```

```java
Expression exp = parser.parseExpression("new String('hello world').toUpperCase()");
String message = exp.getValue(String.class);
```

- XML
  - (생략)
- @Value

  - 필드, 메소드, 메소드, 생성자 매개변수에 적용 가능
  - `#{ }` - 표현식
  - `${ }` - 프로퍼티
    - `${user.region}` == `#{ systemProperties['user.region'] }`

  ```groovy
  my.value = 100
  ```

  ```java
  @Component
  public class Sample {
    private int data = 200;
  }
  ```

  ```java
  @Value("#{1 + 1}")
  int value;            // 2

  @Value("#{'hello ' + 'world'}")
  String greeting;      // hello world

  @Value("#{1 eq 1}")
  boolean trueOrFalse;  // true

  @Value("hello")
  String hello;         // hello

  @Value("${my.value}")
  int myValue;          // 100

  @Value("#{${my.value} eq 100}")
  boolean isMyValue100; // true

  @Value("#{'spring'}")
  String spring;        // spring

  @Value("#{sample.data}") // Bean References
  int sampleDate;       // 200
  ```

- Language Reference

  - <https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#expressions-language-ref>

- 활용
  - @ConditionalOnExpression 애노테이션
    - @ConditionalOn - 선택적으로 빈을 등록하거나 빈 설정 파일을 읽어들일 때
    - Expression 기반으로 빈을 선별 가능.
  - 스프링 시큐리티
    - 메소드 시큐리티, @PreAuthorize, @PostAuthorize, @PreFilter, @PostFilter
    - 시큐리티에서 사용되는 함수들은 EvaluationContext에서 오는 것이다.
    - EvaluationContext로 Bean을 만들어주면 빈이 제공하는 함수들을 쓸 수 있다.
  - 스프링 데이터
    - @Query
      - 메서드에서 받은 파라미터 인자에 들어있는 필드 값을 참조
      - 인덱스 기반으로 참조
  - Thymeleaf

## Null-safety

- org.springframework.lang
- Spring framework 5

  - @Nullable: 리턴이나 필드에 null 허용.
  - @NonNull: 리턴이나 필드에 null 허용하지 않음.
  - @NonNullApi: 패키지 범위의 매개변수나 리턴 값에 NonNull
  - @NonNullFields: 패키지 범위의 필드에 NonNull

## Data Buffers and Codecs

- Java NIO(New I/O) provides
  - DataBufferFactory - data buffer 생성 추사화
  - DataBuffer - 풀 될 수 있는 byte buffer
  - DataBufferUtils - data buffers를 위한 유틸리티 메서드
  - Codecs - data buffer streams을 상위 객체로 디코딩, 인코딩.

```java
DataBuffer buffer = factory.allocateBuffer();
boolean release = true;
try {
    // serialize and populate buffer..
    release = false;
}
finally {
    if (release) {
        DataBufferUtils.release(buffer);
    }
}
return buffer;
```

## Logging

- <https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#features.logging>

- Log Format

  ```text
  2019-03-05 10:57:51.112  INFO 45469 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet Engine: Apache Tomcat/7.0.52
  ```

  - 날짜 | 시간 | LogLevel | Process ID | --- | Thread name | Logger name | The log message.

- Color-coded Output

  - `spring.output.ansi.enabled`
    - 터미널이 ANSI를 지원하면 컬러로 출력.
    - 프로퍼티에 설정.

- File Output

  - logging.file.name - 로그파일 지정
  - logging.file.path - 디렉터리 지정.
  - 출력 기본 값 - error, warn, info
  - 파일과 디렉터리 모두 지정하지 않으면 콘솔에만 출력.

- Log Level

  ```groovy
  logging.level.<logger-name>=<level>
  ```

  ```groovy
  logging.level.root=warn
  logging.level.org.springframework.web=debug
  logging.level.org.hibernate=error
  ```

  - TRACE, DEBUG, INFO, WARN, ERROR, FATAL
    - 오른쪽으로 갈수록 높은 레벨.
  - 설정한 레벨이상의 로그가 출력됨.
  - OFF - 로그 출력 끄기

### 사용

- slf4j - 인터페이스

  - 구현체

    - **logback**
    - log4j

- Logger 객체 선언

  ```java
  public class MyBean {
      private final Log log = LogFactory.getLog(getClass());
      // ...
  }
  ```

  - @Slf4j - lombok 어노테이션
    - `private static final org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(LogExample.class);` 코드를 생성 함.

  ```java
  @Slf4j
  public class MyBean {
      // ...
  }
  ```

- 사용

  ```java
  log.info("메시지");
  ```

---

## 출처

- [Spring] 스프링 Resource 추상화( Spring Resource Abstraction )- <https://engkimbs.tistory.com/724>
- [스프링 프레임워크 핵심 기술] Resource / Validation - <https://dailyheumsi.tistory.com/194?category=874866>
- Resource 추상화 - <https://yadon079.github.io/2021/spring/resource-abstraction>
- [Spring] @Valid와 @Validated를 이용한 유효성 검증의 동작 원리 및 사용법 예시 - (1/2) - <https://mangkyu.tistory.com/174>
- Validation 어디까지 해봤니? - <https://meetup.toast.com/posts/223>
- [SpringBoot] Spring Validation을 이용한 유효성 검증 - <https://velog.io/@_koiil/SpringBoot-Spring-Validation%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%A6%9D>
- Spring @Valid 어노테이션으로 파라미터 검증하기 - <https://tweety1121.tistory.com/170>
- [Spring] Spring Null 처리 하는 법 (Null-safety) - <https://sujl95.tistory.com/11>
- Spring Null-Safety Annotations - <https://www.baeldung.com/spring-null-safety-annotations>
