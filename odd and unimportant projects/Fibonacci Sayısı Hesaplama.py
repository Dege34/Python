"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur

1,1,2,3,5,8,13,21,34,55.........

Çıkmak için "Q"ya basın
"""
a = 1
b = 1
fibonacci = [a,b]

for i in range(20):
    a,b = b,a+b

    print("a",a,"b:",b)

    fibonacci.append(b)
print(fibonacci)
