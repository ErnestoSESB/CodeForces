'''Vasya não gosta que as pessoas misturem letras maiúsculas e minúsculas dentro de uma mesma palavra. Ele
quer inventar uma extensão de navegador que transforme qualquer palavra em uma versão totalmente
maiúscula ou totalmente minúscula, alterando o menor número possível de letras.
Por exemplo, a palavra HoUse deve virar house , e a palavra ViP deve virar VIP .
Se a palavra tiver a mesma quantidade de letras maiúsculas e minúsculas, ela deve ser convertida para
minúsculas. Por exemplo, maTRIx deve virar matrix .
Entrada: uma única linha contendo uma palavra s , formada só por letras latinas (maiúsculas e minúsculas),
com comprimento entre 1 e 100.
Saída: a palavra corrigida s . Se s tiver estritamente mais letras maiúsculas do que minúsculas, imprima-a
toda em maiúsculas; caso contrário, imprima-a toda em minúsculas.
Exemplos
Entrada Saída
HoUse house
ViP VIP
maTRIx matrix  '''      

while True:
    plv = input()

    if len(plv) > 100 and len(plv) < 1:
        print("essa palavra não corresponde a quantidade de caracteres permitida")
    else:
        break

maisucula = sum(1 for i in plv if i.isupper())
minuscula = sum(1 for i in plv if i.islower())
if maisucula > minuscula:
    print(plv.upper())
elif minuscula >= maisucula:
    print(plv.lower())



