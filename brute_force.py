from itertools import product
from utils import check_cnf
def solve_cnf_bruteforce(cnf):
    vars_set = set()
    for clause in cnf:
        for lit in clause:
            vars_set.add(abs(lit))
    vars_list = list(vars_set)
    for values in product([False, True], repeat=len(vars_list)):
        assignment = {vars_list[i]: values[i] for i in range(len(vars_list))}
        if check_cnf(cnf, assignment):
            return [v if assignment[v] else -v for v in vars_list]

    return None
