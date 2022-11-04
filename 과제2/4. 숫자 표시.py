count = ["", "", "이", "삼", "사", "오", "육", "칠", "팔", "구"]

number = int(input("숫자는? "))

if number > 999:
    print(number//1000, ",", number%1000//100, number%100//10, number%10, "원", sep="")
else:
    print(number, "원", sep="")

if number // 10000 != 0:
    print(count[number//10000], "만", sep="", end="")
number = number % 10000
if number // 1000 != 0:
    print(count[number//1000], "천", sep="", end="")
number = number % 1000
if number // 100 != 0:
    print(count[number//100], "백", sep="", end="")
number = number % 100
if number // 10 != 0:
    print(count[number//10], "십", sep="", end="")
number = number % 10
if number == 1:
    print("일원")
elif number == 0:
    print("원")
else:
    print(count[number], "원", sep="")