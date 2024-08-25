a = 1
b = 1
fibonacci = [a,b]

for i in range(int(input("fibonacci almak istediğin sayıyı gir:"))):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)