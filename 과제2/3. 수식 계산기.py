cal = input("수식을 입력하세요: ")

cal = cal.split("+") # +을 기준으로 우선 문자열을 쪼갠다

total = 0 # 계산 결과

for i in cal: # +를 기준으로 쪼갠 문자열이 들어있는 배열의 요소 i
    i = i.split("-") # 요소를 -로 쪼갠다

    if len(i) > 1: # -로 쪼갠 배열의 길이가 1보다 크다 = 30-21과 같이 -연산이 들어있다면
        total += int(i[0]) # 계산 결과에 -로 쪼갠 문자열이 들어있는 배열의 첫 요소를 더하고
        for j in range(1, len(i)):
            total -= int(i[j]) # 두번째 요소 부터는 -연산을 한다
    else: # -로 쪼갠 배열의 길이가 1이라면 = 30과 같이 -연산이 들어있지 않다면
        total += int(i[0]) # 해당 값을 더한다

print("=", total)