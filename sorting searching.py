import numpy as np
array1 = np.array(list(map(int, input().split())))
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))
a = np.where(array1 == search_value)[0]
print(a)
b = np.count_nonzero(array1 == count_value)
print(b)
c = array1 + broadcast_value
print(c)
d = np.sort(array1)
print(d)