arr = ["apple"]

score = 0

for _ in range(10):
    user_input = input("단어(%s): " %arr[-1])

    last_word = arr[-1]
    if user_input in arr:
        score -= 1
        print("이미 나온 단어입니다. 1점 차감. 현재 점수 %d점" %score)
    elif len(user_input) > 6 or len(user_input) < 3:
        score -= 1
        print("단어의 길이는 3 ~ 6글자 사이로 입력해주세요. 1점 차감. 현재 점수 %d점" %score)
    elif user_input[0] != last_word[-1]:
        score -= 1
        print("끝말잇기가 안됩니다. 1점 차감. 현재 점수 %d점" %score)
    else:
        arr.append(user_input)
        score += 1
        print("1점 획득. 현재 점수 %d점" %score)