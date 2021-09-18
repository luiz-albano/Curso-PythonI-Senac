from biblioteca.Voo import VooModel
from biblioteca.Voo import VooView

class VooController :

    def cadastrarVoo() :

        #RASCUNHO DE IDEIA
        dados = VooView.obterDados()
        
        voo = VooModel()
        voo.numero = dados.numero
        voo.preco = dados.preco

        voo.salvar()

