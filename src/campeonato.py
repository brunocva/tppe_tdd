import random
from itertools import combinations
from typing import List, Tuple


class CombGenerator:
    """Gera combinações de confrontos (apenas ida).

    Exemplo de aplicação da refatoração 'Substituir método por objeto-método'.
    """

    def generate(self, equipes: list):
        return [(mandante, visitante) for mandante, visitante in combinations(equipes, 2)]


class ClassificacaoPrinter:
    """Classe responsável pela impressão da tabela de classificação.

    Extraída do método privado para separar responsabilidade (Extract Class).
    """

    @staticmethod
    def imprimir(classificacao):
        print("\n===== CLASSIFICAÇÃO =====")
        print(f"{'Pos':<4}{'Time':<20}{'Pts':<5}{'Vit':<5}{'SG':<5}{'GM':<5}{'GS':<5}")
        for i, e in enumerate(classificacao, start=1):
            print(f"{i:<4}{e.nome:<20}{e.pontos:<5}{e.vitorias:<5}{e.saldo_de_gols():<5}{e.gols_marcados:<5}{e.gols_sofridos:<5}")

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


    # SORTEIO / RODADAS

    def sortear_jogos(self):
        """
        Gera o calendário em turno e returno (round-robin duplo).

        - Para N equipes (ajustado com bye se N for ímpar), gera N-1 rodadas na ida.
        - O returno repete os confrontos invertendo mandante/visitante.
        """
        equipes = self._preparar_lista_com_bye()
        rodadas_ida = self._gerar_round_robin(equipes)
        rodadas_volta = self._inverter_mandos(rodadas_ida)
        self.rodadas = rodadas_ida + rodadas_volta

    def _preparar_lista_com_bye(self):
        """
        Garante número par de equipes, adicionando um bye (None) quando necessário.
        """
        lista = self.equipes[:]
        if len(lista) % 2 != 0:
            lista.append(None)
        return lista

    def _gerar_round_robin(self, equipes):
        """Gera as rodadas de uma perna (ida) usando o algoritmo round-robin."""
        rodadas = []
        lista_rotativa = equipes[:]
        total_rodadas = len(lista_rotativa) - 1
        for _ in range(total_rodadas):
            rodadas.append(self._gerar_rodada(lista_rotativa))
            lista_rotativa = self._rotacionar_equipes(lista_rotativa)
        return rodadas

    def _gerar_rodada(self, lista):
        """
        Cria uma rodada a partir do arranjo atual de equipes.
        """
        rodada = []
        n = len(lista)
        for indice in range(n // 2):
            mandante = lista[indice]
            visitante = lista[n - 1 - indice]
            if mandante is not None and visitante is not None:
                rodada.append((mandante, visitante))
        return rodada

    def _rotacionar_equipes(self, lista):
        """
        Roda a lista mantendo o primeiro elemento fixo (algoritmo round-robin).
        """
        return [lista[0]] + [lista[-1]] + lista[1:-1]

    def _inverter_mandos(self, rodadas):
        """Cria o returno invertendo mandante/visitante de cada jogo."""
        rodadas_invertidas = []
        for rodada in rodadas:
            rodada_volta = [(vis, man) for man, vis in rodada]
            rodadas_invertidas.append(rodada_volta)
        return rodadas_invertidas

    def _gerar_combinacoes(self, equipes: list):
        """
        Retorna todas as combinações possíveis de confrontos (somente ida).

        Recebe uma lista de equipes (objetos) e retorna pares (mandante, visitante).
        Exemplo: para [A, B, C, D] retorna 6 combinações distintas.
        """
        # Substitui a implementação direta por um objeto gerador para
        # demonstrar a refatoração "Substituir método por objeto-método".
        gen = CombGenerator()
        return gen.generate(equipes)

    def _dividir_em_rodadas(self, jogos: list):
        """
        Divide os jogos em rodadas de forma simples:

        - Em um campeonato com N times, cada rodada tem N/2 jogos (todos jogam).
        - Se N for ímpar, usa-se floor(N/2) para jogos por rodada.

        Mantido simples para fins de TDD.
        """
        n_times = len(self.equipes)
        # calculamos quantos jogos por rodada (N times -> N/2 jogos por rodada)
        jogos_por_rodada = max(1, n_times // 2)
        rodadas = []
        # particionamos a lista de jogos em blocos de tamanho jogos_por_rodada
        for i in range(0, len(jogos), jogos_por_rodada):
            rodadas.append(jogos[i:i + jogos_por_rodada])
        return rodadas

 
    # CLASSIFICAÇÃO

    def calcular_classificacao(self):
        """
        Retorna a tabela ordenada pelos critérios do enunciado:
        1) Pontos
        2) Número de vitórias
        3) Saldo de gols
        4) Gols marcados
        """
        # Ordena em ordem decrescente por (pontos, vitórias, saldo, gols marcados).
        # Observação: cada objeto em self.equipes deve expor os atributos usados.
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
        # Delegar impressão a ClassificacaoPrinter (Extract Class)
        ClassificacaoPrinter.imprimir(classificacao)


    # COMPETIÇÕES / REBAIXAMENTO

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
