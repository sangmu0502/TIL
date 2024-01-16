# python Lesson day 2
---
> 지난 시간 복습
### Data Types
- 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
#### 데이터 타입 분류
- Numeric Type
    - int (정수), float (실수), complex (복소수)
- Sequence Types
    - list, tuple, range
- Text Sequence Type
    - str (문자열)
- Set Types
    - set
- Mapping Types
    - dict
- 기타
    - None, Boolean, Functions

## Sequence Types
 
 여러 개의 값들을 순서대로 나열하여 저장하는 자료형 (str, list, tuple, range)
 - 특징
1. 순서(Sequence)
    - 값들이 순서대로 저장 (정렬X)
2. 인덱싱(Indexing)
    - 각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정 할 수 있음.
3. 슬라이싱(Slicing)
    - 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
4. 길이(Length)
    - len()함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
5. 반복(Iteration)
    - 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음
> list

여러개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형
- 리스트 표현
    - 0개 이상의 객체를 포함하며 데이터 목록을 저장
    - 대괄호([])로 표기
    - 데이터는 어떤 자료형도 저장할 수 있음
    - ex)   
     my_list_1 = []    
     my_list_2 = [1, 'a', 3, 'b', 5]   
     my_list_3 = [1, 2, 3, 'Python', ['hello','world', '!!!']]
    - ex2)   
    my_list = [1, 'a', 3, 'b' ,5]      
    #인덱싱   
    print(my_list[1]) =>a   
       
       #슬라이싱   
       print(my_list[2:4]) => [3, 'b']   
       print(my_list[:3]) => [1, 'a', 3]   
       print(my_list[3:]) => ['b', 5]   
       print(my_list[0:5:2]) => [1, 3, 5]   
       print(my_list[::-1]) => [5, 'b', 3, 'a', 1]   
          
        #길이   
        print(len(my_list)) => 5   
    - ex3)  
     my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]   
       
       print(len(my_list)) => 5   
       print(my_list[4][-1]) => !!!   
       print(my_list[-1][1][0]) => w   
    - ex4) list 는 가변 (변경 가능)  
     my_list = [1, 2, 3]   
     my_list[0] = 100   
        
        print(my_list) => [100, 2, 3]
> tuple

여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형

- 튜플 표현
    - 0개 이상의 객체를 포함하며 데이터 목록을 저장
    - 소괄호 (())로 표기
    - 데이터는 어떤 자료형도 저장할 수 있음   
    - ex)   
    my_tuple_1 = ()   
    my_tuple_2 = (1,) => 콤마를 넣어줘야 한다. 빠져버리면 튜플이 아니고 정수 1이 된다.   
    my_tuple_3 = (1, 'a', 3, 'b', 5)  
    - ex2) 튜플은 불변   
    my_tuple = (1, 'a', 3, 'b', 5)   
       
       #TypeError : 'tuple' object does not support item assignment   
       my_tuple[1] = 'z'
- 튜플은 어디에 쓰일까
    - 개발자가 직접 사용하기 보다 '파이썬 내부 동작' 에서 주로 사용됨   
    x, y = (10, 20)   
       
       print(x) => 10   
       print(y) => 20


> range

연속된 **정수 시퀀스**를 생성하는 변경 불가능한 자료형

- range 표현
    - range(n)
        - 0부터 n-1까지의 숫자의 시퀀스
    - range(n, m)
        - n부터 m-1까지의 숫자 시퀀스
        - ex)   
    my_range_1 = range(5)   
    my_range_2 = range(1, 10)   
       
       &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;print(my_range_1) => range(0, 5)  
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;print(my_range_2) => range(1, 10)   
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;print(list(my_range_1)) => [0, 1, 2, 3, 4]   
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;print(list(my_range_2)) => [1, 2, 3, 4, 5, 6, 7, 8, 9]
    - 주로 반복문과 함께 사용 예정

## Non_sequence Types
>dict

*key - value*  쌍으로 이루어진 *순서와 중복*이 없는 *변경 가능*한 자료형

- dictionary 표현
    1. key는 변경 불가능한 자료형만 사용 가능(str, int, float, tuple, range ....)
    2. value는 모든 자료형 사용 가능
    3. 중괄호({})로 표기
- ex)   
my_dict_1 = {}   
my_dict_2 = {'key' : 'value'}  
my_dict_3 = {'apple' : 12, 'list' : [1, 2, 3]}   
   
   print(my_dict_1) =>{}   
   print(my_dict_2) =>{'key' : 'value'}   
   print(my_dict_3) =>{'apple': 12, 'list': [1, 2, 3]}   
- ex2) key를 통해 value에 접근   
my_dict = {'apple' : 12, 'list' : [1, 2, 3]}   
   
   print(my_dict['apple']) => 12   
   print(my_dict['list']) => [1, 2, 3]   
      
    #값 변경   
    my_ dict['apple'] = 100   
    print(my_dict) => {'apple' : 100, 'list' : [1, 2, 3]}   
- ex3) dict는 중복이 안된다   
my_dict = {'apple' : 12, 'list' : [1, 2, 3], 'apple' : 100}   
   
   print(my_dict) => {'apple' : 100, 'list' : [1,2,3]} : key가 중복이 안되기 때문에 똑같이 넣으면 마지막에 넣은 값으로 갱신된다.
> set

순서와 중복이 없는 변경 가능한 자료형
- 세트 표현
    - 수학에서의 집합과 동일한 연산 처리 가능
    - 중괄호({})로 표기
- ex)   
my_set_1 = set()  =====> 중요 : dict와 표현이 같아서 이렇게 선언해줘야함   
my_set_2 = {1, 2, 3}   
my_set_3 = {1, 1, 1}   
   
   print(my_set_1) => set()   
   print(my_set_2) => {1, 2, 3}   
   print(my_set_3) => {1}
- ex2) 세트의 집합 연산   
my_set_1 = {1, 2, 3}   
my_set_2 = {3, 6, 9}   
   
   #합집합   
   print(my_set_1 | my_set_2) => {1, 2, 3, 6, 9}   
      
   #차집합   
   print(my_set_1 - my_set_2) => {1, 2}   
      
   #교집합  
   print(my_set_1 & my_set_2) => {3}   
> None

파이썬에서 '값이 없음'을 표현하는 자료형
- None 표현
    - variable = None   
       
       print(variable) => None
>Boolean

참(True)과 거짓(False)을 표현하는 자료형
- 불리언 표현
    - 비교 / 논리 연산의 평가 결과로 사용됨
    - 주로 조건 / 반복문과 함께 사용   
    bool_1 = True   
    bool_2 = False   
       
       print(bool_1) => True   
       print(bool_2) => False   
       print(3 > 1) => True   
       print('3' != 3) => True (!=not)
## Collection
여러 개의 항목 또는 요소를 담는 자료 구조 (str, list, tuple, set, dict)

|컬렉션|변경 가능 여부|순서 여부|
|:---:|:---:|:---:|
|str|X|O|
|list|O|O|
|tuple|X|O|
|set|O|X|
|dict|O|X|

순서여부 O = 시퀀스   
순서여부 X = 비시퀀스

## 타입 변환 Type Conversion
>암시적 형변환

파이썬이 자동으로 형변환을 하는 것

- 암시적 형변환 예시
    - Boolean과 Numeric Type에서만 가능   
    print(3 + 5.0) => 8.0 (int + float = float)   
    print(True + 3) => 4 (Boolean + Numeric = Numeric)   
    print(True + False) => 1 (True = 1, False = 0)

>명시적 형변환

개발자가 직접 형변환을 하는 것 암시적 형변환이 아닌 경우를 모두 포함

- 명시적 형변환 예시
    - str -> integer : 형식메 맞는 숫자만 가능
    - integer -> str : 모두 가능
- ex)   
print(int('1')) -> 1   
print(str(1) + '등') -> 1등   
print(float('3.5')) -> 3.5   
print(int(3.5)) -> 3   
   
   #ValueError : invalid literal ...   
   print(int('3.5'))

## 연산자
> 산술 연산자

|기호|연산자|
|:---:|:---:|
|-|음수 부호|
|+|덧셈|
|-|뺄셈|
|*|곱셈|
|/|나눗셈|
|//|정수 나눗셈 (몫)|
|%|나머지|
|**|지수 (거듭제곱)|

> 복합 연산자

- 연산과 할당이 함께 이뤄짐

|기호|예시|의미|
|:---:|:---:|:---:|
|+=|a += b|a = a + b|
|-=|a -= b|a = a - b|
|*=|a *= b|a = a * b|
|/=|a /= b|a = a / b|
|//=|a //= b|a = a // b|
|%=|a %= b|a = a % b|
|**=|a **= b|a = a ** b|

```python
y = 10
y -= 4
print(y) # 6

z = 7
z *= 2
print(z) ```
> 비교 연산자

|기호|내용|
|:---:|:---:|
|<|미만|
|<=|이하|
|>|초과|
|>=|이상|
|==|같음(a=b : 할당)|
|!=|같지 않음|
|is|같음|
|is not|같지 않음|

- is 비교 연산자
    - 메모리 내에서 같은 객체를 참조하는지 확인
    - ==는 동등성(equality), is는 식별성(identity)
    - 값을 비교하는 == 와 다름
    - 3 == 3.0 : True   
    3 is 3.0 : False
        - is 연산자는 레퍼런스(주소)를 비교하기 때문에 같지 않다. 되도록이면 None, True, False 등을 비교할 때 사용.
- ex)   
print(1 == True) -> True   
print(1 is True) -> False

>논리 연산자

|기호|연산자|내용|
|:---:|:---:|:---:|
|and|논리곱|두 피연산자 모두 True인 경우에만 전체 표현식을 True로 평가|
|or|논리합|두 피연산자 중 하나라도 True인 경우 전체 표현식을 True로 평가|
|not|논리부정|단일 피연산자를 부정|

- 비교 연산자와 함께 사용 가능
```python
num = 15
result = (num > 10) and (num % 2 == 0)
print(result) # False
# 10이상인 짝수 구하기
```

```python
name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result) # True
```

> 단축 평가

- 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

```python
vowels = 'aeiou'

print(('a' and 'b') in vowels) # False : in -> a and b 평가후에 작동한다. a and b = b
print(('b' and 'a') in vowels) # True

print(3 and 5) # 5/True -> and 연산자는 False가 나올때까지 실행한다.
print(3 and 0) # 0/False
print(0 and 3) # 0/False
print(0 and 0) # 0/False

print(5 or 3) # 5/True -> or연산자는 True가 나올때까지 실행한다.
print(3 or 0) # 3/True
print(0 or 3) # 3/True
print(0 or 0) # 0/False
```

- 단축평가 이유
    - 코드 실행을 최적화하고, 불필요한 연산을 피할 수 있도록 함

>멤버십 연산자
- 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인

|기호|내용|
|:---:|:---:|
|in|왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지를 확인|
|not in|왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인|

```python
word = 'hello'
numbers = [1, 2, 3, 4, 5]

print('h' in word) # True
print('z' in word) # False

print(4 not in numbers) # False
print(6 not in numbers) # True
```
>시퀀스형 연산자
- +와 * 는 시퀀스 간 연산에서 산술 연산자일때와 다른 역할을 가짐

|연산자|내용|
|:---:|:---:|
|+|결합 연산자|
|*|반복 연산자|

```python
# Gildong Hong
print('Gildong' + 'Hong')

# hihihihihi
print('hi' * 5)

# [1, 2, 'a', 'b']
print([1, 2] + ['a', 'b'])

# [1, 2, 1, 2]
print([1,2] * 2)
```

- 연산자 우선순위 정리

|우선순위|연산자|내용|
|:---:|:---:|:---:|
|높음|()|소괄호 grouping|
||[]|인덱싱,슬라이싱|
||**|거듭제곱|
||+, -|단항 연산자 양수/음수|
||*, /, //, %|산술 연산자|
||+, -|산술 연산자|
||<, <=, >, >=, ==, !=|비교 연산자|
||is, is not|객체 비교|
||in, not in|멤버십 연산자|
||not|논리 부정|
||and|논리 AND|
|낮음|or|논리 OR|

