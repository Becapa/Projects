from datareader import DataReader
from node import Node

class KNN:
    def __init__(self, dataset, tree):
        self.dataset = dataset
        self.tree = tree

if __name__ == '__main__':
    try:
        #with open('datasets/Table4-3.arff', 'r') as training_file:
        with open('datasets/lakesDiscreteFold1.arff', 'r') as training_file:
            training_dataset = DataReader.parse_file_into_dataset(training_file)
        
    except EnvironmentError as e:
        print(e)
            