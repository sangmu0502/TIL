N = int(input())
num_list = list(map(int, input().split()))
compare_num = 0
result = 0

for i in range(N):
    count_up = 0
    count_down = 0
    compare_num = num_list[i]
    for j in range(N):
        if compare_num < num_list[j]:
            count_up += 1
        if compare_num > num_list[j]:
            count_down += 1
    if count_up == count_down:
        result = compare_num

print(result)