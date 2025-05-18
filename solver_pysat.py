# pysat.py
from pysat.solvers import Glucose3

def solve_cnf_pysat(cnf_clauses):
    solver = Glucose3()
    for clause in cnf_clauses:
        solver.add_clause(clause)

    if solver.solve():
        return solver.get_model()  
    else:
        return None
