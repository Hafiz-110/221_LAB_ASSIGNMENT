import sys
input = sys.stdin.readline

def again_sort(length):
    idd = input().split(); mark = input().split()
    swaps = 0; 
    for i in range(length-1):
        max_i = i; flag = True
        for j in range(i+1, length):
            if int(mark[max_i])<int(mark[j]):
                max_i = j; flag = False
            elif int(mark[max_i])==int(mark[j]):
                if int(idd[max_i])>int(idd[j]):
                    max_i = j; flag = False
        # swap
        mark[i], mark[max_i] = mark[max_i], mark[i]
        idd[i], idd[max_i] = idd[max_i], idd[i]
        
        if flag == False: swaps += 1; 
            
    print(f'Minimum swaps: {swaps}')
    for i in range(length):
        print(f'ID: {idd[i]} Mark: {mark[i]}')

again_sort(int(input()))