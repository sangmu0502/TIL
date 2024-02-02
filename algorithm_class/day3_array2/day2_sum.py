"""
다음 100 x 100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하여라.
[제약 사항]
총 10개의 테스트 케이스가 주어진다.
배열의 크기는 100x100으로 동일하다.
각 행의 합은 integer 범위를 넘어가지 않는다.
동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.
[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
"""
for test_case in range(1, 11):
    n = int(input())
    num_map = [list(map(int, input().split())) for _ in range(100)]

    col_sum_list = [0] * 100
    row_sum_list = [0] * 100
    dia_sum_list = [0] * 2

    for i in range(100):
        for j in range(100):
            col_sum_list[i] += num_map[j][i]
            row_sum_list[i] += num_map[i][j]
            if i == j:
                dia_sum_list[0] += num_map[i][j]
            if i + j == 99:
                dia_sum_list[1] += num_map[i][99-j]
    compare = 0

    for a in range(100):
        if compare < col_sum_list[a]:
            compare = col_sum_list[a]

    for b in range(100):
        if compare < row_sum_list[b]:
            compare = row_sum_list[b]

    for c in range(2):
        if compare < dia_sum_list[c]:
            compare = dia_sum_list[c]

    print(f'#{test_case} {compare}')