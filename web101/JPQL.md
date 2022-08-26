# JPQL

## TypeQuery, Query

### TypeQuery

- TypeQuery : 반환 타입 명확하게 지정 가능

```java
@Query("select r " +
        "from RestaurantEntity r " +
        "left join fetch r.restaurantCategories rc " +
        "left join fetch rc.category c " +
        "where r.id = :id")
Optional<RestaurantEntity> findByIdWithCategory(@Param("id") Long id);
```

```java
RestaurantEntity restaurant = restaurantRepository.findByIdWithCategory(restaurantId)
                .orElseGet(() -> restaurantRepository.getById(restaurantId));
```

### Query

- Query : 반환 타입 명확하게 지정 불가능
- SELECT 절에서 여러 엔티티나 컬럼을 선택 시 반환 타입이 명확하지 않으므로 사용
- 조회 대상의 갯수에 따라 반환 타입이 달라짐
  - 둘 이상 : Object[]
  - 하나 : Object

```java
@Query("select r, (abs(r.latitude-:latitude) + abs(r.longitude-:longitude)) as distance " +
        "from RestaurantEntity r " +
        "order by distance asc")
Page<Object[]> findByLatitudeAndLongitude(double latitude, double longitude, Pageable pageable);
```

- r(RestaurantEntity), distance 두 가지를 반환하므로 `Object[]`

```java
Page<Object[]> restaurants = restaurantRepository.findByLatitudeAndLongitude(latitude, longitude, pageable);

List<Object[]> content = restaurants.getContent();
RestaurantEntity restaurant = (RestaurantEntity) content.get(0)[0];

// page 타입 변환
Page<RestaurantDTO> restaurantDTOPage = restaurants.map(o -> new RestaurantDTO((RestaurantEntity) o[0]));
```

- object[0]은 RestaurantEntity

> 임시 클래스를 만들어서 받자

---

## 출처

- [JPA] Chapter 10. 객체지향 쿼리 언어 1 - JPQL - <https://velog.io/@yu-jin-song/JPA-Chapter-10.-객체지향-쿼리-언어-1-JPQL>
