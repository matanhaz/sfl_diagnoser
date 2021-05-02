from .FullMatrixCompSimilarity import FullMatrixCompSimilarity
from .dynamicSpectrum import dynamicSpectrum
from functools import partial


class DynamicSpectrumCompSimilarity(dynamicSpectrum):
    def __init__(self):
        super(DynamicSpectrumCompSimilarity, self).__init__()
        self.CompSimilarity_matrix = dict()
        self.CompSimilarity_alpha = 0

    def set_CompSimilarity_matrix(self, matrix):
        self.CompSimilarity_matrix = matrix

    def set_CompSimilarity_alpha(self, alpha):
        self.CompSimilarity_alpha = alpha

    def convertToFullMatrix(self):
        zeros_vector = [0 for _ in self.getprobabilities()]

        def get_test_vector(test, getter=lambda x: 1):
            vector = []
            for c in test:
                vector.extend(zeros_vector[len(vector):c] + [getter(c)])
            vector.extend(zeros_vector[len(vector):])
            return vector

        ans = FullMatrixCompSimilarity()
        ans.probabilities = list(self.getprobabilities())
        ans.error = list(self.geterror())
        ans.matrix = [get_test_vector(test) for test in self.getTestsComponents()]
        CompSimilarity_matrix = []
        for test_id, test in enumerate(self.getTestsComponents()):
            CompSimilarity_matrix.append(get_test_vector(test, self.CompSimilarity_matrix[test_id].get))
        ans.CompSimilarity_matrix = CompSimilarity_matrix
        ans.CompSimilarity_alpha = self.CompSimilarity_alpha
        return ans
