from math import sqrt
from typing import Dict, List


# A class that implements the basic functionality and characteristics of a neuron
class Neuron:
    # A list of all the possible receptor types. At some point every receptor
    # type will be implemented as a subclass of the Receptor class
    receptor_list = ['AMPA', 'NMDA', 'D1', 'D2', 'kainate']

    def __init__(self, length, res_m, cap_m, res_a,  inputs, outputs, receptors=Dict[str, int]):
        self.length = length
        self.res_m = res_m
        self.cap_m = cap_m
        self.res_a = res_a
        self.tau = res_m * cap_m
        self.length_constant = sqrt(res_m / res_a)
        self.receptors = receptors
        self.inputs = inputs
        self.outputs = outputs

    # Returns the up-to-date list of all possible receptors
    @staticmethod
    def acceptable_receptors():
        return Neuron.receptor_list
