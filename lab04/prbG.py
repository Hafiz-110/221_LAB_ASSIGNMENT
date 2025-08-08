import sys
input = sys.stdin.readline

def knight_attacks_knight(n, m, k):
    b = [[0]*m for i in range(n)]
    p = []
    for i in range(k):
        given = list(map(int, input().split()))
        given[0] -= 1; given[1] -= 1
        p.append(given)

    p_set = set(tuple(i) for i in p)    # to fix the time limit error issue

    for i in range(k):
        x, y = p[i]
        move_combo = [[x-2, y-1], [x-1, y-2],
                      [x-2, y+1], [x-1, y+2],
                      [x+1, y-2], [x+2, y-1],
                      [x+1, y+2], [x+2, y+1]
        ]
        for j in move_combo:
            if 0<=j[0]<=n-1 and 0<=j[1]<=m-1:
                if tuple(j) in p_set: return f'YES'

    return f'NO'

n, m, k = list(map(int, input().split()))
print(knight_attacks_knight(n, m, k))
