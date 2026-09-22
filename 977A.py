
'''A menininha Tanya está aprendendo a diminuir um número em uma unidade, mas ela faz isso de um jeito
diferente quando o número tem dois ou mais dígitos. O algoritmo dela é:
se o último dígito do número for diferente de zero, ela subtrai 1 do número;
se o último dígito do número for zero, ela divide o número por 10 (ou seja, remove o último dígito).
Você recebe um número inteiro n . Tanya vai aplicar essa “subtração” k vezes seguidas. Sua tarefa é imprimir
o resultado depois das k operações.
'''

n = int(input())
k = int(input())
i = 0
while i < k:
    if n % 10 == 0:
        n = n // 10
        i = i + 1
        print(n)
    elif n % 10 != 0:
        n = n - 1
        i = i + 1
        print(n)
    

    


