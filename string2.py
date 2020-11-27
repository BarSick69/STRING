n = str(input("dati un sir de caractere: "))
nr_maj = 0
nr_cifre = 0
nr_carac_spec = 0
for i in range (0, len(n)):
    if 90 >= ord(n[i]) >= 65:
        nr_maj += 1
    if 57 >= ord(n[i]) >= 48:
        nr_cifre += 1
    if((ord(n[i])>=33)and(ord(n[i])<=47))or((ord(n[i])>=58)and(ord(n[i])<=64))or((ord(n[i])>=91)and(ord(n[i])<=96))or((ord(n[i])>=123)and(ord(n[i])<=127)):
            nr_carac_spec += 1
print(f'Numarul de litere majuscule este {nr_maj}')
print(f'Numarul de cifre este {nr_cifre}')
print(f'Numarul de caractere speciale este {nr_carac_spec}')

