while 1:
    N = list(input("수? "))

    if N[0] == '0':
        break

    answer = 0

    for i in range(len(N) // 2):
        if N[i] != N[-1-i]:
            answer = 1
            break
        
    if answer == 1:
        print("대칭수가 아닙니다.")
    else:
        print("대칭수 입니다.")