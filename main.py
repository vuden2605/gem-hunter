import time
import os
from brute_force import solve_cnf_bruteforce
from backtrack import solve_cnf_backtrack
from utils import load_grid_from_file, write_output
from generate_cnf import generate_cnf
from solver_pysat import solve_cnf_pysat

def solve_and_write(method_name, solve_fn, cnf, var_map, grid, output_path):
    print(f"\nĐang giải bằng thuật toán {method_name}...")
    start_time = time.time()
    model = solve_fn(cnf)
    end_time = time.time()
    elapsed = end_time - start_time

    if model:
        write_output(output_path, model, var_map, grid)
        with open(output_path, 'a', encoding='utf-8') as f:
            f.write(f"\nThời gian thực hiện: {elapsed:.4f} giây\n")
        print(f"{method_name}: Có nghiệm. Thời gian chạy: {elapsed:.4f} giây")
    else:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("Vô nghiệm\n")
            f.write(f"Thời gian thực hiện: {elapsed:.4f} giây\n")
        print(f"{method_name}: Vô nghiệm. Thời gian chạy: {elapsed:.4f} giây")

def main():
    while True:
        # Menu chọn thuật toán
        print("\n==== CHỌN THUẬT TOÁN ====")
        print("0. Thoát")
        print("1. PySAT")
        print("2. Brute-force")
        print("3. Backtracking")
        algo_choice = input("Nhập lựa chọn (0/1/2/3): ").strip()

        if algo_choice == '0':
            print("Đã thoát chương trình.")
            break

        if algo_choice not in {'1', '2', '3'}:
            print("Lựa chọn không hợp lệ.")
            continue

        # Menu chọn map
        print("\n==== CHỌN MAP ====")
        print("0. Quay lại")
        print("1. input/input1.txt")
        print("2. input/input2.txt")
        print("3. input/input3.txt")
        map_choice = input("Nhập lựa chọn (0/1/2/3): ").strip()

        if map_choice == '0':
            continue

        if map_choice not in {'1', '2', '3'}:
            print("Lựa chọn không hợp lệ.")
            continue

        input_file = f"input/input{map_choice}.txt"
        algo_names = {'1': 'pysat', '2': 'brute', '3': 'backtrack'}
        output_file = f"output/output_{algo_names[algo_choice]}_{map_choice}.txt"

        if not os.path.exists(input_file):
            print(f"Không tìm thấy file {input_file}")
            continue
        grid = load_grid_from_file(input_file)
        cnf, var_map = generate_cnf(grid)

        if algo_choice == '1':
            solve_and_write("PySAT", solve_cnf_pysat, cnf, var_map, grid, output_file)
        elif algo_choice == '2':
            solve_and_write("Brute-force", solve_cnf_bruteforce, cnf, var_map, grid, output_file)
        elif algo_choice == '3':
            solve_and_write("Backtracking", solve_cnf_backtrack, cnf, var_map, grid, output_file)

        input("\n Nhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()
