# python Lesson Day 5
---

## Data Structure
여러 데이터를 효과적으로 사용, 관리하기 위한 구조(str, list, dict 등)

### 자료구조
- 컴퓨터 공학에서는 '자료구조'라고 함
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

### 데이터 구조 활용
---
---
- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 *메서드*를 호출하여 다양한 기능을 활용하기

### 메서드
객체에 속한 함수   
객체의 상태를 조작하거나 동작을 수행

> 메서드 특징
- 메서드는 클래스 내부에 정의되는 함수
- 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용해왔음
- 예를 들어 help 함수를 통해 str을 호출해보면 class 였다는 것을 확인가능
- 메서드는 어딘가(클래스)에 속해 있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재

> 메서드 호출 방법
- 데이터 타입 객체.메서드()
```python
# 문자열 메서드 예시
'hello'.capitalize()   #Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]
=============================
append() # 함수 호출
리스트.append()   # 메서드 호출
객체.메서드()
```

## 시퀀스 데이터 구조
---
### 문자열 메서드
|메서드|설명|
|:---:|:---:|
|s.find(x)|x의 첫 번째 위치를 반환. 없으면, -1을 반환|
|s.index(x)|x의 첫 번째 위치를 반환. 없으면, 오류 발생|
|s.isalpha()|알파벳 문자 여부|
|s.isupper()|대문자 여부|
|s.islower()|소문자 여부|

```python
# .find(x) 예시
# x의 첫 번째 위치를 반환. 없으면, -1을 반환
print('banana'.find('a')) #  1
print('banana'.find('z')) # -1

# .index(x)
# x의 첫 번째 위치를 반환. 없으면, 오류 발생
print('banana'.index('a')) #  1
print('banana'.index('z')) #  ValuError: substring not found

# .isupper(x) / .islower(x)
# 문자열이 모두 대문자/소문자로 이루어져 있는지 확인
string1 = 'HELLO'
string2 = 'hello'
print(string1.isupper()) #  True
print(string2.isupper()) #  False
print(string1.islower()) #  False
print(string2.islower()) #  False

# .isalpha(x)
# 문자열이 알파벳으로만 이루어져 있는지 확인
string1 = 'Hello'
string2 = '123'
print(string1.isalpha()) # True
print(string2.isalpha()) # False
```

### 문자열 조작 메서드(새 문자열 변환)(원본을 바꾸지 않는다.)

|메서드|설명|
|:---:|:---:|
|s.replace(old, new[,count])|바꿀 대상 글자를 새로운 글자로 바꿔서 반환|
|s.strip([chars])|공백이나 특정 문자를 제거|
|s.split(sep=None, maxsplit=-1)|공백이나 특정 문자를 기준으로 분리|
|'separator'.join([iterable])|구분자로 iterable을 합침|
|s.capitalize()|가장 첫 번째 글자를 대문자로 변경|
|s.title()|문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환|
|s.upper()|모두 대문자로 변경|
|s.lower()|모두 소문자로 변경|
|s.swapcase()|대<->소문자 서로 변경|
> 문자열 조작 메서드
```python
# 베커스 나우르 표기법(ebnf)
======================
# s.replace(old, new[,count])

text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python!

# .strip([chars])

text = '      Hello, world!        '
new_text = text.strip()
print(new_text) # 'Hello, wordl!"

# .split(sep=None, maxsplit=-1)

text = 'Hello, world!'
words = text.split(',')
print(words) # ['Hello, 'world!']

# 'separator'.join([iterable])

words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # 'Hello-world!'


text = 'heLLo, woRld!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()

print(new_text1) # Hello, world!
print(new_text2) # hello, World!
print(new_text3) # HELLO, WORLD!
print(new_text4) # HEllo, WOrLD!

text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l','z')
print(new_text) #HEzzO, WOrLD!
```

## 리스트 메서드

- append와 extend의 차이는 append는 괄호가 풀리지 않고 추가한다. extend는 항목들만 추가.

|메서드|설명|
|:---:|:---:|
|L.append(x)|리스트 마지막에 항목 x를 추가|
|L.extend(m)|Iterable m의 모든 항목들을 리스트 끝에 추가|
|L.insert(i, x)|리스트 인덱스 i에 항목 x를 삽입|
|L.remove(x)|리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거. 항목이 존재하지 않을 경우,ValueError|
|L.pop()|리스트 가장 오른쪽에 있는 항목을 반환 후 제거|
|L.pop(i)|리스트의 인덱스 i에 있는 항목을 반환 후 제거|
|L.clear()|리스트의 모든 항목 삭제|

```python
# .append(x)
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]

# .extend(iterable)
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]

# .intser(i, x)
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) #[1, 5, 2, 3]

# .remove(x)
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list) #[1, 3]

# .pop(i)
my_list = [1, 2, 3, 4, 5]

item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
print(item2) # 1
print(my_list) # [2, 3, 4]

# .clear()
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []
```

|문법|설명|
|:---:|:---:|
|L.index(x, start, end)|리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환|
|L.reverse()|리스트의 순서를 역순으로 변경(정렬x)|
|L.sort()|리스트를 정렬 (매개변수 이용가능)|
|L.count(x)|리스트에서 항목 x의 개수를 반환|

```python
# .index(x)
my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1

# .count(x)
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count) # 3

# .sort()
my_list = [3, 2, 1]
my_list.sort()
print(my_list) # [1, 2, 3]
# 내림차순
my_list.sort(reverse=True)
print(my_list) # [3, 2, 1]

# .reverse()
my_list = [1, 3, 2, 8 ,1, 9]
my_list.reverse()
print(my_list) # [9, 1, 8, 2, 3, 1]
```

## 데이터 타입과 복사
- 파이썬에서는 데이터의 분류에 따라 복사가 달라짐
- "변경 가능한 데이터 타입"과 "변경 불가능한 데이터 타입"을 다르게 다룸

```python
# list 는 가변 데이터여서 주소가 복사가 됨
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]
===========================
# 정수는 불변 데이터여서 다른 주소값이 복사가 됨. 
a = 20
b = a
b = 10

print(a) # 20
print(b) # 10

```
### 복사 유형
1. 할당 (Assignment)
2. 얕은 복사 (Shallow copy)
3. 깊은 복사 (Deep copy)

```python
# 리스트 복사 예시
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]

copy_list[0] = 'hi'
print(original_list, copy_list) # ['hi', 2, 3] ['hi', 2, 3]
 
# 리스트 얕은 복사 예시
# 슬라이싱을 통해 생성된 객체는 왼본 객체와 독립적으로 존재
a = [1, 2, 3]
b = a[:]
print(a, b) # [1, 2, 3][1, 2, 3]

b[0] = 100
print(a, b) # [1, 2, 3][100, 2, 3]

# 리스트 깊은 복사 예시
import copy

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2],[0]

print(original_list) # [1, 2 [1, 2]]
print(deep_copied_list) # [1, 2, [100, 2 ]]
```

> 참고
- isdecimal()
    - 문자열이 모두 숫자 문자 로만 이루어져 있어야 True
- isdigit()
    - isdecimal()과 비슷하지만, 유니코드 숫자도 인식
- isnumeric()
    - isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식