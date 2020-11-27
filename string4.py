a = str(input("dati un sir de caractere: "))
b = str(input("dati un sir de caractere: "))
c = str(input("dati un sir de caractere: "))
d = str(input("dati un sir de caractere: "))
sir = ''
if (len(a) > 2) and (len(b) > 2) and (len(c) > 2) and (len(d) > 2):
    sir = a[:2] + b[:1] + c[:3] + d[:len(d) // 2]
else:
    print("alegeti alte siruri, mai lungi de 2 caractere")
print(sir)
