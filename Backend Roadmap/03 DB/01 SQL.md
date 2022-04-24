# 1. 기초 SQL

- [1. DB 명령어](#1-db-명령어)
  - [1.1. SHOW DATABASES](#11-show-databases)
  - [1.2. SHOW TABLES](#12-show-tables)
  - [1.3. SHOW COLUMNS](#13-show-columns)
- [2. SQL](#2-sql)
- [3. DDL(Data Definition Language)](#3-ddldata-definition-language)
  - [3.1. SQL Data Types](#31-sql-data-types)
  - [3.2. CREATE](#32-create)
  - [3.3. DROP](#33-drop)
  - [3.4. ALTER](#34-alter)
- [4. DML(Data Manipulation Language), DQL(Data Query Language)](#4-dmldata-manipulation-language-dqldata-query-language)
  - [4.1. Create](#41-create)
  - [4.2. Read](#42-read)
  - [4.3. Update](#43-update)
  - [4.4. Delete](#44-delete)
  - [4.5. 추가 기능](#45-추가-기능)
  - [4.6. Alias](#46-alias)
    - [4.6.1. WHERE 조건절](#461-where-조건절)
    - [4.6.2. 서브 쿼리](#462-서브-쿼리)
    - [4.6.3. ORDER BY - 정렬](#463-order-by---정렬)
    - [4.6.4. DISTINCT - 중복제거](#464-distinct---중복제거)
    - [4.6.5. LIMIT & OFFSET - 출력 개수 제한](#465-limit--offset---출력-개수-제한)
    - [4.6.6. Aggregation](#466-aggregation)
    - [4.6.7. GRUOP BY - 그룹으로 묶기](#467-gruop-by---그룹으로-묶기)
    - [4.6.8. HAVING - 그룹의 조건](#468-having---그룹의-조건)
    - [4.6.9. WITH ROLLUP - 중간 합계도 출력](#469-with-rollup---중간-합계도-출력)
    - [4.6.10. JOIN - 테이블 조합](#4610-join---테이블-조합)
    - [4.6.11. UNION & INTERSECT](#4611-union--intersect)
  - [4.7. MySQL 내장 함수](#47-mysql-내장-함수)
- [5. DCL(Data Control Language)](#5-dcldata-control-language)
  - [5.1. GRANT](#51-grant)
  - [5.2. REVOKE](#52-revoke)
- [6. TCL(Transaction Control Language)](#6-tcltransaction-control-language)
  - [6.1. 트랜잭션](#61-트랜잭션)
  - [6.2. 명령어](#62-명령어)
- [7. 출처](#7-출처)

## 1. DB 명령어

- `-- 주석은 이렇게`

### 1.1. SHOW DATABASES

- MySQL - `SHOW DATABASES`
- Oracle - 오라클은 데이터베이스 개념이 없음. 단일 데이터베이스.
- PostgreSQL - `SELECT datname FROM pg_database;`

### 1.2. SHOW TABLES

- MySQL
  - `SHOW TABLES`
  - `SHOW TABLE STATUS` - 테이블 정보
- Oracle
  - `SELECT * FROM ALL_ALL_TABLES`
  - `SELECT TABLE_NAME FROM TABS WHERE TABLESPACE_NAME = '테이블 스페이스명';`
- PostgreSQL
  - `SELECT table_name FROM information_schema.tables WHERE table_schema = '스키마명';`

### 1.3. SHOW COLUMNS

- MySQL
  - `SHOW COLUMNS FROM 테이블명`
  - `DESCRIBE 테이블명` or `DESC 테이블명`
- Oracle
  - `DESCRIBE 테이블명`
- PostgreSQL
  - `SELECT column_name FROM information_schema.columns WHERE table_name = '테이블명';`

## 2. SQL

- Structured Query Language
- 관계형 데이터베이스 관리 시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

- RDBMS 밴더마다 문법이 약간 씩 다름. (Oracle, MySQL, PostgreSQL 등)
- 대소문자를 구분하지 않음.

## 3. DDL(Data Definition Language)

- 데이터 정의 언어
- 데이터베이스, 테이블, 뷰, 인덱스 등의 개체를 생성/삭제/변경
- DDL은 트랜잭션을 발생시키지 않음.
- ROLLBACK, COMMIT 사용 불가
- DLL문은 즉시 적용.

### 3.1. SQL Data Types

- 문자
  - CHAR(n) - 고정 길이 문자열, 공간 낭비가 생길 수 있음.
  - VARCHAR(n) - 가변 길이 문자열, 최대 n개 이내에서 크기를 값에 맞춤. 최댓값이 너무 크면 느림.
- 숫자
  - BIT(n)
  - INT, BIGINT, SMALLINT - 정수형 타입
  - FLOAT
  - DECIMAL(p,s)
    - 정확한 숫자를 저장하기 위한 타입.
    - p 자릿수의 숫자, s 소수점 이하의 자릿수, 정수 자릿수는 p - s.
  - REAL(s)
- 날짜 & 시간
  - DATE
  - TIME
  - TIMESTAMP

### 3.2. CREATE

- CREATE - 데이터베이스 객체 생성 명령어

  - `CREATE DATABASE CITYINFO` - CITYINFO 데이터베이스 생성
  - `USE DATABASE CITYINFO` - CITYINFO 데이터베이스 사용
  - CREATE TABLE - 테이블 생성

  ```sql
  CREATE TABLE USER (
      ID VARCHAR2(100) NOT NULL PRIMARY KEY,
      PASSWORD VARCHAR2(30) NOT NULL,
      NAME VARCHAR2(30) NOT NULL,
      ADDRESS VARCHAR2(30) NULL,
      PHONE VARCHAR2(30) NOT NULL
      )
  ;
  ```

### 3.3. DROP

> DROP과 ALTER는 쓰지 말자!

- DROP - 데이터베이스 객체 삭제
  - `DROP DATABASE CITYINFO`
  - `DROP TABLE USER`
- TRUNCATE - 테이블의 내용을 지움, DROP 후 CREATE

|      기능      |  DROP  | TRUNCATE | DELECT |
| :------------: | :----: | :------: | :----: |
|      DATA      |  삭제  |   삭제   |  삭제  |
|   저장 영역    |  삭제  |   삭제   |  보존  |
|  테이블 구조   |  삭제  |   보존   |  보존  |
| ROLLBACK 여부  | 불가능 |  불가능  |  가능  |
| FLASHBACK 여부 |  가능  |  불가능  |  가능  |

- `FLASHBACK TABLE 테이블명 TO BEFORE DROP` - 테이블을 DROP 전으로 되돌기.

### 3.4. ALTER

> DROP과 ALTER는 쓰지 말자!

- 테이블 수정 명령

- ADD - 칼럼 추가

```SQL
ALTER TABLE USER
ADD NUMBER INT NULL;
```

- MODIFY - 칼럼 변경

```SQL
ALTER TABLE USER
ADD ADDRESS VARCHAR2(255) NOT NULL;
```

- DROP - 칼럼 삭제

```SQL
ALTER TABLE USER
DROP NUMBER INT NULL;
```

## 4. DML(Data Manipulation Language), DQL(Data Query Language)

- 데이터 조작 언어
- 데이터를 선택, 삽입, 수정, 삭제
- DML의 대상은 테이블의 행, 테이블이 미리 정의되어 있어야 함.
- 트랜잭션 발생.

- SQL 구문 순서

  ```sql
  SELECT 칼럼명
  FROM 테이블명
  WHERE 조건
  GROUP BY 칼럼명
  HAVING 그룹 조건
  ORDER BY 칼럼명
  LIMIT 개수
  ```

- SQL 실행 순서

  - `FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY` -> `LIMIT`

- CRUD

  | 이름   | 조작       | SQL    |
  | ------ | ---------- | ------ |
  | Create | 생성       | INSERT |
  | Read   | 읽기, 검색 | SELECT |
  | Update | 갱신, 편집 | UPDATE |
  | Delete | 삭제       | DELETE |

### 4.1. Create

- INSERT - 테이블에 데이터를 삽입하는 명령어
- `INSERT INTO 테이블명 (칼럼명 1, 칼럼명 2, 칼럼명 3) VALUES (값 1, 값 2, 값 3);`
- 모든 칼럼에 데이터를 저장하는 경우 칼럼명 생략 가능.

```sql
INSERT INTO USER (ID, PASSWORD, NAME, ADDRESS, PHONE)
    VALUES ('user1', '1234', '김철수', '서울', '010-1234-1234');

INSERT INTO USER
    VALUES ('user1', '1234', '김철수', '서울', '010-1234-1234');
```

### 4.2. Read

- SELECT - 테이블에 저장된 데이터를 조회하는 명령어
- `SELECT 칼럼명 FROM 테이블명 WHERE 조건 ORDER BY 칼럼명 ASC or DESC LIMIT 개수;`
- \* - 모든 칼럼의 데이터를 조회.

```sql
SELECT *
FROM USER;

SELECT
  ID,
  NAME,
  ADDRESS
FROM USER;
```

### 4.3. Update

- UPDATE - 테이블에 저장되어있는 데이터를 수정하는 명령어
- `UPDATE 테이블명 SET 칼럼명 1 = 변경할 값 1, 칼럼명 2 = 변경할 값 2 WHERE 조건`
- 조건(WHERE)절이 없으면 모든 행에 적용됨.

```sql
UPDATE USER
  SET
    ID = 'user2',
    PASSWORD = '4567',
    ADDRESS = '경기'
;
```

```sql
UPDATE USER
  SET
    PASSWORD = '4567',
    ADDRESS = '경기'
WHERE ID = 'user2';
```

### 4.4. Delete

- DELETE - 테이블에 저장된 데이터를 삭제하는 명령어.
- `DELETE FROM 테이블명 WHERE 조건`
- 조건절이 없으면 모든 데이터 삭제.

```sql
DELETE
FROM USER
WHERE ID = 'user2';
```

### 4.5. 추가 기능

### 4.6. Alias

- 테이블이나 칼럼의 별칭을 지정하여 사용, 출력 가능.
- SQL 실행 순서 때문에 SELECT에서 지정한 alias 이름을 WHERE 조건에 쓸 수 없음.
  마찬가지 이유로 ORDER BY에는 가능.
- Column aliases

  ```sql
  SELECT
    inv_no AS invoice_no,
    amount,
    due_date AS 'Due date',
    cust_no 'Customer No' -- 생략 가능, 하지만 혼용하지 말 것.
  FROM
    invoices;
  ```

- Table alias

  ```sql
  SELECT
    e.first_name,
    e.last_name
  FROM
    employees AS e;
  ```

#### 4.6.1. WHERE 조건절

- 특정 조건을 만족하는 결과만 보고 싶을 때
- 조건 연산자 - =, <, >, <=, >=, <>, !=
- 관계 연산자 - OR, AND, NOT
- 범위 지정 - BETWEEN(연속 값), IN(이산 값)
  - `WHERE COST BETWEEN 100 AND 200` - 100 이상 200 이하
  - `WHERE COUNTRY IN('KOR', 'USA', 'JPN')
- LIKE - 문자열 검색
  - % - 여러 문자
  - \_ - 한 문자
  - `WHERE COUNTRY LIKE 'K%'` - K로 시작하는 나라들

#### 4.6.2. 서브 쿼리

- 쿼리문 안에 또 쿼리문을 넣는 것
- 서브 쿼리 결과가 둘 이상이면 에러
- e.g. 이름이 서울인 나라의 코드를 찾고, 그 나라의 도시 검색.

```SQL
SELECT *
FROM CITY
WHERE COUNTRY = (
    SELECT COUNTRY
    FROM CITY
    WHERE NAME = 'SEOUL'
);
```

- SOME, ANY - 여러 개의 결과 중 하나라도 만족해도 됨.

  - S로 시작하는 이름의 도시들 중 하나보다 인구수가 많은 도시 검색.

  ```SQL
  SELECT *
  FROM CITY
  WHERE POPULATION > ANY (
    SELECT POPULATION
    FROM CITY
    WHERE NAME LIKE 'S%'
  );
  ```

- ALL - 여러 개의 결과를 모두 만족해야 함.

  - S로 시작하는 이름의 모든 도시들보다 인구수가 많은 도시 검색.

  ```SQL
  SELECT *
  FROM CITY
  WHERE POPULATION > ALL (
    SELECT POPULATION
    FROM CITY
    WHERE NAME LIKE 'S%'
  );
  ```

#### 4.6.3. ORDER BY - 정렬

- ASC - ASCENDING, 오름차순, 생략 가능.
- DESC - DESCENDING, 내림차순.

```sql
ORDER BY
  COUNTRY,
  POPULATION DESC; -- 나라 오름차순, 인구수 내림차순 정렬.
```

#### 4.6.4. DISTINCT - 중복제거

```sql
SELECT DISTINCT COUNTRY
FROM CITY; -- 나라를 중복 없이 검색
```

#### 4.6.5. LIMIT & OFFSET - 출력 개수 제한

- MySQL, PostgreSQL

  - `LIMIT 10` - 10개로 출력 제한.
  - `OFFSET 3` - 3개 skip 하고 출력.

  ```sql
  SELECT
      employee_id, first_name, last_name
  FROM
      employees
  ORDER BY first_name
  LIMIT 5 OFFSET 3;
  ```

  ![MYSQL LIMIT OFFSET](images/01%20SQL_MYSQL_LIMIT_OFFSET.png)

- Oracle

  ```sql
  SELECT
    employee_id, first_name, last_name
  FROM
    employees
  ORDER BY first_name
  OFFSET 3 ROWS
  FETCH NEXT 5 ROWS ONLY;
  ```

#### 4.6.6. Aggregation

- AVG() - 평균
- MIN() - 최솟값
- MAX() - 최댓값
- COUNT() - 개수
- COUNT(DISTINCT) - 중복되지 않은 개수
- STDEV() - 표준편차
- VARIANCE() - 분산

```sql
SELECT
  AVG(salary)
FROM
  employees;
```

#### 4.6.7. GRUOP BY - 그룹으로 묶기

- 주로 Aggregation과 함께 사용.
- e.g. 나라별 도시 평균 인구 검색

```SQL
SELECT
  COUNTRY,
  AVG(POPULATION) AS '평균 인구'
FROM CITY
GROUP BY COUNTRY;
```

#### 4.6.8. HAVING - 그룹의 조건

- e.g. 도시 평균 인구가 1000000 초과인 나라 검색
- SELECT 절에서 설정한 Alias를 사용 가능. (왜지?)

```SQL
SELECT
  COUNTRY,
  AVG(POPULATION) AS '평균 인구'
FROM CITY
GROUP BY COUNTRY
HAVING AVG(POPULATION) > 1000000;
```

#### 4.6.9. WITH ROLLUP - 중간 합계도 출력

- 각 도시의 인구와 인구 총합을 함께 검색

```SQL
SELECT
  COUNTRY,
  NAME,
  SUM(POPULATION)
FROM CITY
GROUP BY COUNTRY, NAME WITH ROLLUP;
```

#### 4.6.10. JOIN - 테이블 조합

- INNER - 기준 테이블과 조인 테이블 모두에 데이터가 존재해야 함.
- OUTTER - 기준 테이블에만 데이터가 존재하면 됨.

- JOIN(INNER JOIN)

  - CITY 테이블의 COUNTRYCODE와 COUNTRY 테이블의 CODED와 COUNTRYLANGUAGE 테이블의 CODE가 같은 조합 결과 검색.

  ```SQL
  SELECT *
  FROM
    CITY
    JOIN COUNTRY
      ON CITY.COUNTRYCODE = COUNTRY.CODE;
    JOIN COUNTRYLANGUAGE
      ON CITY.COUNTRYCODE = COUNTRYLANGUAGE.CODE;
  ```

- LEFT/RIGHT OUTTER JOIN

  - 기준 테이블에는 있지만 조인 테이블에 없으면 NULL로 표기
  - CITY에 있지만 COUNTRY 없는 데이터도 출력

  ```SQL
  SELECT *
  FROM
    CITY
    LEFT JOIN COUNTRY
      ON CITY.COUNTRYCODE = COUNTRY.CODE;
  ```

- CROSS JOIN - 교차 조인

  - A 테이블과 B 테이블의 모든 조합을 출력, A\*B

  - e.g. 직원들의 성과 이름의 모든 조합. SELF CROSS JOIN.

  ```SQL
  SELECT E1.LASTNAME, E2.FIRSTNAME
  FROM EMPLOYEES E1
  CROSS JOIN EMPLOYESS E2
  ORDER BY E1.EMPLYEEID;
  ```

- SELF JOIN - 자기 자신의 테이블과 조인

```sql
SELECT
  e.first_name || ' ' || e.last_name AS employee,
  m.first_name || ' ' || m.last_name AS manager
FROM
  employees e
  LEFT JOIN employees m
    ON m.employee_id = e.manager_id
ORDER BY manager;
```

![Self_Join](images/01%20SQL_Self_Join.png)

#### 4.6.11. UNION & INTERSECT

- 두 테이블의 집합 연산. 칼럼이 일치해야 함.

  - UNION - 합집합, 중복제거
  - UNION ALL - 중복 포함.

    ```SQL
    SELECT
      NAME,
      CITY
    FROM CUSTOMERS
    UNION
    SELECT
      NAME,
      CITY
    FROM SUPPLIERS;
    ```

  - INTERSECT - 교집합

    ```SQL
    SELECT
      NAME,
      CITY
    FROM CUSTOMERS
    INTERSECT
    SELECT
      NAME,
      CITY
    FROM SUPPLIERS;
    ```

### 4.7. MySQL 내장 함수

- 문자열

  - LENGTH() - 문자열 길이
  - CONCAT() - 문자열 합치기, 인자 중 하나라도 NULL이면 NULL 반환
  - LOCATE('ABC', 'ABCDE') - 문자열의 위치 반환, 1부터 시작
  - LEFT(5), RIGHT(5) - 각 방향에서 정해진 문자 수(5)만큼 반환
  - LOWER(), UPPER() - 소문자로, 대문자로 변경
  - REPLECE('MSSQL', 'MS', My') - 문자열 변경, MSSQL을 MySQL로 변경.
  - TRIM() - 문자열 앞뒤의 특정 문자(기본값 공백) 제거.
    - BOTH - 양쪽, 기본값
    - LEADING - 앞
    - TRAILING - 뒤
    - `SELECT TRIM(LEADING '0' FROM '000123');' - 앞의 0 제거 후 123 출력

- 숫자

  - FORMAT(123123.123123, 2) - 숫자에 쉼표, 소수점 이하 자릿수 지정, 123,123.12
  - SQRT(), POW(), EXP(), LOG()
  - SIN(), COS(), TAN(), PI() - SIN(PI())
  - ABS()
  - RAND() - 0.0 이상 1.0 미만

- 날짜

  - NOW() - 현재 날짜, 시각
  - CURDATE() - 현재 날짜
  - CURTIME() - 현재 시각
  - DATE() - 전달받은 값의 날짜 반환
  - MONTH(), DAY(), HOUR(), MINUTE(), SECOND()
  - MONTHNAME(), DAYNAME() - 달 이름, 요일 출력
  - DAYOFWEEK(), DAYOFMONTY(), DAYOFYEAR()
  - DATE_FORMAT(NOW(), '% y % b % d % a') - 22 APR 23 SAT

## 5. DCL(Data Control Language)

- 데이터 제어 언어
- 사용자를 등록하고, 사용자에게 특정 데이터베이스를 사용할 권리를 부여.

### 5.1. GRANT

- 권한 부여

- 시스템 권한 - `GRANT 권한 TO 사용자 계정`

  - CREATE USER : 계정 생성 권한
  - DROP USER : 계정 삭제 권한
  - DROP ANY TABLE : 테이블 삭제 권한
  - CREATE SESSION : 데이터베이스 접속 권한
  - CREATE TABLE : 테이블 생성 권한
  - CREATE VIEW : 뷰 생성 권한
  - CREATE SEQUENCE : 시퀀스 생성 권한
  - CREATE PROCEDURE : 함수 생성 권한

- 객체 권한 - `GRANT 권한 ON 객체 TO 사용자 계정`

  - ALTER : 테이블 변경 권한
  - INSERT : 데이터 조작 권한
  - DELETE : 데이터 조작 권한
  - SELECT : 데이터 조작 권한
  - UPDATE : 데이터 조작 권한
  - EXECUTE : PROCEDURE 실행 권한

### 5.2. REVOKE

- 권한 회수
  - `REVOKE 권한 FROM 사용자 계정`
  - `REVOKE 권한 ON 객체 FROM 사용자 계정`

## 6. TCL(Transaction Control Language)

- 트랜잭션 제어 언어
- 안전한 거래 보장
- 동시에 다수의 작업을 독립적으로 안전하게 처리하기 위한 상호 작용 단위

### 6.1. 트랜잭션

- 일 처리 단위
- 한 개 이상의 데이터베이스 조작
- 하나 이상의 SQL 문장
- 분할할 수 없는 최소 단위
- 한 트랜잭션 결과가 모두 반영되거나 또는 모두 취소되어야 함.

### 6.2. 명령어

- `COMMIT` - 거래 내역 확정
- `ROLLBACK` - 거래 내역 취소
- `SAVEPOINT`, `CHECKPOINT` - 저장점 설정(ROLLBACK 위치 지정)
  - COMMIT을 하면 이전의 SAVEPOINT는 사라짐.
  - SAVEPOINT는 여러 개 생성 가능.

---

## 7. 출처

- SQL Tutorial - <https://www.sqltutorial.org/>
- SQL - <https://ko.wikipedia.org/wiki/SQL>
- CRUD - <https://ko.wikipedia.org/wiki/CRUD>
- CRUD - <http://wiki.hash.kr/index.php/CRUD>
- 오라클 CRUD란? - <https://nancording.tistory.com/9>
- [SQL] SQL 구문(문법) 순서 - select, from, where, group by, having, order by - <https://data-make.tistory.com/23>
- 기본 SQL Query문 정리 ( SELECT, INSERT, UPDATE, DELETE ) - <https://lcs1245.tistory.com/entry/기본-SQL-Query문-정리-SELECT-INSERT-UPDATE-DELETE>
- [MySQL] DDL 명령어 사용하는 방법(CREATE, DROP, ALTER, RENAME, TRUNCATE) - <https://kkamikoon.tistory.com/entry/MySQL-DDL-명령어-사용하는-방법 CREATE-DROP-ALTER-RENAME-TRUNCATE>
- SQL DDL, DML, DCL이란? - <https://zzdd1558.tistory.com/88>
- [SQL] 13. 데이터 정의 언어(DDL문) - <https://superkong1.tistory.com/21>
- [SQL] SQL 정리 1 - <https://velog.io/@ye050425/SQL-SQL-정리>
- SQL 기초 & 자주쓰는 쿼리문 정리 - <https://365kim.tistory.com/102>
- SQL 활용(기본 SQL 작성-DML)-명령문 - <https://velog.io/@ansalstmd/SQL 활용 기본 SQL 작성-DML-명령문>
- 6.  [MySQL] GROUP BY , 집계 함수와 산술 함수 알아보기 - <https://velog.io/@yj-leee/06.-MySQL-GROUP-BY-집계 함수와-산술 함수-알아보기>
- [PostgreSQL] SELECT LIMIT ~ OFFSET 사용하기 (ft. 페이징 활용) - <https://mine-it-record.tistory.com/346>
- [MSSQL] 조인 방법 쉽게 정리 (INNER JOIN, OUTER JOIN) - <https://gent.tistory.com/376>
- MySQL 데이터베이스 한 번에 끝내기 SQL Full Tutorial Course using MySQL Database - <https://www.youtube.com/watch? v=vgIc4 ctNFbc>
- 왕초보용! 갖고 노는 MySQL 데이터베이스 강좌 - <https://www.youtube.com/watch?v=dgpBXNa9vJc>
- DCL (Data Cntrol Language) - <https://velog.io/@ansalstmd/SQL 활용 기본 SQL 작성-DCL>
