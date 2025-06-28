def even_odd(i):
    for j in range(i):
        inp = int(input())
        if inp%2 == 0:
            print(f"{inp} is an Even number.")
        else:
            print(f"{inp} is an Odd number.")

num_inp = int(input())
even_odd(num_inp)