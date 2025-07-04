import sys
input = sys.stdin.readline

def even_odd(i):
    for j in range(i):
        inp = input()
        if int(inp)%2 == 0:
            print(f"{int(inp)} is an Even number.")
        else:
            print(f"{int(inp)} is an Odd number.")

num_inp = int(input())
even_odd(num_inp)
