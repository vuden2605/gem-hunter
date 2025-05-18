import time
import os
from brute_force import solve_cnf_bruteforce
from backtrack import solve_cnf_backtrack
from utils import load_grid_from_file, write_output
from generate_cnf import generate_cnf
from solver_pysat import solve_cnf_pysat
def main():
    grid = load_grid_from_file('input/input1.txt')
    cnf, var_map = generate_cnf(grid)

    model_pysat = solve_cnf_pysat(cnf)
    if model_pysat:
        write_output('output/output_pysat.txt', model_pysat, var_map, grid)
        print("PySAT: Có nghiệm")
    else:
        print("PySAT: Vô nghiệm")

    model_bf = solve_cnf_bruteforce(cnf)
    if model_bf:
        write_output('output/output_bruteforce.txt', model_bf, var_map, grid)
        print("Bruteforce: Có nghiệm")
    else:
        print("Bruteforce: Vô nghiệm")

    model_bt = solve_cnf_backtrack(cnf)
    if model_bt:
        write_output('output/output_backtrack.txt', model_bt, var_map, grid)
        print("Backtrack: Có nghiệm")
    else:
        print("Backtrack: Vô nghiệm")

if __name__ == "__main__":
    main()