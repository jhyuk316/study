# JPA

## 사용해야하는 이유

```java
class Team{
    long id;
    String name;
}

class Member{
    long id;
    Team team;
    String name;
}
```

- 생산성
  - 저장 - jpa.persist(member)
  - 조회 - Member member = jpa.find(memberId)
  - 수정 - member.setName("name")
  - 삭제 - jpa.remove(member)
- 유지보수
  - class변경시 자동으로 쿼리를 변경해줌.
- 패러다임의 불일치 해결

  - 상속
    - 저장 - 객체 분해 후 각각의 테이블에 저장.
    - 조회 - 각각의 테이블의 정보를 취합해서 객체 반환.
  - 연관관계 저장

    ```java
    member.setTeam(team);
    jpa.persist(member);
    ```

  - 객체 그래프 탐색

    ```java
    Member member = jpa.find(Member.class, memberId);
    Team team = member.getTeam();
    ```

  - 신뢰 할 수 있는 엔티티, 계층
  - 비교하기 - 동일한 트랜잭션에서 조회한 엔티티는 같음을 보장.
  - 성능 최적화
    > 레이어가 추가되면 오버헤드가 발생하지만, 캐쉬와 버퍼를 넣을 수 있어서 오히려 더 빠른 작업을 할 수도 있음.
    - 1차 캐시와 동일성(identity)보장
      - 같은 트랙잭션 안에서는 같은 엔티티 반환 - 약간의 조회 성능 향상
      - DB Isolation Level이 Read Commit이어도 애플리케이션에서 Repeatable Read 보장.
    - 트랜잭션을 지원하는 쓰기 지연
      - 트랜잭션을 커밋 할 때까지 INSERT SQL을 모음.
      - JDBC BATCH SQL 기능을 사용해서 한번에 SQL 전송.
      - 트랜잭션이 원자값이기 때문에 모아서해도 문제 없음.

- 지연 로딩과 즉시 로딩
  - 지연로딩 - 객체가 실제 사용 될 때 로딩.
    - member만 조회하고 team을 쓸때 team을 조회
  - 즉시로딩 - JOIN SQL로 한버에 연관된 객체까지 미리 조회.
    - member Join team을 한번에 가져옴.
  - team을 자주 쓰면 즉시로딩이 가끔 쓰면 지연로딩이 효율적임.

### ORM

- 객체지향 코딩과 RDB의 패러다임 불일치를 해결해 줌.
