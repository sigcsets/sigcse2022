import sys
import datetime
import calendar

# Converts AUTHOR (AFFILIATION);AUTHOR (AFFILIATION)*\t]

inputfile = '_scripts/authors.tsv'

try:
    with open(inputfile, encoding='utf8') as f:
        content = f.readlines()
except Exception as e:
    print('File could not be opened.', e)
    sys.exit(3)

f = open("_data/pathable_authors.csv", "w", encoding='utf8')

for line in content:
    entry = line.strip().split("\t")
    print(entry)