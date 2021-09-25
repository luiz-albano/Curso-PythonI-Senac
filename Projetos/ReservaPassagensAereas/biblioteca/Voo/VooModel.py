from biblioteca.Util import FileIO as File

class VooModel :
    
    # Nome do arquivo que armazena os dados de voos
    nome_arquivo = 'dados/voos.csv'

    def __init__( self ) :
        self.numero = ''
        self.preco = 0.0
        self.aeroporto_origem = ''
        self.aeroporto_destino = ''
        self.horario_partida = ''
        self.horario_chegada = ''
        self.quantidade_lugares = 0


    def __str__(self):
        return self.numero + ';' + str( self.preco ) + ';' + \
            self.aeroporto_origem + ';' + self.aeroporto_destino + ';' + \
            self.horario_partida + ';' + self.horario_chegada + ';' + \
            str( self.quantidade_lugares )


    def salvar( self ) :
        File.FileIO.salvar( self.nome_arquivo, str( self ) )

    def carregarVoos( self ) :
        voos = File.FileIO.obter( self.nome_arquivo )
        return voos.split( '\n' )