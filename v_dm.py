import numpy as np
from collections import defaultdict

dataset_file = "affinity_dataset.txt"
X = np.loadtxt(dataset_file)

#define three default dict

valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurrences = defaultdict(int)

#try to count support and calculate confidence
def v_dm():
    for sample in X:
        for premise in range(5):
            if sample[premise] == 0 :
                continue
            else:
                num_occurrences[premise] += 1
            for conclusion in range(5):
                if premise == conclusion :
                    continue
                if sample[conclusion] == 1 :
                    valid_rules[(premise,conclusion)] += 1
                else :
                    invalid_rules[(premise,conclusion)] += 1
    support = valid_rules
    for key, value in valid_rules.items():
        print(key,value)
v_dm()



