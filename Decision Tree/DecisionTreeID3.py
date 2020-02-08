import numpy as np , random, math, uuid, sys

def readAttributes (TXTFile,is_there_unknown):
    with open(TXTFile,'r') as f:
        given_attr = dict()
        given_numeric = dict()
        given_order = list()
        given_unknow = set()

        for line in f:
            #building the braches/sets
            values = line.split()
            name_of_att = values[0]
            given_order.append(name_of_att)
            given_attr[name_of_att] = set()
            if values[1]== "numeric":
                given_attr[name_of_att].add(1)
                given_attr[name_of_att].add(-1)
                given_numeric[name_of_att] = values[0]
            else:
                for type in range(1,len(values)):
                    if is_there_unknown:
                        if values[type]:
                            given_unknow.add(name_of_att)
                            continue
                    given_attr[name_of_att].add(type)
        return given_attr,given_order,given_numeric,given_unknow



def reading_Data_from_csv(CSVFile,given_order,given_numeric,given_unknow):
    with open(CSVFile, 'r') as f:
        data_from_csv = list()
        index = 0
        for line in f:
            terms = line.strip().split(',')
            section = dict()
            for val in range(len(terms)-1):
                type = given_order[val]
                value= section[val]
                if type in given_numeric:
                    given_numeric[type].append(int(value))
                section[type] = value
                section['label']=terms[len(terms) - 1]
                section['index']= index
            index+=1
            data_from_csv.append(section)
        if given_numeric is not None:
            #changing data to numeric
            data_from_csv
        if given_unknow is not None:
            #chain
            data_from_csv
        return data_from_csv


def main ():
    try :
        #if you want to choose b
        if sys.argv[1]=="bank":
           given_attr,given_order,given_numeric,given_unknow = readAttributes("../Decision Tree/bank/bank_data.txt", True)
           train = reading_Data_from_csv("../Decision Tree/bank/train.csv",given_order,given_numeric,given_unknow)
           test = reading_Data_from_csv("../Decision Tree/bank/test.csv",given_order,given_numeric,given_unknow)
        if sys.argv[1]=="car":
            given_attr, given_order, given_numeric, given_unknow = readAttributes("../Decision Tree/car/car_data.txt",False)
            train = reading_Data_from_csv("../Decision Tree/car/train.csv",given_order,given_numeric,given_unknow)
            test = reading_Data_from_csv("../Decision Tree/car/test.csv",given_order,given_numeric,given_unknow)

    except:
        print "python DecisionTreeID3.py <car or bank>"

if __name__ == '__main__':
    main()
