from kaitaistruct import KaitaiStream
from compiled.test_cell import TestCell
from compiled.test_col_fixed import TestColFixed

import time
import random
import statistics
import sys

# https://stackoverflow.com/a/34482761
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

num_iterations = 256
times = {}
cases = ['test_cell', 'test_col_fixed']

for k in cases:
    times[k] = []

# https://www.peterbe.com/plog/how-to-do-performance-micro-benchmarks-in-python
for i in progressbar(range(num_iterations), "Running benchmark: ", 40):
    choice = cases[random.randint(0, 1)]
    k = None
    row_0 = None
    t0 = time.time()

    with open('./sample.bin', 'rb') as f:
        if choice == 'test_cell':
            k = TestCell(KaitaiStream(f))
            row_0 = k.table.table_rows[0].entries
        elif choice == 'test_col_fixed':
            k = TestColFixed(KaitaiStream(f))
            row_0_type = k.table.table_rows[0]
            row_0 = [row_0_type.a, row_0_type.b, row_0_type.c, row_0_type.d]

    t1 = time.time()
    assert len(k.table.table_rows) == 8192, 'len(k.table.table_rows) = {} must be {}'.format(len(k.table.table_rows), 4096)
    assert row_0 == [0x7a46, 0x86b97d9c, 0.842150092124939, 0.5340359913176319], 'row_0 = {} does not match'.format(row_0)
    times[choice].append((t1 - t0) * 1000)

stats = [
    ('MEDIAN', lambda numbers: statistics.median(numbers)),
    ('MEAN', lambda numbers: statistics.mean(numbers)),
    ('STDEV', lambda numbers: statistics.stdev(numbers)),
    ('1st', lambda numbers: numbers[0]),
    ('MIN', lambda numbers: min(numbers)),
    ('MAX', lambda numbers: max(numbers)),
]

for name, numbers in times.items():
    print('FUNCTION: {} [Used {} times]'.format(name, len(numbers)))
    for stat in stats:
        print('\t{:6} {:=10.4f} ms'.format(stat[0], stat[1](numbers)))
    print('')
