# This Python file uses the following encoding: utf-8

# -------------------- #
#    Documentation     #
# -------------------- #

"""
NOME:
    otto_FTAF.chem.chem_tests - Testes com módulo unittest

IMPORT:
    import otto_FTAF.chem_tests

DESCRIÇÃO:
    Este módulo inclui testes para os módulos air.py, elem.py e molec.py do pacote chem.
    Este módulo não é importado automaticamente ao importar otto_FTAF visto que ele não deve ser utilizado de fato em
    programas que incluem este pacote. O presente módulo deve ser executado individualmente apenas para o desenvolvedor
    testar suas modificações.
"""

# ------- #
# Imports #
# ------- #

import unittest
from otto_FTAF.chem import air
from otto_FTAF.chem import elem
from otto_FTAF.chem import molec


# ---------- #
#   Testes   #
# ---------- #

class ChemTestes(unittest.TestCase):

    def setUp(self):
        self.ar = air.Ar()
        self.elementos = molec.elements()
        self.isotopos = molec.isotopes()

    def test_psi(self):
        """
        Teste para módulo air.py. Testando valor de psi.
        """
        self.assertEqual(self.ar.psi, 3.76)

    def test_mix_air(self):
        """
        Teste para módulo air.py. Testando o dicionário de mistura.
        """
        self.assertIsInstance(self.ar.mix_air, dict)
        self.assertEqual(self.ar.mix_air['O2'], 1 / (1 + 3.76))
        self.assertEqual(self.ar.mix_air['N2'], 3.76 / (1 + 3.76))

    def test_comp(self):
        """
        Teste para módulo air.py. Testando a lista da composição da mistura.
        """
        self.assertIsInstance(self.ar.comp, list)
        self.assertIn('O2', self.ar.comp)
        self.assertIn('N2', self.ar.comp)

    def test_elem(self):
        """
        Teste para módulo elem.py. Testando valores do dicionário isot.
        """
        self.assertEqual(elem.isot[6]['sym'], 'C')
        self.assertIsInstance(elem.isot[6]['iso'][12], dict)
        self.assertEqual(elem.isot[6]['iso'][12]['m'], 12.0)
        self.assertEqual(elem.isot[6]['iso'][12]['a'], 98.938)

    def test_elements(self):
        """
        Teste para módulo molec.py. Testando função elements().
        """
        self.assertIsInstance(self.elementos, list)
        self.assertEqual(self.elementos[0], (1, 'H'))

    def test_isotopes(self):
        """
        Teste para módulo molec.py. Testando função isotopes().
        """
        self.assertIsInstance(self.isotopos, list)
        self.assertEqual(self.isotopos[3], (4, 'Be', [9]))

    def test_isotopes_of(self):
        """
        Teste para módulo molec.py. Testando função isotopes_of.
        """
        self.assertEqual(molec.isotopes_of('H'), [1, 2, 3])

    def test_atomize(self):
        """
        Teste para módulo molec.py. Testando função atomize().
        """
        self.assertIsInstance(molec.atomize('C8H18'), dict)
        self.assertEqual(molec.atomize('C8H18'), {'C': 8, 'H': 18})
        self.assertEqual(molec.atomize('H2'), {'H': 2})

    def test_massa_molar(self):
        """
        Teste para módulo molec.py. Testando função massa_molar().
        """
        self.assertEqual(molec.massa_molar('C8H18'), 114.22946172503093)


if __name__ == "__main__":
    unittest.main()
