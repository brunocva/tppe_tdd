# tests/test_equipe_extra.py
import pytest
from src.equipe import Equipe

@pytest.mark.parametrize(
    "nome, gols_marcados, gols_sofridos, pontos_esperados, vitorias_esperadas",
    [
        ("Time A", 3, 1, 3, 1),  # Vitória
        ("Time B", 2, 2, 1, 0),  # Empate
        ("Time C", 1, 3, 0, 0),  # Derrota
    ],
)
def test_atualizar_estatisticas(nome, gols_marcados, gols_sofridos, pontos_esperados, vitorias_esperadas):
    equipe = Equipe(nome)
    equipe.atualizar_estatisticas(gols_marcados, gols_sofridos)

    assert equipe.pontos == pontos_esperados
    assert equipe.vitorias == vitorias_esperadas
    assert equipe.gols_marcados == gols_marcados
    assert equipe.gols_sofridos == gols_sofridos

def test_atualizar_estatisticas_gols_negativos():
    """Deve levantar ValueError se gols forem negativos."""
    equipe = Equipe("Flamengo")
    with pytest.raises(ValueError):
        equipe.atualizar_estatisticas(-1, 0)
    with pytest.raises(ValueError):
        equipe.atualizar_estatisticas(0, -2)


def test_vitoria_derrota_empate_contabilizacao():
    """Testa se as estatísticas são atualizadas corretamente após diferentes resultados."""
    time = Equipe("Palmeiras")

    # Vitória
    time.atualizar_estatisticas(3, 1)
    assert (time.pontos, time.vitorias, time.empates, time.derrotas) == (3, 1, 0, 0)

    # Empate
    time.atualizar_estatisticas(2, 2)
    assert (time.pontos, time.vitorias, time.empates, time.derrotas) == (4, 1, 1, 0)

    # Derrota
    time.atualizar_estatisticas(0, 1)
    assert (time.pontos, time.vitorias, time.empates, time.derrotas) == (4, 1, 1, 1)


def test_saldo_de_gols_varios_jogos():
    """Testa se o saldo de gols é calculado corretamente após várias partidas."""
    time = Equipe("Corinthians")
    resultados = [(2, 1), (1, 1), (0, 3)]  # +1, 0, -3 → total -2

    for gm, gs in resultados:
        time.atualizar_estatisticas(gm, gs)

    assert time.saldo_de_gols() == -2
    assert time.gols_marcados == 3
    assert time.gols_sofridos == 5


def test_saldo_de_gols_consistente():
    time = Equipe("Grêmio")
    partidas = [(1, 0), (0, 2), (3, 3), (2, 1)]  # saldo: +1, -2, 0, +1 => total 0
    for gm, gs in partidas:
        time.atualizar_estatisticas(gm, gs)
    assert time.saldo_de_gols() == 0
    assert time.gols_marcados == 6
    assert time.gols_sofridos == 6


def test_str_formatacao():
    """Verifica se a formatação do __str__ contém informações esperadas."""
    time = Equipe("Botafogo")
    time.atualizar_estatisticas(2, 0)  # vitória
    texto = str(time)
    assert "Botafogo" in texto
    assert "3 pts" in texto
    assert "1V" in texto
    assert "0E" in texto
    assert "0D" in texto
    assert "GM 2" in texto
    assert "GS 0" in texto


def test_derrota_nao_soma_pontos():
    time = Equipe("Santos")
    time.atualizar_estatisticas(0, 2)  # derrota
    assert time.pontos == 0
    assert time.vitorias == 0
    assert time.empates == 0
    assert time.derrotas == 1
    assert time.gols_marcados == 0
    assert time.gols_sofridos == 2

def test_acumula_multiplas_partidas_misto_totais():
    """
    2 vitórias (2x0, 3x1), 1 empate (1x1), 1 derrota (0x2)
    Pontos: 3+3+1+0 = 7
    """
    time = Equipe("Athletico-PR")
    partidas = [(2, 0), (1, 1), (0, 2), (3, 1)]
    for gm, gs in partidas:
        time.atualizar_estatisticas(gm, gs)

    assert time.pontos == 7
    assert time.vitorias == 2
    assert time.empates == 1
    assert time.derrotas == 1
    assert time.gols_marcados == 6  # 2+1+0+3
    assert time.gols_sofridos == 4  # 0+1+2+1
    assert time.saldo_de_gols() == 2


