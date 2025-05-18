def read_input_file(path):
    grid = []
    with open(path, 'r') as f:
        for line in f:
            grid.append([x.strip() for x in line.strip().split(',')])
    return grid

def write_output_file(path, grid):
    with open(path, 'w') as f:
        for row in grid:
            f.write(', '.join(row) + '\n')