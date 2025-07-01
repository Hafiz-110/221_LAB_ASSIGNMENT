def fast_sum(test):
    for i in range(test):
        n = int(input())
        summ = n*(n+1)/2
        print(int(summ))

test = int(input())
fast_sum(test)