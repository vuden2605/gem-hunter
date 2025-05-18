# utils.py
def load_grid_from_file(filepath):
    grid = []
    with open(filepath, 'r') as f:
        for line in f:
            row = []
            for cell in line.strip().split(','):
                cell = cell.strip()
                if cell == '_':
                    row.append('_')
                else:
                    row.append(int(cell))
            grid.append(row)
    return grid

def write_output(filepath, assignments, var_map, original_grid):
    inverse_map = {v: k for k, v in var_map.items()}
    rows = len(original_grid)
    cols = len(original_grid[0])
    output_grid = [[str(original_grid[i][j]) if isinstance(original_grid[i][j], int) else '_' 
                    for j in range(cols)] for i in range(rows)]

    for var in assignments:
        coord = inverse_map.get(abs(var))
        if coord:
            x, y = coord
            if original_grid[x][y] == '_':
                output_grid[x][y] = 'T' if var > 0 else 'G'

    with open(filepath, 'w') as f:
        for row in output_grid:
            f.write(','.join(row) + '\n')

