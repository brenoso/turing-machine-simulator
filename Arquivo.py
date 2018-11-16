import sys

class Arquivo(object):

    '''
    Construtor da classe
    '''
    def __init__(self):
        self._conteudo = self._ler_arquivo()

    def _ler_arquivo(self):
        return sys.stdin.readlines()

    def get_estados(self):
        
        estados = self._conteudo[1]
        
        # Manipulando as strings
        estados = estados.split(',')
        estados = [estados.strip() for estados in estados]
        estados = [estados.replace("{", "").replace("}", "") for estados in estados]
        estados = list(filter(None, estados))

        return estados

    def get_alfabeto_entrada(self):

        alfabetoEntrada = self._conteudo[2]

        # Manipulando as strings
        alfabetoEntrada = [alfabetoEntrada.strip() for alfabetoEntrada in alfabetoEntrada]
        alfabetoEntrada = [alfabetoEntrada.replace("{", "").replace("}", "").replace(",", "") for alfabetoEntrada in alfabetoEntrada]
        alfabetoEntrada = list(filter(None, alfabetoEntrada))

        return alfabetoEntrada

    def get_alfabeto_fita(self):

        alfabetoFita = self._conteudo[3]

        # Manipulando as strings
        alfabetoFita = [alfabetoFita.strip() for alfabetoFita in alfabetoFita]
        alfabetoFita = [alfabetoFita.replace("{", "").replace("}", "").replace(",", "") for alfabetoFita in alfabetoFita]
        alfabetoFita = list(filter(None, alfabetoFita))

        return alfabetoFita

    def get_transicoes(self):

        # Considera como transição toda linha que contém um caractere '>'
        transicoes = [transicao for transicao in self._conteudo if '>' in transicao]

        # Manipulando as strings
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

    def get_estado_inicial(self):
        
        estadoInicial = self._conteudo[len(self._conteudo) -3]

        # Manipulando as strings
        estadoInicial = [estadoInicial.strip()]
        estadoInicial = [estadoInicial.replace("{", "").replace("}", "") for estadoInicial in estadoInicial]
        
        return estadoInicial

    def get_palavra_entrada(self):
        
        palavraEntrada = self._conteudo[len(self._conteudo) -1]

        return palavraEntrada
