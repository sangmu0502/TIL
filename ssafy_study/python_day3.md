python Lesson day3
-
# 함수 Functions
---
특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

> 함수를 사용하는 이유 ?
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
- 재사용성이 높아지고, 코드의 가독성과 유지보수성 향상

## 내장 함수
- 파이썬이 기본적으로 제공하는 함수(별도의 import 없이 바로 사용 가능)
- 주의 사항 : 외장 함수라는 단어는 원문에서 찾아볼 수 없는 단어.

>예시
```python
# abs 함수 호출의 반환 값을 result에 할당

result = abs(-1)

print(result) #1
```

### 함수 호출 (function call)
---
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것. 
- 함수 호출 할 때에는 소괄호 () 를 사용하여야 한다.

```
함수 구조
INPUT x  ㅡㅡ> parameter(매개변수)
  l
  v
Docstring
function body
  l
  v
OUTPUT f(x)  ㅡㅡ> return value
```
```python
def make_sum(pram1, pram2) # pram1, pram2 = 파라미터(매개변수)
   """이것은 두 수를 받아      
   두 수의 합을 반환하는 함수이니다.

   >>>make_sum(1, 2)
   3
   """
   return pram1 + pram2
```

>함수의 정의와 호출
- 함수 정의(정의)
    - 함수 정의는 def 키워드로 시작
    - def 키워드 이후 함수이름 작성
    - 괄호안에 매개변수를 정의할 수 있음
    - 매개변수는 함수에 전달되는 값을 나타냄
- 함수 body
    - 클론(:) 다음에 들여쓰기 된 코드 블록
    - 함수가 실행 될 때 수행되는 코드를 정의
    - Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수설명서
- 함수 반환 값
    - 함수는 필요한 경우 결과를 반환할 수 있음
    - return 키워드 이후에 반환할 값을 명시
    - return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
- 함수 호출
    - 함수를 호출하기 위해서는 함수의 이름과 필요한 인자(argument)를 전달해야 함
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨
        - 정의할 때는 parameter, 호출할 때는 argument

### 매개변수와 인자
---
> 매개변수 parameter
- 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
> 인자 argument
- 함수를 호출할 때, 실제로 전달되는 값

#### 매개변수와 인자 예시
```python
def add_numbers(x, y): # x와 y는 매개변수
    result = x + y
    return result
    
a = 2
a = 3
sum_result = add_numbers(a, b) # a와 b는 인자
print(sum_result)
```

### 인자의 종류
---
### 1. Positional Arguments (위치인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
* 위치인자는 함수 호출시 반드시 값을 전달해야 함
```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
    
greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
```

### 2. Default Argument Values (기본인자)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
```python
def greet(name , age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
    
greet('Alice') # 안녕하세요, Alice님! 30살이시군요.
greet('BOb', 40) # 안녕하세요, Bob님! 40살이시군요.
```

### 3. Keyword Arguments (키워드인자)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수의 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하며 전달
- 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함.
```python
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
    
greet(name='Dave', age=35) # 안녕하세요 Dave님! 35살이시군요.
greet(age=35, name='Dave') # 안녕하세요 Dave님! 35살이시군요.
greet(age=35, 'Dave') # positional argument follows keyword argument
```
### 4. Arbitary Argument Lists (임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
```python
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')
    
"""
(1, 2, 3)
합계: 6
"""
calculate_sum(1, 2, 3)
```

### 5. Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리
```python
def print_info(**kwargs):
    print(kwargs)
    
print_info(name='Eve', age=30) # {'name' : 'Eve', 'age' = 30}
```

### 함수 인자 권장 작성순서
---
- 위치 ㅡ> 기본 ㅡ> 가변 ㅡ> 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
- 단, 모든 상황에 저용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음
```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print(pos1, pos2, age=30, *args, **kwargs)

# func(1, 2, 3, 4, 5)
# 1 2 3 (4, 5) {}

# func(1, 2, 3, a=100, b=100)
# 1 2 3 () {'a' : 100, 'b' : 100}

```

### Python의 범위(Scope)
---
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope(함수 내부에서만 참조 가능)
- variable
    - global variable : g;obal scope에 정의된 변수
    - local variable : local scope에 정의된 변수

> Scope 예시
- num은 local scope에 존재하기 때문에 global에서 사용할 수 없음
- 이는 변수의 수명주기와 연관이 있음
```python
def func():
    num = 20
    print('local', num) # local 20
    
func()

print('global', num) # NameError : name 'num' is no defined
```

### 변수의 수명 주기(life cycle)
- 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
1. built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙 (Name Resoulution)
- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
    1. Local scope : 지역 범위(현재 작업 중인 범위)
    2. Enclosed scope : 지역 범위 한 단계 위 범위
    3. Global scope : 최상단에 위치한 범위
    4. Built-in scope : 모든 것을 담고 있는 범위

>LEGB Rule 예시
```python
print(sum)   # built-in function sum
print(sum(range(3)))   #3

sum = 5

print(sum)  #5
print(sum(range(3)))  # TypeError : 'int' object is not callable
```

>'global' 키워드

```python
num = 0 # 전역 변수

def increment():
    global num
    num += 1

print(num) #0
increment()
print(num) #1
```

- global 키워드는 가급적 사용하지 않는 것을 권장
- 함수로 값을 바꾸고자 한다면 항상 인자로 넘기고 함수의 반환 값을 사용하는 것을 권장

## 재귀 함수
- 함수 내부에서 자기 자신을 호출하는 함수
>재귀 함수 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
-1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

>재귀 함수 예시 - 팩토리얼
- n!, n*(n-1)!

```python
def factorial(n):
    #종료 조건 : n이 0이면 을 반환
    if n == 0:
        return 1
    # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n-1)
    
#팩토리얼 계산 예시
result = factorial(5)
print(result) # 120
```
```
재귀 함수는
1. 종료 조건을 명확히 (안그러면 무한 loop에 빠짐)
2. 반복되는 호출이 종료 조건을 향하도록
```

### 유용한 내장 함수
---
>map(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)
print(list(result)) # ['1', '2', '3']
# 마치 반복문을 쓴 것처럼 list안에 있는 숫자들을 str형태로 바꿔줌
```
```python
numbers = input().split() # split은 '1 2 3 4 5' 를 ['1', '2', '3', '4', '5']로 만들어줌
print(numbers) # ['1', '2', '3', '4', '5']

result = map(int, numbers)

print(result) # map object at 0x00....
print(list(result)) # [1, 2, 3, 4, 5]

result = list(map(int, input().split())) # 한 줄로 쓰기.
```

>zip(*iterables) *iterables = 가변인자
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)
print(list(pair)) # [('jane', 'peter), ('ashley', 'jay')]
```
> lambda 함수

`lambda 매개변수 : 표현식`
- 이름 없이 정의되는 함수
- 일회성으로 함수를 쓸 때 많이 사용
- map이랑 많이 쓰인다.

```python
numbers = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2

result = list(map(func, numbers))
print(result) # [1, 4, 9, 16, 25]

result2 = list(map(lambda x: x**2, numbers))
```

# Packing 패킹
- 여러 개의 값을 하나의 변수에 묶어서 담는 것
> 패킹 예시
- 변수에 담긴 값들은 튜플 형태로 묶임
```python
packed_values = 1,2,3,4,5
print(packed_values) # (1, 2, 3, 4, 5)
```
>*를 이용한 패킹
```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a) #1
print(b) #(2, 3, 4)
print(c) #5
```
# Unpacking 언패킹
> 언패킹 예시
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당

```python
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values

print(a, b, c, d, e) # 1, 2, 3, 4, 5
```
```python
names = ['alice', 'jane', 'peter']
print(*names) # alice jane peter
```
```python
def my_function(x, y, z):
    print(x, y, z)
    
my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict) # 1 2 3 
```
- '*'
    - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜플로 묶는 역할
    - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달
- '**'
    - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 키워드 인자로 언패킹하여 함수의 인자로 전달하는 역할
