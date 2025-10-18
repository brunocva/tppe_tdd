import unittest
from src.time import Equipe

class TestEquipe(unittest.TestCase):
    def test_atualizar_estatisticas_vitoria(self):
        equipe = Equipe("Time A")
        equipe.atualizar_estatisticas(3, 1)
        self.assertEqual(equipe.pontos, 3)
        self.assertEqual(equipe.vitorias, 1)
        self.assertEqual(equipe.gols_marcados, 3)
        self.assertEqual(equipe.gols_sofridos, 1)

    def test_atualizar_estatisticas_empate(self):
        equipe = Equipe("Time B")
        equipe.atualizar_estatisticas(2, 2)
        self.assertEqual(equipe.pontos, 1)
        self.assertEqual(equipe.vitorias, 0)
        self.assertEqual(equipe.gols_marcados, 2)
        self.assertEqual(equipe.gols_sofridos, 2)

    def test_atualizar_estatisticas_derrota(self):
        equipe = Equipe("Time C")
        equipe.atualizar_estatisticas(1, 3)
        self.assertEqual(equipe.pontos, 0)
        self.assertEqual(equipe.vitorias, 0)
        self.assertEqual(equipe.gols_marcados, 1)
        self.assertEqual(equipe.gols_sofridos, 3)

if __name__ == "__main__":
    unittest.main()
