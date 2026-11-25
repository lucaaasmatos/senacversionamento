'''EXERCICIO 4:
- Crie um programa que recebe números inteiros positivos um a um.
- Valide que o número seja maior que zero.
- Verifique se a sequência está sempre crescendo.
- Permita que o usuário pare quando quiser.
- Se em algum momento o número informado for menor ou igual ao anterior, interrompa a entrada e informe
que a sequência não é crescente.
- Caso o usuário pare involuntariamente, informe se a sequência é crescente ou não.
- Exiba a soma e a quantidade de números informados.
'''


soma = 0
quant = 0
ant = 0
cres = True

while True:
    nro = int(input("digitar nro inteiro positivo ou 0 para parar: "))

    # Verifica se o usuário deseja parar
    if nro == 0:
        break

    # Valida se o número é positivo
    if nro < 0:
        print("somente nros positivos")
        continue

    # Verifica se a sequência está crescendo
    if quant > 0 and nro <= ant:
        cres = False
        print("decrescente")
        break

    # Atualiza os valores
    soma += nro
    quant += 1
    ant = nro

# Exibe os resultados
print("\nresultado:")

if cres:
    print("crescente")
else:
    print("decrescente")

print("soma nros:", soma)
print("quant nros:", quant)
