from abc import ABC, abstractmethod    
import math
import pandas   
#import os

GRADES = ['Fail', '3', '3/4', '4', '4', '4/5', '5', '5']

class DataHandlingStrategy(ABC):   
    @abstractmethod
    def process(self):
        pass



class DataCorrecting(DataHandlingStrategy):
    def process(self, dataset):
        try:
            del dataset['STUDENTID']
            del dataset['AGE']
            del dataset['GENDER']
            del dataset['HS_TYPE']
            del dataset['WORK']
            del dataset['PARTNER']
            del dataset['SALARY']
            del dataset['TRANSPORT']
            del dataset['LIVING']
            del dataset['MOTHER_EDU']
            del dataset['FATHER_EDU']
            del dataset['#_SIBLINGS']
            del dataset['KIDS']
            del dataset['MOTHER_JOB']
            del dataset['FATHER_JOB']
            del dataset['ATTEND_DEPT']
            del dataset['CLASSROOM']
            del dataset['EXP_GPA']
            del dataset['COURSE ID']
            return 1
        except Exception as e:
            print('Invalid dataset\n')
            return -1

class DataValidating(DataHandlingStrategy):
    def process(self, dataset, data):
        if data.shape[1] == dataset.shape[1] - 1:
            return 1
        print('Incorrect input data\n')
        return -1


class DataParsing(DataHandlingStrategy):
    def process(self, dataset, data):
        #ncols = data.shape[1]
        nrows = dataset.shape[0]
        values = []
        valuemax = 0
        for row in range(0,nrows):
            value = 0
            for col in data.columns:
                if dataset[col].values[row] == data[col].values[0]:
                    value = value + 1
            if value > valuemax:
                valuemax = value
                values.clear()
                values.append(row)
            elif value == valuemax:
                values.append(row)

        grades = []
        
        for row in values:
            grades.append(dataset['GRADE'].values[row])
    
        avgrade = math.ceil(sum(grades)/len(grades))

        return GRADES[avgrade]

class StudentData:
    def __init__(self, sourcepath, data):
        self.dataset = pandas.read_csv(sourcepath, sep=',', header='infer', names=None, encoding="utf-8")
        self.data = data
        self.strategy = None
        self.cor = None
        
    def set_strategy(self, mode):
        if mode == 'c':
            self.strategy = DataCorrecting()
            self.cor = True
        elif mode == 'v':
            self.strategy = DataValidating()
            self.cor = False
        elif mode == 'p':
            self.strategy = DataParsing()
            self.cor = False

    def process(self):
        if self.strategy != None:
            #if self.result != True:
            #    return self.
            if self.cor == True:    
                return self.strategy.process(self.dataset)
            elif self.cor == False:
                return self.strategy.process(self.dataset, self.data)



    

