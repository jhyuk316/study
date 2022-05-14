# servlet

## servlet

- 자바를 사용하여 웹페이지를 동적으로 생성하는 서버측 프로그램 혹은 그 사양
- 웹 요청과 응답의 흐름을 간단한 메서드 호출만으로 체계적으로 다룰 수 있게 해주는 기술

### 특징

- 클라이언트의 Request에 대해 동적으로 작동하는 웹 애플리케이션 컴포넌트
  HTML을 사용하여 Response
- JAVA의 스레드를 이용하여 동작
- MVC 패턴에서의 컨트롤러로 이용
- HTTP 프로토콜 서비스를 지원하는 javax.servlet.http.HttpServlet 클래스를 상속
- UDP보다 속도가 느림.
- HTML 변경 시 Servlet을 재 컴파일해야 하는 단점이 있음.

## servlet container

- 서블릿을 담고 관리해주는 컨테이너

### 주요기능

- 서블릿 생명주기 관리
  - 스프링 컨테이너 생성시점과 빈객체의 생성시점은 동일
- 통신 지원
- 멀티스레딩 관리
- 선언적인 보안관리

---

## 출처

- [Web] 서블릿(Servlet)이란 무엇인가? 서블릿 총정리 - <https://coding-factory.tistory.com/742>
