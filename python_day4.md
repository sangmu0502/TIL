# python Lesson Day 4
---

## 모듈
- 한 파일로 묶인 변수와 함수의 모음.   
특정한 기능을 하는 코드가 작성된 파이썬 파일 (.py)

> 모듈 예시
- 파이썬의 math 모듈
- 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈
```python
import math

print(math.pi) # 3.141592653589793

print(math.sqrt(4)) # 2.0
```

> 모듈 가져오기
- 모듈 내 변수와 함수에 접근하려면 import 문이 필요
```python
import math
```
```python
help(math)
``` 
> 모듈 사용하기
- '.(dot)' 은   
"점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라" 라는 의미의 연산자
> 모듈을 import하는 다른 방법
- from절을 활용해 특정 모듈을 미리 참조하고 어떤 요소를 import 할지 명시
- from 으로 불러오면 명시적이지 않다.
```python
from math import pi, sqrt

print(pi)

print(sqrt(4))
```

## 파이썬 표준 라이브러리
- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

> 패키지
- 관련된 모듈들을 하나의 디렉토리에 모아 놓은 것

### 파이썬 패키지 관리자(pip)
- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치 (중요)
- 
```python
pip install SomePackage
pip install SomePackage == 1.1.0

pip install requests

import requests

url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()

print(response)
```

> 패키지 사용 목적
- 모듈들의 이름공간을 구분하여 충돌을 방지

# 제어문 Control Statement
---
- 코드의 실행흐름을 제어하는 데 사용되는 구문   
**조건**에 따라 코드 블록을 실행하거나 **반복적**으로 코드를 실행

## 조건문 Conditional Statement

- 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀
```python
if 표현식:   # if, elif에서 평가.
    코드블록
elif 표현식:
    코드블록
else:
    코드블록
```

## for
- 임의의 시퀀스(str, tuple, list, range)의 항목들을 그 시퀀스에 들어있는 순서대로 반복
```python
for 변수 in 반복 가능한 객체:
    코드 블록
# for statement의 기본 구조 
# 반복 가능한 객체 = 시퀀스 + dict + set   
```
> for 문 원리
- 리스트 내 첫 항목이 반복 변수에 할당되고 코드 블록이 실행
- 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행
- ... 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행
```python
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)
"""
apple
banana
coconut
"""
===============================================
country = 'Korea'

for char in country:
    print(char)

"""
K
o
r
e
a
"""
================================================
for i in range(5):
    print(i)
"""
0
1
2
3
4
"""
==================================================
my_dict = {'x': 10, 'y': 20, 'z': 30}

for key in my_dict:
    print(key)
    print(my_dict[key])

"""
x
10
y
20
z
30
"""
================================================
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)
==========================================
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)

"""
A c
A d
B c
B d
"""
===========================================
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)

"""
['A', 'B']
['c', 'd']
"""
for elem in elements:
    for item in elem:
        print(item)
"""
A
B
c
d
"""
```
## while
- 주아진 조건식이 참(True)인 동안 코드를 반복해서 실행 == 조건식이 거짓(False)가 될 때 까지 반복

```python
a = 0

while a <3:
    print(a)
    a += 1
    
print('끝')

"""
0
1
2
끝
"""

number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')
# while 문은 반드시 종료 조건이 필요하다.
```

> - for은 iterable의 요소를 하나씩 순회하며 반복.   
> - while 은 주어진 조건식이 참인 동안 반복

- for
    - 반복 횟수가 명확하게 정해져 있는 경우에 유용
    - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때

- while
    - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때 까지 반복하는 경우

## 반복 제어
- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

> break : 반복을 즉시 중지
> continue : 다음 반복으로 건너뜀

### 주의 사항
- break 와 continue를 남용하는 것은 코드의 가독성을 저하시킬 수 있음
- **특정한 종료 조건**을 만들어  break를 대신하거나, **if문을 사용**해 continue 처럼 코드를 건너 뛸 수도 있음
- 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고 코드으 ㅣ의도를 명확하게 작성하도록 노력하는 것이 중요

## List Comprehension
- List Comprehension 구조
```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
================================
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)  # [1, 4, 9, 16, 25]


# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]

print(squared_numbers)  # [1, 4, 9, 16, 25]


result = []
for i in range(10):
    if i % 2 == 1:
        result.append(i)

# List comprehension
result = [i for i in range(10) if i % 2 == 1]

```
## 참고
> pass
- 아무런 동작도 수행하지 않고 넘어가는 역할
    - 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용

1. 코드 작성 중 미완성 부분
    - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일 하는 동안 오류가 발생하지 않음
2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법

### enumerate
> enumerate(lierable, start=0)
- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')


print(enumerate(fruits))  # <enumerate object at 0x000002133DA99700>
print(list(enumerate(fruits)))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

``````