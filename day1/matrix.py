import numpy as np
#working with matrix array
a = np.array([[1,2,3,4],[4,55,1,2],[8,3,20,19],[11,12,13,22]])
m = np.reshape(a,(4,4))
print(m)

print("Accessing the elements")
print(a[1])
print(a[2][0])

print("Adding elements")
m = np.append(m,[[1,15,13,11]],0)
print(m)

print("Deleting elements")
m = np.delete(m,[1],0)
print(m)