import sys
from Arquivo import Arquivo
from TuringMachine import TuringMachine

arquivo = Arquivo()

estados = arquivo._getEstados()
print("estados: ")
print(estados)

alfabetoEntrada = arquivo._getAlfabetoEntrada()
print("alfabetoEntrada: ")
print(alfabetoEntrada)

alfabetoFita = arquivo._getAlfabetoFita()
print("alfabetoFita: ")
print(alfabetoFita)

transicoes = arquivo._getTransicoes()
print("transicoes: ")
print(transicoes)

estadoInicial = arquivo._getEstadoInicial()
print("estadoInicial: ")
print(estadoInicial)

palavraEntrada = arquivo._getPalavraEntrada()
print("palavraEntrada: ")
print(palavraEntrada)

turingMachine = TuringMachine(estados, alfabetoEntrada, alfabetoFita, transicoes, estadoInicial)
turingMachine._executar(palavraEntrada)

