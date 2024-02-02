"""
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
[입력]
첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과 1로 구성된 수열이 공백없이 제공된다.
1 <= T <= 10, 10 <= N <= 1000
[출력]
#과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
"""

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    num_col = list(map(int, input()))

    count = 0
    result = 0

    for i in num_col:
        if int(i) == 1:
            count += 1
        else:
            count = 0
        if result < count:
            result = count
    print(f'#{test_case} {result}')