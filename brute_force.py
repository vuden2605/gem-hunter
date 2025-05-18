from itertools import product

def check_clause(clause, assignment):
    for lit in clause:
        var = abs(lit)
        val = assignment.get(var, False)
        if (lit > 0 and val) or (lit < 0 and not val):
            return True
    return False

def check_cnf(cnf, assignment):
    for clause in cnf:
        if not check_clause(clause, assignment):
            return False
    return True

def solve_cnf_bruteforce(cnf):
    vars_set = set()
    for clause in cnf:
        for lit in clause:
            vars_set.add(abs(lit))
    vars_list = sorted(vars_set)
    for values in product([False, True], repeat=len(vars_list)):
        assignment = {vars_list[i]: values[i] for i in range(len(vars_list))}
        if check_cnf(cnf, assignment):
            return [v if assignment[v] else -v for v in vars_list]
    return None
