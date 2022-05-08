def r_file(filename):#讀取檔案
    print('讀取檔案開始')
    contents = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for c in f:
            contents.append(c.strip())
    print('_讀取檔案結束')
    return contents

def decide_name(contents, names, re_contents):
    print('開始重寫')
    name = ''
    for c in contents:
        if c in names:
            name = c
        else:
            re_contents.append(name + ':' + c)
    print('_重寫結束')
    return re_contents

def count_pics(re_contents):
    pic = 0
    stamp = 0
    allen_word_count = 0
    viki_word_count = 0
    for c in re_contents:
        if c[2] == '圖片':
            pic = pic + 1
        elif c[2] == '貼圖':
            stamp = stamp + 1
        elif c[1] == 'Allen':
            allen_word_count += len(c[2])
        elif c[1] == 'Viki':
            viki_word_count += len(c[2])
    print('共有', pic, '張圖片與', stamp, '張貼圖')
    print('Allen一共說了', allen_word_count, '字')
    print('Viki一共說了', viki_word_count, '字')

def contents_print(re_contents): #把contents逐條印出
    print('開始逐條印出')
    for c in re_contents:
        print(c)
    print('_結束逐條印出')

def w_file(filename, re_contents):
    print('開始儲存檔案')
    with open(filename, 'w')as f:
        for c in re_contents:
            f.write(str(c) + '\n')
    print('_儲存檔案結束')

def split_contents(contents, re_contents):
    print('開始表格化檔案')
    for c in contents:
        s = c.split(' ',2)
        time = s[0]
        name = s[1]
        content = s[2]
        re_contents.append([time, name, content])
    print('_結束表格化檔案')
    return re_contents

def exercise1():
    filename = 'exercise1_input.txt'
    names = ['Allen', 'Tom']
    re_contents = []
    contents = r_file(filename)
    decide_name(contents, names, re_contents)
    contents_print(re_contents)
    w_file('re_' + filename, re_contents)

def exercise2():
    filename = 'exercise2_input.txt'
    re_contents = []
    contents = r_file(filename)
    re_contents = split_contents(contents, re_contents)
    count_pics(re_contents)
    while True:
        print_choose = input('是否需要檢視檔案 y/n?')
        if print_choose == 'y':
            contents_print(re_contents)
            break
        elif print_choose == 'n':
            break
        else:
            print('請重新輸入')
            continue
    w_file('re_' + 'exercise2_input.csv', re_contents)

def main():
    print('1.FB紀錄重整')
    print('2.Line對話紀錄清單化')
    choose_program = input('請輸入練習程式別')
    if choose_program == '1':
        exercise1()
    elif choose_program == '2':
        exercise2()
    else:
        print('無輸入有效程式，退出程式')


##################

main()
