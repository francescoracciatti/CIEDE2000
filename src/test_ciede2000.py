"""
Unit test for CIEDE2000.
"""

import unittest
from typing import Dict, Tuple
import pandas as pd

from src.ciede2000 import CIEDE2000


class TestCIEDE2000(unittest.TestCase):
    """
    Tests CIEDE2000 colors distance.
    """

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_ciede2000_distance(self) -> None:
        """
        Tests CIEDE2000 distance.

        Uses data in data/lab-distances.xlsx, from doc/ciede2000-color-difference.pdf pag 24.
        """

        xlsx = pd.read_excel('../data/lab-distances.xlsx', engine='openpyxl')
        for row in xlsx.index:
            pair = xlsx['Pair'][row]
            lab1 = (xlsx['L1'][row], xlsx['a1'][row], xlsx['b1'][row])
            lab2 = (xlsx['L2'][row], xlsx['a2'][row], xlsx['b2'][row])
            deltaE_00 = xlsx['DeltaE00'][row]
            distance = round(CIEDE2000.distance(lab1, lab2), 4)
            msg = f"Pair {pair}: Lab1 {lab1}, Lab2 {lab2}, distance {distance} vs DeltaE_00 {deltaE_00}"
            self.assertEqual(deltaE_00, distance, msg)

            # Revers the colors ordering
            distance = round(CIEDE2000.distance(lab2, lab1), 4)
            msg = f"Pair {pair} reverse: Lab1 {lab1}, Lab2 {lab2}, distance {distance} vs DeltaE_00 {deltaE_00}"
            self.assertEqual(deltaE_00, distance, msg)
