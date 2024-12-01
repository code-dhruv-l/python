a=int(input("Enter a:"));
b=int(input("Enter b:"));
print("Enter 1. for ascending order");
print("Enter 2. for ascending order");

ord=int(input("Enter your choice:"));

if ord==1:
    for i in range(a,b+1):
        print(i);
if ord==2:
    for i in range(b,a-1,-1):
        print(i);
