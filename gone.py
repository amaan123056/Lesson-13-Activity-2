def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiplication(P,Q):
    return P*Q
def division(P,Q):
    return P/Q
print("Please select your operation")
print("a.add")
print("b.subtract")
print("c.multiplication")
print("d.division")
choice=input("Please enter your choice a/b/c/d")
num_1 =int(input("PleASE enter first no.1"))
num_2 =int(input("PleASE enter first no.2"))
if choice=="a":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=="b":
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif choice=="c":
    print(num_1,"*",num_2,"=",multiplication(num_1,num_2))
elif choice=="d":
    print(num_1,"/",num_2,"=",division(num_1,num_2))
else:
    print("Invalid input")