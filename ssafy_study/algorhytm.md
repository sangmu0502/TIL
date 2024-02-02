# 알고리즘 주요 메서드

## 내장 함수

> sum()
- iterable 객체 (리스트, 사전 자료형, 튜플)
```python
result = sum([1, 2, 3, 4, 5])
print(result) # 15
```

> min(), max()
- 파라미터가 2개 이상 들어왔을 때.
```python
result = min(7, 3, 5, 2)
print(result) # 2
result = max(7, 3, 5, 2)
print(result) # 7
```

> eval() 
- 수학 수식이 '문자열' 형식으로 들어오면 해당 수식을 계산한 결과를 반환
```python
result = eval("(3 + 5) * 7)")
print(result) # 56
```

> sorted()
- iterable 객체가 들어왔을 때, 정렬된 결과를 반환
    - key 속성으로 정렬 기준을 명시할 수 있음
    - reverse 속성으로 정렬된 결과 리스트를 뒤집을 지의 여부 설정할 수 있음
    - 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있어서 sort() 함수로도 정렬 가능, 이 경우에는 리스트 객체의 내부 값이 정렬된 값으로 바로 변경됨.
```python
result = sorted([9, 1, 8, 5, 4])
print(result) # [1, 4, 5, 8, 9]
result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result) # >>> [9, 8, 5, 4, 1]

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result) # >>> [('이순신', 75), ('아무개', 50), ('홍길동', 35)]

data = [9, 1, 8, 5, 4]
data.sort()
print(data) # >>> [1, 4, 5, 8, 9]
```

## itertools
- 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
> permutations
- 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산
    - permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용해야 함
```python
from itertools impot permutations

data = ['A', 'B', 'C'] #데이터 준비
result = list(permutations(data, 3))

print(result) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A, 'B'), ('C', 'B', 'A')]
 ```

 # 개인적으로 보는 자주쓰는 기본 함수들.

 > ord()/ chr()
 - ord()는 문자열을 아스키코드(숫자)로 반환하는 함수이고, chr()는 아스키코드를 문자열로 반환하는 함수
 - 위치가 C2 등으로 주어질 때 C의 row 위치를 숫자로 반환해야할 때
 ```python
 chr(65) # A
 ord('a') # 97
 ```

 > isalpha()/ isalnum()
 - isalpha()는 문자열이 True, 아니면 False를 리턴하고, isalnum()은 숫자면 True, 아니면 False를 리턴함
 ```python
 text1 = 'abcd'
 text1.isalpha() # True
 
 text2 = 1234
 text2.isalnum() # True
 ```

 > filter (조건함수, 순회 가능 데이터)
 - filter는 일부의 데이터만 추려낼 때 사용하는 함수. 특히 출력을 filter 자료형으로 하기 때문에 출력 값에 list를 씌워줘야 한다.
 ```python
 string = '0001100'
 res = list(filter(lambda x: string[x] == '0', range(len(string))))
 >>> [0, 1, 2, 5 ,6]
 ```

 > eval (수식)
 - eval은 python code 로 실행 가능한 문자열을 인자로 받아 실제로 실행해주는 함수. 예를들면 '5+3' 등의 수식을 실제로 계산해주거나, 'round(4.9)'를 실제로 반올림 해주는 등의 기능을 한다.
 ```python
 eval('5+4')
 >>> 9
 eval('round(4.9)')
 >>> 5
 ```
 
 > itertools 라이브러리 (permutations, combinations)
 - 리스트에서 순열, 조합을 계산해주는 내장 라이브러리이다. 두개의 리스트에서 모든 조합을 계산할 때는 product method사용
 ```python
 items = ['1', '2', '3', '4', '5']
 
 from itertools import permutations
 list(permutations(items, 2)) # 중복 허용할 때 (순열)
 >>> [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '1'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '5'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4')]

 from itertools import combinations   # 중복 허용하지 않을 때 (조합)
list(combinations(items, 2))
>>> [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

 ```
 
 ### 튜플 사용법
 1. 인덱싱
 2. 슬라이싱
 3. 더하기
 4. 곱하기 (이 때, 튜플은 수정, 삭제할 수 없으므로 새로운 변수에다가 저장해야 한다.)
 5. 메서드
    - len, min, max 함수
### 리스트 사용법
- 리스트에는 다양한 자료형을 포함할 수 있다. 예를 들어, 문자열, 정수, 실수, 불리언 값 등을 포함한 리스트를 생성할 수 있다.
```python
mixed_list = [1, 'hellod', 3.14, True]
```










### 딕셔너리 사용법
- 리스트와 딕셔너리의 차이점
    - 리스트는 순서가 있다.
    - 리스트는 요소에 접근할 때는 인덱스를 사용한다.
    - 리스트는 많은 양의 데이터를 효율적으로 저장하기에 적합하지 않다.
- 딕셔너리
    - 딕셔너리는 키와 값의 쌍으로 구성된 자료 구조로 순서가 없다.
    - 딕셔너리에서 요소에 접근할 때는 키를 사용한다.
    - 딕셔너리는 많은 양의 데이터를 효율적으로 저장하기에 적합하다.

1. zip(), dict()함수 사용법
- 파이썬 zip()함수는 여러 개의 리스트를 같은 위치에 있는 요소끼리 묶어서 튜플의 리스트를 생성하는 함수이다. 아래 코드는 keys, values 리스트의 각 요소를 zip()함수를 이용해 요소끼리 묶고 생성된 튜플의 리스트 [('name', 'John Doe'), ('age', 30), ('city', 'Seoul')]를 dict()함수를 통해 딕셔너리로 변환하는 코드
```python
keys = ['name', 'age', 'city']
values = ['John Doe', 30, 'Seoul']
person = dict(zip(keys, values))
print(person) # {'name' : 'John Doe', 'age' : 30, 'city': 'Seoul'}
```
2. 딕셔너리에 요소 추가, 변경
- 파이썬 딕셔너리에 새로운 요소를 추가할 때에는 "딕셔너리 이름[key] = value"를 통해 새로운 요소를 추가 할 수 있다.
- 변경은 같은 코드를 통해 기존에 있던 요소를 새로운 요소의 값으로 변경할 수 있다.

3. 딕셔너리 요소 접근
- key를 이용하는 방법
    - "딕셔너리 이름[key]"를 통해 요소에 접근할 수 있다.
- get()메서드를 이용하는 방법
    - get()메서드는 요소가 없을 경우 None을 반환한다.

4. 딕셔너리 요소 제거
- pop()메서드를 이용하는 방법
    - pop()메서드는 제거된 요소의 값을 반환한다.
- del 구문을 이용하는 방법
    - "del 딕셔너리 이름[key]"를 통해 제거할 수 있다.
- clear()메서드를 이용하는 방법
    - clear()메서드를 사용하면 모든 요소가 제거된다.

5. 딕셔너리 메서드
- keys() 메서드
    - keys() 메서드를 사용하면 파이썬 딕셔너리의 키만을 가져올 수 있다.
- values() 메서드
    - values() 메서드를 사용하여 파이썬 딕셔너리의 값만을 가져올 수 있다.
- copy() 메서드
    - copy() 메서드를 사용하여 파이썬 딕셔너리의 복사본을 생성할 수 있다.

6. 딕셔너리 응용
- 중첩 딕셔너리
    - 파이썬 딕셔너리에서 딕셔너리를 다중으로 중첩할 수 있다.
- 반복문을 이용한 딕셔너리 키와 값 동시 처리
    - 반복문(for)과 파이썬 딕셔너리를 사용하여, 딕셔너리의 키와 값을 동시에 처리할 수 있다.
```python
person = {'name' : 'John Doe', 'age' : 30, 'city': 'Seoul'}
for key, value in person.items():
    print(f'{key}: {value}')
"""
name : John Doe
age : 30
city : seoul
"""    
```
- 조건문을 이용한 딕셔너리 특정 키 존재 확인
```python
person = {'name' : 'John Doe', 'age' : 30, 'city': 'Seoul'}
if 'age' in person:
    print("Key 'age' exists in the dictionary.")
else:
    print("Key 'age' does not exist in the dictionary.")
```

7. FAQ
- 딕셔너리에서 키와 값의 순서는 중요한가
    - 딕셔너리는 키를 사용하여 값에 접근하기 때문에, 순서는 중요하지 않다.
- 딕셔너리에서 키는 중복되지 않는다. 새 요소가 이전 요소를 덮어씌운다.
- 딕셔너리에서 값은 중복될 수 있다. 키를 사용하여 값에 접근하기 때문에, 동일한 값을 가진 요소가 여러 개 존재할 수 있다.
- 딕셔너리에서 문자열과 숫자 타입의 키를 같이 사용할 수 있다. 키는 문자열, 숫자, 튜플 등 다양한 타입의 값을 가질 수 있다. 단, 키는 가변 타입의 값(리스트, 딕셔너리 등)을 가질 수 없다.