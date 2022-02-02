# Objective
# Today, we will learn about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.

# Example


# Print 4 3 2 1. Each integer is separated by one space.

# Input Format

# The first line contains an integer,  (the size of our array).
# The second line contains  space-separated integers that describe array 's elements.



import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    new_arr=[]
    def f(arr):
        new_arr=arr[::-1]
        return new_arr
    print(' '.join(map(str,f(arr))))

