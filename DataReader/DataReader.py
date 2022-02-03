from asyncore import read
from arff import DataSet

class DataReader:
    def __init__(self) -> None:
        self.arff_data = DataSet()

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
        if('{' not in words[2]): 
            feature['value_type'] = words[2]
        elif('{' in words[2] and '}' in words[2]):
            feature['value_type'] = 'discrete'
            feature['possible_values'] = words[2].strip('{}').split(',')
        else:
            types = []
            words_length = len(words)
            for index in range(2, words_length):
                types.append(words[index])
                if(words[index] == '}'):
                    break
            feature['value_type'] = 'discrete'
            feature['possible_values'] = types
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
        elif(feature['value_type'] == 'discrete'):
            print("All possible values for", feature['name'], ": ", feature['possible_values'])
    target_feature = input("What is the target feature? ")
    split_feature = input("What is the feature to split on? ")
    print("The information gain for ph with a runoff split is:", reader.arff_data.information_gain(target_feature, split_feature))
            