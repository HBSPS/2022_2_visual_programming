import sys

N = int(input("N을 입력하세요: "))
M = int(input("M을 입력하세요: "))

if N > 9 or M > 9 or N < 2 or M < 2:
    print("N과 M은 2와 9사이의 숫자를 입력해주세요.")
    sys.exit()
if M < N:
    print("N은 M보다 작거나 같은 수를 입력해주세요.")
    sys.exit()
if M-N > 3:
    print("M과 N의 차이는 3을 넘을 수 없습니다.")
    sys.exit()

if M-N == 3: # N과 M에 따라 출력되는 구구단의 단수가 다르므로 공백도 다르게 설정해야 한다
    space = "           "
elif M-N == 2:
    space = "               "
elif M-N == 1:
    space = "                      "
else:    
    space = "                                    "

for i in range(N, M+1):
    print(space, end="")
    print("[", i, "단] ", sep="", end ="")
print(space)

for a in range(2, 10):
    for i in range(N, M+1):
        print(space, end="")
        if i*a < 10:
            tmp = " " # 2X2와 같이 연산의 결과가 한자릿수인 경우 자릿수를 맞추기 위해 공백을 한 칸 넣는다
        else:
            tmp = ""
        print(i, "X", a, "=", i*a, tmp, sep="", end="")
    print(space)