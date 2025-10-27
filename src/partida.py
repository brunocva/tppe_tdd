class Partida:
    """
    Representa uma partida entre duas equipes, incluindo o placar e o processamento do resultado.
    """

    def __init__(self, mandante, visitante, gols_mandante, gols_visitante):
        """
        Inicializa a partida com as equipes e os gols marcados.
        """
        # Validações básicas: não aceitamos gols negativos nem o mesmo time em ambas as posições
        if gols_mandante < 0 or gols_visitante < 0:
            raise ValueError("Gols marcados não podem ser negativos.")
        if mandante == visitante:
            raise ValueError("Uma partida não pode ter a mesma equipe como mandante e visitante.")

        # Atribui campos — objetos mandante/visitante devem ser instâncias de Equipe
        self.mandante = mandante
        self.visitante = visitante
        self.gols_mandante = gols_mandante
        self.gols_visitante = gols_visitante

    def processar_resultado(self):
        """
        Atualiza as estatísticas das equipes de acordo com o resultado da partida.
        """
        # Atualiza as estatísticas de cada equipe.
        # Observação: primeiro atualizamos o mandante, depois o visitante. A ordem
        # não altera o resultado final porque cada chamada atualiza o objeto correspondente.
        self.mandante.atualizar_estatisticas(self.gols_mandante, self.gols_visitante)
        self.visitante.atualizar_estatisticas(self.gols_visitante, self.gols_mandante)

    def __str__(self):
        """
        Retorna o resultado da partida como string.
        """
        # Formato: "Mandante <gols_mandante> x <gols_visitante> Visitante"
        return f"{self.mandante.nome} {self.gols_mandante} x {self.gols_visitante} {self.visitante.nome}"
