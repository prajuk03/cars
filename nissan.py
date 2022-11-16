class nissan:
    def __init__(self):
        self.models = ['altima','370z','cube','rogue']
        
    def outModels(self):
        print('These are the available models for nissan')
        for model in self.models:
            print('t\%s' % model)