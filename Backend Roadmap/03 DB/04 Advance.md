# 1. Advance

## 1. 스케일 업(Scale-up)과 스케일 아웃(Scale-out)

![Scale-up_Scale-out](images/04%20Advance_Scale-up_Scale-out.png)

- 스케일 업(Scale-up) - 수직 스케일링(vertical scaling)
  - 기존의 서버를 보다 높은 사양으로 업그레이드하는 것
- 스케일 아웃(Scale-out) - 수평 스케일링(horizontal scaling)
  - 서버를 추가로 연결해 처리할 수 있는 데이터 용량이 증가

## 2. Partitining

- table을 ‘파티션(partition)’이라는 작은 단위로 나누어 관리 기법

- 장점

  - 성능(Performance) - 특정 DML과 Query의 성능을 향상. Scan범위를 줄임.
  - 가용성(Availability) - 각 분할 영역(partition별로)을 독립적으로 백업하고 복구.
  - 관리용이성(Manageability) - 큰 table들을 제거하여 관리를 쉬움.

- 단점

  - table간 JOIN에 대한 비용이 증가
  - table과 index를 별도로 파티셔닝할 수 없음. table과 index를 같이 파티셔닝해야 함. (?무슨 뜻이지?)

### 2.1. Vertical Partitioning vs Horizontal Partitioning

![Partitions](images/04%20Advance_Partitions.png)

- Vertical Partitioning

  - Column 단위로 수직 분할
  - 도메인에 따라 분리
  - application level에서 CRUD를 구현
  - 정규화도 일종의 수직 분할

- Horizontal Partitioning

  - Row 단위로 수평 분할
  - 같은 테이블 스키마를 가진 데이터를 다수의 데이터베이스에 분산하여 저장
  - application level에서도 가능하지만 database level에서도 가능
  - 샤딩

### 2.2. 분할 기준

![Partitioning기준](images/04%20Advance_Partitioning_기준.png)

- 범위 분할 (range partitioning)

  - 분할 키 값이 범위 내에 있는지 여부로 구분한다.
  - eg. 우편번호로 분할

- 목록 분할 (list partitioning)

  - 분할 키 값의 목록을 만들어 그 목록에 따라 분할.
  - eg. Country의 값이 Iceland , Norway , Sweden , Finland , Denmark 중 하나이면 북유럽 국가 파티션으로 설정.

- 해시 분할 (hash partitioning)

  - 해시 함수의 값에 따라 파티션 결정.
  - eg. id값을 4로 나누어 나머지(0~3)에 따라 파티션 결정.

- 합성 분할 (composite partitioning)

  - 상기 기술을 결합하는 것.
  - eg.범위 분할하고, 다음에 해시 분할 같은 것
  - 컨시스턴트 해시법 - 해시 분할 및 목록 분할의 합성

## 3. Sharding

- Sharding - 한 테이블의 row들을 여러 개의 서로 다른 테이블, 즉 파티션으로 분리하는 것.(수평 분할)
- Shards - 샤딩을 통해 나누어진 블록.
- 주로 어플리케이션 레벨에서 구현. 일부 DBMS에서 DB레벨에서 지원.

### 3.1. 장단점

- 장점
  - 수평적 확장(Scale-Out)이 가능.
    - 수평적 확장 - 스택에 머신을 추가
    - 수직적 확장 - 서버의 하드웨어(cpu,ram 등)을 업그레이드
  - 쿼리 반응 속도를 빠름.
  - 신뢰성을 높힘. - 오류가 생겨도 단일 Shard만 영향을 받음.
- 단점
  - 데이터 손실 위험이 큼.
  - Shard 분배를 잘못하면 샤딩이 무의미함.
  - 한 번 쪼개면 다시 un-sharded구조로 돌리기 어려움.
  - 모든 DBMS에서 네이티브하게 지원하지 않음.

### 3.2. 구조

#### 3.2.1. Key Based Sharding

![Key Based Sharding](images/04%20Advance_Key_Based_Sharding.png)

- hash based sharding
  - 추가된 데이터로 Hash함수를 돌려 Shard ID를 생성.
- Shard Key
  - Hash함수에 들어갈 Column
  - Key값으로 쓰인다는 점에서 PK와 비슷.
  - Shard Key는 정적이어야 함.

#### 3.2.2. Range Based Sharding

![Range Based Sharding](images/04%20Advance_Range_Based_Sharding.png)

- 주어진 value의 범위를 기반으로 데이터를 쪼갬.
- 실행이 간단함.
- 데이터를 골고루 분배하지 못하므로 hotspot이 발생.

#### 3.2.3. Directory Based Sharding

![Directory Based Sharding](images/04%20Advance_Directory_Based_Sharding.png)

- 어떤 shard가 어떤 데이터를 갖고 있는지를 추적할 수 있는 shard key를 사용하는 lookup table을 만들고 유지
- shard key가 낮은 cardinality를 가질 때 좋은 선택
- 유연성이 좋음.
- 성능이 좋지 않음 - 쿼리하거나 write하기 전에 lookup table에 연결이 필요하기 때문.
- lookup table이 손상되면 데이터에 접근할 수 없음.

## 4. Clustering vs Replication

![Clustering](images/04%20Advance_Clustering.png)

- Clustering

  - 여러 개의 DB를 수평적인 구조로 구축하여 Fail Over한 시스템을 구축하는 방식
  - 동기 방식으로 노드들 간의 데이터를 동기화
  - 장점 - 1개의 노드가 죽어도 다른 노드가 살아 있어 시스템을 장애없이 운영할 수 있음.
  - 단점 - 여러 노드들 간의 데이터를 동기화하는 시간이 필요하므로 Replciation에 비해 쓰기 성능이 떨어짐.

![Replication](images/04%20Advance_Replication.png)

- Replication
  - 여러 개의 DB를 권한에 따라 수직적인 구조(Master-Slave)로 구축하는 방식
  - 비동기 방식으로 노드들 간의 데이터를 동기화
  - 장점 - 비동기 방식으로 데이터가 동기화되어 지연 시간이 거의 없음
  - 단점 - 노드들 간의 데이터가 동기화되지 않아 일관성있는 데이터를 얻지 못할 수 있음.

## 5. CAP

## 6. Connection pool

## 7. 영속성(Persistence)

- 데이터를 생성한 프로그램이 종료되더라도 사라지지 않는 데이터의 특성

- Object Persistence(영구적인 객체)

  - 메모리 상의 데이터를 파일 시스템, 관계형 테이터베이스 혹은 객체 데이터베이스 등을 활용하여 영구적으로 저장하여 영속성 부여

- 데이터를 데이터베이스에 저장하는 3가지 방법

  - JDBC (java에서 사용)
  - Spring JDBC (Ex. JdbcTemplate)
  - Persistence Framework (Ex. Hibernate, Mybatis 등)

- Persistence Layer

  - 프로그램의 아키텍처에서, 데이터에 영속성을 부여해주는 계층
  - JDBC를 이용하여 직접 구현하거나 Persistence framework를 이용해 개발

- Persistence Framework
  - 데이터를 가공하는 자바 객체 층과 데이터를 저장하는 데이터베이스 층 사이를 매끄럽게 연결하는 이음매
  - 데이터의 저장, 조회, 변경, 삭제를 다루는 클래스 및 설정 파일들의 집합
  - ORM(Object Relational Mapping) - 객체(Object)와 관계형 데이터베이스(RDBMS)을 매핑하여 데이터베이스 테이블을 객체지향적으로 사용하기 위한 기술 - Hibernate
  - SQL Mapper - 객체(Object)와 SQL 문을 매핑하여 데이터를 객체화하는 기술 - Mybatis

## 8. ORM

- Object Relational Mapping - 객체-관계 매핑
  - 자바 객체를 통해 간접적으로 데이터베이스 데이터를 다루게 해줌.
  - 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 것
  - 객체 모델(OOP)과 관계형 모델(RDB) 간의 패러다임 불일치 해소

### 8.1. 장단점

- 장점
  - 객체 지향적인 코드로 인해 더 직관적이고 비즈니스 로직에 더 집중
  - 재사용 및 유지보수의 편리성이 증가
  - DBMS에 대한 종속성 감소.
- 단점
  - ORM만으로 완벽한 서비스를 구현하기가 어려움.
  - 학습량이 많아 진입장벽이 높음.
  - 프로시저가 많은 시스템에선 ORM의 객체 지향적인 장점을 활용하기 어려움.

### The Object-Relational Impedance Mismatch

- 객체-관계의 패러다임 불일치

- Granularity(세분성) - 테이블 수와 객체의 수는 일치 하지 않음.
- Inheritance(상속) - 관계형 DB에서는 상속 개념이 없음.
- Identity(일치) - 관계형DB는 기본키로 같음을 판단하지만, 객체에서는 객체 동일성(equales)을 정의 해야함
- Associations(연관성) - 관계형DB는 외래키로 나타내지만, 객체는 reference로 나타냄.
- Navigation(탐색/순회) - 관계형DB는 JOIN으로 연결하지만, 객체는 레퍼런스 연결로 그래프 형태로 연결.

### Association(연관성), 방향성

- 객체의 참조는 방향성이 있음. Directional
  - 양방향 관게가 필요할 경우 양쪽으로 두번 정의해야함.
- RDBMS는 왜래키로 양방향을 가짐. 방향성이 없음. Direction-Less

#### One-To-One Relationship

- RDBMS - 왜래키 테이블을 만듬.

- Object

```java
public class Person {
 private long personId;
 private String personName;
 private Address personAddress; // Person -> Address
 …
}
public class Address {
 private long addressId;
 private String address;
 private String zipcode;
}
```

#### One-To-Many Relationship

- RDBMS

  - 여러개의 Phone 레코드가 같은 personId를 가짐.
  - Join으로 연결.

- Object

```java
public class Person {
 private long personId;
 private String personName;
 private Set<Phone> personPhoneNumbers; // Student -> Some Phones
 …
}
public class Phone {
 private long phoneId;
 private String phoneType;
 private String phoneNumber;
}
```

## 9. Sql Injection

## 10. N+1 문제

---

## 출처

- [DB] DB 파티셔닝(Partitioning)이란 - <https://gmlwjd9405.github.io/2018/09/24/db-partitioning.html>
- DB 파티셔닝 (Partitioning) 개념 - <https://soye0n.tistory.com/267>
- https://en.wikipedia.org/wiki/Shard_(database_architecture) - <https://en.wikipedia.org/wiki/Shard_(database_architecture)>
- (번역) Database sharding이란? 🔨 - <https://velog.io/@matisse/Database-sharding에-대해>
- DB분산처리를 위한 sharding - <https://techblog.woowahan.com/2687/>
- [Database] 리플리케이션(Replication) vs 클러스터링(Clustering) - <https://mangkyu.tistory.com/97>
- [DB] ORM이란 - <https://gmlwjd9405.github.io/2019/02/01/orm.html>
