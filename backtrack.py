from utils import check_cnf

def clause_unsatisfied(clause, assignment):
    for lit in clause:
        var = abs(lit)
        if var not in assignment:
            return False  # chưa gán hết biến -> chưa chắc clause này sai
        if (lit > 0 and assignment[var]) or (lit < 0 and not assignment[var]):
            return False  # clause thỏa mãn
    return True  # tất cả literal đều sai -> clause không thỏa mãn

def solve_cnf_backtrack(cnf, assignment=None, vars_list=None, idx=0):
    if vars_list is None:
        vars_set = set()
        for clause in cnf:
            for lit in clause:
                vars_set.add(abs(lit))
        vars_list = list(vars_set)
    if assignment is None:
        assignment = {}

    # Early pruning: nếu có clause nào không thể thỏa với assignment hiện tại -> quay lui
    for clause in cnf:
        if clause_unsatisfied(clause, assignment):
            return None

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
