N = int(input("원금을 입력하세요(원). "))
M = int(input("금리를 입력하세요(%). "))

print("원금 ", N, "원 금리 ", M, "% 입니다.", sep="")

print ("기간    합계")

for i in range(1, 21):
    N = N + N * (M / 100)
    print(i, "년    ", round(N, 1), sep="")