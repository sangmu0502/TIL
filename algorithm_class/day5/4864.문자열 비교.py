t = int(input())

for test_case in range(1, t+1):
    str1 = input()
    str2 = input()
    result = 0
    # 문자열이 str2안에 존재한다면 result 바뀜
    if str1 in str2:
        result = 1
    print(f"#{test_case} {result}")