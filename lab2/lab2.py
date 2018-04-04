#!/usr/bin/env python
from bisect import bisect_left
import json

import numpy as np
from scipy.optimize import linear_sum_assignment


def main():
    with open('data.json') as infile:
        data = json.load(infile)

    costs = (
        -np.array(data['efficiency'])
        .repeat(data['groups'], axis=0)
        .repeat(data['tasks'], axis=1)
    )

    row_ind, col_ind = linear_sum_assignment(costs)

    print(f'Total efficiency: {-costs[row_ind, col_ind].sum()}')

    for i in range(len(row_ind)):
        worker_group = bisect_left(np.cumsum(data['groups']) - 1, row_ind[i])
        work_group = bisect_left(np.cumsum(data['tasks']) - 1, col_ind[i])
        print(f'Worker from group {worker_group} assigned to task group {work_group}, '
              f'efficiency: {-costs[row_ind[i], col_ind[i]]}')


if __name__ == '__main__':
    main()
