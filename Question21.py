def max_of_three_numbers(x, y, z):
    if x>y and x>z:
        print(f"{x} is greatest")
    elif y>x and y>z:
        print(f"{y} is greatest")
    else:
        print(f"{z} is greatest")

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

max_of_three_numbers(x, y, z)