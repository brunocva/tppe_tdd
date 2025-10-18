class Equipe:
    """
    Representa uma equipe no campeonato, armazenando suas estatísticas.
    """

    def __init__(self, nome: str):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0

    def atualizar_estatisticas(self, gols_marcados: int, gols_sofridos: int):
        """
        Atualiza as estatísticas da equipe com base no resultado de uma partida.
        """
        if gols_marcados < 0 or gols_sofridos < 0:
            raise ValueError("Os gols não podem ser negativos.")

        self.gols_marcados += gols_marcados
        self.gols_sofridos += gols_sofridos

        if gols_marcados > gols_sofridos:
            self.pontos += 3
            self.vitorias += 1
        elif gols_marcados == gols_sofridos:
            self.pontos += 1
            self.empates += 1
        else:
            self.derrotas += 1

    def saldo_de_gols(self) -> int:
        """
        Retorna o saldo de gols da equipe.
        """
        return self.gols_marcados - self.gols_sofridos

    def __str__(self):
        return f"{self.nome}: {self.pontos} pts, {self.vitorias}V, {self.empates}E, {self.derrotas}D | GM {self.gols_marcados} / GS {self.gols_sofridos}"
