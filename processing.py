from abc import ABC, abstractmethod
from strategy import StudentData
import pandas   
#import os

GRADES = ['Fail', '3', '3/4', '4', '4', '4/5', '5', '5']

class DataProcessor(ABC):
    def __init__(self, sourcepath, data):
        self._sourcepath = sourcepath   
        self._data = data 

    @abstractmethod
    def read(self) -> bool:
        pass
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def print_result(self):
        pass

    
        
class StudentDataProcessor(DataProcessor):
    def __init__(self, sourcepath, data):
        DataProcessor.__init__(self, sourcepath, data) 
        self.student_data = None
        self.result = None
    
    def read(self):
        try:
            self.student_data = StudentData(self._sourcepath, self._data)
            return True
        except Exception as e:
            print(str(e))
            return False

    def run(self):
        if self.student_data != None:
            for mode in ['c','v','p']:
                self.student_data.set_strategy(mode)
                self.result = self.student_data.process()

    def print_result(self):
        print (f"Grade: {self.result}")





