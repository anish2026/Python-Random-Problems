## Day 14 Scope 

### Task

Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the  __element  instance variable.

A computeDifference method that finds the maximum absolute difference between any 2 numbers in  and stores it in the  instance variable.

Input Format

You are not responsible for reading any input from stdin. The locked Solution class in the editor reads in 2 lines of input. The first line contains N, the size of the elements array.
The second line has N space-separated integers that describe the  array.

```python 

class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        
        maxx=0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                absolute = abs(self.__elements[i]-self.__elements[j])
                if absolute>maxx:
                    maxx=absolute
                    
        self.maximumDifference=maxx
               

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
```
Input
```
3
1 2 5
```
Ouput
```
4
```
