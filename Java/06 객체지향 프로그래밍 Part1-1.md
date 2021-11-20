# 객체지향 프로그래밍

## 1. 객체지향언어  
- 클래스란? 실제 사물의 속성과 기능을 분석한 다음, 데이터(변수)와 함수로 정의함  

    - 특징  
    캡슐화  
    상속  
    추상화  
    다형성  

    - 장점  
    높은 재사용성  
    용이한 코드 관리  
    신뢰성 높은 프로그래밍  

- 너무 객체지향에 얽매여 고민하기 보다 기능적으로 완성한 다음 객체지향적으로 코드를 개선 할 수 있을 지 고민 할 것

### 2. 클래스와 객체
- 클래스 - 객체 생성을 위해 객체를 정의해 놓은 것  
객체 - 기능을 하기 위해 실존하는 것  
- 클래스를 인스턴스화하여 객체(인스턴스)를 만듬
- 속성(property) - 멤버변수(member variable), 특성(attribute), 필드(field), 상태(state)  
기능(function) - 메서드(method), 함수(function), 행위(behavior)  

- 예시  
TV 속성 - 색깔, 전원상태, 볼륨, 채널  
TV 기능 - 켜기, 끄기, 볼륨조절, 채널변경  
    ```java
    class TV{
        String color;
        boolean power;
        int channel;

        void power() {power = !power;}
        void channelUp() { ++channel;}
        void channelDown() { --channel;}
    }
    ```

- 인스턴스 생성과 사용
    ```java
    TV tv1 = new TV();
    tv1.channel = 7;
    TV tv2 = new TV();
    tv2.channel = 0;
    //각각 다른 TV를 가르키고 있다.
    System.out.println(tv1.channel); // 7
    System.out.println(tv2.channel); // 0

    tv2 = tv1;
    // 같은 tv를 가르키고 있다.
    System.out.println(tv1.channel); // 7
    System.out.println(tv2.channel); // 7
    ```
    - 여러개의 변수가 하나의 인스턴스를 가르킬 수 있음.  
    하나의 변수가 여러개의 인스턴스를 가르킬 수 없음.

- 객체 배열
    ```java
    TV[] tvList = new TV[3]; //참조변수 배열만 생성됨
    for(int i = 0 ; i < 3; ++i){
        tvList[i] = new TV(); //생성자 호출
    }
    System.out.println(tvList[0].channel);
    ```

### 3. 변수와 메서드
- 선언 위치에 따른 변수의 종류
    ```java
    class Vari{
        static int cv; // 클래스 변수
        int iv; // 인스턴스 변수
        void method(){
            int lv; // 지역 변수
        }
    }
    ```  

    |변수종류|선언위치|생성시기|호출|
    |:---:|:---:|:---:|:---:|
    |클래스 변수|클래스 영역|클래스를 메모리 로드시|전역|
    |인스턴스 변수|클래스 영역|인스턴스 생성시|각 인스턴스|
    |지역 변수|클래스 영역 이외(메서드, 생성자, 초기화 블럭)|변수 선언문 수행시|블럭 내|

- 메서드  
    입력으로 작업을 수행해서 결과를 반환  
    - 장점  
    높은 재사용성  
    중복된 코드의 제거  
    프로그램의 구조화

- 메서드 선언과 구현  
    ```java
    class MyMath{
        long add(long x, long y){
            return x + y;
        }
        double divide(double x, double y){
            return x / y;
        }
    }
    ```
- 메서드 호출
    ```java
    MyMath mm = new MyMath();
    long res = mm.add(1L, 3L);
    double res2 = mm.divide(5L,3L);
    ```
- return
    ```java
    int max(int a, int b){
        if(a>b) return a;
        else return b;   //거짓일 때 리턴이 없으면 에러
    }
    ```
- JVM의 메모리 구조

    |메모리 영역||변수||
    |---|---|---|---|
    |Heap|인스턴스|인스턴스 변수|
    |Call stack|main|로컬 변수|호출된 메소드를 위한 공간
    |Method Area|클래스 데이터|클래스 변수|

    - 호출 스택(Call Stack)  
    메서드가 호출되면 필요한 메모리를 스택에 할당
    메서드가 수행을 마치면 메모리를 반환하고 스택에서 제거
    호출 스택 제일 위는 현재 실행 중인 메서드
    아래에 있는 메서드가 바로 위의 메서드를 호출한 메서드

    ```java
    class CallStackTest{
        public static void main(String[] args){
            firstMethod();
        }

        static void firstMethod(){
            secondMethod();
        }

        static void secondMethod(){
            System.out.println("secondMethod");
        }
    }
    ```

    ||
    |---|
    |println|
    |secondMethod|
    |firstMethod|
    |main|

- 기본형 매개변수와 참조형 매개변수  
    - 기본형 매개변수 : Read only
    - 참조형 매개변수 : Read & Write

    ```java
    public static void main(){
        int a = 10;
        int[] b = {10};

        System.out.println(change1(a));  // 10
        System.out.println(change2(b));  // 100

    }
    static void chage1(int x){  // 기본형 파라미터
        x = 100;
        return;
    }
    static void chage2(int[] x){  // 참조형 파라미터
        x[0] = 100;
        return;
    }
    ```

    참조형은 변수의 주소를 넘겨 준 것으로 값이 변경됨

- 참조형 반환타입
    ```java
    class Data{int x;}
    ...
        public static void main(){
            Data d = new Data();
            d.x = 10;

            Data d2 = copy(d)

            System.out.println(d.x);  // 10
            System.out.println(d2.x);  // 10
        }

        static Data copy(Data d){  // 참조형 반환
            Data tmp = new Data();
            tmp.x = d.x;
            return tmp;
        }
    ```
    
    참조형 반환타입은 메서드가 **객체의 주소**를 반환 한다는 것

- 재귀 호출  
    메서드가 자기 자신을 다시 호출 하는 것
    ```java
    void mathod(){
        mathod(); // 재귀호출. 종료조건이 없어서 무한루프
    }
    ```
    제곱수 구하기
    ```java
    int power(int x,int n){
        if(n == 1) return x;
        return x * power(n-1);
    }
    ```

- 클래스 메서드(static)와 인스턴스 메서드
    |종류|작용 대상|인스턴스 생성|
    |---|---|---|
    |클래스 메서드|인스턴스와 무관한 변수|필요 없음|
    |인스턴스 메서드|인스턴스 변수 연산|필요|

    모든 인스턴스에 동일해야 하는 변수는 static으로 선언  
    클래스 메서드는 인스턴스 변수를 사용 할 수 없음.
    
- 클래스 멤버와 인스턴스 멤버간의 참조와 호출
    ```java
    class TestClass{
        void instanceMethod();      // 인스턴스 메서드
        static void staticMethod(); // 스태틱 메서드

        int iv;                     // 인스턴스 변수
        static int cv;              // 클래스 변수

        void instanceMethod2(){
            instanceMethod();
            staticMethod();
            System.out.println(iv);
            System.out.println(cv);
        }

        static void staticMethod2(){
            instanceMethod();       // ERROR! 인스턴스 메소드 호출 불가
            staticMethod();
            System.out.println(iv); // ERROR! 인스턴스 변수 호출 불가
            System.out.println(cv);
        }
    }
    ```

    클래스 메소드는 인스턴스가 생성되지 않아도 작동해야 하기 때문.




