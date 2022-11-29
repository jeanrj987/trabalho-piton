lista01 = ['Cleiton','Leonardo','Pedro','Willian','Kauã','Alexandre','Antonia']
lista02 = ['Cleiton','Leonardo','Pedro','Willian','Kauã','Alexandre','Antonia']
lista03 = ['Cleiton','Leonardo','Pedro','Willian','Kauã','AlexAandre','Antonia']

for i in range(0,7):

    print(lista01[i],lista02[i],lista03[i])

primeira = input("Escolha uma coluna: ")

if primeira == 'A' or primeira == 'a':
    round1 = lista02 + lista01 + lista03
elif primeira == 'B' or primeira == 'b':
    round1 = lista01 + lista02 + lista03
else:
    round1 = lista01 + lista03 + lista02

n = 3
round2 = [round1[i::n] for i in range(3)]

lista01 = round2[0]
lista02 = round2[1]
lista03 = round2[2]

for i in range(0,7):

    print(lista01[i],lista02[i],lista03[i])

primeira = input("Escolha uma coluna: ")

if primeira == 'A' or primeira == 'a':
    round1 = lista02 + lista01 + lista03
elif primeira == 'B' or primeira == 'b':
    round1 = lista01 + lista02 + lista03
else:
    round1 = lista01 + lista03 + lista02

n = 3
round2 = [round1[i::n] for i in range(3)]

lista01 = round2[0]
lista02 = round2[1]
lista03 = round2[2]

for i in range(0,7):

    print(lista01[i],lista02[i],lista03[i])

primeira = input("Escolha uma coluna: ")

if primeira == 'A' or primeira == 'a':
    round1 = lista02 + lista01 + lista03
elif primeira == 'B' or primeira == 'b':
    round1 = lista01 + lista02 + lista03
else:
    round1 = lista01 + lista03 + lista02

n = 3
round2 = [round1[i::n] for i in range(3)]

lista01 = round2[0]
lista02 = round2[1]
lista03 = round2[2]

resultado = lista01 + lista02 + lista03
print(resultado[10])