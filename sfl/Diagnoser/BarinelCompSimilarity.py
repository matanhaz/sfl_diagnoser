__author__ = 'amir'

import csv
import math
import sys
from .Barinel import Barinel
from .TFCompSimilarity import TFCompSimilarity


class BarinelCompSimilarity(Barinel):

    def __init__(self):
        super(BarinelCompSimilarity, self).__init__()
        self.CompSimilarity_matrix = dict()
        self.CompSimilarity_alpha = 0

    def set_CompSimilarity_matrix(self, matrix):
        self.CompSimilarity_matrix = matrix

    def set_CompSimilarity_alpha(self, alpha):
        self.CompSimilarity_alpha = alpha

    def tf_for_diag(self, diagnosis):
        return TFCompSimilarity(self.get_matrix(), self.get_error(), diagnosis, self.CompSimilarity_matrix, self.CompSimilarity_alpha)
