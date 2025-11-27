class EstatisticasEquipe:
    """
    Dado extraído de Equipe para isolar a responsabilidade de armazenar
    e atualizar estatísticas.
    """

    def __init__(self):
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0

    def registrar_gols(self, gols_marcados: int, gols_sofridos: int):
        self.gols_marcados += gols_marcados
        self.gols_sofridos += gols_sofridos

    def registrar_vitoria(self):
        self.pontos += 3
        self.vitorias += 1

    def registrar_empate(self):
        self.pontos += 1
        self.empates += 1

    def registrar_derrota(self):
        self.derrotas += 1

    def saldo_de_gols(self) -> int:
        return self.gols_marcados - self.gols_sofridos


class AtualizacaoEstatisticas:
    """
    Objeto-método para atualizar estatísticas de uma equipe,
    substituindo a lógica direta no método original.
    """

    def __init__(self, equipe, gols_marcados: int, gols_sofridos: int):
        self.equipe = equipe
        self.gols_marcados = gols_marcados
        self.gols_sofridos = gols_sofridos

    def executar(self):
        self._validar_gols()
        self._atualizar_totais()
        self._registrar_resultado()

    def _validar_gols(self):
        if self.gols_marcados < 0 or self.gols_sofridos < 0:
            raise ValueError("Os gols não podem ser negativos.")

    def _atualizar_totais(self):
        self.equipe.estatisticas.registrar_gols(self.gols_marcados, self.gols_sofridos)

    def _registrar_resultado(self):
        if self.gols_marcados > self.gols_sofridos:
            self.equipe.estatisticas.registrar_vitoria()
        elif self.gols_marcados == self.gols_sofridos:
            self.equipe.estatisticas.registrar_empate()
        else:
            self.equipe.estatisticas.registrar_derrota()


class Equipe:
    """
    Representa uma equipe no campeonato, armazenando suas estatísticas.
    """

    def __init__(self, nome: str):
        self.nome = nome
        self.estatisticas = EstatisticasEquipe()

    def atualizar_estatisticas(self, gols_marcados: int, gols_sofridos: int):
        """
        Atualiza as estatísticas da equipe a partir de um resultado, delegando
        a lógica para um objeto-método dedicado.
        """
        AtualizacaoEstatisticas(self, gols_marcados, gols_sofridos).executar()

    @property
    def pontos(self):
        return self.estatisticas.pontos

    @pontos.setter
    def pontos(self, valor):
        self.estatisticas.pontos = valor

    @property
    def vitorias(self):
        return self.estatisticas.vitorias

    @vitorias.setter
    def vitorias(self, valor):
        self.estatisticas.vitorias = valor

    @property
    def empates(self):
        return self.estatisticas.empates

    @empates.setter
    def empates(self, valor):
        self.estatisticas.empates = valor

    @property
    def derrotas(self):
        return self.estatisticas.derrotas

    @derrotas.setter
    def derrotas(self, valor):
        self.estatisticas.derrotas = valor

    @property
    def gols_marcados(self):
        return self.estatisticas.gols_marcados

    @gols_marcados.setter
    def gols_marcados(self, valor):
        self.estatisticas.gols_marcados = valor

    @property
    def gols_sofridos(self):
        return self.estatisticas.gols_sofridos

    @gols_sofridos.setter
    def gols_sofridos(self, valor):
        self.estatisticas.gols_sofridos = valor

    def saldo_de_gols(self) -> int:
        """
        Retorna o saldo de gols da equipe.
        """
        return self.estatisticas.saldo_de_gols()

    def __str__(self):
        # Representação compacta com os campos principais
        return f"{self.nome}: {self.pontos} pts, {self.vitorias}V, {self.empates}E, {self.derrotas}D | GM {self.gols_marcados} / GS {self.gols_sofridos}"
