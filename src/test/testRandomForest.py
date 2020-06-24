'''
Created on Jun 22, 2020

@author: pharten
'''
import unittest

import RandomForest as rf

from pathlib import Path

class TestRandomForest(unittest.TestCase):
    
    def test_readcsv1(self):
        self.assertIsNotNone(rf.readcsv(self, "../../data/LC50_training_set-2d.csv")," no train_features")
        
    def test_readcsv2(self):
        train_features = rf.readcsv(self, "../../data/LC50_training_set-2d.csv")
        shape = train_features.shape
        self.assertEqual(shape[0], 659,  " training set has wrong number of rows")
        self.assertEqual(shape[1], 799,  " training set has wrong number of columns")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()