import copy
import math
import random
from math import ceil
from .dynamicSpectrumCompSimilarity import DynamicSpectrumCompSimilarity
from .Experiment_Data import Experiment_Data
import numpy
from .ExperimentInstance import ExperimentInstance

TERMINAL_PROB = 0.7


class ExperimentInstanceCompSimilarity(ExperimentInstance):
    def __init__(self, initial_tests, error, priors, bugs, pool, components, estimated_pool=None, **kwargs):
        super(ExperimentInstanceCompSimilarity, self).__init__(initial_tests, error, priors, bugs, pool, components, estimated_pool, **kwargs)
        """ check the CompSimilarity matrix and CompSimilarity alpha"""
        for sim in Experiment_Data().CompSimilarity:
            assert 0.0 <= sim <= 1.0 , "wrong value of CompSimilarity_alpha"
        tests = Experiment_Data().POOL.keys()
        for test in tests:
            assert len(set(Experiment_Data().POOL[test])) == len(Experiment_Data().POOL[test]), \
                "trace of test {0} is faulty".format(test)
        
    def initials_to_DS(self):
        ds = DynamicSpectrumCompSimilarity()
        ds.setTestsComponents(copy.deepcopy([Experiment_Data().POOL[test] for test in self.get_initials()]))
        ds.setprobabilities(list(self.priors))
        ds.seterror([self.get_error()[test] for test in self.get_initials()])
        ds.settests_names(list(self.get_initials()))
        ds.set_CompSimilarity(dict(enumerate(Experiment_Data().CompSimilarity)))
        return ds
