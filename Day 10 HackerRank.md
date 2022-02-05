### Task

Convert an integer into binary and count the consecutive 1's.

```python 
n = int(input().strip())
maxx =0
count=0

while(n>0):
    rem = n%2
    if rem == 1:
        count+=1
        if count>maxx:
            maxx = count
    else:
        count=0
    
    n=n//2
    print(rem)

print(maxx)



