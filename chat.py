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

def contents_print(re_contents):#把contents逐條印出
    print('開始逐條印出')
    for c in re_contents:
        print(c)
    print('_結束逐條印出')

def w_file(filename, re_contents):
    print('開始儲存檔案')
    with open(filename, 'w')as f:
        for c in re_contents:
            f.write(c + '\n')
    print('_儲存檔案結束')

def main():
    filename = 'exercise1_input.txt'
    names = ['Allen', 'Tom']
    re_contents = []
    contents = r_file(filename)
    decide_name(contents, names, re_contents)
    contents_print(re_contents)
    w_file('re_' + filename, re_contents)

##################

main()
