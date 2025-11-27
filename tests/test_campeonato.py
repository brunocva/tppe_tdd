from src.equipe import Equipe
from src.campeonato import Campeonato 
from src.partida import Partida

def test_sortear_jogos():
    equipes = [Equipe(f"Time {i}") for i in range(4)]
    campeonato = Campeonato(equipes)
    campeonato.sortear_jogos()

    # Soma o total de jogos em todas as rodadas
    total_jogos = sum(len(rodada) for rodada in campeonato.rodadas)
    assert total_jogos == 12  # 4 equipes => ida+volta (6 combinacoes * 2)


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

def test_desempate_por_numero_de_vitorias_mesmos_pontos():
    equipes = [
        Equipe("A"), Equipe("B"), Equipe("C"),
        Equipe("D"), Equipe("E"), Equipe("F")
    ]
    camp = Campeonato(equipes)
    camp.sortear_jogos()

    # pega referências às Equipes já criadas dentro do Campeonato
    A = next(e for e in camp.equipes if e.nome == "A")
    B = next(e for e in camp.equipes if e.nome == "B")

    # escolhe oponentes diferentes para A
    oponentes_A = [e for e in camp.equipes if e.nome not in ("A", "B")][:2]

    # A: vence primeiro, perde o segundo
    Partida(A, oponentes_A[0], 2, 0).processar_resultado()  # vitória de A
    Partida(A, oponentes_A[1], 0, 1).processar_resultado()  # derrota de A

    # B: 3 empates contra três oponentes
    oponentes_B = [e for e in camp.equipes if e.nome not in ("A", "B")][:3]
    for opp in oponentes_B:
        Partida(B, opp, 0, 0).processar_resultado()

    tabela = camp.calcular_classificacao()
    nomes = [t.nome for t in tabela]
    assert nomes.index("A") < nomes.index("B"), \
        "Com 3 pts cada, A (mais vitórias) deve ficar à frente de B"

def test_todos_os_times_jogam_uma_vez_por_rodada():
    equipes = [Equipe(f"Time {i}") for i in range(6)]
    campeonato = Campeonato(equipes)
    campeonato.sortear_jogos()
    for rodada in campeonato.rodadas:
        times_na_rodada = set()
        for mandante, visitante in rodada:
            times_na_rodada.add(mandante.nome)
            times_na_rodada.add(visitante.nome)
        assert len(times_na_rodada) == len(equipes), "Nem todos os times jogaram na rodada"

def test_desempate_por_saldo_de_gols():
    equipes = [Equipe("A"), Equipe("B")]
    camp = Campeonato(equipes)
    A, B = camp.equipes
    # Ambos com 3 pontos, mas A tem saldo melhor
    Partida(A, B, 2, 0).processar_resultado()  # A vence
    Partida(B, A, 1, 0).processar_resultado()  # B vence
    tabela = camp.calcular_classificacao()
    assert tabela[0].nome == "A" and tabela[1].nome == "B", "A deve ficar à frente por saldo de gols"

def test_desempate_por_gols_marcados():
    equipes = [Equipe("A"), Equipe("B")]
    camp = Campeonato(equipes)
    A, B = camp.equipes
    # Ambos vencem um jogo por 2x0 e perdem por 2x0, mas A faz mais gols em outro empate
    Partida(A, B, 2, 0).processar_resultado()  # A vence
    Partida(B, A, 2, 0).processar_resultado()  # B vence
    Partida(A, B, 3, 3).processar_resultado()  # empate, A faz mais gols no total
    tabela = camp.calcular_classificacao()
    assert tabela[0].nome == "A" and tabela[1].nome == "B", "A deve ficar à frente por gols marcados"

def test_confrontos_ocorrem_duas_vezes_no_maximo():
    equipes = [Equipe(f"Time {i}") for i in range(4)]
    campeonato = Campeonato(equipes)
    campeonato.sortear_jogos()
    confrontos = {}
    for rodada in campeonato.rodadas:
        for mandante, visitante in rodada:
            chave = tuple(sorted([mandante.nome, visitante.nome]))
            confrontos[chave] = confrontos.get(chave, 0) + 1
    for qtd in confrontos.values():
        assert qtd <= 2, "Cada confronto deve ocorrer no máximo duas vezes (turno e returno)"

def gerar_rodadas(equipes):
    """Gera rodadas no formato round-robin para número par de equipes."""
    if len(equipes) % 2 != 0:
        equipes.append(None)  # Adiciona um 'bye' se for ímpar

    n = len(equipes)
    rodadas = []
    lista = equipes[:]
    for i in range(n - 1):
        rodada = []
        for j in range(n // 2):
            time1 = lista[j]
            time2 = lista[n - 1 - j]
            if time1 is not None and time2 is not None:
                rodada.append((time1, time2))
        lista = [lista[0]] + [lista[-1]] + lista[1:-1]
        rodadas.append(rodada)
    return rodadas


def test_gerar_combinacoes_retorna_todas_as_parcerias():
    equipes = [Equipe(f"T{i}") for i in range(4)]
    camp = Campeonato(equipes)
    combos = camp._gerar_combinacoes(camp.equipes)
    # C(4,2) = 6 combinações
    assert len(combos) == 6
    # checa presença de uma combinação esperada
    assert any(c[0].nome == 'T0' and c[1].nome == 'T1' for c in combos)


def test_dividir_em_rodadas_chunck_simples():
    equipes = [Equipe(f"T{i}") for i in range(6)]
    camp = Campeonato(equipes)
    jogos = list(range(6))  # objetos arbitrários representam jogos
    rodadas = camp._dividir_em_rodadas(jogos)
    # Para 6 equipes, jogos_por_rodada = 3
    assert all(len(r) <= 3 for r in rodadas)
    # Deve produzir pelo menos duas rodadas para 6 jogos com chunk=3
    assert len(rodadas) == 2


def test_sortear_jogos_com_numero_impar_inclui_bye_e_divide_corretamente():
    equipes = [Equipe(f"Time {i}") for i in range(5)]
    camp = Campeonato(equipes)
    camp.sortear_jogos()

    # Para 5 times, espera-se 10 rodadas (ida+volta com bye) e 2 jogos por rodada
    assert len(camp.rodadas) == 10
    for rodada in camp.rodadas:
        # cada rodada deve conter exatamente 2 jogos (um time em bye)
        assert len(rodada) == 2


def test_exibir_classificacao_imprime_formato(capsys):
    a = Equipe('A')
    b = Equipe('B')
    a.pontos = 3
    b.pontos = 0
    camp = Campeonato([a, b])
    camp.exibir_classificacao()
    out = capsys.readouterr().out
    assert 'CLASSIFICAÇÃO' in out
    assert 'A' in out
    assert 'B' in out
