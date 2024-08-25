ebob1 = int(input("1. EBOBU GİRİN:"))
ebob2 = int(input("2.EBOBU GİRİN:"))

ebob_list1 = list()

ebob_list2 = list()

for i in range(1,ebob1+1):
    if(ebob1 % i == 0):
        ebob_list1.append(i)


for i in range(1,ebob2+1):
    if(ebob2 % i == 0):
        ebob_list2.append(i)

ebob_list1 = set(ebob_list1)
ebob_list2 = set(ebob_list2)
ortak = ebob_list1.intersection(ebob_list2)

print(max(ortak))

