#python code to illustrate the module
class audi:
    def __init__(self):
        self.models = ['q7','a6','a8','a3']
        
    def outModels(self):
        print('These are the available models for audi')
        for model in self.models:
            print('\t%s ' % model)
            