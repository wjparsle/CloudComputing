#!/usr/bin/env/python

from collections import defaultdict
import sys

total_counts = defaultdict(int)
max_year = None
max_count = -1
for line in sys.stdin:
    (year, count) = line.split(";")
    count = int(count)
    total_counts[year] += count
    if count > max_count:
        max_count = count
        max_year = year
print(f'{max_year}:{max_count}')