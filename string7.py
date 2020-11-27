nume_pren = str(input("dati numele si prenumele: "))
nr_lit = 0
for i in range(0, len(nume_pren)):
    if ord(nume_pren[i]) in range(65, 123):
        nr_lit += 1
sir = nume_pren.split()
nume = sir[0]
prenume = sir[1]
if (nume.title() == nume) and (prenume.title() == prenume):
    print("numele dat e corect")
else:
    print("numele nu e corect")
