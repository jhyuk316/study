# 일단 적어

## REST

- Representational state transfer

  - 자원(RESOURCE) - URI
  - 행위(Verb) - HTTP METHOD
  - 표현(Representations)

- 특징
  - Uniform (유니폼 인터페이스)
  - Stateless (무상태성)
  - Cacheable (캐시 가능)
  - Self-descriptiveness (자체 표현 구조)
  - Client - Server 구조
  - 계층형 구조

### RESTful

- REST의 기본 원칙을 잘 지킨 서비스 디자인.

  - URI는 **정보의 자원**을 표현
  - 자원에 대한 **행위는 HTTP Method(GET, POST, PUT, DELETE)**로 표현

- REST API 제대로 알고 사용하기 - <https://meetup.toast.com/posts/92>

- REST 아키텍처를 훌륭하게 적용하기 위한 몇 가지 디자인 팁 - <https://spoqa.github.io/2012/02/27/rest-introduction.html>

## Spirng

### TestProperty 설정

- Proerties
  - `@TestPropertySource(location = "classpath:application-test.properties")`
- YML 설정법
  - `@TestPropertySource(properties = {"spring.config.location = classpath:application-test.yml"})`

### assertj

- AssertJ Exception Assertions - <https://www.baeldung.com/assertj-exception-assertion>

### Oauth2

- ClientRegistrationRepository ERROR
- [Error] 소셜 로그인 구현시 oauth client 관련 오류 - <https://4ngeunlee.tistory.com/370>

### @component

- 어노테이션
- spring에서 관리되는 가장 기본적인 객체를 표기
- scan-auto-detection과 dependency injection을 사용하기 위해서 사용.

- @Component
  - @Controller - Web MVC 코드에 사용되는 어노테이션
  - @Repository - Persistence Layer와 1:1 매칭
  - @Service - 비지니스 로직, respository레이어를 호출.

## ORM(Object Relational Mapping)

- ORM이란?

  - 어플리케이션의 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑해주는 것을 의미
  - 즉, java 클래스와 BD의 테이블 매핑
  - 객체지향 프로그래밍과 관계형 데이터베이스의 차이로 발생하는 제약사항을 해결해주는 역할을 수행
  - JPA, Hibernate 등이 있음(persistent API)

- 장점

  - SQL 쿼리가 아닌 직관적인 코드로 데이터를 조작할 수 있음.
  - 재사용 및 유지보수가 편리
  - DBMS에 대한 종속성이 줄어듬

- 단점

  - 복잡한 경우 ORM만으로 구현하기 어려움.
    - 직접 쿼리를 구현하지 않아 복잡한 설계가 어려움.
  - 잘못 구현할 경우 속도 저하 발생.
  - 대형 쿼리는 별도의 튜닝이 필요.

### JPA

- JPA란?
  - JAVA Persistance API - ORM과 관련된 인터페이스의 모음.
  - JAVA 진영의 표준 ORM
  - ORM은 큰 개념, JPA는 더 구체화된 스펙

### Hibernate

- ORM Framework
- JPA의 구현체 중 하나.

- [DB] 하이버네이트(Hibernate)란? - <https://livenow14.tistory.com/70>
- 하이버네이트 쉽게 입문하기 (기초)-환경설정,입력조회 개발 - <https://bcho.tistory.com/906>

### Spring Data JPA

- Spirng Framework에서 JPA를 편리하게 사용할 수 있게 지원하는 라이브러리.

  - CRUD 처리용 인터페이스 제공
  - Repersitory 개발 시 인터페이스만 작성하면 구현 객체를 동적으로 생성해서 주입.
  - 데이터 접근 계층 개발시 인터페이스만 작성해도 됨.

- [배워보자 Spring Data JPA] Spring Data JPA 의 기본과 프로젝트 생성 - <https://wonit.tistory.com/464>
- [스프링부트 (4)] Spring Boot DataBase 연동하기 (MariaDB, MyBatis, HikariCP) - <https://goddaehee.tistory.com/205>
- [Spring Boot] MariaDB + JPA 연동하기 - <https://wecandev.tistory.com/71>
- [Database] Docker 로 MariaDB 설치하기 - <https://wecandev.tistory.com/63>
- Spring Boot JPA로 MariaDB 연동 - <https://gofnrk.tistory.com/20>
- Spring Boot (게시판) - 2 | 데이터베이스(MariaDB) 연동 및 JPA CRUD - <https://kitty-geno.tistory.com/122>
- [JPA] jpa 관련 application.properties 설정 - <https://m.blog.naver.com/writer0713/221536526190>

### 엔티티

- [JPA] 엔티티와 매핑. @Entity, @Table, @Id, @Column.. - <https://data-make.tistory.com/610>

### JPA 팁

- JPA 선호하는 패턴 - <https://www.popit.kr/jpa-%EC%84%A0%ED%98%B8%ED%95%98%EB%8A%94-%ED%8C%A8%ED%84%B4/>

### Pagination

- Pageable을 이용한 Pagination을 처리하는 다양한 방법 - <https://tecoble.techcourse.co.kr/post/2021-08-15-pageable/>
- [Spring] Spring Data JPA에서 Paging 간단하게 구현하는 법 - <https://devlog-wjdrbs96.tistory.com/414>
- REST Pagination in Spring - <https://www.baeldung.com/rest-api-pagination-in-spring>

### indexing

- [SQL] Index(인덱스) - <https://velog.io/@gillog/SQL-Index%EC%9D%B8%EB%8D%B1%EC%8A%A4>
- 성능 향상을 위한 SQL 작성법 - <https://d2.naver.com/helloworld/1155>
- 페이징 성능 향상 기법 MSSQL 쿼리 - <https://jhappy.tistory.com/entry/%ED%8E%98%EC%9D%B4%EC%A7%95-%EC%84%B1%EB%8A%A5-%ED%96%A5%EC%83%81-%EA%B8%B0%EB%B2%95-MSSQL-%EC%BF%BC%EB%A6%AC>

## H2

- [Spring Boot JPA] JPA를 사용하기 위해 꼭 필요한 Dialect(방언)에 대해 알아보자. - <https://firework-ham.tistory.com/106>
- [Spring boot] Test H2 DB설정 - <https://velog.io/@jeong-god/Springboot-Test-H2-DB%EC%84%A4%EC%A0%95>

## mariaDB

- MariaDB 데이터베이스 생성 - <https://jdm.kr/blog/132>

## test

- Junit5(jupiter) Controller 테스트코드 작성법 (WebMvcTest, MockMvc, MockBean을 사용한 테스트) - <https://frozenpond.tistory.com/82>

### RestTemplate

- 스프링 RestTemplate - <https://advenoh.tistory.com/46>

## OpenAPI

### swagger

- api 설명 페이지 자동 생성
- gradle 설정

```text
implementation 'io.springfox:springfox-boot-starter:3.0.0'
implementation 'io.springfox:springfox-swagger-ui:3.0.0'
```

- SpringBoot 2.6 이상 springfox-swagger3.0 적용 시 에러 해결

  - <https://velog.io/@ohjinseo/SpringBoot-2.6-%EC%9D%B4%EC%83%81-springfox-swagger3.0-%EC%A0%81%EC%9A%A9-%EC%8B%9C-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0>
  - application.properties에서 spring.mvc.pathmatch.matching-strategy=ant_path_matcher로 default 값을 변경한다.
  - spring boot의 버전을 2.5.x로 낮춘다.

- OpenAPI Specification 3(OAS 3)에 맞게 문서 작성하기 - <https://blog.sonim1.com/217>
- OpenAPI 와 Swagger/redoc 란 - <https://www.lesstif.com/software-engineering/openapi-swagger-redoc-106857823.html>
- OpenAPI를 사용한 REST API 문서 생성 - <https://www.ibm.com/docs/ko/was-liberty/base?topic=liberty-generating-rest-api-documentation-openapi>
- Spring Rest Docs를 Markdown으로 작성하기 - <https://jojoldu.tistory.com/289>
- API 문서 자동화 - Spring REST Docs 팔아보겠습니다 - <https://tecoble.techcourse.co.kr/post/2020-08-18-spring-rest-docs/>
- Swagger와 Spring Restdocs의 우아한 조합 (by OpenAPI Spec) - <https://taetaetae.github.io/posts/a-combination-of-swagger-and-spring-restdocs/>
- Spring Rest Docs 적용 - <https://techblog.woowahan.com/2597/>

## DB

- Spring JPA 다대다 설정 및 성능 주의 ( Many To Many ) - <https://happyer16.tistory.com/entry/Spring-JPA-%EB%8B%A4%EB%8C%80%EB%8B%A4-%EC%84%A4%EC%A0%95-%EB%B0%8F-%EC%A3%BC%EC%9D%98-Many-To-Many>
