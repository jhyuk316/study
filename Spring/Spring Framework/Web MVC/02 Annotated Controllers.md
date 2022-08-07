# Annotated Controllers

- [1. Declaration](#1-declaration)
- [2. Request Mapping](#2-request-mapping)
  - [2.1. URI patterns](#21-uri-patterns)
- [3. Handler Methods](#3-handler-methods)
  - [3.1. Method Arguments](#31-method-arguments)
  - [3.2. Return Values](#32-return-values)
  - [3.3. ~~@ModelAttribute~~](#33-modelattribute)
  - [3.4. @SessionAttributes](#34-sessionattributes)
- [4. ~~Model~~](#4-model)
- [5. ~~DataBinder~~](#5-databinder)
- [6. Exceptions](#6-exceptions)
  - [6.1. REST API exceptions](#61-rest-api-exceptions)
- [7. Controller Advice](#7-controller-advice)
- [출처](#출처)

## 1. Declaration

- @Controller
  - MVC 컨트롤러
  - 컴포넌트 스캔의 대상
- @RestController
  - @Controller + @ResponseBody
  - 모든 메소드에 @ResponseBody를 단 효과.

## 2. Request Mapping

```java
@RestController
@RequestMapping("/persons")
class PersonController {

    @GetMapping("/{id}")
    public Person getPerson(@PathVariable Long id) {
        // ...
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public void add(@RequestBody Person person) {
        // ...
    }
}
```

- @GetMapping
- @PostMapping
- @PutMapping
- @DeleteMapping
- @PatchMapping

### 2.1. URI patterns

- AntPathMatcher

  - 5.3 이전 스프링 MVC의 방식 - 지금도 기본값.
  - ?
    - 1 글자
    - /resources/ima?e.png
  - \*
    - 0개 이상의 글자
    - /resources/\*.png
  - \*\*
    - 0개 이상의 path segments(/경로/)
    - 끝에서만 사용가능.
    - /pages/{\*\*}
  - {spring:[a-z]+}
    - regex를 변수 spring으로 받음
    - /projects/{project:[a-z]+}/versions

- PathPattern

  - 웹 추천 방식
  - WebFlux은 PathPattern만 사용.
  - AntPathMatcher + @
  - \*\* - 중간에도 사용가능.
  - {spring} - 1개의 path segments를 변수 spring으로 받음.
  - {\*spring} - 0개 이상의 path segments를 변수 spring으로 받음.

```java
@Controller
@RequestMapping("/owners/{ownerId}")
public class OwnerController {

    @GetMapping("/pets/{petId}")
    public Pet findPet(@PathVariable Long ownerId, @PathVariable Long petId) {
        // ...
    }
}
```

- @PathVariable("customId")

  - URI 변수명을 명시적 표기.
  - ("customId") - 자바 8 부터는 변수명과 같으면 생략 가능.

- 접미사 매칭 - 마지막에 \*을 넣는 것
  - reflected file download (RFD) 공격의 위험이 있음.
  - 확장자를 \*로 매칭하는 것은 차단되어 있음.

## 3. Handler Methods

### 3.1. Method Arguments

- javax.servlet.ServletRequest, javax.servlet.ServletResponse
  - HttpServletRequest, HttpServletResponse
- javax.servlet.http.HttpSession

- @PathVariable
  - URI 템플릿 변수
- @RequestParam

  - 서블릿 Request 매개변수
  - @RequestParam(required=true) - 필수 값이 기본 값.
  - @RequestParam(required=true) - false 설정시 생략 가능.
    - @RequestParam(required=true, defualt="1") - 디폴트 값 설정 가능.

  ```java
  // /pets?petId=1
  @GetMapping("/pets")
  public String setupForm(@RequestParam("petId") int petId, Model model) {
      Pet pet = this.clinic.loadPet(petId);
      model.addAttribute("pet", pet);
      return "petForm";
  }
  ```

- @RequestHeader - request headers

  ```http
  Keep-Alive              300
  ```

  ```java
  @GetMapping("/demo")
  public void handle(@RequestHeader("Keep-Alive") long keepAlive) {
      //...
  }
  ```

- @CookieValue - 쿠키
- @RequestBody - HTTP request body
  - HttpMessageConverter에의해 역직렬화된 오브젝트를 받음.
  - @Valid, @validated로 검증 가능.
- HttpEntity\<B\> - request headers, body

- @ModelAttribute - 모델의 에트리뷰트

  ```java
  @PostMapping("/owners/{ownerId}/pets/{petId}/edit")
  public String processSubmit(@ModelAttribute("pet") Pet pet, BindingResult result) {
      if (result.hasErrors()) {
          return "petForm";
      }
      // ...
  }
  ```

  - 모델 검색
  - @SessionAttributes이 클래스에 달려 있으면 HTTP 세션에서 검색
  - 기본 생성자를 사용해 인스턴스화
  - ModelAttribute 인스턴스를 얻은 후 데이터 바인딩이 적용
    - 바인딩 실패시 BindException 발생
    - 바인딩 결과를 BindingResult로 받을 수 있음.
    - 바인딩 후 유효성 검증도 가능 - **@Valid**

- Errors, BindingResult - 검증의 errors, 검증 파라미터 바로 뒤에 선언해야 함.

### 3.2. Return Values

- @ResponseBody
  - HttpMessageConverter로 response body를 serialized해서 리턴.
  - @Valid, @validated로 검증 가능.
- ResponseEntity - @ResponseBody + status + headers
- String - `ViewResolver`에 의해 resolved 될 view name을 리턴

### 3.3. ~~@ModelAttribute~~

- 메소드 위에 붙여서 사용 가능
  - View에서 사용할 데이터를 설정하는 용도로 사용
  - @ModelAttribute가 설정된 메소드는 @RequestMapping 어노테이션이 적용된 메소드보다 먼저 호출
  - @ModelAttribute 메소드 실행 결과로 리턴되는 객체는 자동으로 Model에 저장
  - @ModelAttribute 메소드 실행 결과로 리턴된 객체를 View 페이지에서 사용 가능
  - @SessionAttributes이 클래스에 달려 있으면 HTTP 세션에서 검색

```java
@RequestMapping(value = "getBoardList.do")
public String getBoardList(Model model){
    model.addAttribute("post", new Post());
    return "boardList";
}

@ModelAttribute("commonCodeMap")
public Map<String, String> commonCodeMap(){
    Map<String, String> commonCodeMap = new HashMap<>();
    commonCodeMap.put("code1", "codeValue1");
    return commonCodeMap;
}
```

### 3.4. @SessionAttributes

- 컨트롤러 전역에 걸쳐 세션을 임시 저장소로 사용 가능

```java
@Controller
@SessionAttributes("pet")
public class EditPetForm {
    @PostMapping("/pets/{id}")
    public String handle(Pet pet, BindingResult errors, SessionStatus status) {
        if (errors.hasErrors) {
            // ...
        }
        status.setComplete();
        // ...
    }
}
```

- @ModelAttribute로 리턴된 값을 저장.

- @SessionAttribute

  - 키 값으로 세션의 값을 바인딩

  ```java
  @RequestMapping("/")
  public String handle(@SessionAttribute User user) {
      // ...
  }
  ```

## 4. ~~Model~~

- ~~@ModelAttribute~~ 랑 같은 내용

## 5. ~~DataBinder~~

## 6. Exceptions

- @ExceptionHandler는 Controller계층에서 발생하는 예외를 잡아서 메서드로 처리해주는 기능
- @ExceptionHandler(받을 예외)
  - 생략하면 모든 예외.
  - 최대한 구체적인 예외를 설정할 것.

```java
@Controller
public class SimpleController {
    @ExceptionHandler({FileSystemException.class, RemoteException.class})
    public ResponseEntity<String> handle(Exception ex) {
        // ...
    }
}
```

### 6.1. REST API exceptions

- 예외 발생시 response body에 오류 세부 정보를 포함해야 함.

## 7. Controller Advice

- 전역 컨트롤러
- @ControllerAdvice, @RestControllerAdvice
- @ExceptionHandler, @InitBinder, @ModelAttribute등을 모든 컨트롤러에서 쓸 수 있음.
- @ControllerAdvice(annotations = RestController.class)
  - 괄호 안에 타겟을 설정 할 수 있음. AOP?
  - 예시는 모든 @RestController에 적용.

---

## 출처

- Controller 핸들러 메서드의 Argument 알아보기 - <https://itvillage.tistory.com/41>
- 핸들러 메소드 - 1 (스프링 MVC - 5) - <https://hongchan.tistory.com/30>
- [Spring] Spring MVC: Controller에서 parameter를 받아오는 방법 - <https://ooeunz.tistory.com/99>
- Spring MVC - Handler Methods : Return Type Values - <https://goodgid.github.io/Spring-MVC-Return-Type/>
- [Spring] @ModelAttribute, @RequestAttribute - <https://cornswrold.tistory.com/316>
- Spring MVC / HttpSession, @SessionAttribute, @SessionAttributes - <https://ecsimsw.tistory.com/entry/Spring-MVC-HttpSession-SessionAttribute-SessionAttributes>
