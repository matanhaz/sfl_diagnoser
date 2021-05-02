__author__ = 'amir'

# from LightPSO import LightPSO
import operator
import functools
from.TF import TF


class TFCompSimilarity(TF):
    def __init__(self, matrix, error, diagnosis, CompSimilarity_matrix, CompSimilarity_alpha):
        super(TFCompSimilarity, self).__init__(matrix, error, diagnosis)
        self.CompSimilarity_matrix = CompSimilarity_matrix
        self.CompSimilarity_alpha = CompSimilarity_alpha
        self.CompSimilarity_dict = dict()
        for test_id, test in enumerate(self.CompSimilarity_matrix):
            test_dict = dict(map(lambda c: (c, test[c]), self.get_active_components()[test_id]))
            self.CompSimilarity_dict[test_id] = test_dict

    def maximize(self):
        max_value = super(TFCompSimilarity, self).maximize()
        CompSimilarity_probability = self.probabilty(self.CompSimilarity_dict)
        return max_value * self.CompSimilarity_alpha + CompSimilarity_probability * (1 - self.CompSimilarity_alpha)

    def calculate(self, values):
        return self.probabilty(values)
