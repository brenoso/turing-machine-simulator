import sys

class TuringMachine(object):

    '''
    Construtor da classe
    '''
    def __init__(self, estados, alfabetoEntrada, alfabetoFita,
                    transicoes, estadoInicial):

        self._estados = estados
        self._alfabeto_entrada = alfabetoEntrada
        self._alfabeto_fita = alfabetoFita
        self._transicoes = transicoes
        self._estado_inicial = estadoInicial
        self._estado_atual = self._estado_inicial[0]
        self._posicao_cabeca_leitura = 0


    def executar(self, entrada):

        self._fita = entrada
        self._houve_transicao = True

        print()
        self._imprime_configuracao_atual_fita()        
        
        while (self._houve_transicao):
            simbolo = self._fita[self._posicao_cabeca_leitura]
            self._efetuar_transicao(self._estado_atual, simbolo, self._fita)


    def _efetuar_transicao(self, estadoAtual, simbolo, fita):

        self._houve_transicao = False

        for i, s in enumerate(self._transicoes):

            # Verifica se existe a transição
            if (self._transicoes[i][0] == self._estado_atual
                    and self._transicoes[i][1] == simbolo):
            
                # Escreve o novo simbolo na fita. É necessário transformar a fita em Lista, modificá-la e voltar para
                # String, pois em python Strings são imutáveis
                fita_em_lista = list(self._fita)
                fita_em_lista[self._posicao_cabeca_leitura] = self._transicoes[i][3]
                self._fita = ''.join(map(str, fita_em_lista))

                # Atualiza o estado atual
                self._estado_atual = self._transicoes[i][2]
                
                # Atualiza a cabeça de leitura/gravação
                self._posicao_cabeca_leitura = self._posicao_cabeca_leitura + 1 if self._transicoes[i][4] == 'R' else self._posicao_cabeca_leitura - 1

                if (self._posicao_cabeca_leitura < 0):
                    sys.exit("MT Travou! Nao eh possivel executar transicao a esquerda do inicio da fita!")
                
                self._imprime_configuracao_atual_fita()
                self._houve_transicao = True

                break
    
    def _imprime_configuracao_atual_fita(self):

        # Concatena o estado atual na posicao da cabeça de L/G da fita e imprime
        configuracao = self._fita[:self._posicao_cabeca_leitura] + '{' + self._estado_atual + '}' + self._fita[self._posicao_cabeca_leitura:]
        print(configuracao)