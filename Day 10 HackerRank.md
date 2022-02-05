### Task

Convert an integer into binary and count the consecutive 1's.

```python 
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    rem =0 
    count=0
    while(n>0):
        rem=n%2
        n=n//2
        if rem == 1:
            count+=1
        else:
            count=0
print(count)



