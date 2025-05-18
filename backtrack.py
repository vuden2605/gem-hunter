def solve_cnf_backtrack(clauses, assignment=None):
    if assignment is None:
        assignment = {}

    # Nếu CNF rỗng => thành công
    if not clauses:
        return assignment

    # Nếu có mệnh đề rỗng => thất bại
    if any(len(clause) == 0 for clause in clauses):
        return None

    # Lấy biến chưa gán
    vars_in_clauses = set(abs(lit) for clause in clauses for lit in clause)
    unassigned_vars = vars_in_clauses - set(assignment.keys())
    if not unassigned_vars:
        return assignment

    var = unassigned_vars.pop()

    for value in [True, False]:
        new_assignment = assignment.copy()
        new_assignment[var] = value

        # Thực hiện đơn giản hóa CNF với gán này
        simplified = []
        for clause in clauses:
            if any((lit > 0 and new_assignment.get(abs(lit), None) == True) or
                   (lit < 0 and new_assignment.get(abs(lit), None) == False) for lit in clause):
                continue  # clause true với gán này, bỏ qua
            new_clause = [lit for lit in clause if abs(lit) not in new_assignment]
            simplified.append(new_clause)

        result = solve_cnf_backtrack(simplified, new_assignment)
        if result is not None:
            return result

    return None
