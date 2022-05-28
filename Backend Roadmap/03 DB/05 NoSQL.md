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
    - [3.1.3. Versioning of Datasets in Distributed Scenarios](#313-versioning-of-datasets-in-distributed-scenarios)
    - [3.1.4. Vector Clocks Utilized to Propagate State via Gossip](#314-vector-clocks-utilized-to-propagate-state-via-gossip)
  - [3.2. Partitioning](#32-partitioning)
    - [Consistent Hashing](#consistent-hashing)
    - [Read and Write Operations on Partitioned Data](#read-and-write-operations-on-partitioned-data)
    - [Membership Changes](#membership-changes)
  - [3.3. Storage Layout](#33-storage-layout)
  - [3.4. Query Models](#34-query-models)
  - [3.5. Distributed Data Processing via MapReduce](#35-distributed-data-processing-via-mapreduce)
- [4. 특징](#4-특징)
  - [4.1. Non-Relational](#41-non-relational)
  - [4.2. Distributed](#42-distributed)
- [5. NoSQL 데이터베이스 유형](#5-nosql-데이터베이스-유형)
  - [5.1. Key Value DB](#51-key-value-db)
  - [5.2. Wide Columnar Store](#52-wide-columnar-store)
  - [5.3. Document DB](#53-document-db)
  - [5.4. Graph DB](#54-graph-db)
- [6. 성능](#6-성능)
- [7. 대표 제품 비교](#7-대표-제품-비교)
- [8. SQL과 NoSQL 용어 비교](#8-sql과-nosql-용어-비교)
- [9. 출처](#9-출처)

## 1. Introduction

- NoSQL - 비관계형 데이터 베이스
- 계형 데이터베이스 시스템의 주요 특성을 보장하는 ACID(Atomic, Consistency, Integrity, Duarabity) 특성을 제공하지 않는, 그렇지만 뛰어난 확장성이나 성능 등의 특성을 갖는 수많은 비관계형, 분산 데이터 베이스

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

  - 객체 지향 프로그래밍 언어의 데이터 구조와 유사하게 단순 데이터 구조를 저장.

- Complexity and Cost of Setting up Database Clusters - 데이터베이스 클러스터 설치의 비용과 복잡성

  - 샤딩의 복잡성과 비용 없이 쉽게 확장 가능.

- Compromising Reliability for Better Performance - 더 나은 성능을 위한 안정성 타협

  - HTTP 세션 같은 임시 데이터를 영구적인 DB에 저장할 필요가 없음.

- The Current “One size fit’s it all” Databases Thinking Was and Is Wrong - 현재의 '만능' 데이터베이스는 잘못된 것.

  - 기존의 방식으로 해결할 수 없는 시나리오가 증가.
    - 데이터 볼륨의 지속적 증가.
    - 더 짧은 시간에 더 많은 양의 데이터를 처리할 필요성 증가.
  - Facebook 상태 업데이트, 트윗 등은 ACID가 필요하지 않음.
    - 데이터 손실, 불일치의 가능성을 받아들이고 거대한 규모로 운영.

- The Myth of Effortless Distribution and Partitioning of Centralized Data Models - 중앙 집중식 데이터 모델의 분산과 배포에 대한 신화

- Movements in Programming Languages and Development Frameworks - 프로그래밍 언어와 개발 프레임웍의 이동
  - NoSQL은 프로그래밍 언어에 가까운 자료구조, API를 제공.
- Requirements of Cloud Computing - 클라우드 컴퓨팅의 요구
- The RDBMS plus Caching-Layer Pattern/Workaround vs. Systems Built from Scratch with Scalability in Mind - RDBMS와 캐싱 레이어 vs 확장을 염두에 둔 시스템

#### 2.1.2. Theoretical work

- 관계형 데이터 베이스의 한계

  - 25년 전의 하드웨어 맞는 설계.
    - 디스크 기반의 저장, 인덱싱 구조.
    - 지연을 숨기기 위한 멀 티쓰 레딩
    - Lock 기반의 동시성 제어
    - 로그 기반의 복구
  - 1970년대와는 달라진 비즈니스 데이터 처리
    - 대부분 쿼리를 입력하는 게 아니라 클라이언트 응용프로그램을 사용.

- Design Considerations
  1. Main Memory - 엄청나게 저렴해지고 커진 메모리
  2. Multi-Threading and Resource Control
  3. Grid Computing and Fork-Lift Upgrades
  4. High Availability
  5. No Knobs - 사람보다 컴퓨터가 싼 시대이므로 복잡한 튜닝 노브를 대신 데이터베이스가 스스로 최적화해야 함.

### 2.2. 비판

- 기존 비즈니스에 도입하기엔 리스크가 있음.
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

생략

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

- Consistency
  - Strict Consistency - 복제본에 관계없이 가장 최근에 완료된 쓰기 작업의 데이터를 반환.
  - Eventual Consistency - 결국엔 안정된 상태가 되어 최종으로 쓴 데이터를 반환할 수 있어야 함.
  - Read Your Own Writes (RYOW) Consistency - 쓰기 직후에 업데이트되었음을 확인할 수 있음. 다른 서버에는 아직 써지지 않았더라도.
  - Session Consistency - 같은 세션 안에서는 쓰기 직후에 읽을 수 있음.
  - Casual Consistency - x버전을 읽고 y버전을 쓰면, 다른 클라이언트가 y 버전을 읽으면 x버전도 볼 수 있음.
  - Monotonic Read Consistency - x데이터를 다시 읽으면 같거나 더 최신의 x데이터를 읽을 수 있음.

#### 3.1.3. Versioning of Datasets in Distributed Scenarios

- Timestamps - 시간순으로 저장
- Optimistic Locking - 버전 칼럼을 넣어 버전이 다르면 갱신하지 않음.
  - 읽은 버전과 쓰는 버전이 다르다는 말은 다른 클라이언트가 업데이트했음을 의미.
- Vector Clocks - 순서와 업데이트 간의 추론을 허용.
- Multiversion Storage - 한 행에 대해 여러 버전을 관리.

##### 3.1.3.1. Vector Clocks

![Vector Clocks](images/05%20NoSQL_Vector%20Clocks.png)

![Vector Clocks example](images/05%20NoSQL_Vector_Clocks_example.svg)

- 타임스탬프의 단점인 업데이트의 연관 관계를 알기 위한 방법.
- V[0], V[1], ..., V[n] - tuple, 각 노드의 클럭 값, 타임 스탬프
- Vi[0] - 첫 번째 노드의 클럭 값
- 규칙
  - node i의 연산이 발생하면 Vi[i] 클럭을 갱신
    - Vi[i] = Vi[i] +1
  - node i는 node k에게 메시지 전달, 클럭 값
  - node i가 node j에게 메시지를 받으면
    - Vi = max(Vi,Vmessage)
  - Vi > Vj, 모든 k에 대해 Vi[k] > Vj[k]
- 장점
  - 동기화된 시계에 의존하지 않음. (메시지로 보정.)
  - 추론을 위해 수정 번호의 전체 순서가 필요하지 않음.
  - 모든 노드의 데이터 조각을 여러 버전을 저장하고 유지할 필요가 없음.

#### 3.1.4. Vector Clocks Utilized to Propagate State via Gossip

##### State Transfer Model

- 데이터의 delata가 서버 간에 교환됨.
- 노드는 버전 트리를 유지.

- Query Processing
  ![State_Transfer_Mode_Query_Processing](images/05%20NoSQL_State_Transfer_Mode_Query_Processing.png)

  - 클라이언트는 쿼리 할 때 백터 클럭을 같이 보냄
  - 데이터 서버는 벡터 클럭으로 트리 일부를 응답
  - 클라이언트는 첨부된 서버로 요청 보내고 받은 응답을 병합
    - 클라이언트는 잠재적 버전 충돌을 해소

- Update Processing
  ![State_Transfer_Mode_Update_Processing](images/05%20NoSQL_State_Transfer_Mode_Update_Processing.png)

  - 클라이언트가 업데이트 요청, 벡터 클록 첨부
  - 복제 서버는 첨부된 벡터 클록이 서버 상태보다 큰지 확인하고 크면 업데이트 않으면 무시.

- Internode Gossiping
  ![State_Transfer_Mode_Internode_Gossiping](images/05%20NoSQL_State_Transfer_Mode_Internode_Gossiping.png)

  - 백그라운드에서 벡터 클록과 버전 트리를 교환하고 동기화를 유지하기 위해 병합을 시도

##### Operation Transfer Model

- 지역 데이터에 적용 가능한 명령(작업)을 통신
- 데이터 델타보다 더 적은 대역폭 사용.
- 올바른 순서로 작업을 적용하는 것이 중요.
  - 복제 노드에 데이터를 적요하기 전에 작업 간의 casual
    relationship를 결정
  - 이전의 모든 작업이 실행될 때까지 작업 적용을 연기.
- 다른 복제본의 교환, 통합되는 작업 대기열을 유지.

- 기호

  - Vstate - 데이터의 마지막 업데이트 상태에 해당하는 벡터 클록
  - Vi - 자신의 백터 클럭, 수신한 백터 클럭과 통합된.
  - Vj - 복제본 j로부터 받은 마지막 가십 메시지의 벡터 클럭

- Query Processing
  ![Operation_Transfer_Model_Query_Processing](images/05%20NoSQL_Operation_Transfer_Model_Query_Processing.png)

  - 클라이언트는 벡터 클럭과 함께 요청
  - 복제 서버는 클라이언트 벡터 클럭보다 큰지 확인하여 응답

- Update Processing
  ![Operation_Transfer_Model_Update_Processing](images/05%20NoSQL_Operation_Transfer_Model_Update_Processing.png)

  - 클라이언트가 업데이트 용청을 제출하면 연결된 복제 노드는 업데이트 작업을 적용할 수 있을 때까지 버퍼링.
  - 두 개의 백터 클럭을 태깅
    - Vclient - 클라이언트가 요청한 벡터 클럭.
    - Vreceived - 복제 노드가 업데이트를 수신 한 벡터 클럭.

- Internode Gossiping
  ![Operation_Transfer_Model_Internode_Gossiping](images/05%20NoSQL_Operation_Transfer_Model_Internode_Gossiping.png)
  - 복제 노드는 보류 중인 작업 대기열을 교환하고 서로의 벡터 클록을 업데이트
  - 노드가 작업 대기열을 교환할 때마다 이러한 대기열의 특정 작업을 적용할 수 있는지 여부를 결정.
  - 한 번에 둘 이상의 작업을 실행할 수 있는 경우 올바른 순서로 적용.
    - 교환 법칙이 적용되는 동시 업데이트는 순서가 중요하지 않음.
    - 교환 법칙이 적용되지 않는 동시 업데이트는 벡터 클럭 추론으로 충분하지 않으므로 중앙 카운터로 순서 결정.

### 3.2. Partitioning

- Memory Caches
  - 데이터 베이스에서 가장 자주 요청되는 부분을 메모리에 복제하고 신속하게 전달.
  - 일시적인 인메모리 데이터베이스
  - 키/값 저장
  - 메모리 캐시가 응답하지 않으면 무시하고 다른 메모리 캐시로 암시적으로 리해싱.
- Clustering
- Separationg Reads form Writes
  - 마스터 노드에 쓰기
    - 쓰기 지연이 없지만 복제하기 전에 충돌하면 손실됨.
  - 슬레이브(복제 노드)에서 읽기
  - 읽기의 비중이 쓰기보다 높으면 잘 작동.
- Sharding
  - 요청과 갱신이 같은 노드에 함께 일어나는 데이터 분할.
  - 안정성과 로드 벨런싱을 위해 노드가 복제됨.
  - 샤드 간의 조인이 불가능.

#### Consistent Hashing

- 동일함 함수를 통해 객체와 캐시를 모두 해싱하는 것.

- inital
  ![Initial Situation](images/05%20NoSQL_Initial_Situation.png)

  - A, B, C, D - 캐시 노드
  - 1, 2, 3, 4 - 객체
  - 맵핑
    - 1, 4 - A
    - 2 - B
    - 3 - C

- After
  ![Situation after](images/05%20NoSQL_Situation_after.png)

  - 노드가 사라지면 객체는 인접 노드에 맵핑
  - 다시 들어오면 새 노드에 맵핑

- 노드 간의 불균형 문제

#### Read and Write Operations on Partitioned Data

- 요청된 데이터 조각에 따라 물리적 노드의 읽기 워크로드를 분산할 수 있음.
- R + W > N

  - N - 읽거나 쓸 데이터 조각의 복제본 수
  - R - 읽기 작업에 연결된 머신의 수
  - W - 쓰기 작업을 위해 블록 된 머신의 수

- 쓰기 작업에서는 일관성, 격리되지 않음을 명확히 해야 함.
  - 에러나 예외 없이 쓰기 작업이 완료되었으면 최소 W개 이상의 노드가 수행했음을 알 수 있음.
  - 쓰기 작업에 에러나 예외가 발생하면 다시 쓰기 작업을 수행해야 일관성을 유지할 수 있음.
  - 최소한 한 개의 노드에 쓰기가 성공했으면 복제 노드 간에 값을 교환하여 결국 모든 노드에 값이 쓰이게 됨.

#### Membership Changes

- new node joins the system

  1. 새 노드는 자신의 존재와 식별자를 인접 노드 또는 모든 노드에 알림.
  2. 결합한 노드의 이웃은 개체 및 복제본의 소유권 조정에 의해 반응.
  3. 결합한 노드는 이웃으로부터 반응할 수 있는 데이터 집합을 복제.
  4. 1에서 모든 노드에 알리지 않았으면 모든 노드에 알림.

- Node X joins
  ![Node X joins](images/05%20NoSQL_Node_X_joins.png)

- Node B leaves
  ![Node B leaves](images/05%20NoSQL_Node_B_leaves.png)

  - 노드 이탈은 알릴 수 없기 때문에 감지를 해야 함.
  - 가십 프로토콜을 통해 정기적으로 통신하여 응답하지 않음으로 감지.
  - 노드 이탈이 감지되면 이웃 노드는 데이터를 교환하고 개체 및 복제본의 소유권을 조정

### 3.3. Storage Layout

- Row-Based Storage Layout

  ![Row-Based Storage Layout](images/05%20NoSQL_Row-Based_Storage.png)

  - 다른 칼럼을 읽기 좋음
  - 한 행을 한 번에 읽거나 쓸 수 있음.
  - 한 칼럼이 필요해도 한 행을 읽어야 함.

- Columnar Storage Layout

  ![Columnar Storage Layout](images/05%20NoSQL_Columnar_Storage.png)

  - 칼럼을 연속적으로 저장
  - 한 칼럼을 빠르게 읽을 수 있음
  - 한 행을 읽을 때 한 칼럼씩 읽어야 함.

- Columnar Storage Layout with Locality Groups

  ![Columnar Storage Layout with Locality Groups](images/05%20NoSQL_Columnar_Storage_Layout_with_Locality_Groups.png)

  - 지역 그룹으로 칼럼을 묶음.
  - 행 기반과 칼럼 기반의 장점을 결합.

- Log Structured Merge Trees(LSM-trees)

  ![LSM-trees](images/05%20NoSQL_LSM-trees.png)

  - 랜덤 한 쓰기를 연속적인 쓰기로 변환하는 트리.
  - 메모리에 데이터 청크(memtable)를 유지하고 이러한 메모리 내 데이터 구조에 대한 커밋 로그를 유지하고 memtable을 SSTable에 가끔 플러쉬.
  - 시간이 지나면 SSTable을 압축.

### 3.4. Query Models

> DHT - Distributed Hash Table

- Companinon SQL-database
  ![Companinon SQL-database](images/05%20NoSQL_Companinon_SQL-database.png)

  - 검색 가능한 특성(메타데이터)을 SQL 또는 Text 데이터베이스에 저장.
  - 쿼리는 RDBMS를 검색

- Scatter/Gather Local Search
  ![Scatter_Gather Local Search](images/05%20NoSQL_Scatter_Gather_Local_Search.png)

  - 로컬 DB내에서 인덱싱 및 쿼리 처리 메커니즘 제공.
  - 쿼리 프로세스가 DHT의 모든 노드에 쿼리를 브로드캐스트.
  - DHT는 로컬 검색으로 집합을 단일 응답으로 쿼리 프로세서로 보냄.

- Distiributed B+Trees
  ![Distiributed B+Trees](images/05%20NoSQL_-%20Distiributed_B+Trees.png)

  - 검색 가능 속성을 해시하여 B+트리의 루트 노드를 찾음.
  - 루트 노드의 값에는 자식 노드의 ID가 있음.
  - 클라이언트는 다른 DHT 조회 호출하여 자식 노드를 찾음.
  - 검색 기준과 일치하는 리프 노드에 도달할 때까지 반복.
  - 분할/병합 시 B+Tree노드가 업데이트되는 경우 주의가 필요. 원자적으로 수행되어야 함.

- Prefix Hash Table(Distributed Trie)
  ![Prefix_Hash_Table](images/05%20NoSQL_Prefix_Hash_Table.png)

  - 키에 접두사가 포함된 데이터 구조.
  - 모든 노드의 모든 데이터는 키가 접두사로 붙음.

- OR-Junctions - 검색 결과들을 결합.

- AND-Junctions
  - 일치하는 기준이 교차해야 하므로 커다란 집합을 교차하는 효율적 방법이 필요.
  - 무식한 방법으로는 모든 적합한 오브젝트를 각 서버에 보냄.
  - Bloom 필터 -

### 3.5. Distributed Data Processing via MapReduce

![MapReduce](images/05%20NoSQL_MapReduce.png)

- Map - 코디네이터는 주어진 맵 기능을 실행하고 중간 출력을 생성하는 다수의 노드를 지정.
- Reduce - 중간 결과물은 최종 출력을 생성하는 다수의 기계에 의해 처리.

---

## 4. 특징

- 클러스터에서 실행하기 위해 관계형 모델을 사용하지 않음.
- 21세기 이후에 만들어진 시스템

- 스키마 없이 동작
- 관계형 모델을 사용하지 않으며 테이블 간의 조인 기능 없음
- 직접 프로그래밍을 하는 등의 비 SQL 인터페이스를 통한 데이터 액세스
- 대부분 여러 대의 데이터베이스 서버를 묶어서(클러스터링) 하나의 데이터베이스를 구성

### 4.1. Non-Relational

- 한 필드에 하나의 값만 가질 수 있는 RDB의 한계 극복
- 정합성 및 데이터 일관성 유지를 기반으로 한 시스템에는 사용 불가
- 집합-지향(Aggregate-Oriented) 모델 사용
  - 집합 자료 구조
  - 하나의 엔티티에 대한 트랜잭션을 지원하지 않음, 하나의 집합에 대한 연산에만 트랜잭션 지원.
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

### 4.2. Distributed

- 여러 대의 데이터베이스 서버를 클러스터링 해서 하나의 데이터베이스 구성
- 분산 방식
  - 메타데이터
    - 데이터 배치 정보를 마스터 서버에 저장
    - 클라이언트는 마스터 서버를 경유하여 실제 데이터를 처리할 서버에 접속
    - 마스터에서 관리하기 때문에 관리가 편하며 맵리듀스 활용 용이
    - 마스터 서버가 문제가 생기면 전체 데이터에 접근 불가
  - P2P
    - 메타 정보 없이 해시 함수를 이용해 특정 키를 서비스하는 서버에 접속
    - 서버 장애 시 범위가 적음.
    - 저장된 데이터 분석이 메타데이터 방식보다 어려움.
- 파일 저장 방식
  - 데이터 별도 관리
    - 데이터 파일 저장 - 분산 파일 시스템
    - 논리적 관리 - 데이터 관리 시스템
    - 데이터 복제, 장애 시 복제본 재생성 - 분산 파일 시스템에서 제공(빅 테이블, HBase)
  - 데이터 관리 시스템 내에 데이터 파일 저장
    - 데이터 복제, 장애 시 복구 등에 대한 기능을 담당
    - 대부분의 NoSQL 솔루션

## 5. NoSQL 데이터베이스 유형

### 5.1. Key Value DB

- Key와 Value의 쌍으로 데이터가 저장되는 가장 단순한 형태의 솔루션
- Dictionary, HashMap **자료구조**
- 특징
  - 단순성 - 고유 키를 통해 값을 획득, 값은 제한이 없음.
  - 속도 - 빠름
  - 확장성
- 단점
  - 값을 통한 쿼리 불가능.
  - 범위 쿼리 불가능.
  - 간단한 쿼리만 가능.
- Riak, Vodemort, Tokyo

### 5.2. Wide Columnar Store

- Big Table DB라고도 하며, Google의 BigTable Paper에서 유래
- Key Value에서 발전된 형태의 Column Family 데이터 모델을 사용
- 테이블, 칼럼, 로를 사용하나 로마다 칼럼이 다를 수 있음.
- 구조
  - Row Key - Row 식별자, 자동 정렬, 기본키
  - Column
- HBase, Cassandra, ScyllaDB

### 5.3. Document DB

- Lotus Notes에서 유래
- JSON, XML과 같은 Collection 데이터 모델 구조를 채택
- MongoDB, CoughDB

### 5.4. Graph DB

- Euler & Graph Theory에서 유래한 DB
- Nodes, Relationship, Key-Value 데이터 모델을 채용
- Neo4J, OreientDB

## 6. 성능

| Data model              | Performance |   Scalability   | Flexibility | Complexity |   Functionality    |
| ----------------------- | :---------: | :-------------: | :---------: | :--------: | :----------------: |
| Key–value store         |    high     |      high       |    high     |    none    |  variable (none)   |
| Column-oriented store   |    high     |      high       |  moderate   |    low     |      minimal       |
| Document-oriented store |    high     | variable (high) |    high     |    low     |   variable (low)   |
| Graph database          |  variable   |    variable     |    high     |    high    |    graph theory    |
| Relational database     |  variable   |    variable     |     low     |  moderate  | relational algebra |

## 7. 대표 제품 비교

![NoSQL_대표제품_특징](images/05%20NoSQL_NoSQL_대표제품_특징.png)

![NoSQL_대표제품_특성](images/05%20NoSQL_NoSQL_대표제품_특성.png)

## 8. SQL과 NoSQL 용어 비교

| SQL                     | MongoDB   | DynamoDB           | Cassandra     | Couchbase   |
| ----------------------- | --------- | ------------------ | ------------- | ----------- |
| 테이블                  | 컬렉션    | 테이블             | 테이블        | 데이터 버킷 |
| 열                      | 문서      | 항목               | 열            | 문서        |
| 칼럼                    | 필드      | 속성               | 칼럼          | 필드        |
| 기본 키                 | ObjectId  | 기본 키            | 기본 키       | 문서 ID     |
| 인덱스                  | 인덱스    | 보조 인덱스        | 인덱스        | 인덱스      |
| 보기                    | 보기      | 글로벌 보조 인덱스 | 구체화된 보기 | 보기        |
| 중첩된 테이블 또는 객체 | 포함 문서 | 맵                 | 맵            | 맵          |
| 배열                    | 배열      | 목록               | 목록          | 목록        |

## 9. 출처

- NoSQL - <https://ko.wikipedia.org/wiki/NoSQL>
- 클라우드 컴퓨팅과 AI 서비스 - <http://www.kocw.net/home/cview.do?cid=2e3eddd8fa0ab9d3>
- NoSQL이란 무엇인가? 대량데이터 동시처리위한 DBMS 종류와 특징 - <https://www.samsungsds.com/kr/insights/1232564_4627.html>
- NoSQL이란? - <https://aws.amazon.com/ko/nosql/>
- NoSQL - <https://namu.wiki/w/NoSQL>
- Consistency model - <https://en.wikipedia.org/wiki/Consistency_model#Monotonic_read_consistency>
- Vector clock - <https://en.wikipedia.org/wiki/Vector_clock>
- NOSQL Patterns - <http://horicky.blogspot.com/2009/11/nosql-patterns.html>
- Consistent Hashing - <https://www.secmem.org/blog/2021/01/24/consistent-hashing/>
- Consistent Hashing - <https://tom-e-white.com/2007/11/consistent-hashing.html>
- Query Processing for NOSQL DB - <http://horicky.blogspot.com/2009/11/query-processing-for-nosql-db.html>
