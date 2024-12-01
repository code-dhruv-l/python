studnm=input("Enter Student Name:");
clg=input("Enter College Name:");
sem=input("Enter Semester:");
j2ee=int(input("Enter J2EE Marks:"));
py=int(input("Enter Python Marks:"));
cs=int(input("Enter Cyber Security Marks:"));
total=j2ee+py+cs;
per=total/3;

if per>70:
    cls="didtinction";
elif per<70 and per>60:
    cls="First Class";
elif per<60 and per>50:
    cls="Second Class";
elif per<50 and per>33:
    cls="Third Class";
else :
    cls="Fail";

print("Result");
print("Student Name:",studnm);
print("College Name:",clg);
print("Semester:",sem);
print("J2EE Marks:",j2ee);
print("Python Marks:",py);
print("Cyber Security Marks:",cs);
print("Total is:",total);
print("Percentage is:",per);
