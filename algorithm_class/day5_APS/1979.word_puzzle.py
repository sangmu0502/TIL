"""
N x N 크기의 단어 퍼즐을 만드려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

[예제]
N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때 길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로4 4번)이 된다
[제약 사항]
1. N은 5 이상 15 이하의 정수이다
2. K는 2 이상 N 이하의 정수이다.
[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

"""
# t = int(input())
#
# for test_case in range(1, t + 1):
#     n, k = map(int, input().split())
#     puzzle = [list(map(int, input().split())) for _ in range(n)]
#
#     count = 0
#     result = 0
#     for i in range(n):
#         for j in range(n):
#             if puzzle[i][j] == 1:
#                 count += 1
#                 if puzzle[i][j] == 0:
#                     count = 0
#                 elif j < n and count == k and puzzle[i][j+1] == 0:
#                     result += 1
#                     count = 0
#             if puzzle[j][i] == 1:
#                 count += 1
#                 if puzzle[j][i] == 0:
#                     count = 0
#                 elif j < n and count == k and puzzle[j+1][i] == 0:
#                     result += 1
#                     count = 0
#
#     print(f'#{test_case} {result}')

# K = 3
# N = 6
# arr = [0, 1, 0, 1, 1, 1]
# ans = 0
# cnt = 0
# # for i in range(N):
# #     if arr[i]:
# #         cnt += 1
# #     elif arr[i] == 0 or i == N-1:
# for i in range(N):
#     if arr[i] == 0:
#         if cnt == K:
#             ans += 1
#         cnt = 0
#     else:
#         cnt += 1
#         if i == N-1 and cnt == K:
#             ans += 1
# print(ans)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    N += 1

    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f'#{tc} {ans}')