# QueryDSL

## 설정

```groovy
//querydsl 추가
buildscript {
   dependencies {
      classpath("gradle.plugin.com.ewerk.gradle.plugins:querydsl-plugin:1.0.10")
   }
}

apply plugin: "com.ewerk.gradle.plugins.querydsl"

dependencies {
    implementation 'com.querydsl:querydsl-jpa'
    implementation 'com.querydsl:querydsl-apt'
}

def querydslDir = "$buildDir/generated/querydsl"

querydsl {
   library = "com.querydsl:querydsl-apt"
   jpa = true
   querydslSourcesDir = querydslDir
}

compileQuerydsl{
   options.annotationProcessorPath = configurations.querydsl
}

configurations {
   querydsl.extendsFrom compileClasspath
}

```

## 사용

---

## 출처

- QueryDSL 설정 - <https://www.inflearn.com/questions/219898>
- Spring Boot에 QueryDSL을 사용해보자 - <https://tecoble.techcourse.co.kr/post/2021-08-08-basic-querydsl/>
- [gradle] 그레이들 Annotation processor 와 Querydsl - <http://honeymon.io/tech/2020/07/09/gradle-annotation-processor-with-querydsl.html>
