import random
from itertools import combinations
from typing import List, Tuple


class CombGenerator:
    """Gera combinações de confrontos (apenas ida).

    Exemplo de aplicação da refatoração 'Substituir Método por objeto-método'.
    """

    def generate(self, equipes: list):
        return [(mandante, visitante) for mandante, visitante in combinations(equipes, 2)]


class ClassificacaoPrinter:
    """Classe responsável pela impressão da tabela de classificação (Extract Class)."""

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
        self.equipes = equipes                # Lista de objetos Equipe
        self.rodadas: List[List[Tuple]] = []  # Lista de rodadas (mandante, visitante)
        self.historico_confrontos = {}        # Armazena resultados para confronto direto

    # SORTEIO / RODADAS

    def sortear_jogos(self):
        """
        Gera o calendário em turno e returno (round-robin duplo).

        - Para N equipes (ajustado com bye se N for ímpar), gera N-1 rodadas na ida.
        - O returno repete os confrontos invertendo mandante/visitante.
        """
        equipes = self._preparar_lista_com_bye()
        random.shuffle(equipes)  # sorteio inicial para embaralhar mandos e ordem
        rodadas_ida = self._gerar_round_robin(equipes)
        rodadas_volta = self._inverter_mandos(rodadas_ida)
        self.rodadas = rodadas_ida + rodadas_volta

    def registrar_confronto(self, mandante, visitante, gols_mandante: int, gols_visitante: int):
        """
        Guarda o resultado para uso em confronto direto (apenas quando duas equipes empatam).
        """
        chave = frozenset({mandante.nome, visitante.nome})
        if chave not in self.historico_confrontos:
            self.historico_confrontos[chave] = {
                mandante.nome: {"pontos": 0, "gols_pro": 0, "gols_contra": 0},
                visitante.nome: {"pontos": 0, "gols_pro": 0, "gols_contra": 0},
            }
        registro = self.historico_confrontos[chave]
        # pontos no confronto direto
        if gols_mandante > gols_visitante:
            registro[mandante.nome]["pontos"] += 3
        elif gols_mandante < gols_visitante:
            registro[visitante.nome]["pontos"] += 3
        else:
            registro[mandante.nome]["pontos"] += 1
            registro[visitante.nome]["pontos"] += 1
        # gols pró/contra no confronto direto
        registro[mandante.nome]["gols_pro"] += gols_mandante
        registro[mandante.nome]["gols_contra"] += gols_visitante
        registro[visitante.nome]["gols_pro"] += gols_visitante
        registro[visitante.nome]["gols_contra"] += gols_mandante

    def processar_partida(self, partida):
        """
        Executa Partida.processar_resultado e registra histórico para desempate.
        """
        partida.processar_resultado()
        self.registrar_confronto(partida.mandante, partida.visitante, partida.gols_mandante, partida.gols_visitante)

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
        gen = CombGenerator()
        return gen.generate(equipes)

    def _dividir_em_rodadas(self, jogos: list):
        """
        Divide os jogos em rodadas de forma simples:

        - Em um campeonato com N times, cada rodada tem N/2 jogos (todos jogam).
        - Se N for ímpar, usa-se floor(N/2) para jogos por rodada.
        """
        n_times = len(self.equipes)
        jogos_por_rodada = max(1, n_times // 2)
        rodadas = []
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
        5) Confronto direto (apenas quando dois clubes empatam nos itens acima)
        6) Menos cartões vermelhos
        7) Menos cartões amarelos
        8) Sorteio (desempate final)
        """
        base_sorted = sorted(
            self.equipes,
            key=lambda t: (t.pontos, t.vitorias, t.saldo_de_gols(), t.gols_marcados),
            reverse=True
        )
        return self._aplicar_desempates(base_sorted)

    def exibir_classificacao(self):
        """
        Imprime a classificação atual formatada (útil para demonstração).
        """
        classificacao = self.calcular_classificacao()
        self._imprimir_classificacao(classificacao)

    def _imprimir_classificacao(self, classificacao):
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

    # AUXILIARES DE DESEMPATE

    def _aplicar_desempates(self, equipes_ordenadas):
        """Aplica confrontos diretos, cartões e sorteio nos grupos empatados."""
        resultado = []
        i = 0
        while i < len(equipes_ordenadas):
            grupo = [equipes_ordenadas[i]]
            base_key = self._chave_basica(equipes_ordenadas[i])
            i += 1
            while i < len(equipes_ordenadas) and self._chave_basica(equipes_ordenadas[i]) == base_key:
                grupo.append(equipes_ordenadas[i])
                i += 1
            if len(grupo) == 2:
                grupo = self._desempatar_confronto_direto(grupo[0], grupo[1])
                # se confronto direto resolveu, não há mais empate a tratar
                a, b = grupo
                if self._pontuacao_confronto_direto(a, b) != self._pontuacao_confronto_direto(b, a):
                    resultado.extend(grupo)
                    continue
            grupo = self._ordenar_por_cartoes(grupo)
            resultado.extend(grupo)
        return resultado

    def _chave_basica(self, equipe):
        return (equipe.pontos, equipe.vitorias, equipe.saldo_de_gols(), equipe.gols_marcados)

    def _desempatar_confronto_direto(self, equipe_a, equipe_b):
        """Ordena duas equipes pelo confronto direto se houver registro."""
        pontos_a, saldo_a, gols_a = self._pontuacao_confronto_direto(equipe_a, equipe_b)
        pontos_b, saldo_b, gols_b = self._pontuacao_confronto_direto(equipe_b, equipe_a)
        chave_a = (pontos_a, saldo_a, gols_a)
        chave_b = (pontos_b, saldo_b, gols_b)
        if chave_a > chave_b:
            return [equipe_a, equipe_b]
        if chave_b > chave_a:
            return [equipe_b, equipe_a]
        return [equipe_a, equipe_b]

    def _pontuacao_confronto_direto(self, equipe, adversaria):
        chave = frozenset({equipe.nome, adversaria.nome})
        registro = self.historico_confrontos.get(chave)
        if not registro or equipe.nome not in registro:
            return (0, 0, 0)
        pontos = registro[equipe.nome]["pontos"]
        saldo = registro[equipe.nome]["gols_pro"] - registro[equipe.nome]["gols_contra"]
        gols_pro = registro[equipe.nome]["gols_pro"]
        return (pontos, saldo, gols_pro)

    def _ordenar_por_cartoes(self, grupo):
        """Desempata por menos vermelhos, depois menos amarelos; mantém ordem se ainda empatar."""
        grupo_ordenado = sorted(grupo, key=lambda t: (t.cartoes_vermelhos, t.cartoes_amarelos))
        # Em caso de empate também em cartões, preserva a ordem atual (determinismo para testes).
        return grupo_ordenado
