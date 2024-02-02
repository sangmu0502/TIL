t = int(input())
for test_case in range(1, t+1):
    num = int(input())
    num_list = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

    for i in range(6):
        num_list[num % 10] += 1
        num //= 10

    i = 0
    tri = run = 0
    while i < 10:
        if num_list[i] >= 3: # triplet 조사 후 데이터 삭제
            num_list[i] -= 3
            tri += 1
            continue
        if num_list[i] >= 1 and num_list[i+1] >= 1 and num_list[i+2] >= 1: # run 조사 후 데이터 삭제
            num_list[i] -= 1
            num_list[i+1] -= 1
            num_list[i+2] -= 1
            run += 1
            continue
        i += 1
    if run and tri:
        print(f'#{test_case} Baby Gin')
    elif run == 1 and tri == 0:
        print(f"#{test_case} run")
    elif tri == 1 and run ==0:
        print(f"#{test_case} triplet")
    else: print(f"#{test_case} Lose")