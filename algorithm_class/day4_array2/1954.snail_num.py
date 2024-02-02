t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    num_list = [[0] * n for _ in range(n)]

    # 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = 0
    y = 0
    i = 0
    count = 1
    num_list[0][0] = 1

    while count < n * n:
        nx = x + dx[i]      # 이동할 곳 출력
        ny = y + dy[i]
        # 이동할 위치가 0보다 작거나 n보다 크거나 (index 여서 = 추가) 이동할 위치의 값이 0이 아니면.
        if nx < 0 or nx >= n or ny < 0 or ny >= n or num_list[nx][ny] != 0:
            i = (i + 1) % 4
            nx = x + dx[i]
            ny = y + dy[i]

        x = nx      # 내 위치 이동
        y = ny
        count += 1
        num_list[nx][ny] = count

    print(f'#{test_case}')
    for index in range(n):
        print(*num_list[index])   # list 없이 값만 출력해줄 때 * 사용 key, value 뽑고 싶을 때는 **