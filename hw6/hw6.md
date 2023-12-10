6-1
```py
pf1 = set(input().split(','))
pf2 = set(input().split(','))
pf3 = set(input().split(','))

result1=list(pf1 & pf2 & pf3)
allstocks=pf1 | pf2 | pf3

result2=[]

for product in allstocks:
    cnt=0

    for pf in [pf1, pf2, pf3]:
        if product in pf:
            cnt+=1

    if cnt==1:
        result2.append(product)

result2.sort()

print(result1)
print(result2)
```


6-2
```py
def get_max_int(*args,**kwargs):  
    lst=[]  
  
    for arg in args:  
        if type(arg)==int:  
            lst.append(arg)  
        elif type(arg)==dict:  
            for i in arg.values():  
                if type(i)==int:  
                    lst.append(i)  
  
    for i in kwargs.values():  
        if type(i)==int:  
            lst.append(i)  
  
    return max(lst)  
  
if __name__=="__main__":  
    test()  
```

6-3
```py
def str_dic(st):
    dit={}
    chars=st.split(',')
    for char in chars:
        if char in dit:
            dit[char]+=1
        else:
            dit[char]=1
    return dit
def test():
    instr = input()
    print(str_dic(instr))
if __name__=="__main__":
    test()
```
