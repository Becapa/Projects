from datareader import DataReader
from node import Node

class ID3:
    def __init__(self, dataset, tree):
        self.dataset = dataset
        self.tree = tree
    
    def train_on_dataset(training_dataset):
        tree = ID3.build(training_dataset)
        return tree
    
    def predict_target_value_for_instance(self, instance, node):
        possible_values = self.dataset.target_feature['possible_values']
        label = node.label
        if label in possible_values:
            return label
        next_branch = instance[label]
        for child in node.children:
            if child.parent_branch == next_branch:
                return self.predict_target_value_for_instance(instance, child)

    def build(dataset, parent = None, branch = None):
        node = Node(dataset, parent, branch)
        if dataset.targets_are_the_same():
            node.set_label(dataset.targets_are_the_same())
            return node
        elif dataset.get_num_instances() == 0:
            node.set_label(parent.mode_of_target_feature())
            return node
        elif dataset.features_is_empty():
            node.set_label(dataset.mode_of_target_feature())
            return node
        else:
            best = dataset.get_feature_of_max_info_gain()
            node.set_label(best)
            datasets = dataset.partition_on_feature(best)
            for item in datasets:
                node.children.append(ID3.build(item['dataset'], node, item['branch']))
            return node

if __name__ == '__main__':
    try:
        #with open('datasets/Table4-3.arff', 'r') as training_file:
        with open('datasets/lakesDiscreteFold1.arff', 'r') as training_file:
            training_dataset = DataReader.parse_file_into_dataset(training_file)
        #with open('datasets/Table4-3.arff', 'r') as testing_file:
        with open('datasets/lakesDiscreteFold2.arff', 'r') as testing_file:
            testing_dataset = DataReader.parse_file_into_dataset(testing_file)
        #print(training_dataset.features)
        training_dataset.set_target_feature(-1)
        testing_dataset.set_target_feature(-1)
        decision_tree = ID3.train_on_dataset(training_dataset)
        id3 = ID3(training_dataset, decision_tree)
        num_correct = 0
        for instance in testing_dataset.instances:
            predicted_value = id3.predict_target_value_for_instance(instance, id3.tree)
            if predicted_value == instance[testing_dataset.target_feature['name']]:
                num_correct += 1
        accuracy = num_correct / len(testing_dataset.instances) * 100
        print("The id3 tree predicted the target values on the testing set with an accuracy of", accuracy,"%.")
    except EnvironmentError as e:
        print(e)
            