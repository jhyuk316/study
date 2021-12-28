# 13. 쓰레드(Thread)

- [1. 프로세스와 쓰레드](#1-프로세스와-쓰레드)
  - [멀티쓰레딩의 장단점](#멀티쓰레딩의-장단점)
- [2. 쓰레드의 구현과 실행](#2-쓰레드의-구현과-실행)
- [3. start()와 run()](#3-start와-run)
  - [start()](#start)
- [4. 싱글쓰레드와 멀티쓰레드](#4-싱글쓰레드와-멀티쓰레드)
- [5. 쓰레드의 우선순위](#5-쓰레드의-우선순위)
  - [쓰레드의 우선순위 지정하기](#쓰레드의-우선순위-지정하기)
- [6. 쓰레드 그룹(Thread group)](#6-쓰레드-그룹thread-group)
- [7. 데몬 쓰레드(daemon thread)](#7-데몬-쓰레드daemon-thread)
- [8. 쓰레드의 실행제어](#8-쓰레드의-실행제어)
  - [쓰레드 상태](#쓰레드-상태)
  - [sleep()](#sleep)
  - [interrupt(), interrupted() - 쓰레드의 작업 취소](#interrupt-interrupted---쓰레드의-작업-취소)
  - [suspend(), resume(), stop()](#suspend-resume-stop)
  - [yield() - 다른 쓰레드에게 양보](#yield---다른-쓰레드에게-양보)
  - [join - 다른 쓰레드의 작업을 기다림](#join---다른-쓰레드의-작업을-기다림)
- [9. 쓰레드의 동기화](#9-쓰레드의-동기화)
  - [9.1 synchronized를 이용한 동기화](#91-synchronized를-이용한-동기화)
  - [9.2 wait()와 notify()](#92-wait와-notify)
  - [생산자 소비자 문제](#생산자-소비자-문제)
    - [기아 현상과 경쟁 상태](#기아-현상과-경쟁-상태)
  - [9.3 Lock과 Condition을 이용한 동기화](#93-lock과-condition을-이용한-동기화)
    - [ReentrantLock 생성자](#reentrantlock-생성자)
    - [ReentrantLock과 Condition](#reentrantlock과-condition)
  - [9.4 volatile](#94-volatile)
    - [volatile로 long과 double을 원자화](#volatile로-long과-double을-원자화)
  - [9.5 fork & join 프레임웍](#95-fork--join-프레임웍)
    - [compute()의 구현](#compute의-구현)
    - [다른 쓰레드의 작업 훔쳐오기](#다른-쓰레드의-작업-훔쳐오기)
    - [fork()와 join()](#fork와-join)
- [출처](#출처)

## 1. 프로세스와 쓰레드

> 프로세스 - 실행 중인 프로그램  
> 쓰레드 - 프로세스의 자원을 이용해서 실제로 작업을 수행

### 멀티쓰레딩의 장단점

장점

> cpu사용율 향상
> 효율적인 자원 사용
> 응답성 향상
> 작업이 분리되어 코드 간결화

단점

> 동기화, 교착상태 등을 고려

## 2. 쓰레드의 구현과 실행

Thread 상속

```java
class MyThread extedns Thread{
    public void run(){ /*작업내용*/}    // Thread클래스의 run()을 오버라이딩
}
```

Runnable구현

```java
class MyThread implements Runnable{
    public void run(){ /*작업내용*/}    // Runnable인터페이스의 run()을 구현
}
```

```java
class ThreadEx1 {
    public static void main(String args[]) {
        ThreadEx1_1 t1 = new ThreadEx1_1();

        Runnable r  = new ThreadEx1_2();
        Thread   t2 = new Thread(r);        // 생성자 Thread(Runnable target)

        t1.start();
        t2.start();
    }
}

class ThreadEx1_1 extends Thread {
    public void run() {
        // Thread의 getName()을 호출
        System.out.println(getName()); // Thread-0
    }
}

class ThreadEx1_2 implements Runnable {
    public void run() {
        // Runnable인터페이스이므로 Thread의 메서드를 호출할 수 없음.
        // Thread.currentThread() - 현재 실행 중인 Thread를 반환
        System.out.println(Thread.currentThread().getName());   // Thread-1
    }
}
```

```java
// 쓰레드 이름 지정 방법, 기본값 Thread-번호
Thread(Runnable target, String name);
Thread(String name);
void setName(String name);
```

## 3. start()와 run()

### start()

> 1. main()에서 start()호출
> 2. start()가 새로운 쓰레드 생성, 호출 스택 생성
> 3. 생성된 호출스택에서 run()호출

- run()을 호출 하면 단순히 메서드를 호출하는 것
- start()를 호출 한다고해서 바로 쓰레드가 생성 되진 않음.
- 실행 대기 상태로 등록되어 차례가 되면 실행.

한 번 실행된 쓰레드는 다시 실행 할 수 없음.

```java
ThreadEx t1 = new ThreadEx();
t1.start();
t1.start(); // IllegalThreadStateException 발생

//after
ThreadEx t1 = new ThreadEx();
t1.start();
t1 = new ThreadEx();
t1.start();
```

> 실행 중인 사용자 쓰레드가 없을 때 프로그램 종료됨.

## 4. 싱글쓰레드와 멀티쓰레드

생략

## 5. 쓰레드의 우선순위

우선순위가 높으면 더 많은 작업시간 할당

### 쓰레드의 우선순위 지정하기

```java
void setPriority(int newPriority)
int getPriority()

// 숫자가 클 수록 높은 우선 순위
public static final int MAX_PRIORITY = 10;  // 최대 우선순위
public static final int MIN_PRIORITY = 1;   // 최소 우선순위
public static final int NORM_PRIORITY = 5;  // 보통 우선순위
```

멀티코어에선 병렬실행으로 우선순위가 큰 의미가 없을 수 있음.

소스 참조 - 쓰레드 우선순위 설정 <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadEx8.java>

## 6. 쓰레드 그룹(Thread group)

- 서로 관련된 쓰레드를 그룹화
- 자신이 속한 쓰레드 그룹이나 하위 쓰레드 그룹은 변경 가능
- 다른 쓰레드 그룹의 쓰레드는 변경 불가

| Type        | Method                                         | Description                                                                                                               |
| ----------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
|             | ThreadGroup(String name)                       | 지정된 이름의 쓰레드 그룹 생성                                                                                            |
|             | ThreadGroup(ThreadGroup parent, String name)   | 지정된 쓰레드 그룹에 포함되는 쓰레드 그룹 생성                                                                            |
| int         | activeCount()                                  | 쓰레드 그룹에 포함된 활성 상태인 쓰레드 수 반환                                                                           |
| int         | activeGroupCount()                             | 쓰레드 그룹에 포함된 활성 상태인 쓰레드 그룹 수 반환                                                                      |
| void        | checkAccess()                                  | 현재 실행중인 쓰레드가 쓰레드 그룹을 변경할 권한이 있는 체크. 없으면 SecurityException 발생                               |
| void        | destroy()                                      | **Deprecated** 결함. 쓰레드 그룹과 하위 쓰레드 그룹까지 모두 삭제. 단, 쓰레드 그룹이나 하위 쓰레드 그룹이 비어 있어야 함. |
| int         | enumerate(Thread[] list)                       | 쓰레드 그룹에 속한 쓰레드 또는 하위 쓰레드 그룹의 목록을 지정된 배열에 담고 그 개수를 반환                                |
| int         | enumerate(Thread[] list, boolean recurse)      | -> recurse가 true면 하위 쓰레드 그룹에 속한 하위 쓰레드 그룹까지 포함.                                                    |
| int         | enumerate(ThreadGroup[] list)                  | 쓰레드 그룹에 속한 하위 쓰레드 그룹의 목록을 지정된 배열에 담고 그 개수를 반환                                            |
| int         | enumerate(ThreadGroup[] list, boolean recurse) | -> recurse가 true면 하위 쓰레드 그룹에 속한 하위 쓰레드 그룹까지 포함.                                                    |
| int         | getMaxPriority()                               | 쓰레드 그룹의 최대 우선순위를 반환                                                                                        |
| String      | getName()                                      | 쓰레드 그룹의 이름 반환                                                                                                   |
| ThreadGroup | getParent()                                    | 쓰레드 그룹의 상위 쓰레드 그룹 반환                                                                                       |
| void        | interrupt()                                    | 쓰레드 그룹에 속한 모든 쓰레드를 interrupt                                                                                |
| boolean     | isDaemon()                                     | **Deprecated** 결함.쓰레드 그룹이 데몬 쓰레드인가?                                                                        |
| boolean     | isDestroyed()                                  | **Deprecated** 결함. 쓰레드 그룹이 삭제 되었는가?                                                                         |
| void        | list()                                         | 쓰레드 그룹에 속한 쓰레드와 하위 쓰레드 그룹에 대한 정보 출력                                                             |
| boolean     | parentOf(ThreadGroup g)                        | 지정된 쓰레드 그룹의 상위 쓰레드 그룹인지 확인                                                                            |
| void        | setDaemon(boolean daemon)                      | **Deprecated** 결함. 쓰레드 그룹을 데몬 쓰레드 그룹으로 설정/해제                                                         |
| void        | setMaxPriority(int pri)                        | 쓰레드 그룹의 최대우선순위를 설정                                                                                         |
| String      | toString()                                     | Returns a string representation of this Thread group.                                                                     |

쓰레드 그룹에 포함 시키는 생성자

```java
Thread(ThreadGruop group, String name);
Thread(ThreadGruop group, Runnable target);
Thread(ThreadGruop group, Runnable target, String name);
Thread(ThreadGruop group, Runnable target, String name, long stackSize);
```

- 기본값은 자신을 생성한 쓰레드와 같은 그룹
- system 쓰레드 그룹 - Finalizer 쓰레드(갈비지 컬렉터) 등
- main 쓰레드 그룹 - main 메서드

소스 참조 - 쓰레드 그룹 생성 <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadEx9.java>

## 7. 데몬 쓰레드(daemon thread)

- 작업을 돕는 보조적인 쓰레드
- 일반 쓰레드가 모두 종료되면 데몬 쓰레드는 강제적으로 자동 종료
- 갈비지 컬렉터, 자동저장 등이 있음.

```java
boolean isDaemon();         // 데몬 쓰레드 인가?
void setDaemon(boolean on); // True 데몬 쓰레드 변경, False 사용자 쓰레드로 변경
```

- 쓰레드 start()하기 전에 데몬 쓰레드로 설정해야 함.

소스 참조 - 데몬 쓰레드 생성 <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadEx10.java>

## 8. 쓰레드의 실행제어

쓰레드 메서드

| Modifier and Type | Method                        | Description                                                                                    |
| ----------------- | ----------------------------- | ---------------------------------------------------------------------------------------------- |
| static void       | sleep(long millis)            | ms, ns단위로 쓰레드를 일시 정지. 시간이 지나면 자동적으로 다시 실행 대기 상태가 됨.            |
| static void       | sleep(long millis, int nanos) |                                                                                                |
| final void        | join()                        | 쓰레드가 완료되면 join()을 호출한 쓰레드로 돌아옴                                              |
| final void        | join(long millis)             | 지정된 시간(ms, ns) 동안 쓰레드 실행. 시간이 지나거나 완료되면 join()을 호출한 쓰레드로 돌아옴 |
| final void        | join(long millis, int nanos)  |                                                                                                |
| final void        | stop()                        | **Deprecated** 데드락 문제. 쓰레드 즉시 종료.                                                  |
| final void        | suspend()                     | **Deprecated** 데드락 문제. 쓰레드를 일시 정지.                                                |
| final void        | resume()                      | **Deprecated** 데드락 문제. suspend()된 쓰레드 재개                                            |
| static void       | yield()                       | 실행 중에 자신의 실행시간을 다른 쓰레드에게 양보(yield)하고 자신은 실행 대기 상태가 됨.        |

### 쓰레드 상태

| 상태          | 설명                                                                              |
| ------------- | --------------------------------------------------------------------------------- |
| NEW           | 쓰레드가 생성되고 아직 start()가 호출 되지 않은 상태.                             |
| RUNNABLE      | 실행 중 또는 실행 가능한 상태                                                     |
| BLOCKED       | 동기화 브럭에 의해서 일시정지된 상태(lock이 풀릴 때까지)                          |
| WAITING       | 쓰레드의 작업이 종료되지는 않았지만, 실행가능하지 않은(unrunnable) 일시정지 상태. |
| TIMED_WAITING | 일시정지 시간이 지정된 WAITING 상태                                               |
| TERMINATED    | 쓰레드의 작업이 종료된 상태                                                       |

쓰레드 상태 변화

![thread state](<images/13%20쓰레드(Thread)_thread_state.png>)

1. 쓰레드 생성 후 start()를 호출하면, 실행 대기열에 Runnable 상태로 대기.
2. 자신의 차례가 되면 실행(running).
3. 실행 시간이 다 되거나 yield()를 만나면 다시 실행 대기.
4. 실행 중 suspend(), sleep(), wait(), join(), I/O block에 의해 일시정지.
5. 지정시간 경과(time-out), notify(), resume(), interrupt()가 호출되면 다시 실행 대기열에 대기.
6. 실행을 모두 마치거나 stop()이 호출되면 쓰레드 소멸.

### sleep()

지정된 시간 동안 쓰레드 정지

```java
static void sleep(long millis);
static void sleep(long millis, int nanos);
```

```java
class ThreadEx12 {
    public static void main(String args[]) {
        ThreadEx12_1 th1 = new ThreadEx12_1();
        th1.start();
        try {
            th1.sleep(2000);    // th1이 sleep하지 않음. 실행 중인 thread(main)가 sleep()
                                // sleep()은 static 메소드, Thread.sleep()이 바른 사용법.
        } catch(InterruptedException e) {}

        System.out.print("<<main 종료>>");
    }
}
// 생략
```

- 소스 참조 - sleep() <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadEx12.java>

### interrupt(), interrupted() - 쓰레드의 작업 취소

- 쓰레드에게 작업을 멈추라고 요청.
- 강제로 종료 시키는 것은 아님.
- 쓰레드가 sleep(), wait(), join()에 의해 WAITING상태일 때,  
  interrupt()를 호출 하면 Interrupted Exception이 발생하고 RUNNABLE상태가 됨.

```java
void interrupt();               // 쓰레드의 interrupted상태를 false에서 true로 변경
boolean isInterrupted();        // 쓰레드의 interrupted상태 반환
static boolean interrupted();   // 현재 쓰레드의 interrupted상태를 반환 후, false로 변경
```

소스 참조 - intertupt() <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadEx13.java>

sleep상태 interrupt

```java
class ThreadEx14_1 {
    public static void main(String[] args) throws Exception {
        ThreadEx14_2 th1 = new ThreadEx14_2();
        th1.start();

        th1.interrupt();   // interrupt()를 호출하면, interrupted상태가 true가 된다.
        System.out.println("isInterrupted():"+ th1.isInterrupted());
    }
}

class ThreadEx14_2 extends Thread {
    public void run() {
        int i = 10;
        while(i!=0 && !isInterrupted()) {
            System.out.println(i--);
            try {
                Thread.sleep(1000);  // InterruptedException 발생으로 interrupt 상태 false.
            } catch(InterruptedException e) {
                // interrupt(); InterruptedException 발생했을 때 interrupt 상태를 다시 true로 설정
            }
        }

        System.out.println("카운트가 종료되었습니다.");
    } // main
}
```

- 소스 참조 - sleep상태 interrupt <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadEx14.java>

### suspend(), resume(), stop()

- Deprecated.
- suspend() - 쓰레드를 멈춤. resume()로만 깨어남
- resume() - 쓰레드를 다시 실행 대기 상태로 만듦.
- stop() - 쓰레드 즉시 종료.

소스 참조 - Ex17 <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadEx17.java>

### yield() - 다른 쓰레드에게 양보

- 자신의 실행시간을 다음 차례의 쓰레드에게 양보(yield) 후 실행대기.
- yield()와 interrupt()를 적절히 사용하면, 응답성과 효율을 높임.

yield()와 interrupt() 예제 - Ex17번과 비교

```java
class ThreadEx18 {
    public static void main(String args[]) {
        ThreadEx18_1 th1 = new ThreadEx18_1("*");
        ThreadEx18_1 th2 = new ThreadEx18_1("**");
        ThreadEx18_1 th3 = new ThreadEx18_1("***");
        th1.start();
        th2.start();
        th3.start();

        try {
            Thread.sleep(2000);
            th1.suspend();
            Thread.sleep(2000);
            th2.suspend();
            Thread.sleep(3000);
            th1.resume();
            Thread.sleep(3000);
            th1.stop();
            th2.stop();
            Thread.sleep(2000);
            th3.stop();
        } catch (InterruptedException e) {}
    }
}

class ThreadEx18_1 implements Runnable {
    boolean suspended = false;
    boolean stopped   = false;

    Thread th;

    ThreadEx18_1(String name) {
        th = new Thread(this, name); // Thread(Runnable r, String name)
    }

    public void run() {
        String name =th.getName();

        while(!stopped) {
            if(!suspended) {
                System.out.println(name);
                try {
                    Thread.sleep(1000); // interrupt()에 의해 예외 발생
                } catch(InterruptedException e) {
                    System.out.println(name + " - interrupted");
                }
            } else {
                Thread.yield(); // yield가 없으면 while문을 계속 돌면서 busy waiting을 했을 것
            }
        }
        System.out.println(name + " - stopped");
    }

    public void suspend() {
        suspended = true;
        th.interrupt(); //
        System.out.println(th.getName() + " - interrupt() by suspend()");
    }

    public void resume() {
        suspended = false;
    }

    public void stop() {
        stopped = true; // stop()이 호출돼도 1초간 sleep한뒤 정지
        th.interrupt(); // 하지만 interrupt()로 예외가 발생하여 즉시 종료.
        System.out.println(th.getName() + " - interrupt() by stop()");
    }

    public void start() {
        th.start();
    }
}
```

### join - 다른 쓰레드의 작업을 기다림

- 지정된 시간 동안 특정 쓰레드가 작업하는 것을 기다림.
- interrupt()에 의해 대기상태에서 벗어날 수 있음.

```java
void join();    // 다른 쓰레드가 마치길 계속 기다림.
void join(long millis);
void join(long millis, int nanos);
```

소스 참조 - join() <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadEx19.java>

## 9. 쓰레드의 동기화

- 한 쓰레드가 진행 중인 작업을 다른 쓰레드가 간섭하지 못하도록 막는 것
- 임계 영역 - 공유 데이터를 사용하는 코드 영역
- 공유 데이터가 가지고 있는 lock을 획득한 단 하나의 쓰레드만 수행

### 9.1 synchronized를 이용한 동기화

- 임계 영역 설정
- lock 자동 획득, 반납

```java
// 메서드 전체를 임계 영역으로 지정
public synchronized void calcSum(){
    // 임계 영역
}

// 특정한 영역을 임계 영역으로 지정
synchronized(객체의 참조변수){ // 락을 걸고자 하는 객체
    // 임계 영역
}
```

```java
class ThreadEx22 {
    public static void main(String args[]) {
        Runnable r = new RunnableEx22();
        new Thread(r).start();
        new Thread(r).start();
    }
}

class Account {
    private int balance = 1000; // private으로 해야 동기화가 의미가 있다.
    // public이면 동기화하지 않은 방법으로 변경 가능하기 때문.

    public  int getBalance() {
        return balance;
    }

    public synchronized void withdraw(int money){ // synchronized로 메서드를 동기화
        if(balance >= money) {
            try { Thread.sleep(1000);} catch(InterruptedException e) {}
            balance -= money;
        }
    } // withdraw
}

class RunnableEx22 implements Runnable {
    Account acc = new Account();

    public void run() {
        while(acc.getBalance() > 0) {
            // 100, 200, 300중의 한 값을 임으로 선택해서 출금(withdraw)
            int money = (int)(Math.random() * 3 + 1) * 100;
            acc.withdraw(money);
            System.out.println("balance:"+acc.getBalance());
        }
    } // run()
}
```

### 9.2 wait()와 notify()

효율적인 동기화가 가능  
동기화 블록 내에서만 사용 가능

- wait() - 쓰레드가 락을 반납하고 waiting pool에 대기.
- notify() - waiting pool에서 대기 중인 쓰레드 중 하나를 깨움.
- notifyAll() - waiting pool에서 대기 중인 모든 쓰레드를 깨움.

### 생산자 소비자 문제

- 한 요리사는 Table에 음식 추가, 두 손님은 Table의 음식 소비
- 요리사와 손님이 같은 객체(Table)를 공유

소스 참조 - synchronized가 없을 때 <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadWaitEx1.java>

- 음식 추가하려는데 먹거나, 하나 남은 음식을 두 손님이 먹음

소스 참조 - synchronized만 추가 <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadWaitEx2.java>

- 손님이 lock을 가진 채로 무한히 대기

소스 참조 - synchronized에 wait()와 notify() 적용

```java
class ThreadWaitEx3 {
    public static void main(String[] args) throws Exception {
        Table table = new Table();

        new Thread(new Cook(table), "COOK1").start();
        new Thread(new Customer(table, "donut"),  "CUST1").start();
        new Thread(new Customer(table, "burger"), "CUST2").start();

        Thread.sleep(2000);
        System.exit(0);
    }
}

class Customer implements Runnable {    // 소비자
    private Table table;
    private String food;

    Customer(Table table, String food) {
        this.table = table;
        this.food  = food;
    }

    public void run() {
        while(true) {
            try { Thread.sleep(100);} catch(InterruptedException e) {}
            String name = Thread.currentThread().getName();

            table.remove(food);
            System.out.println(name + " ate a " + food);
        } // while
    }
}

class Cook implements Runnable {    // 생산자
    private Table table;

    Cook(Table table) {	this.table = table; }

    public void run() {
        while(true) {
            int idx = (int)(Math.random()*table.dishNum());
            table.add(table.dishNames[idx]);
            try { Thread.sleep(10);} catch(InterruptedException e) {}
        } // while
    }
}

class Table {
    String[] dishNames = { "donut","donut","burger" }; // donut의 확률을 높인다.
    final int MAX_FOOD = 6;
    private ArrayList<String> dishes = new ArrayList<>();

    public synchronized void add(String dish) {
        while(dishes.size() >= MAX_FOOD) {
                String name = Thread.currentThread().getName();
                System.out.println(name+" is waiting.");
                try {
                    wait(); // COOK쓰레드가 lock을 풀고 대기
                    Thread.sleep(500);
                } catch(InterruptedException e) {}
        }
        dishes.add(dish);
        notify();  // 기다리고 있는 CUST를 깨우기 위함.
        System.out.println("Dishes:" + dishes.toString());
    }

    public void remove(String dishName) {

        synchronized(this) {
            String name = Thread.currentThread().getName();

            while(dishes.size()==0) {
                    System.out.println(name+" is waiting.");
                    try {
                        wait(); // CUST쓰레드를 기다리게 한다.
                        Thread.sleep(500);
                    } catch(InterruptedException e) {}
            }

            while(true) {
                for(int i=0; i<dishes.size();i++) {
                    if(dishName.equals(dishes.get(i))) {
                        dishes.remove(i);
                        notify(); // 잠자고 있는 COOK을 깨우기 위함
                        return;
                    }
                } // for문의 끝

                try {
                    System.out.println(name+" is waiting.");
                    wait(); // 원하는 음식이 없는 CUST쓰레드를 기다리게 한다.
                    Thread.sleep(500);
                } catch(InterruptedException e) {}
            } // while(true)
        } // synchronized
    }

    public int dishNum() { return dishNames.length; }
}
```

- waiting pool에 요리사와 손님이 같이 기다림.
- notify()로 누가 깨어 날지 모름.

#### 기아 현상과 경쟁 상태

- starvation - 운이 나쁘면 요리사는 계속 대기
  - 해결 notifyAll()로 모든 쓰레드를 깨움.
- race condition - notifyAll()로 손님과 요루시가 모두 깨어나 서로 lock을 얻으려고 싸움.

### 9.3 Lock과 Condition을 이용한 동기화

JDK 1.5 추가

synchronized는 메서드 내에서만 사용 가능한 제약이 있음.

Lock 클래스

- ReentrantLock - 재진입이 가능한 lock. 가장 일반적인 배타 lock
- ReentrantReadWriteLock - 읽기에는 공유적(동시에 가능)이고, 쓰기에는 배타적인 lock
  - 읽기 lock은 여러 개가 동시에 됨.
  - 쓰기 lock은 하나만 되며, 읽기 lock과 동시에 되지 않음.
- StampedLock - ReentrantReadWriteLock에 낙관적인 lock의 가능을 추가, JDK 1.8
  - 낙관적인 읽기 lock - 쓰기 lock에 의해 lock이 해제됨.
  - 무조건 읽기 lock을 거는 것이 아니라 쓰기와 읽기가 충돌할 때만 쓰기가 끝난 후에 읽기 lock을 검.

```java
int getBalance(){
    long stamp = lock.tryOptimisticRead();  // 낙관적 읽기 lock

    int curBalance = this.balance;  // 공유 데이터 balance 읽기

    if(!lock.validate(stamp)){      // 쓰기 lock에 의해 낙관적 읽기 lock이 풀렸는지 체크
        stamp = lock.readLock();    // lock이 풀렸으면, 읽기 lock을 얻기 위해 대기

        try{
            curBalance = this.balance;  // 공유 데이터 읽기
        } finally {
            lock.unlockRead(stamp);     // 읽기 lock 해제
        }
    }
}
```

#### ReentrantLock 생성자

```java
ReentrantLock()
ReentrantLock(boolean fair) // true면 lock이 풀렸을 때 가장 오래 기다린 쓰레드가 lock획득.
```

수동으로 lock을 잠그고 품

```java
void lock();        // lock 획득. lock을 얻을 때까지 쓰레드를 block 시킴.
void unlock();      // lock 해제
boolean isLocked(); // lock이 잠겼는가?
```

```java
synchronized(lock){
// 임계 영역
}

// 위아래는 똑같은 코드

lock.lock();
try{
// 임계 영역
} finally { // 언락은 finally로 처리하는 게 안전
    lock.unlock();
}
```

```java
void tryLock(); // lock을 얻으려고 시도, 못 얻으면 포기.(lock()과 달리 대기하지 않음.)
void tryLock(long timeout, TimeUnit unit) throws InterruptedException
// InterruptedException 대기 시간 동안 interrupt()에 의해 작업이 취소될 수 있음을 뜻함.
```

- 일정 시간만 시도하므로 lock()에 비해 응답성이 좋음.

#### ReentrantLock과 Condition

- 위의 예제의 손님과 요리사를 구분하기 위한 condition

```java
private ReentrantLock lock = new ReentrantLock();   // lock 생성
// lock으로 condition 생성
private Condition forCook = lock.newCondition();
private Condition forCust = lock.newCondition();
```

| Object                  | Condition                               |
| ----------------------- | --------------------------------------- |
| void wait()             | void await()                            |
|                         | void awaitUninterruptibly()             |
| void wait(long timeout) | boolean await(long time, TimeUnit unit) |
|                         | long awaitNanos(long nanosTimeout)      |
|                         | boolean awaitUntil(Date deadline)       |
| void notify()           | void signal()                           |
| void notifyAll()        | void signalAll()                        |

소스 참조 - condition을 추가한 소비자 생산자 <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ThreadWaitEx4.java>

- 기아 상태와 경쟁 상태를 줄었음. 완전한 제거는 불가능.

### 9.4 volatile

![multicore_cache](<images/13%20쓰레드(Thread)_multicore_cache.png>)

- 현대의 컴퓨터는 멀티 코어 프로세서를 장착
- 코어마다 별도의 캐시를 가짐.

```java
volatile int counter = 0;   // 코어가 읽을 때 캐시가 아니라 메모리에서 읽어 옴.
```

synchronized 활용

```java
public synchronized void plus(){    // synchronized을 들어갈 때 나올 때, 캐시와 메모리를 동기화함.
    counter++;
}
```

#### volatile로 long과 double을 원자화

변수의 읽기와 쓰기를 원자화 (동기화 해주는 것이 아님을 주의)

- JVM은 4byte 단위로 처리
- int 이하의 자료형은 한 번에 읽거나 씀
- 8byte인 long과 double은 한 번에 읽고 쓸 수 없음.
- 그 사이에 다른 쓰레드가 들어올 수 있음.

```java
volatile long sharedVal;    // long타입(8 byte)를 원자화
volatile double sharedVal;  // double타입(8 byte)를 원자화
```

- 원자화 - 작업을 더 이상 나눌 수 없음. 한 동작으로 취급
- synchronized블록도 일종의 원자화

### 9.5 fork & join 프레임웍

JDK 1.7

> RecursiveAction - 반환 값이 없는 작업을 구현할 때 사용  
> RecursiveTask - 반환 값이 있는 작업을 구현할 때 사용

```java
// RecursiveAction - 반환 값이 없는 작업을 구현할 때 사용
public abstract class RecursiveAction extends ForkJoinTask<void>{
    // ...
    protected abstract void compute();  // 상속으로 구현
    // ...
}
// RecursiveTask - 반환 값이 있는 작업을 구현할 때 사용
public abstract class RecursiveTask<V> extends ForkJoinTask<V>{
    // ...
    protected abstract V compute();  // 상속으로 구현
    // ...
}
```

```java
class SumTask extends RecursiveTask<Long>{
    // ...
    public Long compute(){
        // ...
    }
}

ForkJoinPool pool = new ForkJoinPool(); // 쓰레드 풀 생성
SumTask task = new SumTask(form, to);   // 수행할 작업 생성
Long result = pool.invoke(task);        // invoke()를 호출해서 작업 시작
```

#### compute()의 구현

- 작업 범위를 어떻게 나눌 것인지만 정의해주면 됨.
- 일반적인 재귀 함수와 동일한 구조.

```java
// 5개가 될 때까지 일을 반으로 쪼갬.
public Long compute() {
    long size = to - from;

    if(size <= 5)     // 더할 숫자가 5개 이하면
        return sum(); // 숫자의 합을 반환

    long half = (from+to)/2;

    // 범위를 반으로 나눠서 두 개의 작업을 생성
    SumTask leftSum  = new SumTask(from, half);
    SumTask rightSum = new SumTask(half+1, to);

    leftSum.fork(); // 비동기 메서드, 호출 후 결과를 기다리지 않음.

    return rightSum.compute() + leftSum.join(); // 동기 메서드 호출 결과를 기다림.
}
```

![compute](<images/13%20쓰레드(Thread)_compute.png>)

- 한쪽은 fork() 한쪽은 compute()를 재귀함

#### 다른 쓰레드의 작업 훔쳐오기

![work stealing](<images/13%20쓰레드(Thread)_work_stealing.png>)

- 작업 큐에 추가된 작업 역시 compute()에 의해 더 이상 나눌 수 없을 때까지 나뉨.
- work stealing - 자신의 작업 큐가 비어있는 쓰레드는 다른 쓰레드의 작업규에서 작업을 가져와 수행
- 모든 쓰레드가 골고루 작업하게 됨.

#### fork()와 join()

> fork() - 해당 작업을 쓰레드 풀의 작업 큐에 넣음. 비동기 메서드  
> join() - 해당 작업의 수행이 끝날 때까지 기다렸다가, 수행이 끝나면 결과를 반환. 동기 메서드

- 비동기 메서드 - 호출만 할 뿐, 그 결과를 기다리지 않음.

소스 참조 - fork()와 join() <https://github.com/castello/javajungsuk3/blob/master/source/ch13/ForkJoinEx1.java>

- for문이 더 빠르다 fork()와 join()의 오버헤드 때문에.
- 멀티 쓰레딩이 이득이 되는 작업에만 적절히 적용할 것.

## 출처

- Java Volatile Keyword <http://tutorials.jenkov.com/java-concurrency/volatile.html>
