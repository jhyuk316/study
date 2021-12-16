# 09. java.lang 패키지

## 1. Object 클래스

### 1.1 메서드

- 모든 클래스의 최고 조상. 11개의 메서드를 가지고 있다.
- notify(), wait()는 쓰레드 관련 메서드이다.
- equals(), hashCode(), toString()은 적절히 오버라이딩 해야한다.

#### **protected** Object clone()

객체 자신의 복사본 반환

#### public boolean equals(Object obj)

**주소값을 비교**하여 같은 객체인지 알려준다.

오버라이딩 하여 인스턴스 변수 값을 비교하도록 바꾼다.

#### protected void finalize()

객체 소멸시 가비지 컬렉터에 의해 자동적으로 호출된다. 이 때 수행되어야 하는 코드가 있는 경우만 오버라이드 한다.

#### public Class getClass()

객체 자신의 클래스 정보를 담고 있는 Class 인스턴스를 반환한다.

Class 객체는 클래스의 모든 정보를 담고 있으며, 클래스당 단 1개만 존재한다.

클래스파일이 메모리에 로드될 때 생성된다.

```java
Card c = new Card();
Class cObj = c.getClass();
Class cObj = Card.class;
String className = cObj.getName();
Class cObj = Class.forName("Card");

Card c2 = new Card();
Card c2 = (Card)cObj.newInstance();
String className = Card.class.getName();
```

#### public int hashCode()

객체 자신의 해쉬코드를 반환한다. 때문에 다량의 데이터를 저장&검색하는 해싱에 쓰인다.

equals()의 결과가 true인 두 객체의 hash code는 같아야하기 때문에, equals()를 오버라이딩하면, hashCode()도 같이 오버라이딩 해야한다.

#### public String toString()

객체 자신의 정보를 문자열로 반환한다.

오버라이딩해서 작성.

#### 기타

- public void notify() : 객체 자신을 기다리는 쓰레드를 하나만 깨운다.
- public void notifyAll() : 객체 자신을 기다리는 쓰레드를 모두 깨운다.
- public void wait() : 다른 쓰레드가 notify() 혹은 notifyAll() 호출까지 현재 쓰레드를 무한히 기다리게 한다.
- public void wait(long timeout): timeout ms동안 기다린다
- public void wait(long timeout, int nanos): timeout ms nanso ns 만큼 기다린다.

## 2. String

### 2.1 String클래스의 특징

- 문자형 배열과 그에 관련된 메서드들이 정의 되어 있다.
- 인스턴스 내용은 바꿀 수 없다. (immutable)

```java
String str1 = "abc";
String str2 = "abc";
String str3 = new String("abc");
String str4 = new String("abc");
System.out.println(str1.equals("abc"));           // true
System.out.println(str1.equals(str2));            // true
System.out.println(str1 == str2);                 // true
System.out.println(str1.equals(str3));            // true
System.out.println(str4.equals(str3));            // true
System.out.println(str4 == str3);                 // false
System.out.println(str1.getClass());              // class java.lang.String
System.out.println(str1.getClass().getName());    // java.lang.String
```

### 2.2 빈 문자열("")

- 내용이 없는 문자열. 크기가 0인 char형 배열을 저장하는 문자열

```java
String str = ""; // ok
char c = '';     // can't

// initialize
// bad
String str = null;
char c = '\u0000';
// good
String str = "";
char c = ' ';
```

### 2.3 생성자 및 메소드

![String_API1](images/09%20java.lang패키지와%20유용한%20클래스_String_API1.png)
![String_API2](images/09%20java.lang패키지와%20유용한%20클래스_String_API2.png)
![String_API3](images/09%20java.lang패키지와%20유용한%20클래스_String_API3.png)

### 2.4 문자열과 기본형간 변환

- 기본형 값을 문자열로 바꾸는 두 가지 방법 (방법2가 더 빠름)

```java
int i = 100;
String str1 = i + "";              // 방법 1
String str2 = String.valueOf(i);   // 방법 2
```

- 문자열을 기본형으로 변환

```java
int i = Integer.parseInt("100");
int i2 = Integer.valueOf("100");   // JDK1.5 이후
char c = "A".charAt(0);            //
```

![형변환_API](images/09%20java.lang패키지와%20유용한%20클래스_형변환_API.png)

## 3. StringBuffer

### 3.1 특징

- String처럼 문자형 배열(char[])를 가지고 있다.
- mutable
- 인스턴스 생성 시 버퍼 크기 충분히 지정해주는게 좋다.
  → 버퍼가 작으면 성능 저하 - 작업 중 더 큰 배열이 추가로 생성됨.
- equals()를 오버라이딩하지 않았음.

![StringBuffer_API1](images/09%20java.lang패키지와%20유용한%20클래스_StringBuffer_API1.png)
![StringBuffer_API2](images/09%20java.lang패키지와%20유용한%20클래스_StringBuffer_API2.png)

## 4. Math & Wrapper

### 4.1 Math

- 수학계산에 유용한 메서드로 구성되어 있다.
- 모두 static

![Math_API](images/09%20java.lang패키지와%20유용한%20클래스_Math_API.png)

### 4.2 wrapper

- 기본형을 클래스로 정의.

![wrapper_class](images/09%20java.lang패키지와%20유용한%20클래스_wrapper_class.png)

- 내부적으로 기본형 변수를 가지고 있다.
- equals()가 오버라이딩되어 있다.

### 4.3 Number

숫자를 멤버변수로 갖는 클래스의 조상(추상클래스)

![Number_class](images/09%20java.lang패키지와%20유용한%20클래스_Number_class.png)
