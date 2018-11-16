# -*- coding: utf-8 -*-
import sys

class Arquivo(object):

    '''
    Construtor da classe
    '''
    def __init__(self):
        self.__conteudo = self._lerArquivo()

    '''
    Efetua a leitura no arquivo
    '''
    def _lerArquivo(self):
        return sys.stdin.readlines()


    def _getTodoConteudo(self):

        return self.__conteudo

    def _getEstados(self):
        
        estados = self.__conteudo[1]

        estados = estados.split(',')
        estados = [estados.strip() for estados in estados]
        estados = [estados.replace("{", "").replace("}", "") for estados in estados]
        estados = list(filter(None, estados))

        return estados
    

    def _getAlfabetoEntrada(self):

        alfabetoEntrada = self.__conteudo[2]

        alfabetoEntrada = [alfabetoEntrada.strip() for alfabetoEntrada in alfabetoEntrada]
        alfabetoEntrada = [alfabetoEntrada.replace("{", "").replace("}", "").replace(",", "") for alfabetoEntrada in alfabetoEntrada]
        alfabetoEntrada = list(filter(None, alfabetoEntrada))

        return alfabetoEntrada


    def _getAlfabetoFita(self):

        alfabetoFita = self.__conteudo[3]

        alfabetoFita = [alfabetoFita.strip() for alfabetoFita in alfabetoFita]
        alfabetoFita = [alfabetoFita.replace("{", "").replace("}", "").replace(",", "") for alfabetoFita in alfabetoFita]
        alfabetoFita = list(filter(None, alfabetoFita))

        return alfabetoFita


    def _getTransicoes(self):

        # Considera como transição toda linha que contém um caractere '>'
        transicoes = [transicao for transicao in self.__conteudo if '>' in transicao]
        transicoes = [transicoes.strip() for transicoes in transicoes]
        transicoes = [transicoes.replace("-", ",").replace(">", "").replace("(", "")
                        .replace(")", "").replace("\t", "") for transicoes in transicoes]

        # Parse do tipo das transições
        transicoes = [[transicao] for transicao in transicoes]

        # Quebra as strings únicas de cada transição (linha) em elementos distintos, a partir da virgula
        for i, s in enumerate(transicoes):
            transicoes[i] = transicoes[i][0].split(',')
        
        # Remove espaços em cada um dos elementos de cada transição
        transicoes = [[y.strip() for y in x] for x in transicoes]

        # Remove elementos vazios
        for i, s in enumerate(transicoes):
            for j, s in enumerate(transicoes[i]):
                if (transicoes[i][j] == ''):
                    del transicoes[i][j]

        return transicoes

    def _getEstadoInicial(self):
        
        estadoInicial = self.__conteudo[len(self.__conteudo) -3]

        estadoInicial = [estadoInicial.strip()]
        estadoInicial = [estadoInicial.replace("{", "").replace("}", "") for estadoInicial in estadoInicial]
        
        return estadoInicial

    def _getPalavraEntrada(self):
        
        palavraEntrada = self.__conteudo[len(self.__conteudo) -1]
        # palavraEntrada = [palavraEntrada]

        return palavraEntrada
