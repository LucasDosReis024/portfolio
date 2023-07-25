peso = float(input('Digite seu peso em kg (apenas números): '))
cm = int(input('Digite sua altura em cm (apenas números): '))
m = cm / 100
imc = peso / (m * m)
print('Seu IMC é {:.2f}'.format(imc))
sexo = str(input('Digite seu sexo biológico (h ou m): '))
if sexo == 'h':
    if imc < 20:
        print('Você está abaixo do peso.')
    elif imc >= 20 and imc <= 25:
        print('Você está no peso ideal.')
    elif imc >=25 and imc <= 30:
        print('Você está em sobrepeso.')
    elif imc >= 30 and imc <= 40:
        print('Você está em obesidade.')
    elif imc > 40:
        print('Você está em obesidade mórbida.')
if sexo == 'm':
    if imc < 19:
        print('Você está abaixo do peso.')
    elif imc >= 19 and imc <= 24:
        print('Você está no peso ideal.')
    elif imc >=24 and imc <= 29:
        print('Você está em sobrepeso.')
    elif imc >= 29 and imc <= 39:
        print('Você está em obesidade.')
    elif imc > 39:
        print('Você está em obesidade mórbida.')
