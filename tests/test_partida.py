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

def test_empate():
    mandante = Equipe("Mandante")
    visitante = Equipe("Visitante")
    partida = Partida(mandante, visitante, 1, 1)
    partida.processar_resultado()

    assert mandante.pontos == 1
    assert visitante.pontos == 1
    assert mandante.vitorias == 0
    assert visitante.vitorias == 0

def test_vitoria_visitante():
    mandante = Equipe("Mandante")
    visitante = Equipe("Visitante")
    partida = Partida(mandante, visitante, 0, 3)
    partida.processar_resultado()

    assert mandante.pontos == 0
    assert visitante.pontos == 3
    assert visitante.vitorias == 1
    assert mandante.vitorias == 0


def test_partida_gols_negativos_levanta_value_error():
    mand = Equipe('M')
    vis = Equipe('V')
    import pytest
    with pytest.raises(ValueError):
        Partida(mand, vis, -1, 0)
    with pytest.raises(ValueError):
        Partida(mand, vis, 0, -2)


def test_partida_mesmo_time_levanta_value_error():
    import pytest
    t = Equipe('T')
    with pytest.raises(ValueError):
        Partida(t, t, 1, 0)


def test_str_retorna_formato_esperado():
    m = Equipe('Mandante')
    v = Equipe('Visitante')
    p = Partida(m, v, 2, 1)
    s = str(p)
    assert 'Mandante 2 x 1 Visitante' in s
