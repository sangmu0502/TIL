"""
삼성시에 있는 5000개의 버스 정류장은 관리의 편의를 위해 1에서 5000까지 번호가 붙어 있다.
그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고, Bi이하인 모든 정류장만을 다니는 버스 노선이다.
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.
[입력]
첫 번째 줄에서 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 1 <= N <= 500 이 주어진다
다음 N개의 줄의 i번째 줄에는 두 정수 Ai,Bi (1 <= A <= B <= 5000)가 공백 하나로 구분되어 주어진다
다음 줄에는 하나의 정수 P 1 <= P <= 500가 주어진다.
다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj 1 <= Cj <= 5000 이 주어진다.
[출력]
각 테스트 케이스마다 '#x'를 출력하고 한 칸을 띄운 후, 한 줄에 P개의 정수를 공백 하나로 구분하여 출력한다.
j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수여야 한다.
"""

t = int(input())
for test_case in range(1, t + 1):
    bus_route = int(input())
    bus_station = [0] * 5001
    count = 0
    for i in range(bus_route):
        bus_start, bus_stop = map(int, input().split())
        for j in range(bus_start, bus_stop + 1):
            bus_station[j] += 1

    station_each = int(input())

    station_num = [int(input()) for _ in range(station_each)]
    print(f'#{test_case}', end=' ')
    for i in station_num:
        print(bus_station[i], end=' ')
    print()



