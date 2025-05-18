from itertools import product

def solve_cnf_bruteforce(clauses, num_vars):
    for values in product([False, True], repeat=num_vars):
        assignment = {i+1: values[i] for i in range(num_vars)}

        satisfied = True
        for clause in clauses:
            clause_satisfied = False
            for lit in clause:
                var = abs(lit)
                val = assignment[var]
                if (lit > 0 and val) or (lit < 0 and not val):
                    clause_satisfied = True
                    break
            if not clause_satisfied:
                satisfied = False
                break
        
        if satisfied:
            return assignment
    return None
