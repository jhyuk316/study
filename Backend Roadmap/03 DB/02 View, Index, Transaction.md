# 2. View, Index, Transaction

## 1. View

- 하나 이상의 테이블을 합하여 만든 가상의 테이블
- 읽기 전용과 업데이트 가능 상태로 정의 가능.
- 생성

```sql
CREATE VIEW view_name
AS
SELECT 문

```

- 삭제

```sql
DROP VIEW view_name
```

## 2. Index

- 칼럼을 기준으로 정렬된 색인을 생성함.
- 색인이 없으면 Full-Table Scan을 함.
- 색인을 갱신해야 하므로 쓰기 성능이 떨어짐.

- Index 생성

  ```sql
  CREATE [UNIQUE] INDEX index_name
  ON table_name(column_list);
  ```

  - first_name index

    ```sql
    CREATE INDEX person_first_name_idx
    ON person(first_name);
    ```

  - multi index

    ```sql
    CREATE INDEX person_first_name_last_name_idx
    ON person(last_name, first_name);
    ```

    - 순서가 다른 검색에는 사용되지 않음.
      - `SELECT * FROM person WHERE last_name="kim";` - 빠름.
      - `SELECT * FROM person WHERE last_name="kim" and first_name="john";` - 빠름.
      - `SELECT * FROM person WHERE first_name="john";` - 느림.

### 2.1. Clustered Index

- 클러스터 된 인덱스는 테이블의 실제 구조를 지정하는 인덱스. 가장 효율적인 칼럼 설정할 것.
- 테이블당 한 개만 생성 가능.
- 데이터를 지정된 칼럼에 대해 물리적으로 재배치. 변경하지 말 것.
- 기본적으로 Primary Key는 Clustered Index를 생성.
- 입력/수정/삭제 시 정렬 수행으로 느림.

![Clustered Index](images/02%20고급%20SQL_Clustered_Index.png)

- 구조
  - Root Page - 인덱스가 저장된 페이지
  - Leaf Page - 데이터가 저장된 페이지

### 2.2. Non-Clustered Index

- 테이블당 여러 개 생성 가능.
- 물리적으로 정렬하지 않음.
- 지정된 칼럼에 대해 정렬시킨 인덱스를 만듦.
- 인덱스를 저장할 추가 공간이 필요.
- 클러스터드 보다 검색은 느리지만, 입력/수정/삭제는 더 빠름.
- 구조
  - Root Page - 인덱스 저장
  - Leaf Page - 데이터가 아닌 데이터가 위치하는 포인터(RID)를 저장.
  - Data Page - 데이터가 저장된 곳.

> RID - '파일 그룹번호 - 데이터 페이지 번호 - 데이터 페이지 오프셋'으로 구성되는 포인팅 정보.

![index](images/02%20고급%20SQL_index.png)

### 2.3. Todo

- 실행계획
- B-Tree, Page(block)
- Cardinality
- Composite key

## 3. Transaction

### 3.1. ACID

- Atomicity
  - 분할할 수 없는 최소 단위
  - 한 트랜잭션 결과가 모두 반영되거나 또는 모두 취소되어야 함.
- Consistency
  - 데이터베이스가 변경되면, 유효하고 일관된 상태를 유지
  - eg. primary key - foreign key 참조무결성을 지켜야 함.
- Isolation
  - 어떤 트랜잭션 중에 이루어진 모든 중간 상태 변경이 다른 트랜잭션에 보이지 않아 간섭 없이 동작.
  - 여러 개의 transaction가 동시에 수행되어도 격리가 되어서 순차적으로 수행되는거랑 결과가 같아야 함.
- Durability
  - 트랜잭션이 완료되면 시스템 오류가 발생하여도 데이터가 손실되지 않음.

### Read Phenomena

- The ANSI/ISO standard SQL 92 refers to three different read phenomena when Transaction 1 reads data that Transaction 2 might have changed.
- Dirty Reads
  - 다른 transaction에서 commit 되지 않는 data를 읽어서 나타나는 현상.
- Non-repeatable reads
  - 한 transaction에서 두번 데이터를 읽었는데 두개의 데이터가 다른 현상.
  - read lock이 select를 할 때 일어나지 않거나 select를 하고 read lock을 release 해서 다른 trasaction이 commit을 하는 경우 두번 읽었을 때 다르게 데이터가 나옴.
- Phantom reads
  - tx가 진행되는 동안 다른 tx에서 new row가 added되거나 removed되어서 두번 읽는 경우 다르게 읽게 되는 현상.

### 3.2. isolcation level

- 데이터의 무결성을 보장하기 위해 존재
- 다른 트랜잭션이 현재의 데이터에 대한 무결성을 해치지 않기 위해 잠금을 설정
- 레벨이 높아질수록 느려짐.
- 격리 수준이 낮을 수록 concurrency로인해 이상하게 읽는 상황이 많아짐. 반대로 높아질 수록 concurrency로 인해 이상하게 읽는 상황은 적어지지만 자원을 많이 소모하고 한 transaction이 다른 transaction을 block할 확률이 높아짐.
- Isolation Level은 ANSI/ISO 에 정의되어 있음.

#### 3.2.1. Read Uncommitted(Level 0)

- 트랜잭션에서 처리 중인 아직 커밋되지 않은 데이터를 다른 트랜잭션이 읽는 것을 허용
- Dirty Read, Non-Repeatable Read, Phantom Read 현상이 발생
- Dirty Read - 커밋 않은 데이터를 읽어서 값에 오류가 생김.
  - e.g 데이터를 수정하다가 롤백했는데 그 사이에 다른 트랜잭션이 수정된 데이터를 읽는 상황

#### 3.2.2. Read committed(Level 1)

- 대부분 DBMS의 기본 Lock Level
- 커밋된 것 만 읽는 레벨
- Non-Repeatable Read, Phantom Read 현상이 발생
- Non-Repeatable Read 현상 - 한 트랜잭션 내에서 같은 쿼리를 두 번 수행할 때, 그 사이에 다른 트랜잭션이 값을 수정/삭제함으로써 두 쿼리의 결과가 상이하게 나타나는 현상

  ```sql
  T1 - SELECT * FROM member
  T2 - UPDATE member SET name= "kim" WHERE ID = 1000
  T1 - SELECT * FROM member
  ```

#### 3.2.3. Repeatable Read(Level 2)

- 선행 트랜잭션이 읽은 데이터는 트랜잭션이 종료될 때까지 후행 트랜잭션이 **갱신**하거나 **삭제**하는 것을 불허.
- Phantom Read 현상 발생
  - 한 트랜잭션 안에서 일정 범위의 레코드들을 두 번 이상 읽을 때, 첫 번째 쿼리에서 없던 유령 레코드가 두 번째 쿼리에서 나타나는 현상, **삽입**은 허용하기 때문.

#### 3.2.4. Serializable (Level 3)

- 트랜잭션이 완료될 때까지 다른 사용자는 그 영역에 해당되는 데이터에 대한 수정 및 입력이 불가능
- `SELECT ... WHERE`을 사용하는 range lock도 걸어서 phantom read도 방지.

```sql
SET TRANSACTION ISOLATION LEVEL
    {
        READ COMMITTED
        | READ UNCOMMITTED
        | REPEATABLE READ
        | SERIALIZABLE
    }
```

### 3.3. Lock

- 데이터의 일관성을 보장하기 위한 방법
- Shared Lock - 다른 사용자가 읽는 것은 허용, 변경은 **허용하지 않음**.
- Exclusive Lock - 다른 사용자가 읽고, 변경하는 모두 **허용하지 않음**.

#### Lock 레벨

| LEVEL  | 설명                                                         | 동시성 | 리소스 소비(Lock 개수) |
| ------ | ------------------------------------------------------------ | :----: | :--------------------: |
| ROW    | RID(행)에만 Lock을 설정                                      |  좋음  |          많음          |
| KEY    | 인덱스에 Lock을 설정                                         |   ↑    |           ↑            |
| PAGE   | 데이터 페이지에 Lock을 설정하는 것.                          |   ｜   |           ｜           |
| EXTENT | 익스텐트가 잠김. 8개의 페이지로 구성.                        |   ｜   |           ｜           |
| TABLE  | 테이블 전체 + 관련 인덱스 모두                               |   ↓    |           ↓            |
| DB     | 데이터 베이스 전체, 데이터베이스 복구나 스키마 변경 시 발생. |  나쁨  |          적음          |

#### Lock 종류

- SHARED(S)

  - 트랜잭션이 데이터를 읽는 동안에만 잠금
  - 여러 트랜잭션이 동시에 하나의 개체를 읽을 수 있음. 즉, 공유 잠금끼리는 서로 충돌되지 않는다
  - 다른 트랜잭션이 데이터를 변경할 수 없다.

  - 다음 행을 읽을 때, 현재 행의 공유 잠금을 해제한다.

    - 예외 사항 -REPEATABLE 레벨 이상의 트랜잭션 격리 수준 설정 시 LOCK HINT 써서, 해당 공유 잠금을 트랜잭션 끝까지 유지

    ```sql
    SELECT * FROM EMP(HOLDLOCK)
    ```

- EXCLUSIVE(X)

  - 트랜잭션이 데이터를 변경할 때 배타 잠금.
  - 다른 트랜잭션이 공유 잠금, 배타 잠금을 걸 수 없음.
  - 오직 하나의 트랜잭션만이 데이터에 대한 배타 잠금을 걸 수 있음.
    - 예외 사항 - 트랜잭션 격리 수준을 사용해서 배타 잠금 걸린 데이터를 다른 트랜잭션이 읽을 수 있음.

- UPDATE(U)

  - 트랜잭션이 변경할 데이터를 찾으면 거는 락
  - 나중에 데이터를 변경할 때까지 데이터가 변경되지 않았음을 확신하기 위해 사용.
  - 한 번에 한 트랜잭션에만 업데이트 잠금을 얻을 수 있기 때문에 교착상태(deadLock)가 방지.
  - U 잠금이 걸린 데이터에는 다른 트랜잭션이 U잠금이나 X잠금을 걸 수 없지만, S잠금은 걸 수는 있음.

- INTENT(I)

- 트랜잭션이 대상 데이터에 잠금을 걸 수 있을지 없을지를 신속히 판단할 수 있게 도와주는 잠금
- 직접 테이블의 모든 행, 페이지 잠금을 확인할 필요가 없기 때문에 성능이 향상.

  - 종류

    - IX(의도적 배타 잠금) : 잠금을 걸려는 트랜잭션이 각 리소스 계층(테이블, 페이지, 행)에 대해 X 잠금 설정하여 계층의 아래쪽 일부 리소스 수정

    - SIX(공유 및 의도적 배타 잠금) : 잠금을 걸려는 트랜잭션이 각 리소스 계층에 대해 IX 잠금을 설정하여 계층의 아래쪽에 있는 모든 리소스에 대해서는 읽기 작업 / 일부 리소스는 수정 작업 / 최상위 수준 리소스에서는 동시 IS 잠금 허용

- SCHEMA (Sch)

  - Sch-M (Schema Manipulation)

    - DDL(스키마 변경) 문 실행 시, Schema 자체에 대해서 검.
    - 모든 잠금에 대해 배타적, 어떤 작업도 허용하지 않음.

  - Sch-S (Schema Stability)

    - 쿼리문 컴파일 시 발생.
    - S or X와 호환.
    - 다른 트랜잭션 잠금을 차단하지 않음.
    - DDL 작업은 수행할 수 없음.

#### Lock 옵션(WITH)

- 테이블 힌트

  - `... FROM ... WITH ...` - 옵션 작성
  - 사용자가 원하는 형태로 강제 판단할 수 있음.

- 테이블 힌트 종류

  - NOLOCK ( = READUNCOMMITED)

    - 차단 현상이 발생.
      - 배타적 잠금(X) 걸린 대상에 대해 공유 잠금(S)을 설정하는 경우.
      - 공유 잠금(S)이 걸린 대상에 배타적 잠금(X)을 설정하는 경우
    - 해결책 - SELECT 쿼리를 할 때 **공유 잠금을 설정하지 않고 데이터를 읽음** 즉, 커밋되지 않은 결과를 미리 읽어오는 것

  - ROWLOCK

    - 기본적으로 행 단위 잠금을 사용하지만, 내부적 기준 따라 더 상위 단위(페이지, 테이블) 대상에 대해서 잠금 설정하려면 페이지 , 테이블 잠금을 자동적으로 승격하여 사용.
    - 사용자가 이를 통제하여 행단 위 잠금을 강제하기 위해서 사용하는 옵션

  - READPAST

    - 다른 트랜잭션이 잠근 행을 읽지 않음

  - XLOCK

    - 단독 잠금을 걸고 트랜잭션이 끝날 때 까지 유지

  - UPLOCK

    - SELECT 하는 대상에 대해 곧바로 배타적 잠금 설정 예정일 경우 사용
    - SELECT 하는 대상에 다른 세션에서 배타적 잠금을 설정하지 못하도록 통제하기 위해서 사용
    - e.g. 1번의 UPLOCK으로 인해 2번의 UPDATE 차단

    ```sql
    SPID 1 : SELECT * FROM 테이블 WITH(UPDLOCK)
    SPID 2 : UPDATE 테이블 SET...
    SPID 1 : UPDATE 테이블 SET...
    ```

#### Blocking

- Lock들의 Race condition이 발생하여 특정 세션이 작업을 진행하지 못하고 멈춰 선 상태
- 공유 Lock - 배타적 Lock / 배타적 Lock - 배타적 Lock 끼리 블로킹 발생
- 해결책
  - Transaction commit 또는 Rollback
  - 트랜잭션을 가능한 짧게 정의하면 경합 줄일 수 있음.
  - 동일한 데이터를 동시에 변경하는 작업을 하지 않도록 설계
    - 트랜잭션이 활발한 주간에는 대용량 갱신 작업 수행하면 안 됨
  - 대용량 작업이 불가피할 경우
    - 작업 단위를 쪼개거나, lock_timeout 설정하여 해당 lock 최대 시간 설정

#### DeadLock

- 트랜잭션 간의 교착상태
- 두 개의 트랜잭션 간에 각각의 트랜잭션이 가지고 있는 리소스 Lock 획득 시 , 발생
- 해결책 : 한쪽 트랜잭션 처리를 강제 종료 (비용이 적은 트랜잭션의 처리 강제 종료)

- Two-phase Locking (2PL)

  - In transaction processing, 2PL is a concurrency control method that guarantees serializability.
    Locks are applied and removed in two phases
    - Expanding phase: locks are acquired and no locks are released.
    - Shrinking phase: locks are released and no locks are acquired.
  - Deadlock을 일으킬 수 있음.

- 예시 1

  1. 1번 트랜잭션에서 2번 리소스의 베타 LOCK, 2번 트랜잭션에서 1번 리소스의 베타 LOCK
  2. 1, 2번이 각자 공유 LOCK을 획득하려고 함.

  ![deadlock1](images/02%20고급%20SQL_deadlock1.png)

- 예시 2

  1. 1번 트랜잭션이 공유 LOCK설정 후 Sleep.
  2. 2번 트랜잭션이 배타 LOCK을 설정하려 할 때 무기한 기다림.

  ![deadlock2](images/02%20고급%20SQL_deadlock2.png)

---

## 4. 출처

- 즐겁게 배우는 SQL 11. 색인(인덱스) - <https://velog.io/@jiffydev/즐겁게-배우는-SQL-11.-색인인덱스>
- [SQL] 색인기능, INDEX! - <https://runtoyourdream.tistory.com/136>
- SQL 색인 - <https://learntutorials.net/ko/sql/topic/344/색인>
- [SQL] Clustered Index & Non-Clustered Index - <https://velog.io/@gillog/SQL-Clustered-Index-Non-Clustered-Index>
- [SQL] 인덱스 (클러스터, 비클러스터) 개념 - <https://mongyang.tistory.com/75>
- Clustered vs NonClustered (index 개념) - <https://gwang920.github.io/database/clusterednonclustered/>
- NonClustered Index Structure - <https://www.sqlservercentral.com/articles/nonclustered-index-structure>
- Transaction Isolation Level 이해 - <https://augustines.tistory.com/135>
- 데이터베이스 Transaction Isolation Level - <https://effectivesquid.tistory.com/entry/데이터베이스-Isolation-Level>
- [SQL]LOCK이란? - <https://syujisu.tistory.com/193>
