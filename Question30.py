def decimal_to_binary(value):
    bits = ""
    while value > 0:
        r = value % 2
        bits = str(r) + bits
        value //= 2
    print("Binary:", bits)

num = int(input("Enter decimal value: "))
decimal_to_binary(num)
