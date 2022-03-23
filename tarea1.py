#Ingresar las notas
nota = int(input("Ingresá una nota (-1 para finalizar)"))
lista_de_notas = []
while nota != -1:
    lista_de_notas.append(nota)
    nota = int(input("Ingresá una nota (-1 para finalizar)"))
for elem in lista_de_notas:
    print(elem)