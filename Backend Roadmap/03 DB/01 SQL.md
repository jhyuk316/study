# 1. 기초 SQL

- [1. DB 명령어](#1-db-명령어)
- [2. SQL](#2-sql)
- [3. DDL(Data Definition Language)](#3-ddldata-definition-language)
  - [3.1. CREATE](#31-create)
  - [3.2. DROP](#32-drop)
  - [3.3. ALTER](#33-alter)
- [4. DML(Data Manipulation Language)](#4-dmldata-manipulation-language)
  - [4.1. Create](#41-create)
  - [4.2. Read](#42-read)
  - [4.3. Update](#43-update)
  - [4.4. Delete](#44-delete)
  - [4.5. 추가 기능](#45-추가-기능)
    - [4.5.1. WHERE 조건절](#451-where-조건절)
    - [4.5.2. 서브 쿼리](#452-서브-쿼리)
    - [4.5.3. ORDER BY - 정렬](#453-order-by---정렬)
    - [4.5.4. DISTINCT - 중복제거](#454-distinct---중복제거)
    - [4.5.5. LIMIT n - 출력 개수 제한](#455-limit-n---출력-개수-제한)
    - [4.5.6. GRUOP BY - 그룹으로 묶기](#456-gruop-by---그룹으로-묶기)
    - [4.5.7. HAVING - 그룹의 조건](#457-having---그룹의-조건)
    - [4.5.8. WITH ROLLUP - 중간 합계도 출력](#458-with-rollup---중간-합계도-출력)
    - [4.5.9. JOIN - 테이블 조합](#459-join---테이블-조합)
    - [4.5.10. UNION](#4510-union)
  - [4.6. MySQL 내장 함수](#46-mysql-내장-함수)
- [5. DCL(Data Control Language)](#5-dcldata-control-language)
  - [5.1. GRANT](#51-grant)
  - [5.2. REVOKE](#52-revoke)
- [6. TCL(Transaction Control Language)](#6-tcltransaction-control-language)
  - [6.1. 트랜잭션](#61-트랜잭션)
  - [6.2. 명령어](#62-명령어)
- [출처](#출처)

## 1. DB 명령어

- 데이터 베이스 지정
- SHOW DB명
- USE DB명
- 테이블 리스트 출력

  - `SHOW TABLES`
  - `SHOW TABLE STATUS` - 테이블 정보

- `DESCRIBE 테이블명` or `DESC 테이블명` - 테이블 칼럼 보기

- `-- 주석은 이렇게`

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

### 3.1. CREATE

- CREATE - 데이터베이스 객체 생성 명령어

  - `CREATE DATABASE CITYINFO` - CITYINFO 데이터 베이스 생성
  - `USE DATABASE CITYINFO` - CITYINFO 데이터 베이스 사용
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

### 3.2. DROP

- DROP - 데이터 베이스 객체 삭제
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

### 3.3. ALTER

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

## 4. DML(Data Manipulation Language)

- 데이터 조작 언어
- 데이터를 선택, 삽입, 수정, 삭제
- DML의 대상은 테이블의 행, 테이블이 미리 정의되어 있어야 함.
- 트랜잭션 발생.

  - 실제 테이블에 적용하지 않고 임시로 적용.
  - ROLLBACK, COMMIT 가능

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
    VALUES ('user1', '1234', '김철수', '서울', '010-1234-1234')
;

INSERT INTO USER
    VALUES ('user1', '1234', '김철수', '서울', '010-1234-1234')
;
```

### 4.2. Read

- SELECT - 테이블에 저장된 데이터를 조회하는 명령어
- `SELECT 칼럼명 FROM 테이블명 WHERE 조건 ORDER BY 칼럼명 ASC or DESC LIMIT 개수;`
- \* - 모든 칼럼의 데이터를 조회.

```sql
SELECT *
FROM USER
;

SELECT ID, NAME, ADDRESS
FROM USER
;
```

### 4.3. Update

- UPDATE - 테이블에 저장되어있는 데이터를 수정하는 명령어
- `UPDATE 테이블명 SET 칼럼명 1 = 변경할 값 1, 칼럼명 2 = 변경할 값 2 WHERE 조건`
- 조건(WHERE) 절이 없으면 모든 행에 적용됨.

```sql
UPDATE USER
    SET ID = 'user2',
        PASSWORD = '4567',
        ADDRESS = '경기'
;
```

```sql
UPDATE USER
    SET PASSWORD = '4567',
        ADDRESS = '경기'
    WHERE ID = 'user2'
;
```

### 4.4. Delete

- DELETE - 테이블에 저장되어 있는 데이터를 삭제하는 명령어.
- `DELETE FROM 테이블명 WHERE 조건`
- 조건절이 없으면 모든 데이터 삭제.

```sql
DELETE FROM USER WHERE ID = 'user2'
;
```

### 4.5. 추가 기능

#### 4.5.1. WHERE 조건절

- 특정 조건을 만족하는 결과만 보고 싶을 때
- 조건 연산자 - =, <, >, <=, >=, <>,!=
- 관계 연산자 - OR, AND, NOT
- 범위 지정 - BETWEEN(연속 값), IN(이산 값)
  - `WHERE COST BETWEEN 100 AND 200` - 100 이상 200 이하
  - `WHERE COUNTRY IN('KOR', 'USA', 'JPN')
- LIKE - 문자열 검색
- % - 여러 문자
- \_ - 한 문자
- `WHERE COUNTRY LIKE 'K%'` - K로 시작하는 나라들

#### 4.5.2. 서브 쿼리

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

#### 4.5.3. ORDER BY - 정렬

- ASC - ASCENDING, 오름차순, 생략 가능.
- DESC - DESCENDING, 내림차순.
- `ORDER BY COUNTRY, POPULATION DESC` - 나라 오름차순, 인구수 내림차순 정렬.

#### 4.5.4. DISTINCT - 중복제거

- `SELECT DISTINCT COUNTRY FROM CITY` - 나라를 중복 없이 검색

#### 4.5.5. LIMIT n - 출력 개수 제한

- `LIMIT 10` - 10개로 출력 제한

#### 4.5.6. GRUOP BY - 그룹으로 묶기

- 집계 함수 - Agregate Function과 함께 사용.
  - AVG() - 평균
  - MIN() - 최솟값
  - MAX() - 최댓값
  - COUNT() - 개수
  - COUNT(DISTINCT) - 중복되지 않은 개수
  - STDEV() - 표준편차
  - VARIANCE() - 분산
- e.g. 나라 별 도시 평균 인구 검색

```SQL
SELECT COUNTRY, AVG(POPULATION) AS '평균 인구'
FROM CITY
GROUP BY COUNTRY;
```

#### 4.5.7. HAVING - 그룹의 조건

- e.g. 도시 평균 인구가 1000000 초과인 나라 검색

```SQL
SELECT COUNTRY, AVG(POPULATION) AS '평균 인구'
FROM CITY
GROUP BY COUNTRY
HAVING AVG(POPULATION) > 1000000;
```

#### 4.5.8. WITH ROLLUP - 중간 합계도 출력

- 각 도시의 인구와 인구 총합을 함께 검색

```SQL
SELECT COUNTRY, NAME, SUM(POPULATION)
FROM CITY
GROUP BY COUNTRY, NAME WITH ROLLUP;
```

#### 4.5.9. JOIN - 테이블 조합

- INNER - 기준 테이블과 조인 테이블 모두에 데이터가 존재해야 함.
- OUTTER - 기준 테이블에만 데이터가 존재하면 됨.

- JOIN(INNER JOIN)

  - CITY테이블의 COUNTRYCODE와 COUNTRY테이블의 CODED와 COUNTRYLANGUAGE테이블의 CODE가 같은 조합 결과 검색.

  ```SQL
  SELECT *
  FROM CITY
  JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE;
  JOIN COUNTRYLANGUAGE ON CITY.COUNTRYCODE = COUNTRYLANGUAGE.CODE;
  ```

  - SELF JOIN - 자기 자신의 테이블과 조인

- LEFT/RIGHT OUTTER JOIN

  - 기준 테이블에는 있지만 조인 테이블에 없으면 NULL로 표기
  - CITY에 있지만 COUNTRY 없는 데이터도 출력

  ```SQL
  SELECT *
  FROM CITY
  LEFT JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE;
  ```

- CROSS JOIN - 교차 조인

  - A테이블과 B테이블의 모든 조합을 출력, A\*B

  - e.g. 직원들의 성과 이름의 모든 조합. SELF CROSS JOIN.

  ```SQL
  SELECT E1.LASTNAME, E2.FIRSTNAME
  FROM EMPLOYEES E1
  CROSS JOIN EMPLOYESS E2
  ORDER BY E1.EMPLYEEID;
  ```

#### 4.5.10. UNION

- 두 테이블의 합집합 연산함. 칼럼이 일치해야 함.

- UNION - 합집합, 중복제거
- UNION ALL - 중복 포함.

  ```SQL
  SELECT NAME, CITY
  FROM CUSTOMERS
  UNION
  SELECT NAME, CITY
  FROM SUPPLIERS
  ```

### 4.6. MySQL 내장 함수

- 문자열

  - LENGTH() - 문자열 길이
  - CONCAT() - 문자열 합치기, 인자 중 하나라도 NULL이면 NULL 반환
  - LOCATE('ABC', 'ABCDE') - 문자열의 위치 반환, 1부터 시작
  - LEFT(5), RIGHT(5) - 각 방향에서 정해진 문자 수(5) 만큼 반환
  - LOWER(), UPPER() - 소문자로, 대문자로 변경
  - REPLECE('MSSQL', 'MS', My') - 문자열 변경, MSSQL을 MySQL로 변경.
  - TRIM() - 문자열 앞 뒤의 특정 문자(기본값 공백) 제거.
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
- 사용자를 등록하고, 사용자에게 특정 데이터 베이스를 사용할 권리를 부여.

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

## 출처

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
- [MSSQL] 조인 방법 쉽게 정리 (INNER JOIN, OUTER JOIN) - <https://gent.tistory.com/376>
- MySQL 데이터베이스 한 번에 끝내기 SQL Full Tutorial Course using MySQL Database - <https://www.youtube.com/watch? v=vgIc4 ctNFbc>
- 왕초보용! 갖고 노는 MySQL 데이터베이스 강좌 - <https://www.youtube.com/watch?v=dgpBXNa9vJc>
- DCL (Data Cntrol Language) - <https://velog.io/@ansalstmd/SQL 활용 기본 SQL 작성-DCL>
