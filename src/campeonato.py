import random
from itertools import combinations
from typing import List, Tuple

class Campeonato:
    """
    Gerencia o campeonato: sorteio de jogos (organizados em rodadas),
    cálculo da classificação e relatórios auxiliares.
    """

    def __init__(self, equipes: list):
        """
        Inicializa o campeonato com uma lista de equipes participantes.
        """
        self.equipes = equipes              # Lista de objetos Equipe
        self.rodadas: List[List[Tuple]] = []  # Lista de rodadas, cada rodada é uma lista de jogos (mandante, visitante)

    # ----------------------------
    # SORTEIO / RODADAS
    # ----------------------------
    def sortear_jogos(self):
        equipes = self.equipes[:]
        if len(equipes) % 2 != 0:
            equipes.append(None)  # Adiciona um 'bye' se for ímpar

        n = len(equipes)
        rodadas = []
        lista = equipes[:]
        for i in range(n - 1):
            rodada = []
            for j in range(n // 2):
                time1 = lista[j]
                time2 = lista[n - 1 - j]
                if time1 is not None and time2 is not None:
                    rodada.append((time1, time2))
            lista = [lista[0]] + [lista[-1]] + lista[1:-1]
            rodadas.append(rodada)
        self.rodadas = rodadas

    def _gerar_combinacoes(self, equipes: list):
        """
        Retorna todas as combinações possíveis de confrontos (apenas ida).

        Ex.: para [A, B, C, D] -> (A,B), (A,C), (A,D), (B,C), (B,D), (C,D) — 6 jogos.
        """
        return [(mandante, visitante) for mandante, visitante in combinations(equipes, 2)]

    def _dividir_em_rodadas(self, jogos: list):
        """
        Divide os jogos em rodadas de forma simples:

        - Em um campeonato com N times, cada rodada tem N/2 jogos (todos jogam).
        - Se N for ímpar, usa-se floor(N/2) para jogos por rodada.

        Mantido simples para fins de TDD.
        """
        n_times = len(self.equipes)
        jogos_por_rodada = max(1, n_times // 2)
        rodadas = []
        for i in range(0, len(jogos), jogos_por_rodada):
            rodadas.append(jogos[i:i + jogos_por_rodada])
        return rodadas

    # ----------------------------
    # CLASSIFICAÇÃO
    # ----------------------------
    def calcular_classificacao(self):
        """
        Retorna a tabela ordenada pelos critérios do enunciado:
        1) Pontos
        2) Número de vitórias
        3) Saldo de gols
        4) Gols marcados
        """
        return sorted(
            self.equipes,
            key=lambda t: (t.pontos, t.vitorias, t.saldo_de_gols(), t.gols_marcados),
            reverse=True
        )

    def exibir_classificacao(self):
        """
        Imprime a classificação atual formatada (útil para demonstração).
        """
        classificacao = self.calcular_classificacao()
        self._imprimir_classificacao(classificacao)

    def _imprimir_classificacao(self, classificacao):
        print("\n===== CLASSIFICAÇÃO =====")
        print(f"{'Pos':<4}{'Time':<20}{'Pts':<5}{'Vit':<5}{'SG':<5}{'GM':<5}{'GS':<5}")
        for i, e in enumerate(classificacao, start=1):
            print(f"{i:<4}{e.nome:<20}{e.pontos:<5}{e.vitorias:<5}{e.saldo_de_gols():<5}{e.gols_marcados:<5}{e.gols_sofridos:<5}")

    # ----------------------------
    # COMPETIÇÕES / REBAIXAMENTO
    # ----------------------------
    def determinar_classificacoes(self):
        """
        Determina os grupos de classificação (contexto do enunciado):
        - 6 primeiros: Libertadores
        - 7º ao 12º: Sul-Americana
        - 4 últimos: Rebaixados
        """
        tabela = self.calcular_classificacao()
        return {
            "libertadores": [t.nome for t in tabela[:6]],
            "sul_americana": [t.nome for t in tabela[6:12]],
            "rebaixados": [t.nome for t in tabela[-4:]]
        }
