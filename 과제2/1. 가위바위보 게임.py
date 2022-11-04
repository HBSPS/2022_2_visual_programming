import random

print("가위바위보 게임")

Round = 1
youW = 0
comW = 0
youL = 0
comL = 0
choice = ("가위", "바위", "보") # 순서대로 0, 1, 2

while 1:
    print("(라운드 ", Round, ")", sep="")

    comChoice = str(random.randint(0, 2))
    print("컴퓨터가 결정했습니다.")

    youChoice = input("무엇을 내시겠습니까? (가위, 바위, 보) ")

    if youChoice not in choice:
        print("다시 입력해주세요")
        continue

    if youChoice == choice[0]:
        youChoice = "0"
    elif youChoice == choice[1]:
        youChoice = "1"
    else:
        youChoice = "2"

    choices = comChoice + youChoice

    if choices == "02" or choices == "10" or choices == "21":
        result = "컴퓨터가 이겼습니다."
        comW += 1
        youL += 1
    elif choices == "20" or choices == "01" or choices == "12":
        result = "당신이 이겼습니다."
        youW += 1
        comL += 1
    else:
        result = "비겼습니다. "
    
    print("컴퓨터는 ", choice[int(comChoice)], ", 당신은 ", choice[int(youChoice)], ", " ,result, sep="")

    print("컴퓨터: ", comW, "승 ", comL, "패, 당신: ", youW, "승 ", youL, "패", sep="")
    
    if comW == 3 or youW == 3:
        break

    Round += 1