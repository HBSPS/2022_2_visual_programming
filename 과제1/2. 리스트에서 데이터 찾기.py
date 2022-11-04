arr = ['흑석동', '사당동', '상도동', '노량진동', '규동']

while 1:
    N = input("동을 입력하세요(프로그램 종료를 원한다면 0을 입력하세요): ")
    if N == '0':
        break
    elif N in arr:
        print(arr.index(N) + 1, "번째 동입니다.", sep="")
    else:
        print("새로운 동명입니다. ", len(arr) + 1, "번째 동으로 등록합니다.", sep="")
        arr.append(N)