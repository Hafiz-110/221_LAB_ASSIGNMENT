import sys
input = sys.stdin.readline

def two_sum_trouble(f_line, arr):
    length, target = int(f_line[0]), int(f_line[1])
    i, j = 0, len(arr)-1

    while i<j:
        if int(arr[i])+int(arr[j]) == target:
            return f'{i+1} {j+1}'
        
        elif int(arr[i])+int(arr[j]) > target: j -= 1
        else: i += 1
    return '-1'


first_line = input().split()
arr = input().split()
print(two_sum_trouble(first_line, arr))
