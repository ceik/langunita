#!/usr/bin/env python3

# Non recursive backtracking algorithm for 2Sat


class Backtrack:
    def __init__(self, num_vars, data):
        self.num_vars = num_vars
        self.clauses = data
        self.not_sat_clauses = data
        self.sat_clauses = {}
        self.vars = {}
        self.clause_mapping = {}

        for var in range(num_vars):
            self.vars[var + 1] = None
            self.clause_mapping[var + 1] = []

        for index, clause in enumerate(self.clauses):
            self.clause_mapping[abs(clause[0])].append(index + 1)
            self.clause_mapping[abs(clause[1])].append(index + 1)

        # print(self.clauses)
        # print(self.clause_mapping)

    def main(self):
        for var_id, var_val in self.vars.items():
            print(var_id)
            print(self.clause_mapping[var_id])
            if len(self.clause_mapping[var_id]) == 0:
                self.vars[var_id] = True
                continue
            if var_val is not None:
                print(var_id, 'already set to', var_val)
                continue
            result = self.probe_var(var_id)
            if result == 'not_sat':
                return result
            else:
                self.vars[var_id] = result

        print(self.vars)
        return self.vars

    def probe_var(self, var_id):
        for setting in [True, False]:
            print('trying', var_id, setting)
            success = False
            for clause_id in self.clause_mapping[var_id]:
                clause = self.clauses[clause_id - 1]
                print(clause)
                # Determine positions, ids, and signs
                var_pos = 0 if abs(clause[0]) == var_id else 1
                var_sign = True if clause[var_pos] > 0 else False
                other_pos = var_pos ^ 1
                other_id = abs(clause[other_pos])
                other_sign = True if clause[other_pos] > 0 else False

                # If var_sign and setting don't match (xor) the other var needs
                # to take a certain value in order for the clause to bet
                # satisfied
                if var_sign ^ setting:
                    self.vars[var_id] = setting
                    if self.vars[other_id] is not None:
                        if self.vars[other_id] != other_sign:
                            self.vars[var_id] = None
                            success = False
                            break
                    else:
                        result = self.probe_var(other_id)
                        if result == 'not_sat':
                            self.vars[var_id] = None
                            success = False
                            break
                        else:
                            self.vars[other_id] = result
                success = True
            if success:
                return setting
        return 'not_sat'

    def check_setting(self, var_id, setting):
        implications = {}
        sat_clauses = []
        for clause_id in self.clause_mapping[var_id]:
            clause = self.clauses[clause_id - 1]
            print(clause)
            # Determine positions, ids, and signs
            var_pos = 0 if abs(clause[0]) == var_id else 1
            var_sign = True if clause[var_pos] > 0 else False
            other_pos = var_pos ^ 1
            other_id = abs(clause[other_pos])
            other_sign = True if clause[other_pos] > 0 else False

            # If var_sign and setting don't match (xor) the other var needs to
            # take a certain value in order for the clause to bet satisfied
            if var_sign ^ setting:
                if other_id in implications:
                    if implications[other_id] != other_sign:
                        print('contradiction! other id should be', other_sign,
                              'but it is', implications[other_id])
                        return False
                else:
                    implications[other_id] = other_sign

        return implications

        print(implications)
        print(sat_clauses)
