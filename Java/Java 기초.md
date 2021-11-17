# 자바 기초

자바의 형변환은 큰 쪽은 자동 작은쪽으로는 명시
```java
long l = 30L;
int x = 15;

l = x
x = (int) l
```
출력 포멧
```java
String str = String.format("저는 %s이고, %d살이며, 키는 %fcm입니다.","홍길동", 20, 177.6f);
```
내장 클래스
```java
System.out.println(Math.Max(19,20));

String str = "100";
int i = Integer.parseInt(str);
String str2 = String.valueOf(i);

Random random = new Randow();
int rand = random.nextInt(10);
//5 ~ 9
int rand = random.nextInt(4);
rand = rand + 5
```
문자열 입력
```java
Scanner scanner = new Scanner(System.in);
String str = scanner.next();
int i = scanner.nextInt();
```
if문
```java
int i = 10;
if (i > 8){
    System.out.println("크다");
}else if(i>3){
    System.out.println("보통");
}else{
    System.out.println("작다");
}
```
삼항연산자
```java
boolean = isMarried = true;
String str = isMarried ? "결혼함" : "결혼 안함";
System.out.println(str);
```
switch
```java
String str
switch(str){
    case "결혼함":
        System.out.println("O");
        break;
    case "결혼 안함":
        System.out.println("x");
        break;
    default:
        System.out.println("?");
}
```



