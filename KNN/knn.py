import math
from datareader import DataReader

class KNN:
    def __init__(self, dataset):
        self.dataset = dataset

    def predict_target_value_for_instance(self, instance, k):
        distance_pairs = {}
        for training_instance in self.dataset.instances:
            distances = []
            for feature in self.dataset.features:
                if feature['value_type'] == 'discrete':
                    if instance[feature['name']] != training_instance[feature['name']]:
                        distances.append(1)
                elif feature['value_type'] == 'numeric':
                    #print(training_instance[feature['name']]," - ",instance[feature['name']])
                    distances.append((float(training_instance[feature['name']]) - float(instance[feature['name']])) ** 2)
            sum = 0
            for distance in distances:
                sum += distance
            euclidean_distance = math.sqrt(sum)
            distance_pairs[euclidean_distance] = training_instance[self.dataset.target_feature['name']]
        distance_pairs = sorted(distance_pairs)
        for i in distance_pairs.items():
            print(i)

if __name__ == '__main__':
    try:
        with open('datasets/lakesFold1.arff', 'r') as training_file:
            training_dataset = DataReader.parse_file_into_dataset(training_file)
        with open('datasets/lakesFold2.arff', 'r') as testing_file:
            testing_dataset = DataReader.parse_file_into_dataset(testing_file)
        training_dataset.set_target_feature(-1)
        testing_dataset.set_target_feature(-1)
        k = 1
        knn = KNN(training_dataset)
        num_correct = 0
        for instance in testing_dataset.instances:
            predicted_value = knn.predict_target_value_for_instance(instance, k)
            if predicted_value == instance[testing_dataset.target_feature['name']]:
                num_correct += 1
        accuracy = num_correct / len(testing_dataset.instances) * 100
        print("The k nearest neighbor algorithm with k =", k, "predicted the target values on the testing set with an accuracy of", accuracy, "%.")
    except EnvironmentError as e:
        print(e)
            