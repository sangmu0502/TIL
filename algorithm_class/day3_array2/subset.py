N = 5
arr = [1, 2, 3, 4, 5]

for i in range(1 << N):     # 2의 N 제곱
    for j in range(N):
        if i & (i << j):
            print(arr[j], end=' ')
    print()