import sys
input = sys.stdin.readline

def king_moves(n):
    x, y = list(map(int, input().split())); x-=1; y-=1
    move_combo = [[x-1, y-1], [x-1, y], [x-1, y+1],
                  [x, y-1], [x, y+1],
                  [x+1, y-1], [x+1, y], [x+1, y+1]
                  ] 
    legal_move = []; count = 0
    for i in move_combo:
        if 0<=i[0]<=n-1 and 0<=i[1]<=n-1:
            legal_move.append([i[0]+1, i[1]+1])
            count += 1
    print(count)
    for i in legal_move:
        print(f'{i[0]} {i[1]}')

king_moves(int(input()))
