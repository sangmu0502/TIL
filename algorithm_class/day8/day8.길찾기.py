def DFS(start, end):
    stack = []
    visited = [False] * 100
    stack.append(start)

    while stack:
        now = stack.pop()
        visited[now] = True
        for i in range(1, 100):
            if not visited[i] and node[now][i]:
                stack.append(i)
    if visited[end]:
        return 1
    else:
        return 0


for test_case in range(1, 11):
    t, E = map(int, input().split())   # t = 테스트케이스 수, E는 경로의 수
    num_array = list(map(int, input().split()))   # 입력된 숫자들
    node = [[0] * 100 for j in range(100)]

    for i in range(E):
        node_start = num_array[i * 2]
        node_end = num_array[(i * 2) + 1]
        node[node_start][node_end] = 1

    print(f'#{test_case} {DFS(0, 99)}')
