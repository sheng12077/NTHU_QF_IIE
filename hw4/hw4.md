
4-1
```py
# %%file hw4-1.py

def isodd(a):
    s="~!@#$%^&*()_+-*/<>,.[]\/\'\"=><˙{ }"
    for i in s:
        if a==i:
            return True
    return False

def pw_check(pw):
    upp=False
    low=False
    di=False
    other=False
    leng=False
    title=True

    for i in pw:
        if i.isupper():
            upp=True
        if i.islower():
            low=True
        if i.isdigit():
            di=True
        if isodd(i):
            other=True
    if len(pw)>=8 and len(pw)<=16:
        leng=True
    if pw[0].isdigit():
        title=False
    if (upp and low and di and other and leng and title):
        return True
    else:
        return False
    
def test():
    pw=input()
    flag=pw_check(pw)
    if flag:
        print("Success")
    else:
        print("Fail")
        
        
# 下列兩行程式碼必須一起上傳至etutor     
if __name__=="__main__":
    test()
```
4-2

```py
# %%file hw4-2.py
def guess(n1,n2):
    a=0
    b=0
    for i in range(len(n1)):
        if n2.find(n1[i])!=-1:
            if n1[i]==n2[i]:
                a+=1
            else:
                b+=1
    
    print(f"{a}A{b}B")
    
def test():
    n1=input()
    n2=input()
    guess(n1,n2)

# 下列兩行程式碼必須一起上傳至etutor       
if __name__=="__main__":
    test()
```
