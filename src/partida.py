class Partida:
    """
    Representa uma partida entre duas equipes, incluindo os resultados.

    Atributos:
        mandante (Equipe): Equipe mandante.
        visitante (Equipe): Equipe visitante.
        gols_mandante (int): Gols marcados pela equipe mandante.
        gols_visitante (int): Gols marcados pela equipe visitante.
    """

    def __init__(self, mandante, visitante, gols_mandante, gols_visitante):
        """
        Inicializa uma nova partida com as equipes e os resultados fornecidos.

        Args:
            mandante (Equipe): Equipe mandante.
            visitante (Equipe): Equipe visitante.
            gols_mandante (int): Gols marcados pela equipe mandante.
            gols_visitante (int): Gols marcados pela equipe visitante.

        Raises:
            ValueError: Se os gols marcados forem negativos ou se as equipes forem iguais.
        """
        # Verifica se os gols marcados são válidos e se as equipes são diferentes.
        if gols_mandante < 0 or gols_visitante < 0:
            raise ValueError("Gols marcados não podem ser negativos.")
        if mandante == visitante:
            raise ValueError("Uma partida não pode ter a mesma equipe como mandante e visitante.")

        self.mandante = mandante  # Equipe mandante
        self.visitante = visitante  # Equipe visitante
        self.gols_mandante = gols_mandante  # Gols marcados pela equipe mandante
        self.gols_visitante = gols_visitante  # Gols marcados pela equipe visitante

    def processar_resultado(self):
        """
        Atualiza as estatísticas das equipes com base no resultado da partida.
        """
        self.mandante.atualizar_estatisticas(self.gols_mandante, self.gols_visitante)
        self.visitante.atualizar_estatisticas(self.gols_visitante, self.gols_mandante)

    def __str__(self):
        """
        Retorna uma representação em string do resultado da partida.

        Returns:
            str: Resultado da partida formatado.
        """
        return f"{self.mandante.nome} {self.gols_mandante} x {self.gols_visitante} {self.visitante.nome}"
