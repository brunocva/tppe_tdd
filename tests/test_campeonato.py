from src.time import Equipe
from src.campeonato import Campeonato

def test_sortear_jogos():
    equipes = [Equipe(f"Time {i}") for i in range(4)]
    campeonato = Campeonato(equipes)
    campeonato.sortear_jogos()
    assert len(campeonato.rodadas) == 6  # 4 equipes, combinação de 2 a 2

def test_calcular_classificacao():
    equipe1 = Equipe("Time 1")
    equipe2 = Equipe("Time 2")
    equipe1.pontos = 6
    equipe2.pontos = 3
    campeonato = Campeonato([equipe1, equipe2])
    classificacao = campeonato.calcular_classificacao()
    assert classificacao[0].nome == "Time 1"
    assert classificacao[1].nome == "Time 2"
