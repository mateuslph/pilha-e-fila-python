import time

array = [5, 6, 7, 8]
opcao = ' '
ultimo_elemento = ' '
primeiro_elemento = ' '

while (opcao != 's'):
    escolha = input('Escolha, e digite pilha ou fila ')
    if (escolha == 'pilha'):
        while (True):
            opcao = input('Para adicionar digite add. Para delatar digite del. Qualquer outros para sair. ')
            if (opcao == 'add'):
                entrada = input('Digite o valor: ')
                array.append(entrada)
            elif (opcao == 'del') and (array != []):
                ultimo_elemento = array.pop()
            else:
                break
            if (array != []):
                print(f'O ARRAY é: {array}, e o último elemento retirado da pilha é {ultimo_elemento}')
            else:
                print('O ARRAY está vazio!')
    elif (escolha == 'fila'):
        while (True):
            opcao = input('Para adicionar digite add. Para delatar digite del. Qualquer outros para sair. ')
            if (opcao == 'add'):
                entrada = input('Digite o valor: ')
                array.append(entrada)
            elif (opcao == 'del') and (array != []):
                primeiro_elemento = array.pop(len(array) - len(array))
            else:
                break
            if (array != []):
                print(f'O ARRAY é: {array}, e o primeiro elemento retirado da fila é {primeiro_elemento}')
            else:
                print('O ARRAY está vazio!')
    else:
        print('Você digitou a palavra errada!')
        time.sleep(2)
        break
        