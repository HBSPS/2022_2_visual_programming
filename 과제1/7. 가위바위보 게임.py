import random

print("가위바위보 게임")

Round = 1
youW = 0
comW = 0
youL = 0
comL = 0
arr= ["가위", "바위", "보"]

while 1:
    print("(라운드 ", Round, ")", sep="")

    comChoice = arr[random.randint(0, 2)]
    print("컴퓨터가 결정했습니다.")

    youChoice = input("무엇을 내시겠습니까? (가위, 바위, 보) ")

    choices = comChoice + youChoice

    if choices == "가위보" or choices == "바위가위" or choices == "보바위":
        result = "컴퓨터가 이겼습니다."
        comW += 1
        youL += 1
    elif choices == "보가위" or choices == "가위바위" or choices == "바위보":
        result = "당신이 이겼습니다."
        youW += 1
        comL += 1
    else:
        result = "비겼습니다. "
    
    print("컴퓨터는 ", comChoice, ", 당신은 ", youChoice, ", " ,result, sep="")

    print("컴퓨터: ", comW, "승 ", comL, "패, 당신: ", youW, "승 ", youL, "패", sep="")
    
    if comW == 3 or youW == 3:
        break

    Round += 1