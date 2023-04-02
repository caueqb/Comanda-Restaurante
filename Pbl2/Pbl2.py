import datetime

agora = datetime.datetime.now()

itens = ['Hambúrguer', 'Refrigerante']
precoItens = [14.99, 5.99]
comanda1Item = []
comanda2Item = []
comanda3Item = []
comanda1Preco = []
comanda2Preco = []
comanda3Preco = []
precoComandas = []

opcao = 0
while(opcao != 3):
    print('Que ação deseja realizar?')
    print('1 - Abrir comanda')
    print('2 - Fechar comanda')
    print('3 - Sair')
    opcao = int(input())

    if(opcao == 1):
        def abrirComanda(comandaSelecionada, comandaSelecionadaPreco):
            if(comandaSelecionada == 1):
                comandaSelecionada = comanda1Item
                comandaSelecionadaPreco = comanda1Preco
            elif(comandaSelecionada == 2):
                comandaSelecionada = comanda2Item
                comandaSelecionadaPreco = comanda2Preco
            elif(comandaSelecionada == 3):
                comandaSelecionada = comanda3Item
                comandaSelecionadaPreco = comanda3Preco
            
            simNao = 'S'
            while(simNao != 'N'):
                print('O que deseja pedir?')
                print(f'1 - {itens[0]} : R${precoItens[0]}')
                print(f'2 - {itens[1]} : R${precoItens[1]}')
                adicionarItem = int(input())

                if(adicionarItem == 1):
                    comandaSelecionada.append(itens[0])
                    comandaSelecionadaPreco.append(precoItens[0])
                if(adicionarItem == 2):
                    comandaSelecionada.append(itens[1])
                    comandaSelecionadaPreco.append(precoItens[1])
                
                print('Deseja pedir mais alguma coisa? [S/N]')
                simNao = str(input()).upper()
        
        print('Escolha qual comanda deseja abrir:')
        print('1 - Comanda 1')
        print('2 - Comanda 2')
        print('3 - Comanda 3')
        comandaSelecionada = int(input())
        comandaSelecionadaPreco = comandaSelecionada

        if(comandaSelecionada == 1):
            abrirComanda(comandaSelecionada, comandaSelecionadaPreco)
        elif(comandaSelecionada == 2):
            abrirComanda(comandaSelecionada, comandaSelecionadaPreco)
        elif(comandaSelecionada == 3):
            abrirComanda(comandaSelecionada, comandaSelecionadaPreco)
        else:
            print('Comanda inválida')
    elif(opcao == 2):
        print('Escolha qual comanda deseja fechar:')
        print('1 - Comanda 1')
        print('2 - Comanda 2')
        print('3 - Comanda 3')
        comandaSelecionada = int(input())
        comandaSelecionadaPreco = comandaSelecionada

        numeroComanda = ''
        def fecharComanda(comandaSelecionada, comandaSelecionadaPreco, numeroComanda):
            if(comandaSelecionada == 1):
                comandaSelecionada = comanda1Item
                comandaSelecionadaPreco = comanda1Preco
                numeroComanda = 'comanda1'
            elif(comandaSelecionada == 2):
                comandaSelecionada = comanda2Item
                comandaSelecionadaPreco = comanda2Preco
                numeroComanda = 'comanda2'
            elif(comandaSelecionada == 3):
                comandaSelecionada = comanda3Item
                comandaSelecionadaPreco = comanda3Preco
                numeroComanda = 'comanda3'

            print('Pedidos:')

            precoComandas.append(round(sum(comandaSelecionadaPreco), 2))
            conta = []
            for item, preco in zip(comandaSelecionada, comandaSelecionadaPreco):
                print(f'{item} : R${preco}')
                conta.append(f'{item} : R${preco} \n')
            print('Deseja calcular o valor total? [S/N]')
            simNao = str(input()).upper()
            if(simNao == 'S'):
                print('Soma total:')
                print(f'R${round(sum(comandaSelecionadaPreco), 2)}')
                pessoasTotal = int(input('Digite o número de pessoas que deseja para dividir o total da conta: '))
                print('Valor dividido:')
                print(f'R${round(sum(comandaSelecionadaPreco) / pessoasTotal, 2)} para cada pessoa')
            print('Deseja realmente fechar a comanda? [S/N]')
            simNao = str(input()).upper()
            if(simNao == 'S'):
                with open(f'conta_{numeroComanda}_{agora.strftime("%d-%m-%Y_%H-%M-%S")}.txt', 'w') as arquivoUm:
                    arquivoUm.write(f'conta_{numeroComanda}_{agora.strftime("%d-%m-%Y_%H-%M-%S")}: \n')
                    arquivoUm.writelines(conta)
                    arquivoUm.write('Soma total : ')
                    arquivoUm.write(f'R${round(sum(comandaSelecionadaPreco), 2)} \n \n')
                with open(f'conta_{numeroComanda}_{agora.strftime("%d-%m-%Y_%H-%M-%S")}.txt', 'r') as arquivoUm:
                    linhas = arquivoUm.readlines()
                with open('Vendas_Totais.txt', 'a') as arquivoDois:
                    arquivoDois.writelines(linhas)
                    arquivoDois.write('Receita total : ')
                    arquivoDois.write(f'R${round(sum(precoComandas), 2)} \n \n')
                comandaSelecionada.clear()
                comandaSelecionadaPreco.clear()

        if(comandaSelecionada == 1):
            fecharComanda(comandaSelecionada, comandaSelecionadaPreco, numeroComanda)
        elif(comandaSelecionada == 2):
            fecharComanda(comandaSelecionada, comandaSelecionadaPreco, numeroComanda)
        elif(comandaSelecionada == 3):
            fecharComanda(comandaSelecionada, comandaSelecionadaPreco, numeroComanda)
        else:
            print('Comanda inválida')

    elif(opcao == 3):
        break
    else:
        print('Opção inválda')