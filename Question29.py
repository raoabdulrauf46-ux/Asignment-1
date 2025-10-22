def prime_factors(num):
    factor = 2
    while num > 1:
        if num % factor == 0:
            print(factor)
            num //= factor
        else:
            factor += 1

n = int(input("Enter a number: "))
print("Prime factors:")
prime_factors(n)