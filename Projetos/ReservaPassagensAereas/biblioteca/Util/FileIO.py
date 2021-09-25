
class FileIO :

    @staticmethod
    def salvar( nome_arquivo, informacao_adicional ) :
        conteudo = FileIO.obter( nome_arquivo )
        arquivo = open( nome_arquivo, 'w' )

        if conteudo == None :
            conteudo = informacao_adicional
        else :
            conteudo = conteudo + '\n' + informacao_adicional

        arquivo.write( conteudo )
        arquivo.close()

    @staticmethod
    def obter( nome_arquivo ) :
        try :
            arquivo = open( nome_arquivo, 'r' )
            dados = arquivo.read()
            arquivo.close()
            return dados
        except FileNotFoundError:
            print( 'Arquivo não encontrado.' )