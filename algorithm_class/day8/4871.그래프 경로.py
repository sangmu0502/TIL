def DFS(start, end): # DFS 함수를 만드는데 시작과 끝을 인자로 받기
    stack = []         # 빈 스택 생성
    visited = [False] * (V + 1)  # 경로에 있는지 없는지 확인
    stack.append(start)    # start 인수를 스택에 추가

    while stack:
        now = stack.pop()    # stack을 pop으로 꺼내 현재값 지정
        visited[now] = True
        for i in range(1, V+1):  # 1부터 V까지의 숫자까지(V는 가장 큰 숫자)
            if not visited[i] and node[now][i]:  # 만약 i번째에 방문하지 않고 연결되어있다면
                stack.append(i)  # 경로로 될 수 있으므로 stack에 추가해준다.

    if visited[end]:  # 만약 끝점을 갔었다면
        return 1
    else:
        return 0


t = int(input())


for test_case in range(1, t + 1):
    V, E = map(int, input().split())  # V는 가장큰 숫자, E는 경로의 수
    node = [[0 for i in range(V + 1)] for j in range(V + 1)]  # V + 1 = 숫자들 넣어주려고 인덱스 편하게 + 1 해줌

    for _ in range(E):
        node_start, node_end = map(int, input().split())
        node[node_start][node_end] = 1

    start, end = map(int, input().split())
    print(f"#{test_case} {DFS(start, end)}")