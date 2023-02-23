import os
from itertools import combinations, permutations

PROB_METRICS = ["BAYE", "RAND", "ZSCE", "ODDS", "DZSCE"]
PROB_METRICS1 = ["CHAOTIC", "BAYESIAN", "ZSCORED", "ODDS"]
COMBINERS = ["AVERAGE", "PRODUCT", "SQRT_AVERAGE", "SQRT_PRODUCT", "CBRT_AVERAGE", "CBRT_PRODUCT", "FRT_AVERAGE", "FRT_PRODUCT"]
COMB_PROB_METRICS1 = list(combinations(PROB_METRICS[:4], 2))
COMB_PROB_METRICS2 = list(permutations(PROB_METRICS1, 2))[:6]
COMB_PROB_METRICS3 = list(combinations(PROB_METRICS[:4], 3))
COMB_PROB_METRICS4 = list(combinations(PROB_METRICS[:4], 4))

dir_list = []

for COMBINER in COMBINERS[:4]:
    Z = COMBINER
    for COMB in COMB_PROB_METRICS1:
        X, Y = COMB
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

for PROB in PROB_METRICS:
    X = PROB
    Y = "ANALYSIS"
    Z = "STANDARD"
    dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

for COMB in COMB_PROB_METRICS2:
    X, Y = COMB
    Z = "COMBINATE"
    dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

for COMBINER in COMBINERS:
    Z = COMBINER
    if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[6] and Z != COMBINERS[7]:
        for COMB in COMB_PROB_METRICS3:
            W, X, Y = COMB
            dir_list.append(f"RESULTS - {Z}_{W}_{X}_{Y}")

for COMBINER in COMBINERS:
    Z = COMBINER
    if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[4] and Z != COMBINERS[5]:
        for COMB in COMB_PROB_METRICS4:
            V, W, X, Y = COMB
            dir_list.append(f"RESULTS - {Z}_{V}_{W}_{X}_{Y}")

for dir_ in dir_list:
    try:
        os.makedirs(f"./{dir_}")
    except OSError:
        print("Directory Exists")
