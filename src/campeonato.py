import random

class Campeonato:
    # Classe que gerencia o campeonato, incluindo sorteio de jogos, cálculo de classificação e exibição.

    def __init__(self, equipes):
        # Inicializa um novo campeonato com as equipes fornecidas.
        self.equipes = equipes  # Lista de equipes participantes
        self.rodadas = []  # Lista de rodadas com os jogos sorteados

    def sortear_jogos(self):
        # Realiza o sorteio dos jogos para todas as rodadas do campeonato.
        self.rodadas = self._gerar_combinacoes(self.equipes)

    def _gerar_combinacoes(self, equipes):
        # Gera todas as combinações possíveis de jogos entre as equipes.
        random.shuffle(equipes)  # Embaralha a lista de equipes para garantir aleatoriedade
        combinacoes = []
        for i in range(len(equipes)):
            for j in range(i + 1, len(equipes)):
                combinacoes.append((equipes[i], equipes[j]))
        return combinacoes

    def calcular_classificacao(self):
        # Calcula a classificação das equipes com base nos critérios de pontuação.
        return sorted(
            self.equipes,
            key=lambda x: (-x.pontos, -x.vitorias, -x.saldo_de_gols(), -x.gols_marcados)
        )

    def exibir_classificacao(self):
        # Exibe a classificação atual das equipes no campeonato.
        classificacao = self.calcular_classificacao()
        self._imprimir_classificacao(classificacao)

    def _imprimir_classificacao(self, classificacao):
        # Imprime a classificação formatada.
        for i, equipe in enumerate(classificacao, start=1):
            print(f"{i}. {equipe}")
