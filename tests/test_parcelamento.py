import unittest

from organizador.parcelamento import Parcelamento


class TestParcelaEm(unittest.TestCase):
    def setUp(self):
        # 3 parcelas, de nov/2026 a jan/2027
        self.p = Parcelamento("Notebook", 15000, 3, 2026, 11)

    def test_antes_do_inicio(self):
        self.assertIsNone(self.p.parcela_em(2026, 10))

    def test_durante(self):
        self.assertEqual(self.p.parcela_em(2026, 11), 1)
        self.assertEqual(self.p.parcela_em(2026, 12), 2)

    def test_virada_de_ano(self):
        self.assertEqual(self.p.parcela_em(2027, 1), 3)

    def test_depois_do_termino(self):
        self.assertIsNone(self.p.parcela_em(2027, 2))

    def test_mes_invalido(self):
        with self.assertRaises(ValueError):
            self.p.parcela_em(2026, 13)

    def test_parcelas_invalidas(self):
        p = Parcelamento("X", 100, 0, 2026, 1)
        with self.assertRaises(ValueError):
            p.parcela_em(2026, 1)

    def test_mes_inicio_invalido(self):
        p = Parcelamento("X", 100, 3, 2026, 0)
        with self.assertRaises(ValueError):
            p.parcela_em(2026, 1)


if __name__ == "__main__":
    unittest.main()