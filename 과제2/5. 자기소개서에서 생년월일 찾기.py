"""
제 이름은 홍길동이고 2001년 10월 16일에 태어났습니다. -> 33자
안녕하세요 홍길동입니다. 2001/10/06이 제 생년월일 입니다. -> 37자
홍길동입니다. 생년월일은 20011006입니다. -> 26자
"""
birth = input("문장을 입력하세요: ")

if len(birth) > 35:
    print(birth[14:24])
elif len(birth) < 35 and len(birth) > 30:
    if birth[23] == "일":
        date = "0" + birth[22]
    else:
        date = birth[22:24]

    print(birth[12:16], "/", birth[18:20], "/", date, sep="")
else:
    print(birth[14:18], "/", birth[18:20], "/", birth[20:22], sep="")