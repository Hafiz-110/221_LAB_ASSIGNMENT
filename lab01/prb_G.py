import sys
input = sys.stdin.readline

def again_sort(ln):
    idd = input().split(' '); mark = input().split(' ')
    swaps = 0
    for i in range(ln-1):
        flag = False; max_i = i
        for j in range(i+1,ln):
            if int(mark[max_i])<int(mark[j]):
                max_i = j; flag = True
            elif (int(mark[max_i])==int(mark[j])) and (int(idd[max_i])>int(idd[j])):
                max_i = j; flag = True
        #swap
        mark[i], mark[max_i] = mark[max_i], mark[i]
        idd[i], idd[max_i] = idd[max_i], idd[i]
        if flag: swaps += 1
    print(f'Minimum swaps: {swaps}')
    for i in range(ln):
        print(f'ID: {int(idd[i])} Mark: {int(mark[i])}')

again_sort(int(input()))
