def rev_sort(length):
    arr = input().split()
    for k in range(length):
        swapped = False
        for i in range(length-2):
            if int(arr[i]) > int(arr[i+2]):
                arr[i], arr[i+2] = arr[i+2], arr[i]
                swapped = True
        if swapped == False: break

    flag = True
    for j in range(length-1):
        if int(arr[j]) > int(arr[j+1]):
            flag = False; break
    if flag: print('YES')
    else: print('NO')

length = int(input())
rev_sort(length)