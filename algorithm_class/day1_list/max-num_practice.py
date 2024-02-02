t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    result, max, min, max_index, min_index = 0, 0, 11, 0, 0

    for num in range(n):
        if numbers[num] >= max:
            max = numbers[num]
            max_index = num
        if numbers[num] < min:
            min = numbers[num]
            min_index = num

    if max_index > min_index:
        result = max_index - min_index
    elif min_index > max_index:
        result = min_index - max_index

    print(f'#{test_case} {result}')
