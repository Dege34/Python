vize1 = int(input("Vize 1 Notunuzu Girin:"))
vize2 = int(input("Vize 2 Notunuzu Girin:"))
final = int(input("Final Notunuzu Girin:"))
genelnote = vize1 * 3/10 + vize2 * 3/10 + final * 4/10
if (genelnote<= 55):
    print("FF")
elif (55 <= genelnote <= 60):
    print("FD")
elif (60 <= genelnote <= 65):
    print("DD")
elif (65 <= genelnote <= 70):
    print("DC")
elif (70 <= genelnote <= 75):
    print("CC")
elif (75 <= genelnote <= 85):
    print("CB")
elif (85 <= genelnote <= 90):
    print("FD")
elif (90 <= genelnote <= 95):
    print("DD")
elif (95 <= genelnote <= 100):
    print("DC")

