from operator import itemgetter
import csv
SCORESHEET = '.static/data/SCORESHEET.CSV'

def print_record_count():
    print("there are", len(SCORESHEET), "rows.")