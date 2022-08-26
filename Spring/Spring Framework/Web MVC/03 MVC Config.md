# MVC Config

- [1. Enable MVC Configuration](#1-enable-mvc-configuration)
- [2. MVC Config API](#2-mvc-config-api)
- [3. Type Conversion](#3-type-conversion)
- [4. Validation](#4-validation)
- [5. Interceptors](#5-interceptors)
- [6. Content Types](#6-content-types)
- [7. Message Converters](#7-message-converters)
- [8. View Controllers](#8-view-controllers)
- [9. View Resolvers](#9-view-resolvers)
- [10. Static Resources](#10-static-resources)
- [11. Default Servlet](#11-default-servlet)
- [12. Path Matching](#12-path-matching)
- [출처](#출처)

## 1. Enable MVC Configuration

> The MVC Java configuration and the MVC XML namespace provide default configuration suitable for most applications and a configuration API to customize it.

- `@EnableWebMvc` annotation to enable MVC configuration

```java
@Configuration
@EnableWebMvc
public class WebConfig {
}
```

## 2. MVC Config API

- implement the `WebMvcConfigurer` interface
- (구현하지 않으면 무슨 차이지?)

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    // Implement configuration methods...
}
```

## 3. Type Conversion

- 다양한 숫자 및 날짜 유형에 대한 포맷터가 설치되어 있음.
- @NumberFormat, @DateTimeFormat를 통해 커스터마이징.

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addFormatters(FormatterRegistry registry) {
        DateTimeFormatterRegistrar registrar = new DateTimeFormatterRegistrar();
        registrar.setUseIsoFormat(true);
        registrar.registerFormatters(registry);
    }
}
```

## 4. Validation

- Bean Validation - Hibernate Validator가 디폴트
- the `LocalValidatorFactoryBean` is registered as a global Validator for use with `@Valid` and `Validated` on controller method arguments.

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public Validator getValidator() {
        // ...
    }
}
```

## 5. Interceptors

- register interceptors to apply to incoming requests

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new LocaleChangeInterceptor());
        registry.addInterceptor(new ThemeChangeInterceptor()).addPathPatterns("/**").excludePathPatterns("/admin/**");
    }
}
```

## 6. Content Types

- You can configure how Spring MVC determines the requested media types from the request (for example, Accept header, URL path extension, query parameter, and others).
- By default, only the Accept header is checked.

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void configureContentNegotiation(ContentNegotiationConfigurer configurer) {
        configurer.mediaType("json", MediaType.APPLICATION_JSON);
        configurer.mediaType("xml", MediaType.APPLICATION_XML);
    }
}
```

## 7. Message Converters

- customize HttpMessageConverter in Java configuration
  - overriding configureMessageConverters()
  - overriding extendMessageConverters()

```java
@Configuration
@EnableWebMvc
public class WebConfiguration implements WebMvcConfigurer {

    @Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        Jackson2ObjectMapperBuilder builder = new Jackson2ObjectMapperBuilder()
                .indentOutput(true)
                .dateFormat(new SimpleDateFormat("yyyy-MM-dd"))
                .modulesToInstall(new ParameterNamesModule());
        converters.add(new MappingJackson2HttpMessageConverter(builder.build()));
        converters.add(new MappingJackson2XmlHttpMessageConverter(builder.createXmlMapper(true).build()));
    }
}
```

## 8. View Controllers

- This is a shortcut for defining a ParameterizableViewController that immediately forwards to a view when invoked.
- You can use it in static cases when there is no Java controller logic to run before the view generates the response.
- (컨트롤러 구현하기 귀찮을 때?)

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        registry.addViewController("/").setViewName("home");
    }
}
```

## 9. View Resolvers

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void configureViewResolvers(ViewResolverRegistry registry) {
        registry.enableContentNegotiation(new MappingJackson2JsonView());
        registry.freeMarker().cache(false);
    }

    @Bean
    public FreeMarkerConfigurer freeMarkerConfigurer() {
        FreeMarkerConfigurer configurer = new FreeMarkerConfigurer();
        configurer.setTemplateLoaderPath("/freemarker");
        return configurer;
    }
}
```

## 10. Static Resources

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/resources/**")
                .addResourceLocations("/public", "classpath:/static/")
                .setCacheControl(CacheControl.maxAge(Duration.ofDays(365)));
    }
}
```

## 11. Default Servlet

- Spring MVC allows for mapping the `DispatcherServlet` to `/`
- It configures a DefaultServletHttpRequestHandler with a URL mapping of /\*\* and the lowest priority relative to other URL mappings.

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
        configurer.enable("myCustomDefaultServlet");
    }
}
```

## 12. Path Matching

```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void configurePathMatch(PathMatchConfigurer configurer) {
        configurer
            .setPatternParser(new PathPatternParser())
            .addPathPrefix("/api", HandlerTypePredicate.forAnnotation(RestController.class));
    }

    private PathPatternParser patternParser() {
        // ...
    }
}
```

---

## 출처

- <https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc-config>
