for test_case in range(1, 11):
    length = int(input())
    string_list = [list(input()) for _ in range(8)]
    palindrome_count = 0

    for i in range(8):
        for j in range(8 - length + 1):
            if string_list[i][j:j + length] == string_list[i][j:j + length][::-1]:
                palindrome_count += 1

    for j in range(8):
        for i in range(8 - length + 1):
            column = ''
            for x in range(i, i + length):
                column += string_list[x][j]
            if column == column[::-1]:
                palindrome_count += 1

    print(f'#{test_case} {palindrome_count}')