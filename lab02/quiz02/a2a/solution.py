import sys
input = sys.stdin.readline

def find_position(test):
    for i in range(test):
        length, target = map(int, input().split())
        arr = list(map(int, input().split()))
        i, j = 0, len(arr)-1
        flag = False
        while i<j:
            summ = arr[i]+arr[j]
            if  summ == target:
                flag = True; break
            elif summ < target: i += 1
            else: j -= 1
        if flag: print(f'{i+1} {j+1}')
        else: print('-1')
        
test = int(input())
find_position(test)



exit(0)
