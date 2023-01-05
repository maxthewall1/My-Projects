'''

GERADOR DE CPF (BRAZLIAN ID GENERATOR)

'''
from random import randint



cpf_digitado = str(randint(100000000,999999999))


if  cpf_digitado.isnumeric() and len(cpf_digitado) == 9 and not cpf_digitado == cpf_digitado[0]*9 :

    cpf_digitado = list(cpf_digitado)

    cpf_digitado[0] = int(cpf_digitado[0])
    cpf_digitado[1] = int(cpf_digitado[1])
    cpf_digitado[2] = int(cpf_digitado[2])
    cpf_digitado[3] = int(cpf_digitado[3])
    cpf_digitado[4] = int(cpf_digitado[4])
    cpf_digitado[5] = int(cpf_digitado[5])
    cpf_digitado[6] = int(cpf_digitado[6])
    cpf_digitado[7] = int(cpf_digitado[7])
    cpf_digitado[8] = int(cpf_digitado[8])


    x1 = cpf_digitado[0] * 10
    x2 = cpf_digitado[1] * 9
    x3 = cpf_digitado[2] * 8
    x4 = cpf_digitado[3] * 7
    x5 = cpf_digitado[4] * 6
    x6 = cpf_digitado[5] * 5
    x7 = cpf_digitado[6] * 4
    x8 = cpf_digitado[7] * 3
    x9 = cpf_digitado[8] * 2

    resultado1 = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9

    resultado_novo1 = 11 - (resultado1 % 11)
    if resultado_novo1 > 9:
        cpf_digitado.append(0)
    else:
        cpf_digitado.append(resultado_novo1)

    z1 = cpf_digitado[-10] * 11
    z2 = cpf_digitado[-9] * 10
    z3 = cpf_digitado[-8] * 9
    z4 = cpf_digitado[-7] * 8
    z5 = cpf_digitado[-6] * 7
    z6 = cpf_digitado[-5] * 6
    z7 = cpf_digitado[-4] * 5
    z8 = cpf_digitado[-3] * 4
    z9 = cpf_digitado[-2] * 3
    z10 = cpf_digitado[-1] * 2

    resultado2 = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10

    resultado_novo2 = 11 - (resultado2 % 11)

    if resultado_novo2 > 9:
        cpf_digitado.append(0)

    else:
        cpf_digitado.append(resultado_novo2)

    cpf_digitado[0] = str(cpf_digitado[0])
    cpf_digitado[1] = str(cpf_digitado[1])
    cpf_digitado[2] = str(cpf_digitado[2])
    cpf_digitado[3] = str(cpf_digitado[3])
    cpf_digitado[4] = str(cpf_digitado[4])
    cpf_digitado[5] = str(cpf_digitado[5])
    cpf_digitado[6] = str(cpf_digitado[6])
    cpf_digitado[7] = str(cpf_digitado[7])
    cpf_digitado[8] = str(cpf_digitado[8])
    cpf_digitado[9] = str(cpf_digitado[9])
    cpf_digitado[10] = str(cpf_digitado[10])


    str_cpf= "".join(cpf_digitado)
    print(f'O CPF gerado é {str_cpf}')

else:
    print('Por favor. Reinicie o processo e gere um novo cpf.')
