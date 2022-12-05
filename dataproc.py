from abc import ABC, abstractmethod    
from statistics import mean
import math
import pandas   
#import os

GRADES = ['Fail', '3', '3/4', '4', '4', '4/5', '5', '5']

class DataProcessor(ABC):
    def __init__(self, sourcepath, datapath):
        self._sourcepath = sourcepath   
        self._datapath = datapath           
        self._dataset = None
        self._data = None         

    @abstractmethod
    def read(self) -> bool:
        pass
    
    @abstractmethod
    def run(self):
        pass

    #def sort_data_by_col(self, df, colname, asc) -> pandas.DataFrame:
    #        return df.sort_values(by=[colname], ascending=asc)
        
    @abstractmethod
    def print_result(self):
        pass


class StudentDataCorrector:
    def correct(self, _dataset):
        del _dataset['STUDENTID']
        del _dataset['AGE']
        del _dataset['GENDER']
        del _dataset['HS_TYPE']
        del _dataset['PARTNER']
        del _dataset['WORK']
        del _dataset['SALARY']
        del _dataset['LIVING']
        del _dataset['TRANSPORT']
        del _dataset['MOTHER_EDU']
        del _dataset['FATHER_EDU']
        del _dataset['#_SIBLINGS']
        del _dataset['KIDS']
        del _dataset['MOTHER_JOB']
        del _dataset['FATHER_JOB']
        del _dataset['ATTEND_DEPT']
        del _dataset['CLASSROOM']
        del _dataset['EXP_GPA']
        del _dataset['COURSE ID']

class StudentDataProcessor:
    def process(self, _dataset, _data):
        ncols = _data.shape[1]
        nrows = _dataset.shape[0]
        values = []
        valuemax = 0
        for row in range(0,nrows):
            value = 0
            for col in _data.columns:
                if _dataset[col].values[row] == _data[col].values[0]:
                    value = value + 1
            if value > valuemax:
                valuemax = value
                values.clear()
                values.append(row)
            elif value == valuemax:
                values.append(row)

        grades = []
        
        for row in values:
            grades.append(_dataset['GRADE'].values[row])
    
        avgrade = math.ceil(sum(grades)/len(grades))

        return GRADES[avgrade]

        
class CsvDataProcessor(DataProcessor):
    def __init__(self, sourcepath, datapath):
        DataProcessor.__init__(self, sourcepath, datapath) 
        self.separator = ','       
        self.corrector = None
        self.processor = None
    
    def read(self):
        try:
            self._data = pandas.read_csv(self._datapath, sep=self.separator, header='infer', names=None, encoding="utf-8")
            self._dataset = pandas.read_csv(self._sourcepath, sep=self.separator, header='infer', names=None, encoding="utf-8")
            
            if self.corrector == None:
                self.corrector = StudentDataCorrector()
            self.corrector.correct(self._dataset)
            
            if self._data.shape[1] != self._dataset.shape[1] - 1:
                print('Incorrect input data')
                return False

            col_names = self._dataset.columns
            if len(col_names) < 2:
                return False
            return True
        except Exception as e:
            print(str(e))
            return False

    def run(self):
        if self.processor == None:
            self.processor = StudentDataProcessor()
        self.result = self.processor.process(self._dataset, self._data)

    def print_result(self):
        print (f"Grade: {self.result}")
        #for grade in self.result:
        #    print (f"Grade: {self._dataset['GRADE'].values[grade]}\n")
        #print(f'Running CSV-file processor!\n', self.result)




class TxtDataProcessor(DataProcessor):
    def __init__(self, sourcepath, datapath):
        DataProcessor.__init__(self, sourcepath, datapath) 
        self.separator = '\s+'       
        self.corrector = None
        self.processor = None

    def read(self):
        try:
            self._data = pandas.read_table(self._datapath, sep=self.separator, engine='python')
            self._dataset = pandas.read_table(self._sourcepath, sep=self.separator, engine='python')

            if self.corrector == None:
                self.corrector = StudentDataCorrector()
            self.corrector.correct(self._dataset)
            
            if self._data.shape[1] != self._dataset.shape[1] - 1:
                print('Incorrect input data')
                return False

            col_names = self._dataset.columns
            if len(col_names) < 2:
                return False
            return True

        except Exception as e:
            print(str(e))
            return False

    def run(self):
        if self.processor == None:
            self.processor = StudentDataProcessor()
        self.result = self.processor.process(self._dataset, self._data)

    def print_result(self):
        for grade in self.result:
            print (f"Grade: {self._dataset['GRADE'].values[grade]}\n")
        #print(f'Running CSV-file processor!\n', self.result)




