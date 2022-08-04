# AWS

## EC2

- Elastic Compute Cloud
- 성능, 용량 등을 유동적으로 사용 할 수 있는 서버.
- AWS의 대명사

- 무료 플랜

  - t2.micro
    - vCPU 1 Core
    - 메모리 1GB
    - 월 750시간, 초과시 비용 부과
      - 23시간 \* 31일 = 744시간
      - 1대의 t2.micro만 사용하면 24시간 사용 가능.

- 리전 - 서비스가 구동될 지역, 가까운 서버가 배정됨.

- E2 생성 과정

  - 이름 태그 설정
  - Amazon Machine Image - 아마존이 만들어둔 서버 이미지
    - Amazon Linux AMI 선택
      - 아마존이 개발해서 지원 받기 편함.
      - 레드햇 베이스
      - AWS 서비스와 상성이 좋음.
      - Amazon 독자 레포지토리로 yum이 빠름.
  - 인스턴스 유형 설정
  - 키 페어
    - 키 생성
    - .pem 파일 다운받기.
    - **절대 잃어 버리면 안됨.**
  - 보안 그룹 생성
  - 스토리지 추가

- 탄력적 IP - 고정 IP

  - 탄력적 IP 주소 할당
  - 탄력적 IP 발급

- Windows Terminal 설치

  - 윈도우 스토어에서 설치 가능 - 안되면 git에서 다운.

- OpenSSH

  - 인스턴스에 연결 - SSH 클라이언트의 주소를 참조하여 Config
  - ` ssh -i "AWS-EC2-jhyuk316.pem" ec2-user@ec2-15-164-255-39.ap-northeast-2.compute.amazonaws.com`

  - config

  ```txt
  # MapZip AWS
  Host MapZip-AWS
      HostName ec2-15-164-255-39.ap-northeast-2.compute.amazonaws.com
      User ec2-user
      IdentityFile ~/.ssh/AWS-EC2-jhyuk316.pem
  ```

- 키파일 권한 설정

  - 보안 - 고급
    - 상속 해제
    - 모두 제거
  - 유저(나만) 추가 후
    - 허용 - 읽기 및 실행, 읽기
    - 거부 - 쓰기

- java 설치

  - Amazon Corretto 17 is a no-cost, multiplatform, production-ready distribution of the Open Java Development Kit (OpenJDK).
  - 아마존 OpenJDK

  - `sudo yum install java-17-amazon-corretto-devel`
  - <https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/amazon-linux-install.html>

- 타임존 변경

  - 한국 시간대로 변경

  ```shell
  sudo rm /etc/localtime
  sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime
  ```

## RDS

### 보안 설정

- 보안 그룹을 만듬
  - 인바운드 규칙 추가
    - EC2 보안 그룹을 추가
    - 내 IP를 추가

### DB 접속

- Database Navigator - intelli J 플러그인(쓰지마!)

  - MariaDB 미지원 - 책에서 MySQL로 호환 된다는 거 구라임.
  - URL
    - `jdbc:mariadb://(RDS 엔드포인트 주소):3306`
  - mariadb-java-client-2.7.3.jar 라이브러리 추가
    - <https://downloads.mariadb.com/Connectors/java/connector-java-2.7.3/>
  - 참조 - <https://github.com/jojoldu/freelec-springboot2-webservice/issues/757>

- DBeaver
  - 그냥 바로 연결됨 젠장.

### DB 연결

- build.gradle 설정

- 생성시

  ```yml
  spring:
    datasource:
      driver-class-name: org.mariadb.jdbc.Driver
      url: jdbc:mariadb://(RDS 엔드포인트 주소):3306/(database명)
      username: (DB 루트)
      password: (비밀번호)

  jpa:
    generate-ddl: true
    hibernate:
      ddl-auto: create
  ```

- 운영시

  ```yml
  spring:
    datasource:
      driver-class-name: org.mariadb.jdbc.Driver
      url: jdbc:mariadb://(RDS 엔드포인트 주소):3306/(database명)
      username: (DB 루트)
      password: (비밀번호)

  jpa:
    hibernate:
      ddl-auto: none
  ```

## 문제

### 빌드 실패

- apiKey 같은 Git이 관리 하는 파일이 빠진 경우.
- 서버 환경에서 설정 파일이 안 맞는 경우.

### no main manifest attribute in 에러

- jar파일에서 처음 호출할 Main 메소드를 찾지 못했다는 에러

- spring boot 2.5.0버전 이상부터는 gradle로 빌드를 할때 jar파일이 2개 생성됨.

  - 앱이름.jar

    - bootJar Task로 생성된것
    - 의존성이 포함된 jar파일

  - 앱이름-plain.jar

    - build Task로 생성된것
    - 의존성이 빠진 jar파일

- 원인

  - 앱이름-plain.jar를 java -jar로 실행하면 no main manifest attrubute in에러가 발생

- 해결책

  - 앱이름-plain.jar를 생성하지 않기 위해서는 아래 명령어를 build.gradle에 추가

  ```groovy
  jar {
    enabled = false
  }
  ```

- no main manifest attribute in 에러 - <https://dongjuppp.tistory.com/87>

---

## 출처
