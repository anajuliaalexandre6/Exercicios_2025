palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
quantidade = 0

for letra in palavra:
    if letra in vogais:
        quantidade += 1

print(f"A palavra '{palavra}' tem {quantidade} vogais.")



numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))
numero6 = int(input("Digite o sexto número: "))

numeros = [numero1, numero2, numero3, numero4, numero5, numero6]

for numero in numeros:
    if numero % 2 == 0:
        print(f"Número par: {numero}")


nota1 = float (input("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))
nota3 = float (input("Digite a terceira nota: "))
nota4 = float (input('Digite a quarta nota:'))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A media é: {media}")

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

n = int(input("Digite um número: "))
for i in range(1, n+1):
    print(i)

numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print(f"{numero} é múltiplo de 3.")
else:
    print(f"{numero} não é múltiplo de 3.")


nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")

listaDeNomes = [nome1, nome2, nome3]
listaDeNomes.sort()

print("Nomes em ordem alfabética:")
for nome in listaDeNomes:
    print(nome)

