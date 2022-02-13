from asyncio.windows_events import NULL
from asyncore import read
from datareader import DataReader
from node import Node

class ID3:
    def __init__(self, dataset):
        self.dataset = dataset
        self.tree = self.train_on_dataset(self.dataset)
    
    def train_on_dataset(self, dataset):
        #TODO: Implement
        tree = Node(dataset, NULL)
        return tree
    
    def predict_target_value_for_instance(self, instance):
        #TODO: Implement
        return False
    
    def test_on_dataset(self, dataset):
        #TODO: Implement
        return False

if __name__ == '__main__':
    try:
        with open('datasets/lakesDiscreteFold1.arff', 'r') as training_file:
            id3 = ID3(DataReader.parse_file_into_dataset(training_file))
        with open('datasets/lakesDiscreteFold2.arff', 'r') as testing_file:
            accuracy = ID3.test_on_dataset(DataReader.parse_file_into_dataset(testing_file))
    except EnvironmentError as e:
        print(e)
    for feature in ID3.dataset.features:
        if(feature['value_type'] == 'numeric'):
            print(feature['name'], "min:", ID3.dataset.get_feature_min(feature['name']))
            print(feature['name'], "max:", ID3.dataset.get_feature_max(feature['name']))
        elif(feature['value_type'] == 'discrete'):
            print("All possible values for", feature['name'], ": ", feature['possible_values'])
    target_feature = input("What is the target feature? ")
    split_feature = input("What is the feature to split on? ")
    print("The information gain is:", ID3.dataset.get_information_gain(target_feature, split_feature))
            