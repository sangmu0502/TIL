# CleanCode 정리

## 의미 있는 이름
- 소프트웨어에서 이름은 어디나 쓰인다. 이 장에서는 이름을 잘 짓는 간단한 규칙을 몇 가지 소개한다.

### 의도를 분명히 밝혀라
- 좋은 이름을 지으려면 시간이 걸리지만 좋은 이름으로 절약하는 시간이 훨씬 더 많다.
- 변수(혹은 함수나 클래스)의 존재 이유는? 수행 기능은? 사용 방법은? 따로 주석이 필요하다면 의도를 분명히 드러내지 못했다는 말이다.
- **int d;** 이름 d는 아무 의미도 드러나지 않는다. 경과 시간이나 날짜라는 느낌이 안 든다. 측정하려는 값과 단위를 표현하는 이름이 필요하다.
- 문제는 코드의 **단순성**이 아니라 **함축성** 이다. 다시 말해, 코드 맥락이 모드 자체에 명시적으로 드러나지 않는다.

### 그릇된 정보를 피하라
- 서로 흡사한 이름을 사용하지 않도록 주의한다. 유사한 개념은 유사한 표기법을 사용한다. 이것도 정보다. 일관성이 떨어지는 표기법은 그릇된 정보다.
- 이름으로 그릇된 정보를 제공하는 에가 소문자 L이나 대문자 O변수이다. 이러지 말자.
