a=int(input("Enter A:"));
b=int(input("Enter B:"));
c=int(input("Enter C:"));

if a>b and a>c:
    print(a,"Is Greter than ",b,"And",c);
elif b>c:
    print(b,"Is Greter than",a,"And",c);
else:
    print(c,"Is Greter than",a,"And",b);
   
