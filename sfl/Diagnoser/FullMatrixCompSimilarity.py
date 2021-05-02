from .BarinelCompSimilarity import BarinelCompSimilarity
from .FullMatrix import FullMatrix


class FullMatrixCompSimilarity(FullMatrix):
    def __init__(self):
        super(FullMatrixCompSimilarity, self).__init__()
        self.CompSimilarity_matrix = dict()
        self.CompSimilarity_alpha = 0

    def set_CompSimilarity_matrix(self, matrix):
        self.CompSimilarity_matrix = matrix

    def set_CompSimilarity_alpha(self, alpha):
        self.CompSimilarity_alpha = alpha

    def diagnose(self):
        bar = BarinelCompSimilarity()
        bar.set_matrix_error(self.matrix,self.error)
        bar.set_prior_probs(self.probabilities)
        bar.set_CompSimilarity_matrix(self.CompSimilarity_matrix)
        bar.set_CompSimilarity_alpha(self.CompSimilarity_alpha)
        return bar.run()


    # optimization: remove unreachable components & components that pass all their tests
    # return: optimized FullMatrix, chosen_components( indices), used_tests
    def optimize(self):
        optimizedMatrix, used_components, used_tests = super(FullMatrixCompSimilarity, self).optimize()
        new_CompSimilarity_matrix = FullMatrixCompSimilarity()
        new_CompSimilarity_matrix.set_error(optimizedMatrix.error)
        new_CompSimilarity_matrix.set_matrix(optimizedMatrix.matrix)
        new_CompSimilarity_matrix.set_probabilities(optimizedMatrix.probabilities)
        new_matrix = []
        for test in used_tests:
            new_test = []
            for i in range(len(used_components)):
                new_test.append(self.CompSimilarity_matrix[test][used_components[i]])
            new_matrix.append(new_test)
        new_CompSimilarity_matrix.set_CompSimilarity_matrix(new_matrix)
        new_CompSimilarity_matrix.set_CompSimilarity_alpha(self.CompSimilarity_alpha)
        return new_CompSimilarity_matrix, used_components, used_tests
