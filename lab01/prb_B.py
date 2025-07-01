def solve_arithmetic(tests):
    for i in range(tests):
        exp = input().split(' ')
        f_value, op, l_value = int(exp[1]), exp[2], int(exp[3])
        if op == '+':
            print(round(f_value+l_value, 6))
        elif op == '-':
            print(round(f_value-l_value, 6))
        elif op == '*':
            print(round(f_value*l_value, 6))
        elif op == '/':
            print(round(f_value/l_value, 6))

tests = int(input())
solve_arithmetic(tests)
