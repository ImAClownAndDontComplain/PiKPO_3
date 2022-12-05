from processing import StudentDataProcessor
import pandas

class Interface:
    def __init__(self):        
        #self.separator = ','  
        #self.sourcepath = sourcepath
        #self.dataset = pandas.read_csv(sourcepath, sep=self.separator, header='infer', names=None, encoding="utf-8")
        self.processor = None

    def call(self):
        self.client = input('Enter your name  >>  ')  
        self.enter()

    def enter(self):
        cols = ['SCHOLARSHIP','ACTIVITY','STUDY_HRS', 'READ_FREQ','READ_FREQ_SCI','IMPACT','ATTEND','PREP_STUDY','PREP_EXAM','NOTES','LISTENS','LIKES_DISCUSS','CUML_GPA']
        #self.data = pandas.DataFrame(columns = cols)
        #print('Enter the data:')
        row = [5,1,3,2,2,1,1,1,2,3,3,3,5]
        #while True:
        #    value = input()
        #    if value == 'Restart':
        #        row.clear()
        #        print('Enter the data:')
        #    elif value == 'None':
        #        row.append(-1)
        #    else:
        #        row.append(value)
        #        if len(row) == len (cols):
        #            print('Data input ended\n')
        #            break

        self.data = pandas.DataFrame([row], columns = cols)

    def process(self):
        #self.call()
        self.enter()
        self.processor = StudentDataProcessor('students.csv', self.data)
        self.processor.read()
        self.processor.run()
        self.processor.print_result()




