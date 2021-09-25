from biblioteca.Voo import VooView as View, VooModel as Model

class VooController :

    _voos = []

    def __init__( self ) :
        self.carregarVoos()


    def carregarVoos( self ) :
        voos = Model.VooModel()
        for voo in voos.carregarVoos() :
            dados = voo.split( ';' )
            voo_dados = Model.VooModel()
            voo_dados.numero = dados[0]
            voo_dados.preco = dados[1]
            voo_dados.aeroporto_origem = dados[2]
            voo_dados.aeroporto_destino = dados[3]
            voo_dados.horario_partida = dados[4]
            voo_dados.horario_chegada = dados[5]
            voo_dados.quantidade_lugares = dados[6]

            self._voos.append( voo_dados )


    def cadastrarVoo( self ) :
        view = View.VooView()
        dados = view.obterDados()
        
        voo = Model.VooModel()
        voo.numero = dados['numero']
        voo.preco = dados['preco']
        voo.aeroporto_origem = dados['origem']
        voo.aeroporto_destino = dados['destino']
        voo.horario_partida = dados['partida']
        voo.horario_chegada = dados['chegada']
        voo.quantidade_lugares = dados['lugares']        
        voo.salvar()


    def addVoo( self, voo ) :
        self._voos.append( voo )


    def voos( self ) :
        return self._voos


    def getVoo( self, numero_voo ) :
        for voo in self._voos :
            if voo.numero == numero_voo :
                return voo            
        return None
