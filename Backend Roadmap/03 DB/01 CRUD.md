# 1. CRUD

- [1. Create](#1-create)
  - [1.1 Create](#11-create)
  - [1.2 INSERT](#12-insert)
- [2. Read](#2-read)
- [3. Update](#3-update)
- [4. Delete](#4-delete)
- [출처](#출처)

| 이름   | 조작       | SQL    |
| ------ | ---------- | ------ |
| Create | 생성       | INSERT |
| Read   | 읽기, 검색 | SELECT |
| Update | 갱신, 편집 | UPDATE |
| Delete | 삭제       | DELETE |

## 1. Create

### 1.1 Create

- CREATE - Table 생성 명령어

```sql
CREATE TABLE USER (
    ID VARCHAR2(100),
    PASSWORD VARCHAR2(30),
    NAME VARCHAR2(30),
    ADDRESS VARCHAR2(30),
    PHONE VARCHAR2(30)
    )
;
```

### 1.2 INSERT

- INSERT - 테이블에 데이터를 삽입하는 명령어
- `INSERT INTO 테이블명 (칼럼명1, 칼럼명2, 칼럼명3) VALUES (값1, 값2, 값3);`
- 모든 컬럼에 데이터를 저장하는 경우 컬럼명 생략가능.

```sql
INSERT INTO USER (ID, PASSWORD, NAME, ADDRESS, PHONE)
            VALUES ('user1', '1234', '김철수', '서울', '010-1234-1234')
;

INSERT INTO USER VALUES ('user1', '1234', '김철수', '서울', '010-1234-1234')
;
```

## 2. Read

- SELECT - 테이블에 저장된 데이터를 조회하는 명령어
- `SELECT 컬럼명 FROM 테이블명 WHERE 조건 ORDER BY 컬럼명 ASC or DESC LIMIT 개수;`
- \* - 모든 칼럼의 데이터를 조회.

```sql
SELECT *
    FROM USER
;

SELECT ID, NAME, ADDRESS
    FROM USER
;
```

## 3. Update

- UPDATE - 테이블에 저장되어있는 데이터를 수정하는 명령어
- `UPDATE 테이블명 SET 칼럼명1 = 변경할 값1, 칼럼명2 = 변경할 값2 WHERE 조건`
- 조건(WHERE) 절이 없으면 모든 행에 적용 됨.

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

## 4. Delete

- DELETE - 테이블에 저장되어 있는 데이터를 삭제하는 명령어.
- `DELETE FROM 테이블명 WHERE 조건`
- 조건절이 없으면 모든 데이터 삭제.

```sql
DELETE FROM USER WHERE ID = 'user2'
;
```

---

## 출처

- CRUD - <https://ko.wikipedia.org/wiki/CRUD>
- CRUD - <http://wiki.hash.kr/index.php/CRUD>
- 오라클 CRUD란? - <https://nancording.tistory.com/9>
- 기본 SQL Query문 정리 ( SELECT, INSERT, UPDATE, DELETE ) - <https://lcs1245.tistory.com/entry/%EA%B8%B0%EB%B3%B8-SQL-Query%EB%AC%B8-%EC%A0%95%EB%A6%AC-SELECT-INSERT-UPDATE-DELETE>
