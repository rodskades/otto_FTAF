# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.chem.therm_tests - Testes com módulo unittest

IMPORT:
    import otto_FTAF.therm_tests

DESCRIÇÃO:
    Este módulo inclui testes para os módulos fuels.py, ideal_mix.py e props.py do pacote therm.
    Este módulo não é importado automaticamente ao importar otto_FTAF visto que ele não deve ser utilizado de fato em
    programas que incluem este pacote. O presente módulo deve ser executado individualmente apenas para o desenvolvedor
    testar suas modificações.
"""

# ------- #
# Imports #
# ------- #

import unittest
from otto_FTAF.therm import fuels
from otto_FTAF.therm import ideal_mix
from otto_FTAF.therm import props


# ----------------------------------------------------------------------#
#                                Tests                                 #
# ----------------------------------------------------------------------#

class ThermTestes(unittest.TestCase):

    def setUp(self):
        self.fuel1 = fuels.Fuel('C8H18')
        self.mix1 = ideal_mix.ChemMix(['C8H18', 'O2', 'N2'], [0.13, 0.8, 1.9])
        self.fuel2 = ideal_mix.FuelMix(['C8H18'], [1])
        self.mix2 = ideal_mix.OttoMix(['C8H18'], [1.0], 0.5, 100.0, 300.0, 0.00057142857)

    def test_epsilon(self):
        """
        Teste para o módulo fuels.py. Testando função epsilon().
        """
        self.assertEqual(self.fuel1.eps, 0.08)

    def test_h_form(self):
        """
        Teste para o módulo fuels.py. Testando função h_form().
        """
        self.assertEqual(self.fuel1.hf0, -208.5)

    def test_n_is(self):
        """
        Teste para o módulo fuels.py. Testando função find_n_is().
        """
        self.assertEqual(self.fuel1.n_is['C'], 8)
        self.assertEqual(self.fuel1.n_is['H'], 18)

    def test_props(self):
        """
        Teste para o módulo props.py. Testando o dicionário stdProps.
        """
        self.assertEqual(props.stdProps['CO']['n'], 'Carbon monoxide')
        self.assertIsInstance(props.stdProps['CO']['g'], dict)
        self.assertEqual(props.stdProps['CO']['g']['hf0'], -110.5)
        self.assertEqual(props.stdProps['CO']['g']['gf0'], -137.2)
        self.assertEqual(props.stdProps['CO']['g']['s_0'], 197.7)
        self.assertEqual(props.stdProps['CO']['g']['c_p'], 29.1)

    def test_mols_total(self):
        """
        Teste para o módulo ideal_mix.py. Testando função mols_total().
        """
        self.assertEqual(self.mix1.mols_total(), 2.83)

    def test_fuel_mix_n_is(self):
        """
        Teste para o módulo ideal_mix.py. Testando função n_is().
        """
        nc, nh, no, nn = self.fuel2.n_is()
        self.assertEqual([nc, nh, no, nn], [8.0, 18.0, 0.0, 0.0])

    def test_frac_molar(self):
        """
        Teste para o módulo ideal_mix.py. Testando função frac_molar().
        """
        fracoes_molares = list(self.mix1.frac_molar().values())
        self.assertEqual(sum(fracoes_molares), 1.0)

    def test_ottoMols(self):
        """
        Teste para o módulo ideal_mix.py. Testando valores de número de átomos.
        """
        nc = self.mix2.nc
        nh = self.mix2.nh
        no = self.mix2.no
        nn = self.mix2.nn
        self.assertEqual([nc, nh, no, nn], [8, 18, 0, 0])

    def test_ottoMass(self):
        """
        Teste para o módulo ideal_mix.py. Testando se a massa de entrada é igual a massa de saída.
        """
        massa_ent = self.mix2.massa_total()
        massa_sai = self.mix2.burnt_mass()
        self.assertEqual(massa_ent, massa_sai)

    def test_ottoO2(self):
        """
        Teste para o módulo ideal_mix.py. Testando função burnt_n_i().
        """
        no2 = float(f'{self.mix2.burnt_n_i()[4]:.6f}')
        self.assertEqual(no2, 0.002386)


class OttoMixTests(unittest.TestCase):

    def setUp(self):
        self.mix2 = ideal_mix.OttoMix(['C8H18'], [1.0], 0.5, 100.0, 300.0, 0.00057142857)

    def test_h_formacao(self):
        """
        Teste para o módulo ideal_mix.py. Testando função h_formacao().
        """
        self.mix2.h_formacao()
        self.assertEqual(self.mix2.h_form, -208.5)

    def test_q_total(self):
        """
        Teste para o módulo ideal_mix.py. Testando função q_total() para 4 algarismos significativos.
        """
        q = float(f'{self.mix2.q_total(0.0):.4f}')
        self.assertEqual(q, 0.9766)


if __name__ == '__main__':
    unittest.main()
