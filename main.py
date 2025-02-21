import numpy as np
import django

def add2(number):
    return number + 2

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

for i in range(len(arr)):
    arr[i] = add2(arr[i])

print(arr)
