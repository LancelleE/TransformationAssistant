class Data:
    def __init__(self, dataset, filename):
        self.dataset = dataset
        self.filename = filename

    def var_type(self):
        return '\n'.join([f'Variable: {i} Type: {j}' for i,j in self.dataset.dtypes.items()])
    

