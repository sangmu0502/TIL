t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    for i in range(n-1):
        compare = i
        for j in range(i+1, n):
            if num_list[compare] > num_list[j]:
                compare = j
        num_list[compare], num_list[i] = num_list[i], num_list[compare]

    print(f'#{test_case}', *num_list)