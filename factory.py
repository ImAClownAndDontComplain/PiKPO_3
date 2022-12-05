from abc import ABC, abstractmethod
from dataproc import *
import os


class DataProcessorFactory(ABC):
    def __init__(self):
        self.instance = None

    @abstractmethod
    def get_processor(self, sourcepath, datapath) -> DataProcessor:
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def showres(self):
        pass

class CsvDataProcessorFactory(DataProcessorFactory):
    def get_processor(self, sourcepath, datapath) -> DataProcessor:
        self.instance = CsvDataProcessor(sourcepath, datapath)
        if self.instance.read():
            return self.instance
        elif self.read_with_separator(','):
            return self.instance
        return None

    def read_with_separator(self, sep) -> bool:
        self.instance.separator = sep
        if self.instance.read():
            return True
        return False

    def process(self):
        self.instance.run()

    def showres(self):
        self.instance.print_result()


class TxtDataProcessorFactory(DataProcessorFactory):
    def get_processor(self, sourcepath, datapath) -> DataProcessor:
        self.instance = TxtDataProcessor(sourcepath, datapath)
        if self.instance.read():
            return self.instance
        return None

    def process(self):
        self.instance.run()

    def showres(self):
        self.instance.print_result()




