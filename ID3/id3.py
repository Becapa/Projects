from datareader import DataReader
from node import Node

class ID3:
    def __init__(self, dataset, tree):
        self.dataset = dataset
        self.tree = tree
    
    def train_on_dataset(training_dataset):
        tree = Node(training_dataset)
        tree.build()
        return tree
    
    def predict_target_value_for_instance(self, instance):
        #TODO: Implement
        return False

if __name__ == '__main__':
    try:
        with open('datasets/lakesDiscreteFold1.arff', 'r') as training_file:
            training_dataset = DataReader.parse_file_into_dataset(training_file)
        with open('datasets/lakesDiscreteFold2.arff', 'r') as testing_file:
            testing_dataset = DataReader.parse_file_into_dataset(testing_file)
        print(training_dataset.features)
        decision_tree = ID3.train_on_dataset(training_dataset)
        id3 = ID3(training_dataset, decision_tree)
        num_correct = 0
        for instance in testing_dataset.instances:
            predicted_value = id3.predict_target_value_for_instance(instance)
            if predicted_value == list(instance.values())[-1]:
                num_correct += 1
        accuracy = num_correct / len(testing_dataset.instances) * 100
        print("The id3 tree has an accuracy of", accuracy,"%")
    except EnvironmentError as e:
        print(e)
            