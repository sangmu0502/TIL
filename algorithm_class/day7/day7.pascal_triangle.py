"""
크기가 N인 파스칼의 삼각형을 만들어야 한다.
파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
N이 4일 경우,
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
[제약 사항]
파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.
[출력]
각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""
# https://docs.python.org/ko/3/library/math.html 에 comb함수 있음.
from math import comb

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []    # 행들의 규칙을 찾아서 저장해 줄 빈 리스트 row 선언
        for j in range(i + 1):  # 열의 개수 = i + 1 개
            row.append(comb(i, j))  # (i + 1)의 행의 규칙은 nCr(수학에서 배운 콤비네이션)과 같다
        triangle.append(row)
    return triangle

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    result = pascal_triangle(n)

    print(f'#{test_case}')
    for row in result:
        print(' '.join(map(str, row)))


n = 4
a = [[0]*i for i in range(1, n + 1)]

print(a)