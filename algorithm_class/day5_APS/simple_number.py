t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    little_num = [2, 3, 5, 7, 11]
    little_num_list = [0] * 5
    index = 0

    for i in little_num:
        count = 0
        while n % i == 0:
            n = n//i
            count += 1
        little_num_list[index] = count
        index += 1

    print(f'#{test_case}', *little_num_list)