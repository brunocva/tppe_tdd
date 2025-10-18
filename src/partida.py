class Partida:
    """
    Representa uma partida entre duas equipes, incluindo o placar e o processamento do resultado.
    """

    def __init__(self, mandante, visitante, gols_mandante, gols_visitante):
        """
        Inicializa a partida com as equipes e os gols marcados.
        """
        if gols_mandante < 0 or gols_visitante < 0:
            raise ValueError("Gols marcados não podem ser negativos.")
        if mandante == visitante:
            raise ValueError("Uma partida não pode ter a mesma equipe como mandante e visitante.")

        self.mandante = mandante
        self.visitante = visitante
        self.gols_mandante = gols_mandante
        self.gols_visitante = gols_visitante

    def processar_resultado(self):
        """
        Atualiza as estatísticas das equipes de acordo com o resultado da partida.
        """
        # Atualiza o mandante
        self.mandante.atualizar_estatisticas(self.gols_mandante, self.gols_visitante)
        # Atualiza o visitante
        self.visitante.atualizar_estatisticas(self.gols_visitante, self.gols_mandante)

    def __str__(self):
        """
        Retorna o resultado da partida como string.
        """
        return f"{self.mandante.nome} {self.gols_mandante} x {self.gols_visitante} {self.visitante.nome}"
