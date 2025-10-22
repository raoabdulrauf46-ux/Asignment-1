age1 = int(input("Enter age of first person : "))
age2 = int(input("Enter age of second person : "))
age3 = int(input("Enter age of third person : "))
age4 = int(input("Enter age of fourth person : "))
youngest = age1
if age2 < youngest:
    youngest = age2
if age3 < youngest:
    youngest = age3
if age4 < youngest:
    youngest = age4
print("The youngest age is:", youngest)
