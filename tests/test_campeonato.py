import unittest
from src.time import Equipe
from src.campeonato import Campeonato

class TestCampeonato(unittest.TestCase):
    def test_sortear_jogos(self):
        equipes = [Equipe(f"Time {i}") for i in range(4)]
        campeonato = Campeonato(equipes)
        campeonato.sortear_jogos()
        self.assertEqual(len(campeonato.rodadas), 6)  # 4 equipes, combinação de 2 a 2

    def test_calcular_classificacao(self):
        equipe1 = Equipe("Time 1")
        equipe2 = Equipe("Time 2")
        equipe1.pontos = 6
        equipe2.pontos = 3
        campeonato = Campeonato([equipe1, equipe2])
        classificacao = campeonato.calcular_classificacao()
        self.assertEqual(classificacao[0].nome, "Time 1")
        self.assertEqual(classificacao[1].nome, "Time 2")

if __name__ == "__main__":
    unittest.main()
