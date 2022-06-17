#Python Bytearray gives a mutable sequence of integers in the range 0 <= x < 256.

a = bytearray((12,8,9,25,2))
print("Creating bytearray: ")
print(a)

print("Accesing bytearray elements")
print(a[1])

print("modifying bytearray elements")
a[1] = 3
print(f"Modified bytearray elements: {a}")

print("Appending bytearray elements")
a.append(30)
print(f"After adding bytearray elements: {a}")