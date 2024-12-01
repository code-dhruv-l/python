def rev_str(string):
    st=" ";
    for s in string:
        st=s+st;
        return st;
string="hello!";
print(rev_str(string));
