### Problem Statement 

Consider a non-empty string array inarr whose elements contain only digits from 0 to 5 such that no element in inarr will contain all the digits from 0 to 5.

Identify and print outstr using the logic given below:

Identify the non-consecutive unique pairs of elements of inarr, starting from left most element, such that all the digits
from 0 to 5 are present at least once in the pair of elements
 Form strings for each pair identified by concatenating the elements of the pair such that the order of their
occurrence in inarr is preserved • Set outstr with the largest string formed in the above step.
If more than one string exists as largest strings, set outstr with the string
whose first or second element used for concatenation appear first in inarr when traversing from left to right. 
Largest string is a string with maximum number of characters

```python
elements = list(input().split(','))
n=len(elements)
flag=-1
maxx=0
ans=""
for i in range(n):
    j=i+2
    while(j<n):
        res = elements[i]+elements[j]
        if "0" in res and "1" in res and "2" in res and "3" in res and "4" in res and "5" in res:
            if len(res)>maxx:
                ans=res
                maxx=len(res)
                flag=0
        j+=1        
if flag<0:
    print(flag)
else:
    print(ans)
```    
    
 Input
 ```
 30012,250232,53201,3004355,124111
 ```
 Output
 ```
 300123004355
