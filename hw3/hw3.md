[hw3](https://eeclass.nthu.edu.tw/course/homework/29152)

3-1
```py
s=str(input())
a=0
b=0
k=len(s)//2
# print(k)
if len(s)%2!=0:
    print("Wrong")
else:
    for i in range(0,k,1):
        a+=int(s[i])
        b+=int(s[len(s)-i-1])
    print("Lucky") if a==b else print("Unlucky")
    # print(a,b)
```

3-2
```py
n=int(input())
ans=0
for i in range(0,n+1,4):
    ans+=i
print(ans)
```

3-3
```py
h1,m1=input().split(":")
h2,m2=input().split(":")
h1,h2,m1,m2=int(h1),int(h2),int(m1),int(m2)
t=h2*60-h1*60+m2-m1
if t<120:
    print((t//30)*40)
elif 120<=t<240:
    print(160+((t-120)//30)*50)
else:
    print(360+((t-240)//30)*60)   `
```

3-4
```py
n=int(input())
ans=1
while n>0:
    ans*=n
    n-=1
print(ans)
```

3-5
```py
def gcd(a,b):
    while b>0:
        tmp=b
        b=a%b
        a=tmp
    return a
c=int(input())
d=int(input())
print(gcd(c,d),c*d//gcd(c,d))
```



