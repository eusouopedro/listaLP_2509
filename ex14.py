#exercicio 13, lista de exercicios: Linguagens de Programacao 2023.2 UFRJ

peso = float(input("Informe o peso de peixes[kg]: "))
excesso = peso - 50
multa = excesso*4

if excesso <= 0:
    print("Nao ha excesso de peixes")
else:
    print("O excesso de peixes foi de {}kg, o que resulta numa multa de R${:.2f}".format(excesso, multa))