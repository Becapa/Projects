from datareader import DataReader

class NB:
    def __init__(self, dataset):
        self.dataset = dataset
        self.counts = self.build_counts()

    def build_counts(self):
        counts = {}
        for target_value in self.dataset.target_feature['possible_values']:
            counts[target_value] = {}
            for descriptive_feature in self.dataset.features:
                if descriptive_feature['name'] == self.dataset.target_feature['name']:
                    continue
                counts[target_value][descriptive_feature['name']] = []
                for instance in self.dataset.instances:
                    if instance[self.dataset.target_feature['name']] == target_value:
                        counts[target_value][descriptive_feature['name']].append(instance[descriptive_feature['name']])
        return counts

    def get_feature_count_given_target(self, feature, feature_value, target_feature_value):
        count = 0
        for item in self.counts[target_feature_value][feature]:
            if item == feature_value:
                count += 1
        return count

    def predict_target_value_for_instance(self, instance):
        total_count = len(self.dataset.instances)
        highest_prob = 0.0
        best_target_value = None
        for target_feature in self.counts:
            target_feature_count = 0
            feature_count = 0
            for descriptive_feature in self.counts[target_feature]:
                target_feature_count = len(self.counts[target_feature][descriptive_feature])
            prob = target_feature_count / total_count
            for feature_name in instance:
                if feature_name == self.dataset.target_feature['name']:
                    continue
                feature_count = self.get_feature_count_given_target(feature_name, instance[feature_name], target_feature)
                feature = self.dataset.get_feature_from_features(feature_name)
                prob = prob * (feature_count + 1) / (target_feature_count + (1 * len(feature['possible_values'])))
            if prob > highest_prob:
                highest_prob = prob
                best_target_value = target_feature
        return best_target_value            

if __name__ == '__main__':
    try:
        with open('datasets/lakesDiscreteFold1.arff', 'r') as training_file:
            training_dataset = DataReader.parse_file_into_dataset(training_file)
        with open('datasets/lakesDiscreteFold2.arff', 'r') as testing_file:
            testing_dataset = DataReader.parse_file_into_dataset(testing_file)
        training_dataset.set_target_feature(-1)
        testing_dataset.set_target_feature(-1)
        nb = NB(training_dataset)
        num_correct = 0
        for instance in testing_dataset.instances:
            predicted_value = nb.predict_target_value_for_instance(instance)
            if predicted_value == instance[testing_dataset.target_feature['name']]:
                num_correct += 1
        accuracy = num_correct / len(testing_dataset.instances) * 100
        print("The naive bayes algorithm predicted the target values on the testing set with an accuracy of", accuracy,"%.")
    except EnvironmentError as e:
        print(e)
            