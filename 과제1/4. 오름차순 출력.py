print("데이터를 입력하세요(입력을 마치려면 0을 입력하세요)")

arr = []

while 1:
    N = int(input())

    if N == 0:
        break
    else:
        arr.append(N)

arr.sort()

print("결과: ", end="")
for i in arr:
    print(i, end=" ")
print("(", len(arr), "개)", sep="")