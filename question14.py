even_count = 0
odd_count = 0
numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total even numbers found:", even_count)
print("Total odd numbers found:", odd_count)