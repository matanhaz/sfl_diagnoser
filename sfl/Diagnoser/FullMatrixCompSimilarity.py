from .BarinelCompSimilarity import BarinelCompSimilarity
from .FullMatrix import FullMatrix


class FullMatrixCompSimilarity(FullMatrix):
    def __init__(self):
        super(FullMatrixCompSimilarity, self).__init__()
        self.CompSimilarity = {}

    def set_CompSimilarity(self, s):
        self.CompSimilarity = s

    def diagnose(self):
        bar = BarinelCompSimilarity()
        bar.set_matrix_error(self.matrix,self.error)
        bar.set_prior_probs(self.probabilities)
        bar.set_CompSimilarity(self.CompSimilarity)
        return bar.run()


    # optimization: remove unreachable components & components that pass all their tests
    # return: optimized FullMatrix, chosen_components( indices), used_tests
    def optimize(self):
        optimizedMatrix, used_components, used_tests = super(FullMatrixCompSimilarity, self).optimize()
        new_CompSimilarity_matrix = FullMatrixCompSimilarity()
        new_CompSimilarity_matrix.set_error(optimizedMatrix.error)
        new_CompSimilarity_matrix.set_matrix(optimizedMatrix.matrix)
        new_CompSimilarity_matrix.set_probabilities(optimizedMatrix.probabilities)
        CompSimilarity = {}
        for i in range(len(used_components)):
            CompSimilarity[i] = self.CompSimilarity[used_components[i]]
        new_CompSimilarity_matrix.set_CompSimilarity(CompSimilarity)
        return new_CompSimilarity_matrix, used_components, used_tests
