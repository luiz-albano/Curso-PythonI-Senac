

#Interface para ler os dados

class VooView :

    def obterDados() :
        print( '===> Cadastro de Voo')
        numero = input( 'Número do voo: ')
        preco = float( input('Preço da passagem:' ) )
        origem = input( 'Aeroporto de Origem: ')
        destino = input( 'Aeroporto de Destino: ')
        partida = input( 'Hora de Partida: ')
        chegada = input( 'Hora de Chegada: ')
        lugares = int( input('Quantidade de lugares:' ) )

        return { 
            'numero' : numero, 
            'preco' : preco,
            'origem' : origem,
            'destino' : destino,
            'partida' : partida,
            'chegada' : chegada,
            'lugares' : lugares
        }