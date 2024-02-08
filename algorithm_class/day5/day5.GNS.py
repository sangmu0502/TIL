t = int(input())

for test_case in range(1, t + 1):
    case, num_each = map(str, input().split())
    test_num_list = list(map(str, input().split()))

    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_each_list = [0] * 10

    for i in test_num_list:
        for j in range(10):
            if i == num_list[j]:
                num_each_list[j] += 1

    print(f'{case}')
    for i in range(10):
        print(f'{num_list[i]} ' * num_each_list[i], end='')

    print()

