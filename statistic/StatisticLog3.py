# -*- coding:UTF-8 -*-
def countBirths() :
    ret = []
    for y in range(1880 , 2018) :
        count = 0
        fileName = 'names/yob%d.txt'%y
        with open(fileName , 'r') as f :
            data = f.readlines()
            for d in data :
                if d[-1] == '\n' :      # d 의 마지막요소가 개행문자인 경우
                    d = d[:-1]          # 개행문자 제거
                    # print(d)
                count += int(d.split(',')[2])
            ret.append((y , count))
    return ret

result = countBirths()
# print(result)

with open('birth_by_years.csv' , 'w') as w :
    for year , birth in result :
        data = '%s , %s\n' %(year , birth)
        print(data)
        w.write(data)