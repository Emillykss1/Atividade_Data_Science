# Nome
nome = input('Digite seu nome: ')
print(nome)

#If e Else
tempo = input('Está fazendo sol?, Responda com S ou N ')
dinheiro = input('Você tem dinheiro?, Responda com S ou N ')

if (tempo == 's' and dinheiro == 's'):
    print("Vamos a praia")
else:
    print("Vamos assistir netflix")

# Lista

dias = [3, 1, 10]
dias[0]
     
# -----------------------------

Z = [3,8,9]
Z[0] = 7
Z

# ------------------------------

a = [81, 82, 83]
b = a[:]
print(a == b)
print(a is b)
b[0] = 5
print(a)
print(b)
 
# -------------------------------

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])

# --------------------------------

a = [1, 2, 3] 
b = a[:] 
b[0] = 5
print(a[2])