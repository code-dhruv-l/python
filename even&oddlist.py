a=[1,2,3,4,5,6,7,8,9]

print(a)
evenlist=[i for i in a if i%2==0]
oddlist=[i for i in a if i%2!=0]

print("Even List:",evenlist)
print("Odd List:",oddlist)
