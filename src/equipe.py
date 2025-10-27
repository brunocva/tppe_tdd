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
        Atualiza as estatísticas da equipe a partir de um resultado.

        Parâmetros:
        - gols_marcados: gols marcados pela equipe nesta partida (inteiro >= 0)
        - gols_sofridos: gols sofridos pela equipe nesta partida (inteiro >= 0)

        Efeitos (mutação do objeto):
        - incrementa gols marcados/sofridos
        - atualiza pontos e contadores de vitórias/empates/derrotas

        Lança ValueError se algum dos valores de gols for negativo.
        """
        if gols_marcados < 0 or gols_sofridos < 0:
            # validação simples: gols não podem ser negativos
            raise ValueError("Os gols não podem ser negativos.")

        # atualiza totais de gols
        self.gols_marcados += gols_marcados
        self.gols_sofridos += gols_sofridos

        # atribuição de pontos conforme regras padrão do futebol
        if gols_marcados > gols_sofridos:
            # vitória: 3 pontos
            self.pontos += 3
            self.vitorias += 1
        elif gols_marcados == gols_sofridos:
            # empate: 1 ponto
            self.pontos += 1
            self.empates += 1
        else:
            # derrota: nenhum ponto, conta-se como derrota
            self.derrotas += 1

    def saldo_de_gols(self) -> int:
        """
        Retorna o saldo de gols da equipe.
        """
        return self.gols_marcados - self.gols_sofridos

    def __str__(self):
        # Representação compacta com os campos principais
        return f"{self.nome}: {self.pontos} pts, {self.vitorias}V, {self.empates}E, {self.derrotas}D | GM {self.gols_marcados} / GS {self.gols_sofridos}"
