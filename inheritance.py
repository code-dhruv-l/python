class father:
    surname="Shah";
    def show(self):
        print("My Surname is",self.surname)

class son1(father):
    def Disp(self):
        print("My name is ankit ",self.surname);

class son2(father):
    def Out(self):
        print("My name is amir ",self.surname);

s1=son1()
s2=son2()

s1.Disp()
s2.Out()
