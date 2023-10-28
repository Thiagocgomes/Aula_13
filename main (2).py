# texto = 'Python é uma linguagem de programação. Python é simples. Python é organizado. Python é uma excelente linguagem.'
# print(texto.count('é'))
# print(texto.find('Python', 25, 50))
# print(texto.rfind('lingua'))
# print(texto.index('é'))
# print(texto.rindex('é'))

# texto = 'Olá Mundo!'
# texto_centro = texto.center(20)
# texto_centro_2 = texto.center(20,'=')
# texto_esquerda = texto.ljust(12)
# texto_direita = texto.rjust(12)
# print(texto_centro_2)

#Exercício 1: Escreva um programa que verifique se a palavra "python" está presente na string "Estou aprendendo Python".

string = 'Estou aprendendo Python'
if 'Python' in string:
  print('A palavra Python está presente na string')
  
#Exercício 2: Escreva um programa que peça ao usuário para digitar seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula).

nome = input('Digite seu nome: ')
if nome.startswith('a' or 'A'):
  print('O nome começa com A')
else:
  print('O nome não começa com A')

#Exercício 3: Escreva um programa que peça ao usuário para digitar uma senha e verifique se a senha contém pelo menos 8 caracteres.

senha = input('Digite uma senha: ')
if len(senha) >= 8:
  print('A senha contém 8 digitos')
else:
  print('A senha não contém 8 digitos')

#Exercício 4: Escreva um programa que peça ao usuário para digitar um número e verifique se o número é uma representação numérica (não contém letras ou símbolos).

numero = input('Digite um número: ')
if numero.isnumeric():
  print('É uma representação numérica')
else:
  print('Isso não é uma representação numérica')

#Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vezes a letra "a" (maiúscula ou minúscula) aparece na frase.

frase = input('Digite uma frase: ')
if 'a' or 'A' in frase:
  print('A letra A aparece {} vezes'.format(frase.count('a' or 'A')))
  
  
  
