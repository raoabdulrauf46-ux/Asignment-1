def pascal_triangle(levels):
    from math import factorial
    for n in range(levels):
        for _ in range(1, levels-n):
            print(end=" ")
        for r in range(n+1):
            val = factorial(n) // (factorial(r) * factorial(n-r))
            print(val, end=" ")
        print()

levels = int(input("How many rows do you want? "))
pascal_triangle(levels)
