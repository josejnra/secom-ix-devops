import unittest
import random

from app.main import imc_calc


class IMCFormulaCalcCase(unittest.TestCase):

    def test_imc_abaixo_do_peso(self):
        peso = random.uniform(50, 55)
        altura = random.uniform(1.85, 2)
        imc = imc_calc(peso, altura)
        self.assertLess(imc, 17.0)

    def test_imc_peso_normal(self):
        peso = random.uniform(66, 72.5)
        altura = random.uniform(1.7, 1.75)
        imc = imc_calc(peso, altura)
        self.assertGreaterEqual(imc, 18.5)
        self.assertLess(imc, 25.0)

    def test_imc_obesidade(self):
        peso = random.uniform(120, 150)
        altura = random.uniform(1.5, 1.7)
        imc = imc_calc(peso, altura)
        self.assertGreaterEqual(imc, 40.0)
