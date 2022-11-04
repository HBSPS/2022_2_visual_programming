height = int(input("키(cm)는? "))
weight = int(input("몸무게(kg)는? "))

BMI = weight / ((height / 100) ** 2)

if BMI < 20:
    print("BMI는 ", round(BMI, 2), "로 저체중입니다.", sep="")
elif 20 <= BMI and BMI < 25:
    print("BMI는 ", round(BMI, 2), "로 정상입니다.", sep="")
elif 25 <= BMI and BMI < 30:
    print("BMI는 ", round(BMI, 2), "로 과체중입니다.", sep="")
else:
    print("BMI는 ", round(BMI, 2), "로 비만입니다.", sep="")