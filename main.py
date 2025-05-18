import time
import os
from brute_force import solve_cnf_bruteforce
from backtrack import solve_cnf_backtrack
from utils import read_input_file, write_output_file
from solver_pysat import solve_cnf_pysat
from cnf_generator import generate_cnf

def write_assignment_to_file(path, assignment, rows, cols):
    """Ghi kết quả assignment vào file dưới dạng lưới (nếu có)."""
    if assignment is None:
        with open(path, 'w') as f:
            f.write("No solution\n")
        return

    # Tạo grid trống theo kích thước rows x cols
    grid = [['_' for _ in range(cols)] for _ in range(rows)]
    # Mỗi biến là 1 vị trí theo var_id = x*cols + y +1
    for x in range(rows):
        for y in range(cols):
            var_id = x * cols + y + 1
            val = assignment.get(var_id, False)
            grid[x][y] = '1' if val else '0'

    with open(path, 'w') as f:
        for row in grid:
            f.write(', '.join(row) + '\n')

def run_all_methods(input_path, output_prefix):
    if not os.path.exists(input_path):
        print(f"Input file {input_path} không tồn tại!")
        return

    grid = read_input_file(input_path)
    
    # generate_cnf trả về clauses và var_map
    clauses, var_map = generate_cnf(grid)
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    num_vars = rows * cols

    # Tạo thư mục output nếu chưa tồn tại
    output_dir = os.path.dirname(output_prefix)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # PySAT
    t0 = time.time()
    pysat_result = solve_cnf_pysat(clauses, num_vars)
    t1 = time.time()
    write_assignment_to_file(f"{output_prefix}_pysat.txt", pysat_result, rows, cols)
    print(f"[PySAT] Done in {t1 - t0:.4f}s")

    # Brute-force
    t0 = time.time()
    brute_result = solve_cnf_bruteforce(clauses, num_vars)
    t1 = time.time()
    write_assignment_to_file(f"{output_prefix}_brute.txt", brute_result, rows, cols)
    print(f"[Brute-force] Done in {t1 - t0:.4f}s")

    # Backtracking
    t0 = time.time()
    back_result = solve_cnf_backtrack(clauses, num_vars)
    t1 = time.time()
    write_assignment_to_file(f"{output_prefix}_backtrack.txt", back_result, rows, cols)
    print(f"[Backtracking] Done in {t1 - t0:.4f}s")

if __name__ == "__main__":
    run_all_methods('input/input1.txt', 'output/output1')
