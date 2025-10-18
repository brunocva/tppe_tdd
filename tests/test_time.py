from src.time import Equipe

def test_atualizar_estatisticas_vitoria():
    equipe = Equipe("Time A")
    equipe.atualizar_estatisticas(3, 1)
    assert equipe.pontos == 3
    assert equipe.vitorias == 1
    assert equipe.gols_marcados == 3
    assert equipe.gols_sofridos == 1

def test_atualizar_estatisticas_empate():
    equipe = Equipe("Time B")
    equipe.atualizar_estatisticas(2, 2)
    assert equipe.pontos == 1
    assert equipe.vitorias == 0
    assert equipe.gols_marcados == 2
    assert equipe.gols_sofridos == 2

def test_atualizar_estatisticas_derrota():
    equipe = Equipe("Time C")
    equipe.atualizar_estatisticas(1, 3)
    assert equipe.pontos == 0
    assert equipe.vitorias == 0
    assert equipe.gols_marcados == 1
    assert equipe.gols_sofridos == 3
