class Equipe:
    # Classe que representa uma equipe no campeonato, armazenando suas estatísticas e informações.

    def __init__(self, nome):
        # Inicializa uma nova equipe com o nome fornecido e estatísticas zeradas.
        self.nome = nome
        self.pontos = 0  # Pontos acumulados pela equipe
        self.vitorias = 0  # Número de vitórias da equipe
        self.gols_marcados = 0  # Total de gols marcados pela equipe
        self.gols_sofridos = 0  # Total de gols sofridos pela equipe

    def atualizar_estatisticas(self, gols_marcados, gols_sofridos):
        # Atualiza as estatísticas da equipe com base no resultado de uma partida.
        # Verifica se os gols marcados e sofridos são válidos (não negativos).
        if gols_marcados < 0 or gols_sofridos < 0:
            raise ValueError("Gols marcados e sofridos não podem ser negativos.")

        # Atualiza os gols marcados e sofridos.
        self.gols_marcados += gols_marcados
        self.gols_sofridos += gols_sofridos
        saldo_gols = gols_marcados - gols_sofridos

        # Atualiza os pontos e vitórias com base no saldo de gols.
        if saldo_gols > 0:
            self.pontos += 3  # Vitória
            self.vitorias += 1
        elif saldo_gols == 0:
            self.pontos += 1  # Empate

    def saldo_de_gols(self):
        # Calcula o saldo de gols da equipe (gols marcados - gols sofridos).
        return self.gols_marcados - self.gols_sofridos

    def __str__(self):
        # Retorna uma representação em string das estatísticas da equipe.
        return f"{self.nome}: {self.pontos} pontos, {self.vitorias} vitórias, {self.gols_marcados} gols marcados, {self.gols_sofridos} gols sofridos"
