# 알고리즘
- 알고리즘 : 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다. 주로 컴퓨터 용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
- 간단하게 다시 말하면 어떠한 문제를 해결하기 위한 절차라고 볼 수 있다.
- 예를 들어 1부터 100까지의 합을 구하는 문제를 생각해 보자.
- APS 과정의 목표 중의 하나는 보다 좋은 알고리즘을 이해하고 활용하는 것이다.
- 무엇이 좋은 알고리즘 인가?
    1. 정확성
    2. 작업량
    3. 메모리 사용량
    4. 단순성
    5. 최적성

## 카운팅 정렬(Counting Sort)
- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
- 제한 사항
    - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문.
    - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야한다.
- 시간 복잡도
    - O(n + k) : n은 리스트 길이, k는 정수의 최대값

```python
data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0, 0, 0, 0, 0]
counts_sum = 0

for count in data:
    counts[count] += 1

for num in counts:
    counts_sum += num

print(counts)
print(counts_sum)

N = 6
K = 9
data = [7, 2, 4, 5, 2, 3]
counts = [0] * (K + 1)
temp = [0] * N
# counts 배열에 기록하기
for x in data:
    counts[x] += 1
# counts 누적합 구하기
for i in range(1, K+1):
    counts[i] = counts[i-1] + counts[i]
# data의 마지막 원소부터 정렬하기
for i in range(N-1, -1, -1): # N-1 ㅡ> 0번 인덱스
    counts[data[i]] -= 1 # 개수를 인덱스로 변환(남은 개수 계산)
    temp[counts[data[i]]] = data[i]
print(*temp)

for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)

money = 1300
coin_list = [500, 100, 50, 10]
count = 0
for i in coin_list:
    count += money // i
    money = money % i
print(count)

num = 456999 # Baby Gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run and tri: 
    print("Baby Gin")
elif run == 1 and tri == 0:
    print("run")
elif tri == 1 and run ==0:
    print("triplet")
else: print("Lose")
```
```python
for t in range(int(input())):
    k, n, m = map(int, input().split())
    #: k 이동거리 n: 종점 m: 충전기 설치된 개수
    number = list(map(int, input().split()))

    charge = [0] * (n + 1)  # 충전기 설치
    visited = [0] * (n + 1)

    for i in number:
        charge[i] = 1

    dis = k
    now = k
    while True:
        if now >= n:
            result = sum(visited)
            break
        elif charge[now] == 1:
            dis = k
            visited[now] = 1
            now += k
        elif charge[now] == 0:
            now -= 1
            dis -= 1
            if dis == 0:
                result = 0
                break

    print("#{} {}".format(t + 1, result))
```