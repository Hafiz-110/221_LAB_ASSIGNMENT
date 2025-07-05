import sys
input = sys.stdin.readline

def fast_sum(test):
    for i in range(test):
        n = int(input())
        sum = n*(n+1)/2
        print(round(sum, 6))

fast_sum(int(input()))

exit(0)
