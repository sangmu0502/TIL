
t = int(input())
count = 0

while t > 0:
    t -= 1
    count += 1
    n = list(map(int, input().split()))
    num = list(map(int, input().split()))

    num_list = sorted(num)
    max_num = num_list[-1]
    min_num = num_list[0]

    result = max_num - min_num
    print(f'#{count} {result}')