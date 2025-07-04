def ancient_sort(length):
    arr = input().split(' ')
    for i in range(length):
        swapped = False
        for j in range(length-1):
            a, b = int(arr[j]), int(arr[j+1])
            r_a, r_b = a%2, b%2
            if (a > b) and ((r_a==0 and r_b==0) or (r_a==1 and r_b==1)):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped==False:
            break
    print(*arr)# here * is unpacking the array and it passes the element to pirnt() as separate arguments
                # like print('1', '2', '3')

                # it is the short form of this:
                # let a = [1,2,3,4]
                # for i in a:
                #    print(i, end=' ')

ancient_sort(int(input()))

