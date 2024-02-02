# 한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.
# 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.
# 평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
# 평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려 있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
# 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의한다.
# 가로 길이는 항상 100으로 주어진다.
# 모든 위치에서 상자의 높이는 1 이상 100 이하로 주어진다.
# 덤프 횟수는 1 이상 1000 이하로 주어진다
# 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 ( 주어진 data에 따라 0 또는 1 이 된다)
# [입력] 총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 상자의 높이값이 주어진다
# [출력] 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.

# for test_case in range(1, 11):
#     dump_count = int(input())
#     box_group = list(map(int, input().split()))
#
#     count = 0
#     top_sum = 0
#     for i in box_group:
#         top_sum += i
#
#     box_top = box_group[0]
#     box_low = box_group[0]
#
#     while count < dump_count + 1:
#
#         for i in range(0, 100):
#             if box_top <= box_group[i]:
#                 box_top = box_group[i]
#             elif box_low >= box_group[i]:
#                 box_low = box_group[i]
#
#         if top_sum % 100 == 0:
#             if box_top > box_low:
#                 box_top -= 1
#                 box_low += 1
#                 count += 1
#             elif box_top == box_low:
#                 break
#         else:
#             if box_top > box_low:
#                 box_top -= 1
#                 box_low += 1
#                 count += 1
#             elif box_top - box_low == 1:
#                 break
#
#      print(f'#{test_case} {(box_top - box_low)}')

for test_case in range(1, 11):
    dump_count = int(input())
    box_group = list(map(int, input().split()))

    count = 0
    while count < dump_count:
        max_index = 0
        min_index = 0
        # 최고점과 최저점의 인덱스 찾기
        for i in range(100):
            if box_group[i] > box_group[max_index]:
                max_index = i
            if box_group[i] < box_group[min_index]:
                min_index = i
        # 높이 차이 계산
        diff = box_group[max_index] - box_group[min_index]
        # 이미 최고점과 최저점의 높이 차이가 1 이하일 경우, 더 이상 덤프할 필요 없음
        if diff <= 1:
            break
        # 높이 차이가 1인 경우에는 덤프 후 높이 차이가 최대 1 이내로 유지되도록 처리
        if diff == 2:
            box_group[max_index] -= 1
            box_group[min_index] += 1
        else:
            box_group[max_index] -= 1
            box_group[min_index] += 1

        count += 1

    # 최고점과 최저점의 차이 출력
    # result = max(box_group) - min(box_group)
    max_box_group = 0
    min_box_group = 100

    for tall in range(100):
        if max_box_group <= box_group[tall]:
            max_box_group = box_group[tall]
        elif min_box_group >= box_group[tall]:
            min_box_group = box_group[tall]

    result = max_box_group - min_box_group
    print(f'#{test_case} {result}')
