from pysat.solvers import Solver

def solve_cnf_pysat(clauses, num_vars):
    with Solver(name='glucose3') as solver:
        for clause in clauses:
            solver.add_clause(clause)

        satisfiable = solver.solve()
        if not satisfiable:
            return None
        
        model = solver.get_model()
        assignment = {}
        for i in range(1, num_vars + 1):
            assignment[i] = model[i-1] > 0
        return assignment
