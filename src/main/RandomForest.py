'''
Created on Jun 18, 2020

@author: pharten
'''
# Pandas is used for data manipulation
import pandas as pd

from pathlib import Path

class RandomForest(object):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        '''
        Constructor
        '''
        pass

def readcsv(self, filename):
    path = Path.cwd().joinpath("../../data")
    path = path.joinpath(Path(filename).name)
    
    # Read in data and display first 5 rows
    train_features = pd.read_csv(path)
    return train_features
        

        
    