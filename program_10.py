a = float(input("Enter measurements of first side :"))
b = float(input("Enter measurements of second side :"))
c = float(input("Enter measurements of third side :"))
if a == b == c :
    print ("This is an equilateral Triangle")
elif a == b or b == c or a == c :
    print ("This is an isoceles triangle")
else :
    print ("This is a scalane triangle")