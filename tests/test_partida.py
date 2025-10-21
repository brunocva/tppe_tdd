from src.equipe import Equipe
from src.partida import Partida

def test_processar_resultado():
    mandante = Equipe("Mandante")
    visitante = Equipe("Visitante")
    partida = Partida(mandante, visitante, 2, 1)
    partida.processar_resultado()

    assert mandante.pontos == 3
    assert mandante.vitorias == 1
    assert mandante.gols_marcados == 2
    assert mandante.gols_sofridos == 1

    assert visitante.pontos == 0
    assert visitante.vitorias == 0
    assert visitante.gols_marcados == 1
    assert visitante.gols_sofridos == 2
