# -*- coding: utf-8 -*-
import sys

class TuringMachine(object):

    '''
    Construtor da classe
    '''
    def __init__(self, estados, alfabetoEntrada, alfabetoFita,
                    transicoes, estadoInicial):

        self.__estados = estados
        self.__alfabetoEntrada = alfabetoEntrada
        self.__alfabetoFita = alfabetoFita
        self.__transicoes = transicoes
        self.__estadoInicial = estadoInicial


    def _executar(self, entrada):

        return False
