```py
def sentence(s):
    ans=[]
    for j in range(1,51):
        for i in range(len(s)):
            if len(s[i])==j and s[i] not in ans:
                ans.append(s[i])
    return ans
def test():    
    s=input().lower().replace('.',' ').replace(',',' ').split(' ')
    print(sentence(s)) 
test()
```
