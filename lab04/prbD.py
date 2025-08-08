import sys
input = sys.stdin.readline

def seven_bridges(n, m):    #eulerian path
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))
    d = [0]*(n+1)
    for i in range(m):
        d[n1[i]] += 1; d[n2[i]] += 1

    count = 0
    for i in d:
        if i%2!=0: count +=1    # count = sum(1 for i in d if i%2!=0)

    if count == 0 or count ==2: return f'YES'
    else: return f'NO'


n, m = list(map(int, input().split()))
print(seven_bridges(n, m))
