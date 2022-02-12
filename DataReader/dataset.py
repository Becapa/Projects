import math

#example of dataset structures:
#self.features[0] = ['name' => 'runoff', 'value_type' => 'discrete', 'possible_values' => ['5', '10', '15', '20', '25', '30']]
#self.instances[0] = ['aluminum' => '76', 'calcium' => '0.187', ... , 'inlets' => 'zero', ...etc]

class DataSet:
    def __init__(self):
        self.features = []
        self.instances = []

    def add_feature(self, feature):
        self.features.append(feature)

    def add_instance(self, instance):
        self.instances.append(instance)

    def get_feature_min(self, feature_name):
        current_min = float(self.instances[0][feature_name])
        for instance in self.instances:
            if(float(instance[feature_name]) < current_min):
                current_min = float(instance[feature_name])
        return current_min

    def get_feature_max(self, feature_name):
        current_max = float(self.instances[0][feature_name])
        for instance in self.instances:
            if(float(instance[feature_name]) > current_max):
                current_max = float(instance[feature_name])
        return current_max

    def get_counts(self, target_feature):
        counts = []
        items = []
        feature_values = []
        for instance in self.instances:
            items.append(instance[target_feature].strip('\n'))
        for feature in self.features:
            if (feature['name'] == target_feature):
                feature_values = feature['possible_values']
        for value in feature_values:
            counts.append(items.count(value))
        return counts

    def get_counts_filtered_by(self, target_feature, feature_to_split_on, split_value):
        counts = []
        items = []
        feature_values = []
        for instance in self.instances:
            if(instance[feature_to_split_on] == split_value):
                items.append(instance[target_feature].strip('\n'))
        for feature in self.features:
            if (feature['name'] == target_feature):
                feature_values = feature['possible_values']
        for value in feature_values:
            counts.append(items.count(value))
        return counts

    def get_information_gain(self, target_feature, feature_to_split_on):
        total_instances = len(self.instances)
        my_entropy = self.get_entropy(self.get_counts(target_feature))
        sum_splits_weighted_entropy = 0
        split_values = []
        for feature in self.features:
            if(feature['name'] == feature_to_split_on):
                split_values = feature['possible_values']
        for value in split_values:
            counts = self.get_counts_filtered_by(target_feature, feature_to_split_on, value)
            total = sum(counts)
            sum_splits_weighted_entropy += self.get_entropy(counts) * total/total_instances
        return my_entropy - sum_splits_weighted_entropy
        
    def get_entropy(self, counts):
        denom = sum(counts)
        entropy = 0
        for num in counts:
            prob = num/denom
            if prob > 0:
                entropy -= prob * math.log(prob, 2)
        return entropy