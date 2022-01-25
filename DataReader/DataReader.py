class ArffData:
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

class DataReader:
    def __init__(self) -> None:
        self.arff_data = ArffData()

    def parse_file(self, file):
        data = False
        for line in file:
            if not line.strip():
                continue
            if(line.split()[0] == '@attribute'):
                self.arff_data.add_feature(self.get_feature(line))
            if(line.split()[0] == '@data'):
                data = True
                continue
            if(data == True):
                self.arff_data.add_instance(self.get_data_instance(line))

    def get_feature(self, line):
        words = line.split()
        feature = {}
        feature['name'] = words[1]
        if('{' not in words[2] or ('{' in words[2] and '}' in words[2])):
            feature['value_type'] = words[2]
        else:
            types = ''
            words_length = len(words)
            for index in range(2, words_length):
                types += words[index]
                if(words[index] == '}'):
                    break
            feature['value_type'] = types
        return feature

    def get_data_instance(self, line):
        data = line.split(',')
        instance = {}
        for count, item in enumerate(data):
            feature_name = self.arff_data.features[count]['name']
            instance[feature_name] = item
        return instance


if __name__ == '__main__':
    reader = DataReader()
    try:
        with open(input("What is the path and name of the file? "), 'r') as file:
            reader.parse_file(file)
    except EnvironmentError as e:
        print(e)
    for feature in reader.arff_data.features:
        if(feature['value_type'] == 'numeric'):
            print(feature['name'], "min:", reader.arff_data.get_feature_min(feature['name']))
            print(feature['name'], "max:", reader.arff_data.get_feature_max(feature['name']))
    for feature in reader.arff_data.features:
        if(feature['value_type'] != 'numeric'):
            possible_values = feature['value_type'].strip('{}').split(',')
            print("All possible values for", feature['name'], ": ", possible_values)
            