# Java 개발환경
## vscode에서 java 개발하기

1. vscode 설치
2. 자바 확장프로그램 설치  
vscode:extension/vscjava.vscode-java-pack  
포함된 확장프로그램  
    - Language Support for Java™ by Red Hat  
    Code Navigation  
    Auto Completion  
    Refactoring  
    Code Snippets  
    - Debugger for Java  
    Debugging  
    - Test Runner for Java  
    Run & Debug JUnit/TestNG Test Cases  
    - Maven for Java  
    Project Scaffolding  
    Custom Goals  
    - Project Manager for Java  
    Manage Java projects, referenced   libraries, resource files, packages, classes, and class members
    - Visual Studio IntelliCode  
    AI-assisted development  
    Completion list ranked by AI  
3. java runtime 설정  
command palette(ctrl+shift+P)에 Java:configure java runtime을 입력  
4. JDK설치  
installed JDK - install a JDK - Adoptium openJDK(Eclipse) - 껏다켜야 인식됨
OpenJDK vs OracleJDK  
라이센스 차이  
OpenJDK : GNU GPL 버전2, 완전 오픈소스
OracleJDK : Oracle 라이센스, Oracle Java 8부터는 상업용으로 불가. 상용라이센스 구매가 필요.  
성능 및 안정성  
OracleJDK가 우수하나 JSR(Java Specification Request) 표준에 맞추어 개발된 JDK의 기능을 검증하는 TCK(Technology Compatibility Kit)를 통과한 OpenJDK면 문제는 없음.  
기능  
OracleJDK의 독자적 기능으로 글꼴 라이브러리와 Java Web Start 등이 있으나 없어도 큰 문제 없음.  
결론 - 라이센스에서 자유로운 OpenJDK를 쓰자.  

5. vscode 프로젝트 폴더 만들기 & 열기 ctrl+K ctrl+O
6. java 파일 만들기
7. run 해보기

## intellij
1. intellij를 설치
2. 프로젝트 생성
3. run해보기