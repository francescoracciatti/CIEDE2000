"""
This module provides CIEDE2000 color difference algorithm.
"""

from abc import ABC
from math import sqrt, atan2, pi, sin, cos, exp
from typing import Tuple


class CIEDE2000(ABC):
    """
    Provides CIEDE2000 color difference algorithm.

    See doc/ciede2000-color-difference.pdf
    """

    K_25_7 = 25 ** 7  # Constant, formula (17)

    @classmethod
    def distance(cls, lab1: Tuple[float, float, float], lab2: Tuple[float, float, float]) -> float:
        """
        Gets the CIEDE2000 color distance between the given Lab colors.

        See doc/ciede2000-color-difference.pdf, pag 22.

        :param lab1: the 1st Lab color
        :param lab2: the 2nd Lab color
        :return: the distance between the two colors
        """
        # Splits colors on L-a-b channels, formula (1)
        L1, a1, b1 = lab1[0], lab1[1], lab1[2]
        L2, a2, b2 = lab2[0], lab2[1], lab2[2]

        # Formula (2), (3)
        C1_ab = sqrt(a1 ** 2 + b1 ** 2)
        C2_ab = sqrt(a2 ** 2 + b2 ** 2)
        C_ab_average = (C1_ab + C2_ab) / 2

        # Formula (4)
        G = 0.5 * (1 - sqrt(C_ab_average ** 7 / (C_ab_average ** 7 + cls.K_25_7)))

        # Formula (5)
        L1_ = L1
        L2_ = L2

        a1_ = (1 + G) * a1
        a2_ = (1 + G) * a2

        b1_ = b1
        b2_ = b2

        # Formula (6)
        C1_ = sqrt(a1_ ** 2 + b1_ ** 2)
        C2_ = sqrt(a2_ ** 2 + b2_ ** 2)

        # Formula (7)
        if b1 == 0 and a1_ == 0:
            h1_ = 0
        elif a1_ >= 0:
            h1_ = atan2(b1_, a1_) + 2 * pi
        else:
            h1_ = atan2(b1_, a1_)

        if b2 == 0 and a2_ == 0:
            h2_ = 0
        elif a2_ >= 0:
            h2_ = atan2(b2_, a2_) + 2 * pi
        else:
            h2_ = atan2(b2_, a2_)

        # Formula (8)
        dL_ = L2_ - L1_

        # Formula (9)
        dC_ = C2_ - C1_

        # Formula (10)
        dh_ = h2_ - h1_
        if C1_ * C2_ == 0:
            dh_ = 0
        elif dh_ > pi:
            dh_ -= 2 * pi
        elif dh_ < -pi:
            dh_ += 2 * pi

        # Formula (11)
        dH_ = 2 * sqrt(C1_ * C2_) * sin(dh_ / 2)

        # Formula (12)
        L_average_ = (L1_ + L2_) / 2

        # Formula (13)
        C_average_ = (C1_ + C2_) / 2

        # Formula (14)
        _dh = abs(h1_ - h2_)
        _sh = h1_ + h2_
        C1_C2_ = C1_ * C2_
        if _dh <= pi and C1_C2_ != 0:
            h_average_ = (h1_ + h2_) / 2
        elif _dh > pi and _sh < 2 * pi and C1_C2_ != 0:
            h_average_ = (h1_ + h2_) / 2 + pi
        elif _dh > pi and _sh >= 2 * pi and C1_C2_ != 0:
            h_average_ = (h1_ + h2_) / 2 - pi
        else:
            h_average_ = h1_ + h2_

        # Formula (15)
        T = (1
             - 0.17 * cos(h_average_ - pi / 6)
             + 0.24 * cos(2 * h_average_)
             + 0.32 * cos(3 * h_average_ + pi / 30)
             - 0.2 * cos(4 * h_average_ - 63 * pi / 180))

        # Formula (16)
        h_average_deg_ = h_average_ * 180 / pi
        if h_average_deg_ < 0:
            h_average_deg_ += 360
        elif h_average_deg_ > 360:
            h_average_deg_ -= 360
        dTheta = 30 * exp(-(((h_average_deg_ - 275) / 25) ** 2))

        # Formula (17)
        R_C = 2 * sqrt(C_average_ ** 7 / (C_average_ ** 7 + cls.K_25_7))

        # Formula (18)
        L_50 = (L_average_ - 50) ** 2
        S_L = 1 + 0.015 * L_50 / sqrt(20 + L_50)

        # Formula (19)
        S_C = 1 + 0.045 * C_average_

        # Formula (20)
        S_H = 1 + 0.015 * C_average_ * T

        # Formula (21)
        R_T = -sin(dTheta * pi / 90) * R_C

        # Formula (22)
        k_L, k_C, k_H = 1, 1, 1
        f_L = dL_ / k_L / S_L
        f_C = dC_ / k_C / S_C
        f_H = dH_ / k_H / S_H
        delta_E_00 = sqrt(f_L ** 2 + f_C ** 2 + f_H ** 2 + R_T * f_C * f_H)

        # logging.debug(f"a1_ {a1_}, a2_ {a2_},cC1_ {C1_}, C2_ {C2_}, h1_ {h1_}, h2_ {h2_}, h_avg_' {h_average_deg_}, "
        #               f"G {G}, T {T}, SL {S_L}, SC {S_C}, SH {S_H}, RT {R_T}")

        return delta_E_00

