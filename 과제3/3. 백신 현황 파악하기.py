f = open('owid-covid-data.csv', 'r', encoding='utf-8')
lines = f.readlines()

categories = lines[0].split(',')

'''
for i in range(len(categories)):
    print(i, categories[i])
'''

ISO_CODE = 0
DATE = 3
TOTAL_CASES = 4
NEW_CASES = 5
TOTAL_DEATHS = 7
NEW_DEATHS = 8
TOTAL_VACCINATIONS = 34
NEW_VACCINATIONS = 38

result = {}

for line in lines:
    oneLine = line.split(',')
    nation = oneLine[ISO_CODE]

    if nation == 'KOR':
        result[oneLine[DATE]] = [oneLine[TOTAL_CASES], oneLine[NEW_CASES], oneLine[TOTAL_DEATHS], oneLine[NEW_DEATHS], oneLine[TOTAL_VACCINATIONS], oneLine[NEW_VACCINATIONS]]

dates = list(result.keys())
dates.sort(reverse=True)

newest_date = dates[0]
newest_date_data = result[newest_date]

print("%20s | %20s | %20s | %20s | %20s | %20s | %20s |" % (categories[DATE], categories[TOTAL_CASES], categories[NEW_CASES], categories[TOTAL_DEATHS], categories[NEW_DEATHS], categories[TOTAL_VACCINATIONS], categories[NEW_VACCINATIONS]))
print("%20s | %20s | %20s | %20s | %20s | %20s | %20s |" % (newest_date, int(float(newest_date_data[0])), int(float(newest_date_data[1])), int(float(newest_date_data[2])), int(float(newest_date_data[3])), int(float(newest_date_data[4])), int(float(newest_date_data[5]))))

# float으로 변환 후, int로 변환하는 이유
    # 데이터의 형식이 1234.0의 문자열 형태이므로 바로 int로 바꾸지 못한다.
    # 따라서, 소수점을 나타낼 수 있는 float으로 형변환을 한 뒤 int로 변환해야 오류가 나지 않는다.

f.close()