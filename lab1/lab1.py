from ortools.linear_solver import pywraplp
from ortools.linear_solver.pywraplp import Solver


def init_solver():
    solver = pywraplp.Solver(
        'SolveIntegerProblem',
        pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING,
    )

    full_time_1 = solver.IntVar(0, solver.Infinity(), 'full_time_1')  # 9-12, 13-17, 8h
    full_time_2 = solver.IntVar(0, solver.Infinity(), 'full_time_2')  # 11-14, 15-19, 8h
    part_time_1 = solver.IntVar(0, solver.Infinity(), 'part_time_1')  # 9-13, 6h
    part_time_2 = solver.IntVar(0, solver.Infinity(), 'part_time_2')  # 10-14, 7h
    part_time_3 = solver.IntVar(0, solver.Infinity(), 'part_time_3')  # 11-15, 9h
    part_time_4 = solver.IntVar(0, solver.Infinity(), 'part_time_4')  # 12-16, 10h
    part_time_5 = solver.IntVar(0, solver.Infinity(), 'part_time_5')  # 13-17, 8h
    part_time_6 = solver.IntVar(0, solver.Infinity(), 'part_time_6')  # 14-18, 6h
    part_time_7 = solver.IntVar(0, solver.Infinity(), 'part_time_7')  # 15-19, 6h

    constraint_9_10 = solver.Constraint(16, solver.Infinity())
    constraint_9_10.SetCoefficient(full_time_1, 1)
    constraint_9_10.SetCoefficient(full_time_2, 0)
    constraint_9_10.SetCoefficient(part_time_1, 1)
    constraint_9_10.SetCoefficient(part_time_2, 0)
    constraint_9_10.SetCoefficient(part_time_3, 0)
    constraint_9_10.SetCoefficient(part_time_4, 0)
    constraint_9_10.SetCoefficient(part_time_5, 0)
    constraint_9_10.SetCoefficient(part_time_6, 0)
    constraint_9_10.SetCoefficient(part_time_7, 0)

    constraint_10_11 = solver.Constraint(30, solver.Infinity())
    constraint_10_11.SetCoefficient(full_time_1, 1)
    constraint_10_11.SetCoefficient(full_time_2, 0)
    constraint_10_11.SetCoefficient(part_time_1, 1)
    constraint_10_11.SetCoefficient(part_time_2, 1)
    constraint_10_11.SetCoefficient(part_time_3, 0)
    constraint_10_11.SetCoefficient(part_time_4, 0)
    constraint_10_11.SetCoefficient(part_time_5, 0)
    constraint_10_11.SetCoefficient(part_time_6, 0)
    constraint_10_11.SetCoefficient(part_time_7, 0)

    constraint_11_12 = solver.Constraint(31, solver.Infinity())
    constraint_11_12.SetCoefficient(full_time_1, 1)
    constraint_11_12.SetCoefficient(full_time_2, 1)
    constraint_11_12.SetCoefficient(part_time_1, 1)
    constraint_11_12.SetCoefficient(part_time_2, 1)
    constraint_11_12.SetCoefficient(part_time_3, 1)
    constraint_11_12.SetCoefficient(part_time_4, 0)
    constraint_11_12.SetCoefficient(part_time_5, 0)
    constraint_11_12.SetCoefficient(part_time_6, 0)
    constraint_11_12.SetCoefficient(part_time_7, 0)

    constraint_12_13 = solver.Constraint(45, solver.Infinity())
    constraint_12_13.SetCoefficient(full_time_1, 0)
    constraint_12_13.SetCoefficient(full_time_2, 1)
    constraint_12_13.SetCoefficient(part_time_1, 1)
    constraint_12_13.SetCoefficient(part_time_2, 1)
    constraint_12_13.SetCoefficient(part_time_3, 1)
    constraint_12_13.SetCoefficient(part_time_4, 1)
    constraint_12_13.SetCoefficient(part_time_5, 0)
    constraint_12_13.SetCoefficient(part_time_6, 0)
    constraint_12_13.SetCoefficient(part_time_7, 0)

    constraint_13_14 = solver.Constraint(66, solver.Infinity())
    constraint_13_14.SetCoefficient(full_time_1, 1)
    constraint_13_14.SetCoefficient(full_time_2, 1)
    constraint_13_14.SetCoefficient(part_time_1, 0)
    constraint_13_14.SetCoefficient(part_time_2, 1)
    constraint_13_14.SetCoefficient(part_time_3, 1)
    constraint_13_14.SetCoefficient(part_time_4, 1)
    constraint_13_14.SetCoefficient(part_time_5, 1)
    constraint_13_14.SetCoefficient(part_time_6, 0)
    constraint_13_14.SetCoefficient(part_time_7, 0)

    constraint_14_15 = solver.Constraint(72, solver.Infinity())
    constraint_14_15.SetCoefficient(full_time_1, 1)
    constraint_14_15.SetCoefficient(full_time_2, 0)
    constraint_14_15.SetCoefficient(part_time_1, 0)
    constraint_14_15.SetCoefficient(part_time_2, 0)
    constraint_14_15.SetCoefficient(part_time_3, 1)
    constraint_14_15.SetCoefficient(part_time_4, 1)
    constraint_14_15.SetCoefficient(part_time_5, 1)
    constraint_14_15.SetCoefficient(part_time_6, 1)
    constraint_14_15.SetCoefficient(part_time_7, 0)

    constraint_15_16 = solver.Constraint(61, solver.Infinity())
    constraint_15_16.SetCoefficient(full_time_1, 1)
    constraint_15_16.SetCoefficient(full_time_2, 1)
    constraint_15_16.SetCoefficient(part_time_1, 0)
    constraint_15_16.SetCoefficient(part_time_2, 0)
    constraint_15_16.SetCoefficient(part_time_3, 0)
    constraint_15_16.SetCoefficient(part_time_4, 1)
    constraint_15_16.SetCoefficient(part_time_5, 1)
    constraint_15_16.SetCoefficient(part_time_6, 1)
    constraint_15_16.SetCoefficient(part_time_7, 1)

    constraint_16_17 = solver.Constraint(34, solver.Infinity())
    constraint_16_17.SetCoefficient(full_time_1, 1)
    constraint_16_17.SetCoefficient(full_time_2, 1)
    constraint_16_17.SetCoefficient(part_time_1, 0)
    constraint_16_17.SetCoefficient(part_time_2, 0)
    constraint_16_17.SetCoefficient(part_time_3, 0)
    constraint_16_17.SetCoefficient(part_time_4, 0)
    constraint_16_17.SetCoefficient(part_time_5, 1)
    constraint_16_17.SetCoefficient(part_time_6, 1)
    constraint_16_17.SetCoefficient(part_time_7, 1)

    constraint_17_18 = solver.Constraint(16, solver.Infinity())
    constraint_17_18.SetCoefficient(full_time_1, 0)
    constraint_17_18.SetCoefficient(full_time_2, 1)
    constraint_17_18.SetCoefficient(part_time_1, 0)
    constraint_17_18.SetCoefficient(part_time_2, 0)
    constraint_17_18.SetCoefficient(part_time_3, 0)
    constraint_17_18.SetCoefficient(part_time_4, 0)
    constraint_17_18.SetCoefficient(part_time_5, 0)
    constraint_17_18.SetCoefficient(part_time_6, 1)
    constraint_17_18.SetCoefficient(part_time_7, 1)

    constraint_18_19 = solver.Constraint(10, solver.Infinity())
    constraint_18_19.SetCoefficient(full_time_1, 0)
    constraint_18_19.SetCoefficient(full_time_2, 1)
    constraint_18_19.SetCoefficient(part_time_1, 0)
    constraint_18_19.SetCoefficient(part_time_2, 0)
    constraint_18_19.SetCoefficient(part_time_3, 0)
    constraint_18_19.SetCoefficient(part_time_4, 0)
    constraint_18_19.SetCoefficient(part_time_5, 0)
    constraint_18_19.SetCoefficient(part_time_6, 0)
    constraint_18_19.SetCoefficient(part_time_7, 1)

    objective = solver.Objective()
    objective.SetCoefficient(full_time_1, 8 * 8)
    objective.SetCoefficient(full_time_2, 8 * 8)
    objective.SetCoefficient(part_time_1, 6 * 4)
    objective.SetCoefficient(part_time_2, 7 * 4)
    objective.SetCoefficient(part_time_3, 9 * 4)
    objective.SetCoefficient(part_time_4, 10 * 4)
    objective.SetCoefficient(part_time_5, 8 * 4)
    objective.SetCoefficient(part_time_6, 6 * 4)
    objective.SetCoefficient(part_time_7, 6 * 4)
    objective.SetMinimization()

    variables = [full_time_1, full_time_2, part_time_1, part_time_2, part_time_3,
                 part_time_4, part_time_5, part_time_6, part_time_7]

    constraints = [
        constraint_9_10, constraint_10_11, constraint_11_12, constraint_12_13, constraint_13_14,
        constraint_14_15, constraint_15_16, constraint_16_17, constraint_17_18, constraint_18_19,
    ]

    return solver, variables, constraints, objective


def solve(solver: Solver):
    result = solver.Solve()
    optimal = result == pywraplp.Solver.OPTIMAL
    verified = solver.VerifySolution(1e-4, True)
    return optimal, verified


def show_result(optimal, verified, variables, objective):
    print(f'Optimal: {optimal}')
    print(f'Verified: {verified}')

    for variable in variables:
        print(f'{variable.name()}: {variable.solution_value()}')

    print(f'Objective: {objective.Value()}')
    print()


def main():
    #1
    solver, variables, constraints, objective = init_solver()

    optimal, verified = solve(solver)
    show_result(optimal, verified, variables, objective)

    #2
    solver, variables, constraints, objective = init_solver()

    fulltime_constraint = solver.Constraint(4, solver.Infinity())
    fulltime_constraint.SetCoefficient(variables[0], 1)
    fulltime_constraint.SetCoefficient(variables[1], 1)
    constraints.append(fulltime_constraint)

    optimal, verified = solve(solver)
    show_result(optimal, verified, variables, objective)

    #3
    solver, variables, constraints, objective = init_solver()

    count_constraint = solver.Constraint(0, 94)
    count_constraint.SetCoefficient(variables[0], 1)
    count_constraint.SetCoefficient(variables[1], 1)
    count_constraint.SetCoefficient(variables[2], 1)
    count_constraint.SetCoefficient(variables[3], 1)
    count_constraint.SetCoefficient(variables[4], 1)
    count_constraint.SetCoefficient(variables[5], 1)
    count_constraint.SetCoefficient(variables[6], 1)
    count_constraint.SetCoefficient(variables[7], 1)
    count_constraint.SetCoefficient(variables[8], 1)
    constraints.append(count_constraint)

    optimal, verified = solve(solver)
    show_result(optimal, verified, variables, objective)


if __name__ == '__main__':
    main()
