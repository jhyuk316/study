# 5. NoSQL

- [1. Introduction](#1-introduction)
- [2. The NoSQL-Movement](#2-the-nosql-movement)
  - [2.1. Motives and Main Drivers](#21-motives-and-main-drivers)
    - [2.1.1. Motives of NoSQL practioners](#211-motives-of-nosql-practioners)
    - [2.1.2. Theoretical work](#212-theoretical-work)
  - [2.2. 비판](#22-비판)
  - [2.3. Persistence Design](#23-persistence-design)
- [3. Basic Concept, Techniques and Patterns](#3-basic-concept-techniques-and-patterns)
  - [3.1. Consistency](#31-consistency)
    - [3.1.1. The CAP-Theorem](#311-the-cap-theorem)
    - [3.1.2. ACID vs. BASE](#312-acid-vs-base)
- [4. Key-/Value-Stores](#4-key-value-stores)
- [5. Document Databases](#5-document-databases)
- [6. Column-Oriented Databases](#6-column-oriented-databases)
- [7. 특징](#7-특징)
  - [7.1. Non-Relational](#71-non-relational)
  - [7.2. Distributed](#72-distributed)
- [8. NoSQL 데이터베이스 유형](#8-nosql-데이터베이스-유형)
  - [8.1. Key Value DB](#81-key-value-db)
  - [8.2. Wide Columnar Store](#82-wide-columnar-store)
  - [8.3. Document DB](#83-document-db)
  - [8.4. Graph DB](#84-graph-db)
- [9. 성능](#9-성능)
- [10. 대표 제품 비교](#10-대표-제품-비교)
- [11. SQL과 NoSQL 용어 비교](#11-sql과-nosql-용어-비교)
- [12. 출처](#12-출처)

## 1. Introduction

- NoSQL - 비관계형 데이터 베이스
- 계형 데이터베이스 시스템의 주요 특성을 보장하는 ACID(Atomic, Consistency, Integrity, Duarabity) 특성을 제공하지 않는, 그렇지만 뛰어난 확장성이나 성능 등의 특성을 갖는 수많은 비관계형, 분산 데이터 베이스

<!--
2 The NoSQL-Movement 2
2.1 Motives and Main Drivers
2.2 Criticism
2.3 Classifications and Comparisons of NoSQL Databases
3 Basic Concepts, Techniques and Patterns
3.1 Consistency
3.2 Partitioning
3.3 Storage Layout
3.4 Query Models
3.5 Distributed Data Processing via MapReduce
4 Key-/Value-Stores
4.1 Amazon’s Dynamo
4.2 Project Voldemort
4.3 Other Key-/Value-Stores -->

## 2. The NoSQL-Movement

### 2.1. Motives and Main Drivers

#### 2.1.1. Motives of NoSQL practioners

- NoSQL 데이터 저장소를 개발하고 사용하는 일반적인 이유

- Avoidance of Unneeded Complexity - 불필요한 일관성 검사 배제
- High Throughput - 높은 처리량

  - Google은 MapReduce 방식으로 엄청난 처리를 함.

- Horizontal Scalability and Running on Commodity Hardware - 수평 확장

  - 관계형 DB의 확장의 어려움을 해소.

- Avoidance of Expensive Object-Relational Mapping - 값비싼 객체 관계형 매핑 방지

  - 객체 지향 프로그래밍 언어의 데이터 구조와 유사하거 단순 데이터 구조를 저장.

- Complexity and Cost of Setting up Database Clusters - 데이터베이스 클러스터 설치의 비용과 복잡성

  - 샤딩의 복잡성과 비용없이 쉽게 확장 가능.

- Compromising Reliability for Better Performance - 더 나은 성능을 위한 안정성 타협

  - HTTP 세션 같은 임시 데이터를 영구적인 DB에 저장 할 필요가 없음.

- The Current “One size fit’s it all” Databases Thinking Was and Is Wrong - 현재의 '만능' 데이터베이스는 잘못된 것.

  - 기존의 방식으로 해결 할 수 없는 시나리오가 증가.
    - 데이터 볼륨의 지속적 증가.
    - 더 짧은 시간에 더 많은 양의 데이터를 처리할 필요성 증가.
  - Facebook 상태 업데이트, 트윗 등은 ACID가 필요하지 않음.
    - 데이터 손실, 불일치의 가능성을 받아들이고 거대한 규모로 운영.

- The Myth of Effortless Distribution and Partitioning of Centralized Data Models - 중앙 집중식 데이터 모델의 분산과 배포에 대한 신화

- Movements in Programming Languages and Development Frameworks - 프로그래밍 언어와 개발 프레임웤의 이동
  - NoSQL은 프로그래밍 언어에 가까운 자료구조, API를 제공.
- Requirements of Cloud Computing - 클라우드 컴퓨팅의 요구
- The RDBMS plus Caching-Layer Pattern/Workaround vs. Systems Built from Scratch with Scalability in Mind - RDBMS와 캐싱레이어 vs 확장을 염두해둔 시스템

#### 2.1.2. Theoretical work

- 관계형 데이터 베이스의 한계

  - 25년 전의 하드웨어 맞는 설계.
    - 디스크 기반의 저장, 인덱싱 구조.
    - 지연을 숨기기위한 멀티쓰레딩
    - Lock 기반의 동시성 제어
    - 로그 기반의 복구
  - 1970년대와는 달라진 비지니스 데이터 처리
    - 대부분 쿼리를 입력하는게 아니라 클라이언트 응용프로그램을 사용.

- Design Considerations
  1. Main Memory - 엄청나게 저렴해지고 커진 메모리
  2. Multi-Threading and Resource Control
  3. Grid Computing and Fork-Lift Upgrades
  4. High Availability
  5. No Knobs - 사람보다 컴퓨터가 싼 시대이므로 복잡한 튜닝 노브를 대신 데이터베이스가 스스로 최적화해야 함.

### 2.2. 비판

- 기존 비지니스에 도입하기엔 리스크가 있음.
  - 라이선스 및 상업적 지원
  - 신기술의 과장된 성능과 유지보수의 어려움.
- 관리자 운영자의 어려움.
  - Ad-Hoc Data Querying - 임시적 쿼링이 어려움.
  - Data Export - 데이터 추출해 분석하기 어려움.
- Performance vs. Scalability
  - NoSQL이라고 수평적 확장이 쉬운 것만은 아님.
  - RDBMS도 샤딩을 통해 쉽게 수평적 확장이 가능.
  - Reporting이 필요하면 RDB가 필요.

### 2.3. Persistence Design

| Datastore     | Persistence Design                  |
| ------------- | ----------------------------------- |
| Cassandra     | Memtable / SSTable                  |
| CouchDB       | Append-only B-tree                  |
| HBase         | Memtable / SSTable on HDFS          |
| MongoDB       | B-tree                              |
| Neo4j         | On-disk linked lists                |
| Redis         | In-memory with background snapshots |
| Scalaris      | In-memory only                      |
| Tokyo Cabinet | Hash or B-tree                      |
| Voldemort     | Pluggable (primarily BDB MySQL)     |

- In-Memory Databases
  - very fast
  - data size is inherently limited by the size of RAM
- Memtables and SSTables

  - write operations are buffered in memory
  - after they have been written to an append-only commit log to ensure durability
  - avoids the durability difficulties of pure in-memorydatabases

- B-trees
  - used in databases since their beginning to provide a robust indexing-support

## 3. Basic Concept, Techniques and Patterns

### 3.1. Consistency

#### 3.1.1. The CAP-Theorem

#### 3.1.2. ACID vs. BASE

- BASE

  - **B**asically **A**vailable
  - **S**oft-state
  - **E**ventual consistency - In a steady state, the system
    will eventually return the last written value

- ACID

  - Strong consistency
  - Isolation
  - Focus on “commit”
  - Nested transactions
  - Availability?
  - Conservative (pessimistic)
  - Difficult evolution (e. g. schema)

- BASE
  - Weak consistency – stale data OK
  - Availability first
  - Best effort
  - Approximate answers OK
  - Aggressive (optimistic)
  - Simpler!
  - Faster
  - Easier evolution

## 4. Key-/Value-Stores

## 5. Document Databases

## 6. Column-Oriented Databases

---

## 7. 특징

- 클러스터에서 실행하기위해 관계형 모델을 사용하지 않음.
- 21세기 이후에 만들어진 시스템

- 스키마 없이 동작
- 관계형 모델을 사용하지 않으며 테이블간의 조인 기능 없음
- 직접 프로그래밍을 하는 등의 비SQL 인터페이스를 통한 데이터 액세스
- 대부분 여러 대의 데이터베이스 서버를 묶어서(클러스터링) 하나의 데이터베이스를 구성

### 7.1. Non-Relational

- 한 필드에 하나의 값만 가질 수 있는 RDB의 한계 극복
- 정합성 및 데이터 일관성 유지를 기반으로 한 시스템에는 사용 불가
- 집합-지향(Aggregate-Oriented) 모델 사용
  - 집합 자료 구조
  - 하나의 엔티티에 대한 트랜잭션을 지원하지 않음, 하나으 집합에 대한 연산에만 트랜잭션 지원.
  - 수평적 확장이 용이
    - 연관된 데이터들이 함께 움직임.
    - 키를 이용한 데이터(집합) 검색
    - 조인 연산 불가능. - MongoDB나 Cassandra는 MapReduce지원.
- 데이터의 스키마와 속성들을 다양하게 수용 및 동적 정의 (Schema-less)
  - 데이터 구조를 미리 정의할 필요가 없음.
  - 데이터 구조에 대한 정의의 변경 없이 레코드에 추가 가능.
  - 데이터 베이스가 스키마를 직접 관리하지 않는 것이며, 암묵적인 스키마는 존재.
  - 스키마가 확정되지 않으므로 데이터 값 문제시 탐지가 어려움.
- 다수가 Open Source로 제공
  - 기술 지원을 받기 어려움.

### 7.2. Distributed

- 여러 대의 데이터베이스 서버를 클러스터링해서 하나의 데이터베이스 구성
- 분산 방식
  - 메타데이터
    - 데이터 배치 정보를 마스터 서버에 저장
    - 클라이언트는 마스터 서버를 경유하여 실제 데이터를 처리할 서버에 접속
    - 마스터에서 관리하기 때문에 관리가 편하며 맵리듀스 활용 용이
    - 마스터 서버가 문제가 생기면 전체 데이터에 접근 불가
  - P2P
    - 메타 정보 없이 해시 함수를 이용해 특정 키를 서비스하는 서버에 접속
    - 서버 장애시 범위가 적음.
    - 저장된 데이터 분석이 메타데이터 방식 보다 어려움.
- 파일 저장 방식
  - 데이터 별도 관리
    - 데이터 파일 저장 - 분산 파일 시스템
    - 논리적 관리 - 데이터 관리 시스템
    - 데이터 복제, 장애시 복제본 재생성 - 분산 파일 시스템에서 제공(빅테이블, HBase)
  - 데이터 관리 시스템 내에 데이터 파일 저장
    - 데이터 복제, 장애시 복구 등에 대한 기능을 담당
    - 대부분의 NoSQL 솔루션

## 8. NoSQL 데이터베이스 유형

### 8.1. Key Value DB

- Key와 Value의 쌍으로 데이터가 저장되는 가장 단순한 형태의 솔루션
- Dictionary, HashMap 자료구조
- 특징
  - 단순성 - 고유 키를 통해 값을 획득, 값은 제한이 없음.
  - 속도 - 빠름
  - 확장성
- 단점
  - 값을 통한 쿼리 불가능.
  - 범위 쿼리 불가능.
  - 간단한 쿼리만 가능.
- Riak, Vodemort, Tokyo

### 8.2. Wide Columnar Store

- Big Table DB라고도 하며, Google의 BigTable Paper에서 유래
- Key Value 에서 발전된 형태의 Column Family 데이터 모델을 사용
- 테이블, 칼럼, 로를 사용하나 로 마다 칼럼이 다를 수 있음.
- 구조
  - Row Key - Row 식별자, 자동 정렬, 기본키
  - Column
- HBase, Cassandra, ScyllaDB

### 8.3. Document DB

- Lotus Notes에서 유래
- JSON, XML과 같은 Collection 데이터 모델 구조를 채택
- MongoDB, CoughDB

### 8.4. Graph DB

- Euler & Graph Theory에서 유래한 DB
- Nodes, Relationship, Key-Value 데이터 모델을 채용
- Neo4J, OreientDB

## 9. 성능

| Data model              | Performance |   Scalability   | Flexibility | Complexity |   Functionality    |
| ----------------------- | :---------: | :-------------: | :---------: | :--------: | :----------------: |
| Key–value store         |    high     |      high       |    high     |    none    |  variable (none)   |
| Column-oriented store   |    high     |      high       |  moderate   |    low     |      minimal       |
| Document-oriented store |    high     | variable (high) |    high     |    low     |   variable (low)   |
| Graph database          |  variable   |    variable     |    high     |    high    |    graph theory    |
| Relational database     |  variable   |    variable     |     low     |  moderate  | relational algebra |

## 10. 대표 제품 비교

![NoSQL_대표제품_특징](images/05%20NoSQL_NoSQL_대표제품_특징.png)

![NoSQL_대표제품_특성](images/05%20NoSQL_NoSQL_대표제품_특성.png)

## 11. SQL과 NoSQL 용어 비교

| SQL                     | MongoDB   | DynamoDB           | Cassandra     | Couchbase   |
| ----------------------- | --------- | ------------------ | ------------- | ----------- |
| 테이블                  | 컬렉션    | 테이블             | 테이블        | 데이터 버킷 |
| 열                      | 문서      | 항목               | 열            | 문서        |
| 컬럼                    | 필드      | 속성               | 컬럼          | 필드        |
| 기본 키                 | ObjectId  | 기본 키            | 기본 키       | 문서 ID     |
| 인덱스                  | 인덱스    | 보조 인덱스        | 인덱스        | 인덱스      |
| 보기                    | 보기      | 글로벌 보조 인덱스 | 구체화된 보기 | 보기        |
| 중첩된 테이블 또는 객체 | 포함 문서 | 맵                 | 맵            | 맵          |
| 배열                    | 배열      | 목록               | 목록          | 목록        |

## 12. 출처

- NoSQL - <https://ko.wikipedia.org/wiki/NoSQL>
- 클라우드 컴퓨팅과 AI 서비스 - <http://www.kocw.net/home/cview.do?cid=2e3eddd8fa0ab9d3>
- NoSQL이란 무엇인가? 대량데이터 동시처리위한 DBMS 종류와 특징 - <https://www.samsungsds.com/kr/insights/1232564_4627.html>
- NoSQL이란? - <https://aws.amazon.com/ko/nosql/>
- NoSQL - <https://namu.wiki/w/NoSQL>
