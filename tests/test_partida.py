import unittest
from src.time import Equipe
from src.partida import Partida

class TestPartida(unittest.TestCase):
    def test_processar_resultado(self):
        mandante = Equipe("Mandante")
        visitante = Equipe("Visitante")
        partida = Partida(mandante, visitante, 2, 1)
        partida.processar_resultado()

        self.assertEqual(mandante.pontos, 3)
        self.assertEqual(mandante.vitorias, 1)
        self.assertEqual(mandante.gols_marcados, 2)
        self.assertEqual(mandante.gols_sofridos, 1)

        self.assertEqual(visitante.pontos, 0)
        self.assertEqual(visitante.vitorias, 0)
        self.assertEqual(visitante.gols_marcados, 1)
        self.assertEqual(visitante.gols_sofridos, 2)

if __name__ == "__main__":
    unittest.main()
