listaPecas = []
class Ex1:
    # Bem Vindo ao Controle de Estoque da Bicicletaria da Ana Lucia da Costa Coutinho RU:3932630
    # Início cadastrarPeca
    def cadastrarPeca(codigo):
        print('Cadastrar Peça: ')
        print('O código da peça a ser cadastrada é: {}'.format(codigo))
        nomePeca = input('Digite o nome da peça: ')
        fabricantePeca = input('Digite o fabricante da peça: ')
        valorPeca = float(input('Digite o valor(R$) da peça:'))
        dicionarioPeca = {'código': codigo,
                          'nome': nomePeca,
                          'fabricante': fabricantePeca,
                          'valor': valorPeca}
        listaPecas.append(dicionarioPeca.copy())
    # fim cadastrarPeca

    # Início consultarPeca
    def consultarPeca():
        while True:
            try:
                print('Consultar Peça:')
                opcaoConsultar = int(input('Digite a opção desejada:\n'
                                           '1-Consultar Todas as Peças\n'
                                           '2-Consultar Peças por Códigos\n'
                                           '3-Consultar Peças por Fabricante\n'
                                           '4-Retornar'
                                           '\n>>'))
                if opcaoConsultar == 1:
                    for peca in listaPecas:  # selecionar cada dicionário da minha lista(cada peça da ista de peças)
                        for key, value in peca.items():  # selecionar cada conjunto chave/valor do dicionário
                            print('{} : {} '.format(key, value))
                elif opcaoConsultar == 2:
                    consultarCodigo = int(input('Digite o código da peça a ser consultada: '))
                    for peca in listaPecas:
                        if (peca['código'] == consultarCodigo):
                            for key, value in peca.items():
                                print('{} : {} '.format(key, value))
                elif opcaoConsultar == 3:
                    consultarCodigo = input('Digite o fabricante da peça a ser consultada: ')
                    for peca in listaPecas:
                        if (peca['fabricante'] == consultarCodigo):
                            for key, value in peca.items():
                                print('{} : {} '.format(key, value))
                elif opcaoConsultar == 4:
                    break
                else:
                    print('Você digitou uma opção inválida, tente novamente.')
                    continue
            except ValueError:
                print('Para de digitar valores não inteiros.')
    # fim consultarPeca

    # Início removerPeca
    def removerPeca():
        print('Remover Peça:')
        consultarCodigo = int(input('Digite o código da peça a ser removida: '))
        for peca in listaPecas:
            if (peca['código'] == consultarCodigo):
                listaPecas.remove(peca)
    # fim removerPeca

    # Início Main
    print('Bem Vindo ao Controle de Estoque da Bicicletaria da Ana Lucia da Costa Coutinho RU:3932630')
    registroEstoque = 0  # registroEstoque começa zerado pois ele vai ir acumulando os valores recebidos pelo usuário.
    while True:
        try:
            opcao = int(input('Digite a opção desejada:\n'
                              '1-Cadastrar Peças\n'
                              '2-Consultar Peças\n'
                              '3-Remover Peças\n'
                              '4-Sair'
                              '\n>>'))
            if opcao == 1:
                registroEstoque = registroEstoque + 1
                cadastrarPeca(registroEstoque)
            elif opcao == 2:
                consultarPeca()
            elif opcao == 3:
                removerPeca()
            elif opcao == 4:
                print('Encerrando o programa, até a próxima...')
                break
            else:
                print('Você digitou uma opção inválida, tente novamente.')
                continue
        except ValueError:
            print('Para de digitar valores não inteiros.')