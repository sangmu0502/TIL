# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
#
#
# [입력]
#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
#
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
#
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다

# t = int(input())
#
# for i in range(1, t+1):
#     n, m = map(int, input().split())
#     num_list = list(map(int, input().split()))
#
#     min_sum_num = float('inf')
#     max_sum_num = float('-inf')
#
#     for num in range(n - m + 1):
#         sum_num = sum(num_list[num:num+m])
#         max_sum_num = max(max_sum_num, sum_num)
#         min_sum_num = min(min_sum_num, sum_num)
#
#     result = max_sum_num - min_sum_num
#
#     print(f'#{i} {result}')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):

    # input 값 받기!
    N, M = map(int, input().split())
    n_data = list(map(int, input().split()))

    # N개의 data를 M씩 묶을 때 -> N-M+1만큼의 묶음의 수가 생김
    for i in range(N - M + 1):
        default_sum = 0
        for j in range(i, i + M):
            default_sum += n_data[j]
        """
        case 0)
        - i가 0, 즉 처음 받는 값을
        -> 각각 min_sum, max_sum으로 부여해 줌 --> 즉, 비교를 하는데 기준이 되는 값!
        """
        if i == 0:
            min_sum = default_sum
            max_sum = default_sum
        """
        case 1)
        - 만약, default_sum이 min_sum보다 작으면,
        -> default_sum을 min_sum으로 값을 부여함
        """
        if default_sum < min_sum:
            min_sum = default_sum
        """
        case 2)
         - 만약, default_sum이 max_sum 크면,
         -> default_sum을 min_sum으로 값을 부여함
         """
        if default_sum > max_sum:
            max_sum = default_sum

    # print!
    print(f'#{test_case} {max_sum - min_sum}')

