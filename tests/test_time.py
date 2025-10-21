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
