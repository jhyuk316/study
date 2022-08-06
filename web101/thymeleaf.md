# Thymeleaf

## 템플릿 엔진(Template Engine)

![Template_Engine](images/Template_Engine.png)

- *템플릿*을 *데이터 모델*과 결합하여 결과 문서(HTML)을 생성하는 소프트웨어

- 많은 코드를 줄일 수 있음.
- 재사용성이 높음.
- 유지보수가 용이함.

### 서버 사이드 템플릿 엔진 vs 클라이언트 사이드 템플릿 엔진

- Server Side Template Engine

  - 서버에서 DB 혹은 API에서 가져온 데이터를 미리 정의된 Template에 넣어 html을 그려서 클라이언트에 전달
  - 과정
    1. 필요한 데이터 DB에서 가져오거나 API로 받아옴.
    2. 미리 정의된 Template에 해당 데이터를 적절하게 넣어 HTML 생성.
    3. 생성된 HTML을 클라이언트에 전달.
  - Jsp, Thymeleaf

- Client Side Template Engine

  - html 형태로 코드를 작성할 수 있으며, 동적으로 DOM을 그리게 해주는 역할
  - 과정
    1. 클라이언트에서 공통적인 프레임을 미리 template으로 만듬.
    2. 서버에서 필요한 데이터를 받음.
    3. 데이터를 template의 적절한 위치에 replace하고 DOM 객체에 동적으로 그림.
  - Javascript 라이브러리로 랜더링이 끝난 뒤에 서버 통신 없이 화면 변경이 필요할 경우
  - 단일 화면에서 특정 이벤트에 따라 화면이 계속 변경되어야 하는 경우 (SPA)
  - React, Vue

### Spring 추천 템플릿엔진

- Thymeleaf
- FreeMarker - 강력한 기능.
- Groovy Markup
- Mustache
  - 단순 - View만 가능, 로직 없음.
  - 서버사이드, 클라이언트사이드 모두 지원.
  - Intelli J 플러그인 지원.

## Thymeleaf

- JAVA 서버 사이드 템플릿 엔진.
- natural templates
  - HTML 파일로 브라우저에서 출력됨.
    - html 태그에 속성으로 템플릿 기능을 사용
  - static 프로토타입으로 작동할 수 있음.
    - 디자이너가 만든 HTML 파일을 쉽게 타임리프로 변환 가능.
- Spring Framework와 강력한 호환성.
  - OGNL(Object-Graph Navigation Language) 대신 SpringEL사용.
- Intelli J 플러그인 지원은 울티메이트가 필요.

- 설정 추가

  ```groovy
  implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
  ```

- 타임리프 선언

  - xmlns:th - th속성으로 타임리프를 사용하기 위해 선언된 네임스페이스

  ```html
  <html xmlns:th="http://www.thymeleaf.org"></html>
  ```

### th 문법

- `th:xxx`

  - th:xxx가 있으면 서버사이드에서 렌더링 되고 기존 속성을 대치.
  - th:xxx가 없으면 기존 html의 xxx 속성을 그대로 출력.

- th:text

  ```html
  <div th:text="${data}"></div>
  ```

  - ${} - 컨트롤러로부터 받은 모델에 접근

- th:fragment

  ```html
  <head th:fragment="header">
    <link href="/css/jumbotron-narrow.css" rel="stylesheet" />
  </head>
  ```

  - 공통 영역 정의
  - 반복되는 영역을 재사용하게 해줌.

- th:replace="~{파일경로::조각이름}"

  - `<head th:replace="fragments/header :: header">`
  - fragment로 조각화한 공통 영역로 HTML의 해당 영역을 대체.

- th:insert="~{파일경로 :: 조각이름}"

  ```html
  <div th:insert="~{/common/footer :: footerFragment}"></div>
  ```

  - insert는 태그 내로 조각을 삽입하는 방법

- th:block

  ```html
  <th:block th:fragment="footerFragment"> </th:block>
  ```

  - block은 타임리프 표현을 어느 곳에서든 사용할 수 있도록 하는 구문

- th:each

  ```html
  <tr th:each="member : ${members}">
    <td th:text="${member.id}"></td>
    <td th:text="${member.name}"></td>
    <td th:text="${member.address?.city}"></td>
    <td th:text="${member.address?.street}"></td>
    <td th:text="${member.address?.zipcode}"></td>
  </tr>
  ```

  - 반복 출력

- th:href="@{}"

  ```html
  <a href="#" th:href="@{/items/{id}/edit (id=${item.id})}">수정</a>
  ```

  - @{} - 링크표현식
  - 파라미터 쿼리도 생성 가능.
    - `th:href="@{/basic/items/{itemId}(itemId=${item.id}, query='test')}"`
    - http://localhost:8080/basic/items/1?query=test

  ```html
  <a href="#" th:href="@{|/items/${item.id}/edit|}">수정</a>
  ```

  - 리터럴 대체 문법 - |...|
    - 문자와 표현식등을 합쳐서 쓰고자 할 때 사용

- th:with="${}"

  ```html
  <div th:with="”userId" ="${number}”" th:text="”${usesrId}”"></div>
  ```

  - 변수의 값을 재정의

- th:value="${}"

```html
<input type="text" id="userId" th:value="${userId} + '의 이름은 ${userName}" />
```

- input의 value에 값을 넣을 때 사용.

- th:if, th:unless

  ```html
  <tr th:each="member : ${members}">
    <td th:if="${member.id}"></td>
    <td th:text="${member.id}"></td>
    <td th:text="${member.name}"></td>
    <td th:text="${member.address?.city}"></td>
    <td th:text="${member.address?.street}"></td>
    <td th:text="${member.address?.zipcode}"></td>
  </tr>
  ```

## 문제

### Exception evaluating SpringEL expression

```java
@GetMapping("/restaurants/new")
public String createRestaurants(Model model) {
    model.addAttribute("restaurantForm", new RestaurantDTO());
    return "restaurants/createRestaurantForm";
}

@PostMapping("restaurants/new")
public String create(@Valid @ModelAttribute("restaurantForm") RestaurantDTO restaurantForm, BindingResult result) {
    if (result.hasErrors()) {
        System.out.println("result = " + result);
        return "restaurants/createRestaurantForm";
    }

    System.out.println("restaurantForm = " + restaurantForm);

    // restaurantService.save(restaurantForm);
    return "redirect:/";
}
```

- resurantsForm으로 모델을 받기로 했는데.
- @PostMapping("restaurants/new")에서 모델을 제대로 주지 않는 상황.
  - RestaurantDTO가 디폴트 모델 속성이 됨.
  - 수동으로 지정해줘야 함. `@ModelAttribute("restaurantForm")`

---

## 출처

- [Template Engine] 템플릿 엔진(Template Engine)이란 - <https://gmlwjd9405.github.io/2018/12/21/template-engine.html>
- Template Engines for Spring - <https://www.baeldung.com/spring-template-engines>
- FreeMarker vs Groovy vs Mustache vs Thymeleaf - <https://springhow.com/spring-boot-template-engines-comparison/>
- [Spring Boot] Thymeleaf 란? 타임리프 문법 정리 - <https://myeongdev.tistory.com/20>
