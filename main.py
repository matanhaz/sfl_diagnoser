from sfl.Diagnoser.diagnoserUtils import write_json_planning_file, read_json_planning_instance, read_json_planning_file
from sfl.Diagnoser.Experiment_Data import Experiment_Data
from sfl.Diagnoser.Diagnosis_Results import Diagnosis_Results
import os

import csv

HIGHER_SIMILARITIES = [0.6,0.7,0.8,0.9,1]
LOWER_SIMILARITIES = [0.4,0.3,0.2,0.1]
MATRIXES = os.listdir(os.getcwd()+"\\matrixes")


rows = []
rows.append(['real bug diagnose sim','unreal bug diagnose sim', 'precision','recall', 'original precision', 'original recall' ])


def diagnose(matrix_name):

    ei = read_json_planning_file(matrix_name,0,0, experiment_type = 'normal')
    ei.diagnose()
    diagnoses = Diagnosis_Results(ei.diagnoses, ei.initial_tests, ei.error, ei.pool, ei.get_id_bugs()).metrics
    original_precision = diagnoses['precision']
    original_recall = diagnoses['recall']
    print(original_precision)

    for good_sim in HIGHER_SIMILARITIES:
        for bad_sim in LOWER_SIMILARITIES:
            
            ei = read_json_planning_file(matrix_name,good_sim, bad_sim,'CompSimilarity')
            ei.diagnose()
            #print("e1 = %f , e2 = %f, e3 = %f" %(CompSimilarity[1],CompSimilarity[2],CompSimilarity[3]))
            #print(Diagnosis_Results(ei.diagnoses, ei.initial_tests, ei.error, ei.pool, ei.get_id_bugs()).metrics)
            diagnoses = Diagnosis_Results(ei.diagnoses, ei.initial_tests, ei.error, ei.pool, ei.get_id_bugs()).metrics
            #print(Diagnosis_Results(ei.diagnoses, ei.initial_tests, ei.error, ei.pool, ei.get_id_bugs()).diagnoses)
            print(diagnoses['precision'])
            rows.append([good_sim,bad_sim, diagnoses['precision'],diagnoses['recall'],original_precision,original_recall])



def write_rows(rows):
    with open("data.csv",'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
        pass


# diagnose('test_matrix1')
# diagnose('test_matrix2')
# diagnose('test_matrix3')
# diagnose('test_matrix4')
for matrix in MATRIXES:
    diagnose('matrixes//' + matrix)

print("done")
write_rows(rows)
