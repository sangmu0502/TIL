t = int(input())

for test_case in range(1, t+1):
    k, n, m = map(int, input().split())  # K, N, M
    charge = list(map(int, input().split()))

    station = [0] * (n + 1)
    visited = [0] * (n + 1)

    for i in charge:
        station[i] = 1

    distance = k
    now_bus = k
    result = 0

    while True:
        if now_bus >= n:
            for i in range(n+1):
                result += visited[i]
            break
        elif station[now_bus] == 1:
            distance = k
            visited[now_bus] = 1
            now_bus += k
        elif station[now_bus] == 0:
            now_bus -= 1
            distance -= 1
            if distance == 0:
                result = 0
                break

    print(f'#{test_case} {result}')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    busstop = [0] * (N + 1)
    for x in charger:
        busstop[x] = 1

    bus = 0   # 버스의 현재 위치
    count = 0    # 충전횟수
    while bus + K < N:   # 버스가 종점에 도착하기 전이면
        last = 0
        for i in range(bus + 1, bus + K + 1): # bus => bus + K 사이 마지막 충전기 위치 i 찾기
            if busstop[i]:   # i 정류장에 충전기가 있으면
                last = i
        # 충전기가 없으면
        if last == 0:
            break
        else:   # 충전기가 있으면 (운행할 수 있는 최대 거리)
            bus = last
            count += 1
