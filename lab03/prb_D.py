import sys
input = sys.stdin.read

MOD = 10**9 + 7

def multiply(A, B):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
    
    return [
        [(a * e + b * g) % MOD, (a * f + b * h) % MOD],
        [(c * e + d * g) % MOD, (c * f + d * h) % MOD]
    ]

def matrix_power(matrix, power):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while power > 0:
        if power % 2 == 1:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        power //= 2
    return result

# Read all input at once and process
data = input().split()
index = 0

T = int(data[index])
index += 1

output = []

for _ in range(T):
    a11 = int(data[index])
    a12 = int(data[index + 1])
    a21 = int(data[index + 2])
    a22 = int(data[index + 3])
    index += 4
    X = int(data[index])
    index += 1

    base = [[a11, a12], [a21, a22]]
    res = matrix_power(base, X)

    output.append(f"{res[0][0]} {res[0][1]}")
    output.append(f"{res[1][0]} {res[1][1]}")

# Print all results at once
sys.stdout.write('\n'.join(output) + '\n')
