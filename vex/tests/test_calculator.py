"""Tests unitaires pour le module calculator"""
import unittest
import sys
import os

# Ajouter le dossier parent au path pour importer src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, subtract, multiply, divide, power, modulo


class TestCalculator(unittest.TestCase):
    """Tests pour les fonctions de la calculatrice"""

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_modulo(self):
        self.assertEqual(modulo(7, 3), 1)
        with self.assertRaises(ValueError):
            modulo(5, 0)


if __name__ == '__main__':
    unittest.main()
