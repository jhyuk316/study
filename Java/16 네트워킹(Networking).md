# 16. 네트워킹(Networking)

## 1. 네트워킹(Networking)

- 네트워킹 - 두 대 이상의 컴퓨터를 케이블로 연결하여 구성하는 것.
- java.net

### 1.1 클라이언트/서버(client/server)

- 서버 - 서비스를 제공하는 컴퓨터(service provider)
- 클라이언트 - 서비스를 사용하는 컴퓨터(service user)

- 서비스 - 서버가 클라이언트로부터 요청받은 작업을 처리하여 그 결과를 제공하는 것
  - 파일 서버
  - 메일 서버
  - 애플리케이션 서버

네트워크 모델

|         서버 기반 모델         |           P2P 모델            |
| :----------------------------: | :---------------------------: |
|      안정적인 서비스 제공      |       자원 활용 극대화        |
| 공유 데이터의 관리와 보안 용이 | 자원의 관리 어려움, 보안 취약 |
|  서버 구축 및 관리 비용 비쌈   |  서버 구축 및 운영 비용 절감  |

### 1.2 IP주소(IP address)

- IP 주소 - 컴퓨터를 구별하는 데 사용되는 고윳값.

  - 4 Bytes로 구성.
  - 0.0.0.0 ~ 255.255.255.255
  - 네트워크 주소와 호스트 주소로 구성

- IP와 서브넷 마스크

  IP주소

  - 192.168.10.100
  - x.x.x.0 - 네트워크 주소
  - x.x.x.255 - 브로드캐스트 주소

  ![IP주소](<images/16%20네트워킹(Networking)_IP주소.png>)

  서브넷 마스크

  - 255.255.255.0

  ![서브넷 마스크](<images/16%20네트워킹(Networking)_서브넷_마스크.png>)

  네트워크 주소

  - 192.168.10.0
  - IP 주소 & 서브넷 마스크

  ![네트워크 주소](<images/16%20네트워킹(Networking)_네트워크_주소.png>)

### 1.3 InetAddress

| Modifier and Type    | Method                                 | Description                                                               |
| -------------------- | -------------------------------------- | ------------------------------------------------------------------------- |
| byte[]               | getAddress()                           | IP주소를 byte배열로 반환.                                                 |
| static InetAddress[] | getAllByName(String host)              | 도메인명(host)에 지정된 모든 호스트의 IP주소를 배열에 담아 반환.          |
| static InetAddress   | getByAddress(byte[] addr)              | byte배열로 IP주소를 얻음.                                                 |
| static InetAddress   | getByAddress(String host, byte[] addr) | Creates an InetAddress based on the provided host name and IP address.    |
| static InetAddress   | getByName(String host)                 | 도메인명(host)을 통해 IP주소를 얻음.                                      |
| String               | getCanonicalHostName()                 | FQDN(fully qualified domain name)을 반환.                                 |
| String               | getHostAddress()                       | 호스트의 IP주소 반환.                                                     |
| String               | getHostName()                          | 호스트의 이름 반환.                                                       |
| static InetAddress   | getLocalHost()                         | 지역 호스트의 IP주소 반환.                                                |
| static InetAddress   | getLoopbackAddress()                   | Returns the loopback address.                                             |
| int                  | hashCode()                             | Returns a hashcode for this IP address.                                   |
| boolean              | isAnyLocalAddress()                    | Utility routine to check if the InetAddress is a wildcard address.        |
| boolean              | isLinkLocalAddress()                   | Utility routine to check if the InetAddress is an link local address.     |
| boolean              | isLoopbackAddress()                    | IP가 loopback주소(127.0.0.1)인가?                                         |
| boolean              | isMCGlobal()                           | Utility routine to check if the multicast address has global scope.       |
| boolean              | isMCLinkLocal()                        | Utility routine to check if the multicast address has link scope.         |
| boolean              | isMCNodeLocal()                        | Utility routine to check if the multicast address has node scope.         |
| boolean              | isMCOrgLocal()                         | Utility routine to check if the multicast address has organization scope. |
| boolean              | isMCSiteLocal()                        | Utility routine to check if the multicast address has site scope.         |
| boolean              | isMulticastAddress()                   | IP주소가 멀티캐스트 주소인가?                                             |
| boolean              | isReachable(int timeout)               | Test whether that address is reachable.                                   |
| boolean              | isSiteLocalAddress()                   | Utility routine to check if the InetAddress is a site local address.      |
| String               | toString()                             | Converts this IP address to a String.                                     |

소스 참조 - Inet <https://github.com/castello/javajungsuk3/blob/master/source/ch16/NetworkEx1.java>

### 1.4 RUL(Uniform Resource Location)

- RUL - 인터넷에 존재하는 서버들이 제공하는 자원에 접근할 수 있는 주소
  - `프로토콜://호스트명:포트번호/경로명/파일명?쿼리스트링#참조`
  - eg. <http://www.codechobo.com:80/sample/hello.html?referer=codechobo#index1>
  - 프로토콜 - 자원에 접근하기 우해 서버와 통신하는 데 사용되는 통신 규약(http)
  - 호스트명 - 자원을 제공하는 서버의 이름(www.codechobo.com)
  - 포트번호 - 통신에 사용되는 서버의 포트번호(80)
  - 경로명 - 접근하려는 자원이 저장된 서버상의 위치(/sample/)
  - 파일명 - 접근하려는 자원의 이름(hello.html)
  - 쿼리스트링 - URL에서 '?'이후의 부분(referer=codechobo)
  - 참조 - URL에서 '#'이후의 부분(index1)

```java
URL url = new URL("http://www.codechobo.com/sample/hello.html");
URL url = new URL("www.codechobo.com", "sample/hello.html");
URL url = new URL("http", "www.codechobo.com", "80", "/sample/hello.html");
```

| Modifier and Type | Method                                                   | Description                                          |
| ----------------- | -------------------------------------------------------- | ---------------------------------------------------- |
|                   | URL(String spec)                                         | 지정된 문자열 정보의 URL 객체 생성.                  |
|                   | URL(String protocol, String host, int port, String file) | 지정된 protocol, host, port, file에서 URL 객체 생성. |
|                   | URL(String protocol, String host, String file)           | 지정된 protocol, host, file에서 URL 객체 생성.       |
| String            | getAuthority()                                           | 호스트명과 포트를 문자열로 반환.                     |
| final Object      | getContent()                                             | URL의 Content 객체를 가져옴.                         |
| final Object      | getContent(Class<?>[] classes)                           | URL의 Content 객체를 가져옴.                         |
| int               | getDefaultPort()                                         | URL의 기본 포트 반환.                                |
| String            | getFile()                                                | URL의 파일명 반환.                                   |
| String            | getHost()                                                | URL의 호스트명 반환.                                 |
| String            | getPath()                                                | URL의 경로명 반환.                                   |
| int               | getPort()                                                | URL의 포트 번호 반환.                                |
| String            | getProtocol()                                            | URL의 프로토콜 반환.                                 |
| String            | getQuery()                                               | URL의 쿼리 반환.                                     |
| String            | getRef()                                                 | URL의 참조(anchor) 반환.                             |
| String            | getUserInfo()                                            | URL의 사용자 정보(userInfo) 반환.                    |
| URLConnection     | openConnection()                                         | URL과 연결된 URLConnection을 얻음.                   |
| URLConnection     | openConnection(Proxy proxy)                              | 프락시를 통해 URL과 연결된 URLConnection을 얻음.     |
| final InputStream | openStream()                                             | URL과 연결된 URLConnection의 InputStream을 얻음.     |
| boolean           | sameFile(URL other)                                      | 두 URL이 서로 같은 것인지 확인.                      |
| static void       | setURLStreamHandlerFactory(URLStreamHandlerFactory fac)  | Sets an application's URLStreamHandlerFactory.       |
| String            | toExternalForm()                                         | URL을 문자열로 변환하여 반환.                        |
| URI               | toURI()                                                  | URL을 URI로 변환하여 반환.                           |

- 소스 참조 - URL 메서드 <https://github.com/castello/javajungsuk3/blob/master/source/ch16/NetworkEx2.java>

### 1.5 URLConnection

- URLConnection - 애플리케이션과 URL 간의 통신 연결을 나타내는 클래스의 최상위 추상 클래스.
- 구현 클래스
  - HttpURLConnection - URL 프로토콜이 Http이면 반환됨.
  - JarURLConnection

| 수정 자 및 유형              | Method                                                              | Description                                                                     |
| ---------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| void                         | addRequestProperty(String key, String value)                        | 지정된 키와 값을 RequestProperty에 추가. 기존에 같은 키가 있어도 덮어쓰지 않음. |
| abstract void                | connect()                                                           | URL에 지정된 자원에 대한 통신 연결.                                             |
| boolean                      | getAllowUserInteraction()                                           | UserInteraction의 허용 여부를 반환.                                             |
| int                          | getConnectTimeout()                                                 | 연결 종료 시간(ms)을 반환.                                                      |
| Object                       | getContent()                                                        | URL의 Content객체 반환.                                                         |
| Object                       | getContent(Class<?>[] classes)                                      | URL의 Content객체 반환.                                                         |
| String                       | getContentEncoding()                                                | content의 인코딩 반환.                                                          |
| int                          | getContentLength()                                                  | content의 크기 반환.                                                            |
| long                         | getContentLengthLong()                                              |                                                                                 |
| String                       | getContentType()                                                    | content의 type 반환.                                                            |
| long                         | getDate()                                                           | 헤더의 date 필드 값을 반환.                                                     |
| static boolean               | getDefaultAllowUserInteraction()                                    | allowUserInteraction 값을 반환.                                                 |
| static String                | getDefaultRequestProperty(String key)                               | **Deprecated.** getRequestProperty 사용.                                        |
| boolean                      | getDefaultUseCaches()                                               | useCaches의 기본값을 리턴.                                                      |
| static boolean               | getDefaultUseCaches(String protocol)                                | 주어진 프로토콜에 대한 useCaches 플래그의 기본값을 리턴.                        |
| boolean                      | getDoInput()                                                        | doInput의 값 반환.                                                              |
| boolean                      | getDoOutput()                                                       | doOutput의 값 반환.                                                             |
| long                         | getExpiration()                                                     | 자원(URL)의 만료일자(ms) 반환.                                                  |
| static FileNameMap           | getFileNameMap()                                                    | FileNameMap(mimetable)을 반환.                                                  |
| String                       | getHeaderField(int n)                                               | 헤더의 n번째 필드를 반환.                                                       |
| String                       | getHeaderField(String name)                                         | 헤더에서 지정된 이름의 필드 반환.                                               |
| long                         | getHeaderFieldDate(String name, long Default)                       | 지정된 필드의 값을 날짜 값으로 변환하여 반환. 없으면 Default 반환.              |
| int                          | getHeaderFieldInt(String name, int Default)                         | 지정된 필드의 값을 정수로 변환하여 반환. 없으면 Default 반환.                   |
| String                       | getHeaderFieldKey(int n)                                            | 헤더의 n번째 필드의 키를 반환.                                                  |
| long                         | getHeaderFieldLong(String name, long Default)                       |                                                                                 |
| Map\<String,List\<String\>\> | getHeaderFields()                                                   | 헤더의 모든 필드와 값이 저장된 Map을 반환.                                      |
| long                         | getIfModifiedSince()                                                | ifModifiedSince(변경 여부) 필드의 값을 반환.                                    |
| InputStream                  | getInputStream()                                                    | URLConnection의 InputStream을 반환.                                             |
| long                         | getLastModified()                                                   | last-modified(최종 변경일) 필드의 값을 반환.                                    |
| OutputStream                 | getOutputStream()                                                   | URLConnection의 OutputStream을 반환.                                            |
| Permission                   | getPermission()                                                     | Permission(허용 권한)을 반환.                                                   |
| int                          | getReadTimeout()                                                    | 읽기 제한 시간(ms)의 값을 반환. 0은 무한대.                                     |
| Map\<String,List\<String\>\> | getRequestProperties()                                              | RequestProperties에 저장된 (키, 값)을 Map으로 반환.                             |
| String                       | getRequestProperty(String key)                                      | RequestProperties에서 지정된 키의 값을 반환.                                    |
| URL                          | getURL()                                                            | URLConnection의 URL 반환.                                                       |
| boolean                      | getUseCaches()                                                      | useCaches 사용 여부를 반환.                                                     |
| static String                | guessContentTypeFromName(String fname)                              | 지정된 파일(fname)의 content-type을 추측하여 반환.                              |
| static String                | guessContentTypeFromStream(InputStream is)                          | 지정된 입력 스트림(is)의 content-type을 추측하여 반환.                          |
| void                         | setAllowUserInteraction(boolean allowuserinteraction)               | UserInteraction의 허용 여부 설정.                                               |
| void                         | setConnectTimeout(int timeout)                                      | 연결 종료 시간(ms) 설정.                                                        |
| static void                  | setContentHandlerFactory(ContentHandlerFactory fac)                 | ContentHandlerFactory를 설정.                                                   |
| static void                  | setDefaultAllowUserInteraction(boolean defaultallowuserinteraction) | UserInteraction의 기본값 설정.                                                  |
| static void                  | setDefaultRequestProperty(String key, String value)                 | **Deprecated.** setRequestProperty 사용.                                        |
| void                         | setDefaultUseCaches(boolean defaultusecaches)                       | useCaches 사용 여부의 기본값 설정.                                              |
| static void                  | setDefaultUseCaches(String protocol, boolean defaultVal)            |                                                                                 |
| void                         | setDoInput(boolean doinput)                                         | doInput 필드의 값 설정.                                                         |
| void                         | setDoOutput(boolean dooutput)                                       | doOutput 필드의 값 설정.                                                        |
| static void                  | setFileNameMap(FileNameMap map)                                     | FileNameMap을 설정.                                                             |
| void                         | setIfModifiedSince(long ifmodifiedsince)                            | ifModifiedSince 필드의 값 설정.                                                 |
| void                         | setReadTimeout(int timeout)                                         | 읽기 제한 시간(ms) 설정.                                                        |
| void                         | setRequestProperty(String key, String value)                        | RequestProperty에 (키, 값) 저장.                                                |
| void                         | setUseCaches(boolean usecaches)                                     | useCaches 사용 여부 설정.                                                       |

- 소스 참조 - URL Connection <https://github.com/castello/javajungsuk3/blob/master/source/ch16/NetworkEx3.java>

- 소스 참조 - Content 읽기 <https://github.com/castello/javajungsuk3/blob/master/source/ch16/NetworkEx4.java>

```java
InputStream in = url.openStream();
// 같은 코드
URLConnection conn = url.openConnection();
InputStream in = url.getInputStream();
```

## 2. 소켓 프로그래밍

- 소켓(socket) - 프로세스 간의 통신에 사용되는 양쪽 끝단(endpoint)

### 2.1 TCP와 UDP

| 항목        | TCP                                     | UDP                                  |
| ----------- | --------------------------------------- | ------------------------------------ |
| 연결방식    | 연결 기반(connection-oriented)          | 비연결 기반(connectionless-oriented) |
|             | - 연결 후 통신(전화)                    | - 연결 없이 통신(택배)               |
|             | - 1:1 통신 방식                         | - 1:1, 1:n, n:n 통신방식             |
| 특징        | 데이터의 경계를 구분 안 함(byte-stream) | 데이터의 경계를 구분함.(datagram)    |
|             | 신뢰성 있는 데이터 전송                 | 신뢰성 없는 데이터 전송              |
|             | - 데이터의 전송 순서가 보장됨           | - 데이터의 전송 순서가 바뀔 수 있음. |
|             | - 데이터의 수신 여부를 확인함           | - 데이터의 수신 여부를 확인 안 함    |
|             | (데이터가 손실되면 재전송)              | (데이터가 손실되어도 알 수 없음)     |
|             | - 패킷을 관리할 필요가 없음             | - 패킷을 관리해주어야 함             |
|             | UDP보다 전송속도가 느림                 | TCP보다 전송속도가 빠름              |
| 관련 클래스 | Socket                                  | DatagramSocket                       |
|             | ServerSocket                            | DatagramPacket                       |
|             |                                         | MulticastSocket                      |

### 2.2 TCP 소켓 프로그래밍

- TCP 소켓 프로그래밍은 클라이언트와 서버 간의 일대일 통신

  1. 서버 프로그램에서는 서버 소켓을 사용해서 서버 컴퓨터의 특정 포트에서 클라이언트 연결 요청을 처리할 준비를 함.
  2. 클라이언트 프로그램은 접속할 서버의 IP주소와 포트 정보를 가지고 소켓을 생성하여 서버에 연결을 요청.
  3. 서버 소켓은 클라이언트의 연결 요청을 받으면 서버에 새로운 소켓을 생성해서 클라이언트의 소켓과 연결
  4. 클라이언트의 소켓과 새로 생성된 서버의 소켓은 서버 소켓과 관계없이 일대일 통신.

- Socket

  - 실제 데이터를 주고받는 소켓.
  - InputStream과 OutputStream을 가짐.
  - 여러 개의 소켓이 하나의 포트를 공유할 수 있음.

- ServerSocket

  - 소켓 간의 연결을 처리하는 소켓.
  - 포트를 독점 연결(bind).
  - 요청이 들어오면 Socket을 생성하여 소켓 간의 통신을 이룸.

- 포트 - 0 ~ 65536
  - 1023 이하의 포트는 이미 사용 중일 가능성이 높음.

소켓 간의 입출력 스트림 연결

![소켓 간의 입출력 스트림 연결](<images/16%20네트워킹(Networking)_소켓간의_입출력_스트림_연결.png>)

#### 소켓 연결 과정

1. 서버 소켓 생성

2. 서버 소켓이 클라이언트의 연결 요청을 처리할수록 대기 상태로 만듦.

   `serverSocket = new ServerSocket(7777);` - TcpIpServer.java

   ![소켓통신](<images/16%20네트워킹(Networking)_소켓통신1.png>)

3. 클라이언트에서 소켓을 생성하여 서버 소켓에 연결 요청.

   `Socket socket = new Socket("127.0.0.1",7777);` - TcpIpClient.java

   ![소켓통신](<images/16%20네트워킹(Networking)_소켓통신3.png>)

4. 서버 소켓이 연결 요청을 받아 새로운 소켓을 생성하여 클라이언트의 소켓과 연결.

   `Socket socket = serverSocket.accept();` - TcpIpServer.java

   ![소켓통신](<images/16%20네트워킹(Networking)_소켓통신4.png>)

5. 새로 생성된 서버의 소켓과 클라이언트의 소켓이 통신.

   ![소켓통신](<images/16%20네트워킹(Networking)_소켓통신5.png>)

- 소스 참조 - TCP Server <https://github.com/castello/javajungsuk3/blob/master/source/ch16/TcpIpServer.java>
- 소스 참조 - TCP Client <https://github.com/castello/javajungsuk3/blob/master/source/ch16/TcpIpClient.java>

#### 채팅 프로그램

- 소스 참조 - TCP Server <https://github.com/castello/javajungsuk3/blob/master/source/ch16/TcpIpServer5.java>
- 소스 참조 - TCP Client <https://github.com/castello/javajungsuk3/blob/master/source/ch16/TcpIpClient5.java>

다중 채팅 프로그램

### 2.3 UDP 소켓 프로그래밍

- DatagramPacket - UDP 통신에 사용하는 소켓
- DatagramPacket - 데이터를 담은 패킷
  - 수신할 호스트의 정보를 담아서 보냄.

```java

```

- 소스 참조 - UDP Client <https://github.com/castello/javajungsuk3/blob/master/source/ch16/UdpClient.java>
- 소스 참조 - UDP Server <https://github.com/castello/javajungsuk3/blob/master/source/ch16/UdpServer.java>
