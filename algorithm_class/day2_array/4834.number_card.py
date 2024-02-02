# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
#
# 해결방안 1 (미완 인덱스의 위치를 특정하지 못함) (성공 !)
t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    data = int(input())
    case_data = [0] * 10
    max_count = 0

    for i in range(n):
        case_data[data % 10] += 1
        data = data // 10

    for case in case_data:
        if case >= max_count:
            max_count = case

    max_num = case_data[0]
    max_index = 1

    for j in range(10):
        if case_data[j] >= max_num:
            max_num = case_data[j]
            max_index = j
    print(f'#{test_case} {max_index} {max_count}')

# 해결방안 2
# t = int(input())

# for test_case in range(1, t+1):
#     n = int(input())
#     num = list(map(int, input()))
#     data = [0] * 10

#     for i in num:
#         data[i] += 1
#     max_num = data[0]
#     max_index = 0

#     for j in range(10):
#         if data[j] >= max_num:
#             max_num = data[j]
#             max_index = j
#     print(f'#{test_case} {max_index} {max_num}')

