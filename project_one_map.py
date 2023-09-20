#!/usr/bin/env/python
import pandas as pd
from collections import defaultdict
import sys

df = pd.read_csv(sys.stdin)
data = df['Activity'].dropna()
year_count = defaultdict(int)
for entry in data:
    year_count[entry] += 1
    
for key in year_count.keys():
    if year_count[key] > 3:
        print(f'{key};{year_count[key]}')