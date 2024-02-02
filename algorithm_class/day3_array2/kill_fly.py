"""
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
아래는 N = 5의 예이다.
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
M x M 크기의 파리채를 한 번 내려쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!
[제약 사항]
1. N은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
"""
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    fly_map = [list(map(int, input().split())) for _ in range(n)]
    fly_sum = 0
    for a in range(n - m + 1):
        for b in range(n - m + 1):
            fly_kill = 0
            for c in range(m):
                for d in range(m):
                    fly_kill += fly_map[a + c][b + d]
                    if fly_sum <= fly_kill:
                        fly_sum = fly_kill

    print(f'#{test_case} {fly_sum}')




