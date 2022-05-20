class ExAula6:
    def TuplaLinguagensProgramação():
        LinguagensAmadas = ('Rust','TypeScript', 'Python', 'Kotlin', 'Go', 'Julia', 'Dart', 'C#', 'Swift', 'JavaScript')
        print('Ranking das Linguagens de Programação mais amadas')
        for i in range(0,len(LinguagensAmadas), 1):
           print(i+1, '-', LinguagensAmadas[i])

        print('\n Top 3:', LinguagensAmadas[:3])
        print('\n Últimas 5:', LinguagensAmadas [-5:])

    def ListaDeNotas():
        notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
        print(notas)
        #encontrar quantos alunos tiraram nota 7
        print(notas.count(7))
        #alterar última nota para 4
        notas[-1] = 4
        print(notas)
        #encontrar a maior nota
        print(max(notas))
        #ordenar a lista de notas
        print(sorted(notas))

    def TuplaEx1():
        palavras = ('Ana', 'Raysonn', 'Mimosa', 'Ovo', 'Flor')
        #encontre as vogais
        for palavra in palavras:
            print('\nPaLavra:{} . Vogais:'.format(palavra.upper()), end='')
            for letra in palavra:
                if letra.lower() in 'aeiou':
                    print(letra.upper(), end=' ')

    def DicionárioDeCadastros():
        cadastro = {'nome':[], 'sexo':[], 'ano':[]}

        while True:
            terminar = input('Deseja cadastrar uma pessoa?[S/N]')
            if terminar.upper() in 'N':
                break
            if terminar.upper() not in 'S':
                print('Digite S para sim ou N para não.')
                continue

            nome = input('Qual é o seu nome?: ')
            sexo = input('Qual é o seu sexo? [M/F]: ')
            ano = int(input('Qual é o seu ano de nascimento? :'))
            cadastro['nome'].append(nome)
            cadastro['sexo'].append(sexo.upper())
            cadastro['ano'].append(ano)

        print(cadastro)














