"""
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.


아래 <그림 2>와 같은 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라 (‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).
"""
# t = int(input())
#
# def turn_left(k):
#     return (k + 3) % 4
#
# def turn_right(k):
#     return (k + 1) % 4
#
# def only_down(k):
#     return k == 1
#
# for test_case in range(1, t + 1):
#
#     ladder_map = [list(map(int, input().split())) for _ in range(100)]
#     new_ladder_map = [[0] * 102 for _ in range(100)]
#     for i in range(100):
#         for j in range(100):
#             new_ladder_map[i][j+1] = ladder_map[i][j]
#     x, y = 0, 0
#     k = 1
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]  # 오른쪽 아래 왼쪽 위
#     start = 0
#     for i in range(1, 101):
#         if new_ladder_map[0][i] == 1:
#             while True:
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#
#                 if new_ladder_map[nx][ny + 1] == 1 and new_ladder_map[nx][ny] == 1 and k == 1:
#                     turn_right(k)
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#
#                 if new_ladder_map[nx][ny - 1] == 1 and new_ladder_map[nx][ny] == 1 and k == 1:
#                     turn_left(k)
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#
#                 if new_ladder_map[nx][ny] == 0 and k == 0:
#                     only_down(k)
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#
#                 x = nx
#                 y = ny
#
#                 if new_ladder_map[nx][ny] == 2:
#                     start = i
#                     break
#
#                 if nx == 100:
#                     break
#
#         print(f'#{test_case} {start}')
for _ in range(1, 11):
    t = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for i in range(100):
        if data[0][i] == 1:   # 시작
            x, y = 0, i
            while x != 99:
                x += 1
                if y > 0 and data[x][y-1] == 1:
                    while y > 0 and data[x][y-1] == 1:
                        y -= 1
                elif y < 99 and data[x][y+1] == 1:
                    while y < 99 and data[x][y+1] == 1:
                        y += 1

            if data[x][y] == 2:
                result = i
                break

    print(f'#{t} {result}')
