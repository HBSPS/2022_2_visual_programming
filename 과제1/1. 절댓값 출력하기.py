while 1:
    N = int(input("숫자를 입력하세요: "))
    if N == 0:
        break
    elif N < 0:
        print("=>", -N)
    else:
        print("=>", N)