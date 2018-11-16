from Arquivo import Arquivo
from TuringMachine import TuringMachine

arquivo = Arquivo()
estados = arquivo.get_estados()
alfabeto_entrada = arquivo.get_alfabeto_entrada()
alfabeto_fita = arquivo.get_alfabeto_fita()
transicoes = arquivo.get_transicoes()
estado_inicial = arquivo.get_estado_inicial()
palavra_entrada = arquivo.get_palavra_entrada()

turingMachine = TuringMachine(estados, alfabeto_entrada, alfabeto_fita, transicoes, estado_inicial)
turingMachine.executar(palavra_entrada)

