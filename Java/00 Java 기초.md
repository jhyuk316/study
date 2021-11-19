# 자바 기초

자바의 형변환은 큰 쪽은 자동, 작은쪽으로는 명시
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

반복문
```java
for(int i = 0; i < 10; ++i){
    System.out.println(i);
    if(i == 6){
        continue;
    }
    if(i == 8){
        break;
    }
}

int i = 0;
while(i < 10){
    System.out.println(i);
    i++;
}

do{
    System.out.println(i);
    i++;
}while(i < 10)
```

배열
```java
int[] score = new int[5];
int size = score.length;

score[0] = 10;

int[] score2 = new int[]{10,20,30,40,50};
int[] score3 = {10,20,30,40,50};

System.out.println(score3[score3.length - 1]);

String[] names = {"홍길동", "고길동"};
System.out.println(names[0].length());

ArrayList<Integer> scoreList = new ArrayList<>();
scoreList.add(10);
scoreList.add(20);
scoreList.add(30);
System.out.println(scoreList.size());
System.out.println(scoreList.get(1));
scoreList.add(2, 200); //2번칸에 200추가
System.out.println(scoreList);
scoreList.remove(2);
System.out.println(scoreList);
```

메소드(static), 오버로드
static은 프로그램이 실행될 때 로드됨. 클래스 생성 없이 사용가능한 함수.
```java
public static void main(String[] args){
    System.out.println(add(50, 10));
    System.out.println(add(50, 10, 20));
    System.out.println(add(50, 10, 20, 30, 40));
}

public static int add(int x, int y){
    return x + y;
}

public static int add(int x, int y, int z){
    return x + y + z;
}

public static int add(int... numbers){
    int sum = 0;
    for (int i = 0; i < numbers.length; ++i){
        sum = sum + i;
    }
    return sum;
}
```

Class
과거에는 보안과 무결성을 위해 private 선언 후 getter, setter를 권장했으나, 요즘은 성능을 위해 public을 사용하기도 함.
```java
class Person{
    public String name;
    public int age

    public Person(){

    }

    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString(){
        return "Person{" +
                "name='" + name + "\'" +
                ", age=" + age +
                '}';
    }
}
```
상속, 추상클래스
```java
public class BasicsJava {

    public static void main(String[] args) {
        Person person = new Person();

        System.out.println(person);

        Hero hero1 = new Hero("슈퍼맨");
        Hero hero2 = new Hero("배트맨");

        hero1.attack(hero2);
    }
}

public class Person {
    private String name;
    private int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person {" +
            " name='" + getName() + "'" +
            ", age='" + getAge() + "'" +
            "}";
    }
}

public abstract class Character extends Person{
    public abstract void attack(Character character);
}

public class Hero extends Character{
    public Hero(String name) {
        setName(name);
    }

    @Override
    public void attack(Character character) {
        System.out.println(this.getName() + "은 " + character.getName() + "과 싸운다");
    }
}
```
인터페이스  
직접적인 상속대신 필요한 기능을 가지게 하는 용도
다중 상속할 수 있음.
```java
public abstract class Chara extends Person{
    public abstract void attack(Chara character);
}

public interface ICharacters{
    void attack(Person person);
}

public class Hero extends Chara implements ICharacters {
    public Hero() {
        super();
    }

    public Hero(String name) {
        setName(name);
    }

    @Override
    public void attack(Chara character) {
        System.out.println(this.getName() + "은 " + character.getName() + "과 싸운다");
    }

    @Override
    public void attack(Person person) {
        System.out.println(this.getName() + "은 " + person.getName() + "을 공격 할 수 밖에 없었다.");
    }
}
```
클래스 다형성과 상속 확인
```java
Chara hero4 = new Hero();        
ICharacters hero5 = new Hero();

hero4.attack(hero1);
hero5.attack(person);

//아래 모두 참
if (hero4 instanceof Hero){
    System.out.println("영웅이다");
}
if (hero4 instanceof Person){
    System.out.println("인간이다");
}
if (hero4 instanceof Chara){
    System.out.println("캐릭터이다");
}

ArrayList<Chara> charaList = new ArrayList<>();
charaList.add(hero1);
charaList.add(hero4);
charaList.add(hero5); //ERROR chara의 범위를 벗어남
```
제네릭
어떤 타입이든 받고 쓸 수 있게 하는 것
```java
public static <T> void print(T type) {
    System.out.println(type);
}

print("String");
print(1);
print(3.3f);
```
쓰레드
```java
new Thread(new Runnable() {
    @Override
    public void run() {
        for(int i = 0; i<5;++i){
            try {
                Thread.sleep(300);
                System.out.println(Thread.currentThread().getName() + ":" + i);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}).start();;

new Thread(new Runnable() {
    @Override
    public void run() {
        for(int i = 0; i<5;++i){
            try {
                Thread.sleep(300);
                System.out.println(Thread.currentThread().getName() + ":" + i);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}).start();;
```
- 결과 순서는 돌릴때마다 다름
```
Thread-0:0
Thread-1:0
Thread-0:1
Thread-1:1
Thread-0:2
Thread-1:2
Thread-0:3
Thread-1:3
Thread-0:4
Thread-1:4
```

람다식 - 익명함수  
함수형인터페이스 @FunctionalInterface  
구현해야 할 추상 메소드가 하나만 정의된 인터페이스  
Runnable은 함수형 인터페이스
```java
new Thread(() -> {
    for(int i = 0; i<5;++i){
        try {
            Thread.sleep(300);
            System.out.println(Thread.currentThread().getName() + ":" + i);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}).start();;
```