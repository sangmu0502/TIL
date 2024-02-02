# 알고리즘 array2

## 2차원 배열 
- 1차원 list를 묶어놓은 list
- 2차원 이상의 다차원 list는 차원에 따라 index를 선언
- 2차원 list의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

> arr = [[0, 1, 2, 3], [4, 5, 6, 7]] (2행 4열의 2차원 list)
```python
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
"""
3
1 2 3
4 5 6
7 8 9
"""
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
"""
3
123
456
789
"""
arr = [[0] * N for _ in range(N)] # 이것도 가능
arr = [[0] * N] * N # 은 얕은 복사가 되므로 X
```
### 배열 순회
- N x M 배열의 N * M 개의 모든 원소를 빠짐없이 조사하는 방법

### 행 우선 순회
```python
# col 행의 좌표
# row 열의 좌표
for col in range(n):
    for row in range(m):
        f(array[col][row]) # 필요한 연산 수행
```

### 열 우선 순회
```python
# col 행의 좌표
# row 열의 좌표
for row in range(n):
    for col in range(m):
        f(array[col][row]) # 필요한 연산 수행
```

### 지그재그 순회
```python
# col 행의 좌표
# row 열의 좌표
# 가로길이 = m 세로길이 = n
for col in range(n):
    for row in range(m):
        f(array[col][row + (m-1 - 2*row)*(col % 2)])
```

### 델타를 이용한 2차 배열 탐색
- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
- 인덱스(x, y)인 칸의 상하좌우 칸(nx, ny)
```python
arr = [[0] * N for _ in range(N)]
x, y = 1, 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<= nx <N and 0 <= ny <N
        print(nx, ny)
```
### 전치 행렬
```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

### 부분 집합
- 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2**n개이다.
- 이는 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같다.
```python
bit = [0, 1, 2, 3]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit)
```