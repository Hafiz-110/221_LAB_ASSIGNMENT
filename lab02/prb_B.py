import sys
input = sys.stdin.readline

def sum_revisit(arr1, arr2, target, len1, len2):
    if len1==1 and len2==1: return '1 1'
    else:
        i, j = 0, len2-1
        mini = abs(arr1[i]+arr2[j]-target); pair = (i+1, j+1)
        while i!=len1 and j>=0:
            diff = abs(arr1[i]+arr2[j]-target)
            if diff == 0: return f'{i+1} {j+1}'
            else:               
                if mini>diff:
                    mini = diff; pair = (i+1, j+1)
                
                if arr1[i]+arr2[j]>target: j -= 1
                elif arr1[i]+arr2[j]<target: i += 1
        return f'{pair[0]} {pair[1]}'
            
len1, len2, target = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(sum_revisit(arr1, arr2, target, len1, len2))
