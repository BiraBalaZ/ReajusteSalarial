nome = input('Qual o nome do funcionário?\n>>>')
val = float(input('Quanto {} ganha?: R$'.format(nome)))
novo = val + (val * .15)
print(f'{nome} ganhava R$ {val}, e recebeu um aumento de 15%, e vai passar a receber R${novo:.2f}')