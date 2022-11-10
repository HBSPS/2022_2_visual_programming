import random
import datetime as dt

f = open('dict_test_utf8.TXT', 'r')
words = f.readlines()

wordsArr = []

for word in words:
    try:
        tmp = word.replace('\n', '').split(' : ')
        english = tmp[0]
    except:
        continue

    wordsArr.append(english)

totalScore = 0

print('게임을 시작합니다.')
for i in range(10):
    randomNumber = random.randint(7, 10)

    wordList = random.sample(wordsArr, randomNumber)

    word = ' '.join(map(str, wordList))

    print('(%d/10) 다음을 입력하세요' % (i + 1))
    print('=',word)
    before = dt.datetime.now()
    userInput = input('= ')
    after = dt.datetime.now()
    
    seconds = (after - before).seconds
    microseconds = (after - before).microseconds

    time = str(seconds) + '.' + str(microseconds)
    time = float(time)

    score = int((20 - time) * 1000)

    speed = int(len(word) * (60 // time)) # 분당 타자수를 정수형으로 표현하기 위한 것

    wrongIndex = -1

    for j in range(0, len(word)):
        if word[j] != userInput[j]:
            wrongIndex = j
            break
    
    if wrongIndex != -1:
        print('  ' + ' ' * wrongIndex + '^')
        print('틀렸습니다. (%d타/분)' % speed)
    else:
        print('맞았습니다. (%d점 획득 %d타/분)' % (score, speed))
        totalScore += score

print('당신의 점수는 %d점 입니다.' % totalScore)