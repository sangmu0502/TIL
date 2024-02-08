t = int(input())

for test_case in range(1, t + 1):
    str1 = input()
    str2 = input()
    str_list = [0] * len(str1)

    max_result = 0
    for i in str1:
        result = 0
        for j in str2:
            if i == j:
                result += 1
        if max_result < result:
            max_result = result

    print(f'#{test_case} {max_result}')
