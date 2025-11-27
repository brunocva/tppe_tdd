import pytest
from src.campeonato import Campeonato
from src.equipe import Equipe
from src.partida import Partida


def test_registrar_confronto_mandante_vitoria():
    a = Equipe('A')
    b = Equipe('B')
    camp = Campeonato([a, b])
    camp.registrar_confronto(a, b, 2, 0)
    chave = frozenset({a.nome, b.nome})
    reg = camp.historico_confrontos[chave]
    assert reg[a.nome]['pontos'] == 3
    assert reg[a.nome]['gols_pro'] == 2
    assert reg[b.nome]['gols_pro'] == 0


def test_registrar_confronto_visitante_vitoria():
    a = Equipe('A')
    b = Equipe('B')
    camp = Campeonato([a, b])
    camp.registrar_confronto(a, b, 0, 2)
    chave = frozenset({a.nome, b.nome})
    reg = camp.historico_confrontos[chave]
    assert reg[b.nome]['pontos'] == 3
    assert reg[b.nome]['gols_pro'] == 2


def test_registrar_confronto_empate():
    a = Equipe('A')
    b = Equipe('B')
    camp = Campeonato([a, b])
    camp.registrar_confronto(a, b, 1, 1)
    chave = frozenset({a.nome, b.nome})
    reg = camp.historico_confrontos[chave]
    assert reg[a.nome]['pontos'] == 1
    assert reg[b.nome]['pontos'] == 1


def test_processar_partida_atualiza_estatisticas_e_historico():
    a = Equipe('A')
    b = Equipe('B')
    camp = Campeonato([a, b])
    partida = Partida(a, b, 2, 1)
    camp.processar_partida(partida)
    # checa estatísticas agregadas
    assert a.pontos == 3
    assert b.pontos == 0
    # checa histórico de confrontos
    chave = frozenset({a.nome, b.nome})
    assert chave in camp.historico_confrontos
    assert camp.historico_confrontos[chave][a.nome]['pontos'] == 3


def test_registrar_cartoes_validacao_e_incremento():
    e = Equipe('X')
    # validação: negativos não são permitidos
    with pytest.raises(ValueError):
        e.estatisticas.registrar_cartoes(-1, 0)
    with pytest.raises(ValueError):
        e.estatisticas.registrar_cartoes(0, -2)

    # incremento funciona
    e.estatisticas.registrar_cartoes(2, 1)
    assert e.cartoes_vermelhos == 2
    assert e.cartoes_amarelos == 1


def test_desempatar_confronto_direto_prefere_maior_pontos():
    a = Equipe('A')
    b = Equipe('B')
    camp = Campeonato([a, b])
    # registrar dois confrontos: A ganhou um, B ganhou outro => A terá saldo melhor aqui
    camp.registrar_confronto(a, b, 2, 1)
    camp.registrar_confronto(a, b, 1, 1)
    ordem = camp._desempatar_confronto_direto(a, b)
    assert ordem[0] == a


def test_ordenar_por_cartoes_menor_primeiro():
    a = Equipe('A')
    b = Equipe('B')
    # ajustar chaves básicas iguais para acionar desempate por cartões
    a.pontos = 10
    b.pontos = 10
    a.vitorias = 3
    b.vitorias = 3
    a.gols_marcados = 5
    b.gols_marcados = 5
    # definir cartões para desempate
    a.cartoes_vermelhos = 2
    a.cartoes_amarelos = 3
    b.cartoes_vermelhos = 1
    b.cartoes_amarelos = 4
    camp = Campeonato([a, b])
    ordenado = camp._ordenar_por_cartoes([a, b])
    assert ordenado[0] == b


def test_propriedades_setters_getters_e_str():
    e = Equipe('Z')
    e.pontos = 7
    e.vitorias = 2
    e.empates = 1
    e.derrotas = 0
    e.gols_marcados = 4
    e.gols_sofridos = 2
    e.cartoes_vermelhos = 1
    e.cartoes_amarelos = 2
    assert e.estatisticas.pontos == 7
    assert e.saldo_de_gols() == 2
    assert 'Z: 7 pts' in str(e)


def test_aplicar_desempates_confronto_direto_resolve():
    a = Equipe('A')
    b = Equipe('B')
    # igualar chave básica (pontos/vit/saldo/gols)
    a.pontos = b.pontos = 10
    a.vitorias = b.vitorias = 2
    a.gols_marcados = b.gols_marcados = 5
    a.gols_sofridos = b.gols_sofridos = 2
    camp = Campeonato([a, b])
    # registrar confronto direto onde A vence B
    camp.registrar_confronto(a, b, 2, 0)
    tabela = camp.calcular_classificacao()
    assert tabela[0] == a


def test_aplicar_desempates_confronto_direto_empate_vai_para_cartoes():
    a = Equipe('A')
    b = Equipe('B')
    # igualar chave básica (pontos/vit/saldo/gols)
    a.pontos = b.pontos = 8
    a.vitorias = b.vitorias = 2
    a.gols_marcados = b.gols_marcados = 4
    a.gols_sofridos = b.gols_sofridos = 2
    camp = Campeonato([a, b])
    # confronto direto empatado (1x1)
    camp.registrar_confronto(a, b, 1, 1)
    # definir cartões para que B fique à frente
    a.cartoes_vermelhos = 2
    a.cartoes_amarelos = 3
    b.cartoes_vermelhos = 1
    b.cartoes_amarelos = 1
    tabela = camp.calcular_classificacao()
    assert tabela[0] == b


def test_desempatar_confronto_direto_prefere_visitante():
    a = Equipe('A')
    b = Equipe('B')
    camp = Campeonato([a, b])
    # registrar confronto onde B vence A
    camp.registrar_confronto(a, b, 0, 2)
    ordem = camp._desempatar_confronto_direto(a, b)
    assert ordem[0] == b
