# Arquivo inicial do sistema
# 
# MVC
#
# M - Model: represetação do modelo de negócio
# V - View: controlar a apresentação (interfaces gráficas)
# C - Controller: controla as ações do usuário na interface 
#     e conecta com o modelo de negócollections
# obs: enviar referências aos alunos
from biblioteca.Voo import VooController as VooController

VooController = VooController.VooController

def main() :
    voos = VooController()
    print( voos.voos() )

main()