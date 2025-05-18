from itertools import product
from itertools import combinations
class CNFGenerator:
    def get_neighbors(self, x, y, grid):
        rows, cols = len(grid), len(grid[0])
        neighbors = []
        for dx, dy in product([-1, 0, 1], repeat=2):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '_':
                neighbors.append((nx, ny))
        return neighbors
    
    def generate(self, grid):
        rows, cols = len(grid), len(grid[0])
        var_map = {(nx, ny): nx * cols + ny + 1 for nx, ny in product(range(rows), range(cols))}
        cnf = []
        
        for x, y in product(range(rows), range(cols)):
            if isinstance(grid[x][y], int): 
                neighbors = self.get_neighbors(x, y, grid)
                vars = [var_map[n] for n in neighbors] 
                num = grid[x][y]
                cnf.extend([[-v for v in comb] for comb in combinations(vars, num + 1)])
                cnf.extend([[v for v in comb] for comb in combinations(vars, len(vars) - num + 1)]) 
        
        cnf = list(map(list, set(map(tuple, cnf))))

        return cnf, var_map
