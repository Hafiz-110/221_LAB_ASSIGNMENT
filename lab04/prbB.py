import sys
input = sys.stdin.readline

def adjacency_list(n, m):
    dic = {i+1:[()] for i in range(n)}    # python way to create dic
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))
    w = list(map(int, input().split()))

    for i in range(m):
        if n1[i] not in dic:
            dic[n1[i]] = [(n2[i], w[i])]
        else: dic[n1[i]] +=  [(n2[i], w[i])]

    for k, v in dic.items():
        if v==[()]:
            print(f'{k}:')
        else:
            print(f'{k}:', *v[1:])


n, m = list(map(int, input().split()))
adjacency_list(n, m)