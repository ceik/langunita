#!/usr/bin/env python3

# Don't use this for the assignment
# It's a lot faster than the version from the lecture, but still too slow for
# the bigger datasets from the asignment

from math import log
from random import getrandbits, choice
from datetime import datetime


class Papa:
    def __init__(self, num_vars, data):
        self.num_vars = num_vars
        self.data = data
        self.clause_mapping = {}

        for var in range(num_vars):
            self.clause_mapping[var + 1] = []

        for index, clause in enumerate(self.data):
            self.clause_mapping[abs(clause[0])].append(index + 1)
            self.clause_mapping[abs(clause[1])].append(index + 1)

    def main(self):
        rounds = round(log(self.num_vars, 2))
        tries_per_round = round(pow(2 * self.num_vars, 2))
        # tries_per_round = 1000
        print('start:', datetime.now(), 'with rounds/tries:', rounds, tries_per_round)

        for x in range(rounds):
            print('round', x)
            all_vars = []
            all_clauses = []
            t_clauses = {}
            f_clauses = {}

            # Random Initial Assignment
            for var in range(self.num_vars):
                all_vars.append(bool(getrandbits(1)))

            for index, clause in enumerate(self.data):
                c = []
                for b in clause:
                    abs_b = all_vars[abs(b) - 1]
                    c.append(abs_b if b > 0 else not abs_b)
                all_clauses.append(c)
                if any(c):
                    t_clauses[index + 1] = clause
                else:
                    f_clauses[index + 1] = clause

            if len(f_clauses) == 0:
                print("statisfiable", datetime.now())
                return("statisfiable")

            for _ in range(tries_per_round):
                # Change random variable from random unstatisfied clause
                flip_ind, flip_clause = choice(list(f_clauses.items()))
                flip_var = abs(choice(flip_clause))
                all_vars[flip_var - 1] = not all_vars[flip_var - 1]

                # Go through all clauses that contain flip_var and reevaluate
                for affected_clause_ind in self.clause_mapping[flip_var]:
                    try:
                        affected_clause = t_clauses.pop(affected_clause_ind)
                    except KeyError:
                        affected_clause = f_clauses.pop(affected_clause_ind)

                    updated_clause_result = []
                    for term in affected_clause:
                        abs_term = all_vars[abs(term) - 1]
                        updated_clause_result.append(
                            abs_term if b > 0 else not abs_term)

                    if any(updated_clause_result):
                        t_clauses[affected_clause_ind] = affected_clause
                    else:
                        f_clauses[affected_clause_ind] = affected_clause

                res = len(f_clauses)
                print(res)

                if res == 0:
                    print("statisfiable", datetime.now())
                    return("statisfiable")

        print("not statisfiable", datetime.now())
        return("not statisfiable")
