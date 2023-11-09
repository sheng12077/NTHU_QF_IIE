mock2
```py
s=str(input()).split(',')
ans=''
for i in range(len(s)):
    if(len(s[i])>len(ans)):
        ans=s[i]
arr=[]
for i in range(len(s)):
    if len(s[i])==len(ans):
        arr.append(s[i].lower())
print(arr)
```

mock3
```py
lis=input().split(' ')
flag=True
for i in range(len(lis[0])):
    if lis[0][i]=='.':
        flag=False
for i in range(len(lis[1])):
    if lis[1][i]=='.':
        flag=False
ans=0
if flag:
    a=int(lis[0])
    b=int(lis[1])
    m=max(a,b)
    l=min(a,b)
    for i in range(l,m+1,1):
        if(i%3==0):
            ans+=i
    print(ans)
else:
    print('error')
```

mock4
```py
lis=input().split(',')
flag=0
m=int(lis[0])
for i in range(1,len(lis)):
    if int(lis[i])>=m:
        m=int(lis[i])
    else:
        flag=flag+1
        m=int(lis[i])
if flag>=2:
    print("NO")
else:
    print("YES")
```

mock5
```py
lis=input().split(',')
for i in range(len(lis)):
    lis[i]=int(lis[i])

def inc(nums):
    i=1
    n=len(nums)
    while i<len(nums):
        if nums[i]>nums[i-1]:
            i+=1
        else:  
            if i-2>=0:  
                if nums[i]>nums[i-2]: 
                    del nums[i-1]
                else:  
                    del nums[i]
            else:  
                del nums[i-1]
            break
    if n==len(nums):
        return True
    for i in range(1,len(nums)): 
        if nums[i]<=nums[i-1]:
            return False
    return True

flag=inc(lis)
if flag:
    print("YES")
else:
    print("NO")
```

mock6
```py
dic={"Blank Space": 270,
    "Anti-Hero": 310,
    "Shake It Off" : 240,
    "Bad Blood" : 245,
    "Enchanted" : 350}
s=str(input()).split(',')
bs=0 
ah=0
si=0
bb=0
e=0
lis=[]
for i in range(len(s)):
    if s[i]=="Blank Space":
        bs+=1
    elif s[i]=="Anti-Hero":
        ah+=1
    elif s[i]=="Shake It Off":
        si+=1
    elif s[i]=="Bad Blood":
        bb+=1
    else:
        e+=1
lis.append(bs)
lis.append(ah)
lis.append(si)
lis.append(bb)
lis.append(e)

time=0
cost=0
for i in range(len(s)):
    time+=dic[s[i]]

for i in range(len(lis)):
    if(lis[i]>=3):
        cost+=100
        cost+=(lis[i]-2)*20
    else:
        cost+=(lis[i])*50

print(cost)
h=time//3600
m=(time-h*3600)//60
s=(time-h*3600-m*60)
print(f"{h}:{m}:{s}")
```
