cuvint = str(input("dati un cuvint: "))
litera = str(input("dati o litera: "))
for i in range (0,len(cuvint)):
    print(cuvint.replace(cuvint[i],litera))