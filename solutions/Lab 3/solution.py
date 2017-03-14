
m collections import Counter
import csv
from decimal import *

FILE1 = "/home/guru/pythonfortooldevelopers-master/labs/Lab2/data/trans1.csv"
FILE2 = "/home/guru/pythonfortooldevelopers-master/labs/Lab2/data/trans2.csv"

def generate_rows(filename):
    with open (filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="|", quotechar="\"")
        for row in reader:
            yield row 

def get_amounts(filename):
    for (index, row) in enumerate(generate_rows(filename)):
        if index > 0 and row[-2] == 'DEPOSIT':
            yield row[-1][1:].strip() 
def get_expected(N):
    from math import log10
    return (N * log10(1 + 1.0 / d) for d in range(1, 10)) 

def get_actual(amounts):
    return Counter(map(lambda x: int(x[0]), [x for x in amounts]))

def get_chi_square(expected, actual):
    return sum(((actual[O] - E) ** 2 / E for (O, E) in zip(actual, expected)))

if __name__ == "__main__":
    FILE1_amounts = list(get_amounts(FILE1))
    FILE2_amounts = list(get_amounts(FILE2))
    FILE1_CHI_SQUARE = get_chi_square(get_expected(len(FILE1_amounts)),
                                      get_actual(FILE1_amounts))
                                      FILE2_CHI_SQUARE = get_chi_square(get_expected(len(FILE2_amounts)),
                                                                        get_actual(FILE2_amounts))
     print ("FILE1 Chi square: ", FILE1_CHI_SQUARE)
     print ("FILE2 Chi square: ", FILE2_CHI_SQUARE)
