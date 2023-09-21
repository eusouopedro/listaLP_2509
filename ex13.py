#exercicio 13, lista de exercicios: Linguagens de Programacao 2023.2 UFRJ

h = float(input("Informe sua altura[m]: "))
sexo = (input("Voce eh homem ou mulher? ")).strip()
peso = 0
if sexo[0] == 'h':
    peso = (72.7*h) - 58
elif sexo[0] == 'm':
    peso = (62.1*h) - 44.7
print('O peso ideal para a sua altura eh {:.2f}'.format(peso))