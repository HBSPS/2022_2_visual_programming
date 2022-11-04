phone_dict = {"홍길동": "010-4444-5555", "김중앙": "010-9191-8181", "심청": "010-9191-8181"}

while 1: # 전화번호 추가 후, 검색을 위한 무한 루프 (무한루프가 없을 시, 사용자 추가되면서 프로그램 종료됨)
    name = input("이름(종료를 원하면 0입력)>>")

    if name == "0":
        break

    name_list = list(phone_dict.keys())

    cnt = 0 # 찾는 사용자가 있는지 확인

    if name == "add":
        new_name = input("이름은?")
        new_phone = input("전화번호는?")

        phone_dict[new_name] = new_phone
        print(new_name, "전화번호가 추가되었습니다.")
    else:
        for i in name_list: # 전화번호부 딕셔너리의 이름에 대해
            if name in i: # 사용자가 입력한 값이 각 이름에 포함이 된다면
                name = i
                print(name, phone_dict[name])
                cnt = 0
                break
            else:
                cnt += 1 # 입력을 포함하는 이름이 없다면 cnt를 증가
        
        if cnt > 0: # cnt가 증가되었다면 = 입력을 포함하는 이름이 없다면
            print("찾을 수 없습니다.")