cnp = str(input("dati cnp-ul dumnevoastra: "))
x = len(cnp)
nr = 0
if x != 13:
    print("cnp-ul e gresit")
elif x == 13:
    for i in cnp:
        if (48 <= ord(i)) and (ord(i) <= 57):
            nr += 1
    if nr == 13:
        print("cnp-ul e corect")
    else:
        print("cnp-ul e gresit")
