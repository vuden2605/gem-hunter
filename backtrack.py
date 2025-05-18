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
def get_vars_in_cnf(cnf):
    vars_set = set()
    for clause in cnf:
        for lit in clause:
            vars_set.add(abs(lit))
    return sorted(vars_set)

def solve_cnf_backtrack(cnf, assignment=None, vars_list=None, idx=0):
    if vars_list is None:
        vars_list = get_vars_in_cnf(cnf)
    if assignment is None:
        assignment = {}

    if idx == len(vars_list):
        if check_cnf(cnf, assignment):
            return [v if assignment[v] else -v for v in vars_list]
        else:
            return None

    var = vars_list[idx]

    assignment[var] = True
    res = solve_cnf_backtrack(cnf, assignment, vars_list, idx + 1)
    if res is not None:
        return res

    assignment[var] = False
    res = solve_cnf_backtrack(cnf, assignment, vars_list, idx + 1)
    if res is not None:
        return res

    del assignment[var]
    return None
