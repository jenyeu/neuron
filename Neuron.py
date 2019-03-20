from math import sqrt
from typing import Dict, List


class Neuron:
    receptor_list = ['AMPA', 'NMDA', 'D1', 'D2']

    def __init__(self, length, res_m, cap_m, res_a, receptors = Dict[str, int]):
        self.length = length
        self.res_m = res_m
        self.cap_m = cap_m
        self.res_a = res_a
        self.tau = res_m * cap_m
        self.length_constant = sqrt(res_m / res_a)
        self.receptors = receptors

    @staticmethod
    def acceptable_receptors():
        return Neuron.receptor_list
