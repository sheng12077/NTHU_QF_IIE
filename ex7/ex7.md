7-1
```py
#ex7-1:
import math
def test():
    a = int(input())
    b = int(input())
    c = int(input())
    print(eq2(a,b,c))


def eq2(a,b,c):
    if b**2-4*a*c < 0:
        return "no answer"
    else:
        if (-b+math.sqrt(b**2-4*a*c))/(2*a)>0:
            root1=math.floor((-b+math.sqrt(b**2-4*a*c))/(2*a)*10000)/10000
        else:
            root1=math.ceil((-b+math.sqrt(b**2-4*a*c))/(2*a)*10000)/10000
        if (-b-math.sqrt(b**2-4*a*c))/(2*a)>0:
            root2=math.floor((-b-math.sqrt(b**2-4*a*c))/(2*a)*10000)/10000
        else:
            root2=math.ceil((-b-math.sqrt(b**2-4*a*c))/(2*a)*10000)/10000
        return "('{:.4f}', '{:.4f}')".format(root1, root2)

    
if __name__=="__main__":
    test()
```

7-2
```py
def test():  
    a = float(input())  
    d = float(input())  
    t = float(input())  
    print(tree(a,d,t))  
  
import math  
def tree(a,d,t):  
    return round((t/100+d*math.tan(a*math.pi/180)),2)  
  
  
if __name__=="__main__":  
    test()  
```

7-3
```py
import random as rd
import math as ma

def grouping(n,m):
    people=list(range(1,n+1)) #build the list from 1 to n
    rd.shuffle(people)  #shuffle the list, random.shuffle means to sort the list randomly
    
    groups=[]
    group_size=ma.ceil(n/m)   #ceil() 向上取整

    #想法:先把前m-1组的人分好，最后一组的人單獨處理
    #前面先用random.shuffle()把所有人打亂，再用group_size把人分成m組
    for i in range(m-1):
        start=i*group_size
        end=(i+1)*group_size
        group=people[start:end]
        groups.append(sorted(group))
    
    last_group=people[(m-1)*group_size:]  #the last group arr[n:] means from n to the end
    groups.append(sorted(last_group))
    

    for i in range(len(groups)):
        group=groups[i]
        leader=rd.choice(groups[i])
        print(f"Group {i+1}:{groups[i]}, Leader:{leader}")

grouping(14,3)
```


7-4
```py
import statistics as st
def test():
    inp=input().split(',')
    lst=list(map(int,inp)) 
    print(count(lst))
    

def count(lst):
    return round(st.mean(lst)), round(st.median(lst)), round(st.pstdev(lst),2), round((st.pstdev(lst))**2,2)

    
if __name__=="__main__":
    test()
```
