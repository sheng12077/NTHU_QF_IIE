def id_check(pid):
    code1_table = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,
        'J':18,'K':19,'L':20,'M':21,'N':22,'P':23,'Q':24,'R':25,
        'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33,'I':34,'O':35}

    code1County = ['台北市','台中市','基隆市','台南市','高雄市','新北市','宜蘭縣','桃園市'
                  ,'新竹縣','苗栗縣','台中縣','南投縣','彰化縣','雲林縣','嘉義縣','台南縣','高雄縣'
                  ,'屏東縣','花蓮縣','台東縣','金門縣','澎湖縣','陽明山管理局','連江縣','嘉義市','新竹市']

    cnt = 0
    cnt += int(code1_table[pid[0]]//10*1 + code1_table[pid[0]]%10*9)
    for i in range(1,9):
        cnt += int(pid[i])*(9-i)
    cnt += int(pid[9])

    gender = '男性' if pid[1] == '1' else '女性'

    if cnt %10 != 0:
        print(f'錯誤, 身份證號檢查總和為{cnt}')
    else:
        print(f'正確, {code1County[code1_table[pid[0]]-10]}{gender}身份證號檢查總和為{cnt}')

def test():
    pid = input()
    id_check(pid)
test()
