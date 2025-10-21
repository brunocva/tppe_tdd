from src.equipe import Equipe
from src.campeonato import Campeonato

def test_sortear_jogos():
    equipes = [Equipe(f"Time {i}") for i in range(4)]
    campeonato = Campeonato(equipes)
    campeonato.sortear_jogos()

    # Soma o total de jogos em todas as rodadas
    total_jogos = sum(len(rodada) for rodada in campeonato.rodadas)
    assert total_jogos == 6  # 4 equipes => 6 combinações (C(4,2))


def test_calcular_classificacao():
    equipe1 = Equipe("Time 1")
    equipe2 = Equipe("Time 2")
    equipe1.pontos = 6
    equipe2.pontos = 3
    campeonato = Campeonato([equipe1, equipe2])
    classificacao = campeonato.calcular_classificacao()
    assert classificacao[0].nome == "Time 1"
    assert classificacao[1].nome == "Time 2"

def test_gerar_rodadas_evitando_repeticoes():
    equipes = [Equipe(f"Time {i}") for i in range(6)]
    campeonato = Campeonato(equipes)
    campeonato.sortear_jogos()

    # Garante que há rodadas
    assert len(campeonato.rodadas) > 0

    # Verifica se não há jogos repetidos
    todos_os_jogos = [jogo for rodada in campeonato.rodadas for jogo in rodada]
    pares = {(m.nome, v.nome) for m, v in todos_os_jogos}
    assert len(pares) == len(todos_os_jogos)


def test_determinar_classificacoes():
    equipes = [Equipe(f"Time {i}") for i in range(20)]
    campeonato = Campeonato(equipes)

    for i, e in enumerate(campeonato.equipes):
        e.pontos = 100 - i  # só pra simular pontuações decrescentes

    classificacoes = campeonato.determinar_classificacoes()

    assert len(classificacoes["libertadores"]) == 6
    assert len(classificacoes["sul_americana"]) == 6
    assert len(classificacoes["rebaixados"]) == 4

