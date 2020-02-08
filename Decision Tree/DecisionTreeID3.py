import numpy, random, math, uuid, sys

def readAttributes (TXTFile):
    with open(TXTFile,'r') as f:
        for line in f:
            terms = line.strip().split(',')
            adding_terms = dict()
def read_training(CSVFile):
    with open(CSVFile, 'r') as f:
        for line in f:
            terms = line.strip().split(',')
            adding_terms = dict()
def read_test(CSVFile):
    with open(CSVFile, 'r') as f:
        for line in f:
            terms = line.strip().split(',')
            adding_terms = dict()

def main ():
    try :
        if sys.argv[1]=="car":
            readAttributes("../Decision Tree/bank/data-desc-readable.txt")
        if sys.argv[1]=="bank":
            readAttributes("../Decision Tree/car/data-desc-readable.txt")


    except:
        print "python DecisionTreeID3.py <car or bank>"

if __name__ == '__main__':
    main()
