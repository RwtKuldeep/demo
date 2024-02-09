def greater_num(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# x,y,z = int(input("Enter three numbers :")).split(",")
x = int(input("Enter x :"))
y = int(input("Enter y :"))
z = int(input("Enter z :"))
result = greater_num(x,y,z)
print("greater number is ",result)