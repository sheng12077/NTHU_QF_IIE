[ex3](https://eeclass.nthu.edu.tw/homework/report/698322/?ajaxAuth=fafe23457ac9f74ab7ce814e7fed6edc)

ex3-1
```py
a=str(input())
l=len(a)
flag=True
for i in range(l//2):
    if a[i]!=a[l-i-1]:
        flag=False
print("YES") if flag else print("NO")
```

ex3-2
```py
a=str(input())
l=len(a)
flag=True
i=0
while i<l//2:
    if a[i]!=a[l-i-1]:
        flag=False
    i+=1
print("YES") if flag else print("NO")
```

ex3-3
```py
a=str(input())
b=a[::-1]
if a==b:
    print("YES")
else:
    print("NO")
```
