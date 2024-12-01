a=int(input("Enter number 1:"));
b=int(input("Enter number 2:"));
print(" ");
print("1.Addition");
print("2.Substraction");
print("3.Multiplication");
print("4.Divisiion");

c=int(input("Enter 1,2,3,4 Number to calculate Entered Number:"));

if c==1:
      print("Addition of",a,"And",b,"is",a+b);
elif c==2:
    print("Substraction of",a,"And",b,"is",a-b);
elif c==3:
    print("Multiplication of",a,"And",b,"is",a*b);
elif c==4:
    print("Divisiion of",a,"And",b,"is",a/b);
else:
    print("Invalid Choice");
