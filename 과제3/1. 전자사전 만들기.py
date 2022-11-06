f = open('./과제3/dict_test_utf8.TXT', 'r')
words = f.readlines()

dictionary = {}

for word in words: # 사전을 만드는 과정
    try: # tmp의 원소가 두 개일 때 = 영어와 뜻이 둘 다 제대로 있을 때
        tmp = word.replace('\n', '').split(' : ') # 단어의 맨 마지막에 포함되어있는 개행 문자를 제거하며, ' : '을 기준으로 나누어 tmp에 임시로 저장
        english = tmp[0]
        korean = tmp[1]
    except: # 뜻, 또는 영어 둘 중 하나 이상이 없는 경우
        continue

    dictionary[english] = korean

while (1):
    english = input('(종료를 원한다면 0을 입력)단어? ')
    
    if english == '0':
        break

    try: # 사전에 있는 단어를 입력한다면
        print(english, dictionary[english])
    except: # 사전에 없는 단어를 입력한다면
        print('단어가 사전에 없습니다.')
        continue