# -*- coding: UTF-8 -*-
#テスト

def main():
    a = [1, 2, 3]
    for i in a:
        print(i)

    d = {
    'hoge': 1,
    'fuga': 2,
    'hoga': 3,
    }
    for k,v in d.items():
        print(k + ': ' + str(v + 1))
    pass

if __name__ == '__main__':
    main()
