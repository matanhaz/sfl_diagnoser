__author__ = 'amir'

# from LightPSO import LightPSO
import operator
import functools
from.TF import TF
from functools import reduce


class TFCompSimilarity(TF):
    def __init__(self, matrix, error, diagnosis, CompSimilarity):
        super(TFCompSimilarity, self).__init__(matrix, error, diagnosis)
        self.CompSimilarity = CompSimilarity
        self.CompSimilarity_dict = dict()
        

    def maximize(self):
        max_value = super(TFCompSimilarity, self).maximize()
        #CompSimilarity_probability = self.probabilty(self.CompSimilarity_dict)
        return max_value 

    def calculate(self, values):
        return self.probabilty(values)

    def probabilty(self, h_dict):
        # h_dict is dict of dicts for test to comps
        def test_prob(test_id, v, e):
            # if e==0 : h1*h2*h3..., if e==1: 1-h1*h2*h3...
            return e + ((-2.0 * e + 1.0) * reduce(operator.mul,
                                                   list(map(h_dict[test_id].get, self.get_active_components()[test_id])), 1.0))
        original_calc =  reduce(operator.mul, list(map(lambda x: test_prob(*x), self.get_activity())), 1.0)
        # for i in range(len(self.diagnosis)):
        #     original_calc *= (self.CompSimilarity[i] ** self.get_number_of_repetioions(self.diagnosis[i]))
        return original_calc

    def get_number_of_repetioions(self, comp_index):
        counter = 0
        for test in self.activity:
            counter += test[1][comp_index]
        return counter