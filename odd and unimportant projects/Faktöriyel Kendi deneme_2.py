while True:
    a = input("Faktöriyelini alamk istediğiniz sayıyı girin:")
    a_1 = int(a)
    a_2 = range(2,a_1+1)
    faktoriyel = 1
    for i in a_2:

        faktoriyel *= i
    print(faktoriyel)
    break