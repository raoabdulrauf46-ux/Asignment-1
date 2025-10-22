rows = int(input("How many rows do you want? "))
cols = int(input("How many columns do you want? "))
Array = []
for i in range(0, rows):
    row = []
    for k in range(0, cols):
        row.append(i * k)
    Array.append(row)

print(Array)3
