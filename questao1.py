def primo(numero):
    eh_primo = True  # vai analisar se o numero global é primo
    anteriores_sao_primos = False  # vai determinar se existe algum primo antes do principal
    primos_anteriores = ''  # vai criar uma string com todos os números primos
    for n_anterior in range(2, numero):  # vai testando os números antes do  principal
        if numero % n_anterior == 0:  # se em algum momento a divisão tiver resto 0, não é primo
            eh_primo = False
        anterior_primo = True  #
        for teste in range(2, n_anterior):
            if n_anterior % teste == 0:
                anterior_primo = False
        if anterior_primo:
            anteriores_sao_primos = True
            if primos_anteriores == '':
                primos_anteriores += f'{n_anterior}'
            else:
                primos_anteriores += f', {n_anterior}'
    if n == 1:
        eh_primo = False
    if eh_primo:
        print(f'O número {n} é primo.')
    else:
        print(f'O número {n} não é primo.')
        if anteriores_sao_primos:
            print(f'Entretanto, temos primos no intervalo de 1 à {n}. Estes são:')
            print(primos_anteriores)
        else:
            print(f'Além disso, não temos primos no intervalo de 1 à {n}.')


n = int(input())
primo(n)
print('AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!')
