# coding:utf-8
with open('cmd.txt', 'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        cmd = line.split(' ')
        i = 0
        while i < len(cmd):
            print(cmd[i] + " ", end='')
            i = i + 1
        print("\n")
