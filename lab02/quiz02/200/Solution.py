import sys
input = sys.stdin.readline

def find_int(ln1, ln2, pos, arr1, arr2):
    arr3 = []
    i, j = 0, 0
    while i<ln1 and j<ln2:
        if arr1[i]>=arr2[j]:
            arr3.append(arr2[j]); j += 1
        elif arr1[i]<arr2[j]:
            arr3.append(arr1[i]); i += 1
    
    if i==ln1:
        for k in range(j, ln2):
            arr3.append(arr2[k])
    if j==ln2:
        for m in range(i, ln1):
            arr3.append(arr1[m])

    for n in range(len(arr3)):
        if n == pos-1: return arr3[n]
    return -1
test = int(input())
for i in range(test):
    ln1, ln2, pos = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(find_int(ln1, ln2, pos, arr1, arr2))

exit(0)