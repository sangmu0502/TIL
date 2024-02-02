t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    for i in range(n):
        compare = i
        if i % 2 == 1:
            for j in range(i + 1, n):
                if num_list[compare] > num_list[j]:
                    compare = j
            num_list[compare], num_list[i] = num_list[i], num_list[compare]
        else:
            for j in range(i + 1, n):
                if num_list[compare] < num_list[j]:
                    compare = j
            num_list[compare], num_list[i] = num_list[i], num_list[compare]
    print(f'#{test_case}', *num_list[:10])

# def custom_sort(n, num_list):
#     for i in range(n):
#         for j in range(i, n):
#             if (i % 2 == 1 and num_list[i] > num_list[j]) or (i % 2 == 0 and num_list[i] < num_list[j]):
#                 num_list[i], num_list[j] = num_list[j], num_list[i]
#
#     return num_list
#
#
# t = int(input("테스트 케이스의 개수 입력: "))
#
# for test_case in range(1, t + 1):
#     n = int(input())  # 리스트의 길이 입력
#     num_list = list(map(int, input().split()))  # n개의 정수로 이루어진 리스트 입력
#
#     sorted_list = custom_sort(n, num_list)
#
#     print(f'#{test_case}', *sorted_list)
