from statistics import mode
import math

#example of dataset structures:
#self.features[0] = {'name':'runoff', 'value_type':'discrete', 'possible_values':['5', '10', '15', '20', '25', '30']}
#self.instances[0] = {'aluminum':'76', 'calcium':'0.187', ... , 'inlets':'zero', ...etc}

class DataSet:
    def __init__(self):
        self.features = []
        self.target_feature = {}
        self.instances = []

    def add_feature(self, feature):
        self.features.append(feature)

    def remove_feature(self, feature):
        for i in range(len(self.features)):
            if self.features[i]['name'] == feature:
                del self.features[i]
                break

    def add_instance(self, instance):
        self.instances.append(instance)

    def get_feature_from_features(self, feature_name):
        for feature in self.features:
            if feature['name'] == feature_name:
                return feature

    def set_target_feature(self, index):
        self.target_feature = self.features[index]

    def get_feature_min(self, feature_name):
        current_min = float(self.instances[0][feature_name])
        for instance in self.instances:
            if float(instance[feature_name]) < current_min:
                current_min = float(instance[feature_name])
        return current_min

    def get_feature_max(self, feature_name):
        current_max = float(self.instances[0][feature_name])
        for instance in self.instances:
            if float(instance[feature_name]) > current_max:
                current_max = float(instance[feature_name])
        return current_max

    def get_counts(self):
        counts = []
        target_values = []
        for instance in self.instances:
            target_values.append(instance[self.target_feature['name']])
        feature_values = self.target_feature['possible_values']
        for value in feature_values:
            counts.append(target_values.count(value))
        return counts

    def get_counts_filtered_by(self, feature_to_split_on, split_value):
        counts = []
        target_values = []
        for instance in self.instances:
            if instance[feature_to_split_on] == split_value:
                target_values.append(instance[self.target_feature['name']])
        feature_values = self.target_feature['possible_values']
        for value in feature_values:
            counts.append(target_values.count(value))
        return counts

    def targets_are_the_same(self):
        first_target_value = None
        if len(self.instances) > 0:
            first_target_value = self.instances[0][self.target_feature['name']]
            for instance in self.instances:
                if first_target_value != instance[self.target_feature['name']]:
                    return None
        return first_target_value

    def features_is_empty(self):
        if not self.features:
            return True
        else:
            return False

    def get_num_instances(self):
        num = len(self.instances)
        return num
    
    def mode_of_target_feature(self):
        feature_values = []
        for instance in self.instances:
            feature_values.append(instance[self.target_feature['name']])
        return mode(feature_values)

    def get_feature_of_max_info_gain(self):
        ig = 0
        feature_name = ''
        for feature in self.features:
            if feature['value_type'] != 'numeric' and feature['name'] != self.target_feature['name']:
                feature_ig = self.get_information_gain(feature['name'])
                if feature_ig > ig:
                    ig = feature_ig
                    feature_name = feature['name']
        return feature_name

    def get_information_gain(self, feature_to_split_on):
        total_instances = len(self.instances)
        my_entropy = self.get_entropy(self.get_counts())
        sum_splits_weighted_entropy = 0
        split_values = []
        for feature in self.features:
            if feature['name'] == feature_to_split_on:
                split_values = feature['possible_values']
        for value in split_values:
            counts = self.get_counts_filtered_by(feature_to_split_on, value)
            total = sum(counts)
            sum_splits_weighted_entropy += self.get_entropy(counts) * total/total_instances
        information_gain = my_entropy - sum_splits_weighted_entropy
        return information_gain
        
    def get_entropy(self, counts):
        denom = sum(counts)
        entropy = 0
        for num in counts:
            if denom != 0:
                prob = num/denom
                if prob > 0:
                    entropy -= prob * math.log(prob, 2)
        return entropy

    def partition_on_feature(self, feature_name):
        feature = self.get_feature_from_features(feature_name)
        values = feature['possible_values']
        datasets = []
        for value in values:
            dataset = DataSet()
            for instance in self.instances:
                if instance[feature_name] == value:
                    dataset.add_instance(instance)
            for feature in self.features:
                dataset.add_feature(feature)
            dataset.set_target_feature(-1)
            dataset.remove_feature(feature_name)
            datasets.append({'branch': value, 'dataset': dataset})
        return datasets