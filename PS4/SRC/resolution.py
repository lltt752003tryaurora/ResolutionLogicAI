def pl_resolution(kb, alpha):
    def split_clause(clause):
        return frozenset(sorted(clause.split(' OR ')))

    def negate_literal(literal):
        return literal[1:] if literal.startswith('-') else '-' + literal

    def resolve(clause1, clause2):
        for literal in clause1:
            if negate_literal(literal) in clause2:
                new_clause = clause1.union(clause2) - {literal, negate_literal(literal)}
                # Loại bỏ mệnh đề nếu chứa cả literal và phủ định của nó
                if any(negate_literal(lit) in new_clause for lit in new_clause):
                    return None
                new_clause = sorted(new_clause, key=lambda l: (l[0] == '-', l))
                return frozenset(new_clause)
        return None

    new_clauses = set()
    kb_clauses = set(split_clause(clause) for clause in kb)
    kb_clauses.add(split_clause(negate_literal(alpha)))

    resolution_process = []

    while True:
        new = set()
        pairs = [(c1, c2) for c1 in kb_clauses for c2 in kb_clauses if c1 != c2]
        
        for (clause1, clause2) in pairs:
            resolvent = resolve(clause1, clause2)
            if resolvent is not None:
                if not resolvent:
                    resolution_process.append("{}")
                    return resolution_process, 'YES'
                if resolvent not in kb_clauses and resolvent not in new:
                    new.add(resolvent)
        
        if not new:  # Nếu không có mệnh đề mới được tạo ra, kết thúc quá trình hợp giải
            if new_clauses:  # Nếu có mệnh đề đã được thêm vào trước đó
                resolution_process.append(sorted(map(sorted, new_clauses), key=lambda x: ''.join(x)))
            return resolution_process, 'NO'
        
        kb_clauses |= new
        resolution_process.append(sorted(map(sorted, new_clauses), key=lambda x: ''.join(x)))
        new_clauses = new
