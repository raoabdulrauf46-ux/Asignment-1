def mul_num(values):
    product = 1
    for n in values:
        product *= n
    return product

values = (8,2,3,-1,7)
print("Product is", mul_num(values))