from Arquivo import Arquivo
from TuringMachine import TuringMachine

'''
Efetua a leitura no arquivo e obtém os dados necessários
para criar a M.T.
'''
arquivo = Arquivo()
estados = arquivo.get_estados()
alfabeto_entrada = arquivo.get_alfabeto_entrada()
alfabeto_fita = arquivo.get_alfabeto_fita()
transicoes = arquivo.get_transicoes()
estado_inicial = arquivo.get_estado_inicial()
palavra_entrada = arquivo.get_palavra_entrada()

'''
Cria a M.T. com os dados do arquivo lido e a executa
'''
turingMachine = TuringMachine(estados, alfabeto_entrada, alfabeto_fita, transicoes, estado_inicial)
turingMachine.executar(palavra_entrada)

