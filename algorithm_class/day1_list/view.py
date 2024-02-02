# 강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
# 이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.
# 그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
# 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
# [제약 사항]
# 가로 길이는 항상 1000이하로 주어진다.
# 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다.
# 각 빌딩의 높이는 최대 255이다.
# [입력]
# 총 10개의 테스트 케이스가 주어진다
# 각 테스트케이스의 첫 번째 줄에는 건물의 개수 N이 주어진다. (4 <= N <= 1000)
# 그 다음 줄에는 N개의 건물의 높이가 주어진다. (0 <= 건물 높이 <= 255)

for i in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))

    count = 0
    for line in range(2, n - 2):
        max_height = 0
        for max in [buildings[line - 2], buildings[line - 1], buildings[line + 1], buildings[line + 2]]:
            if max >= max_height:
                max_height = max
        if buildings[line] > max_height:
            count += buildings[line] - max_height

    print(f'#{i} {count}') 

