from dataset import DataSet

class DataReader:
    def parse_file_into_dataset(file):
        dataset = DataSet()
        at_data_section = False
        for line in file:
            if not line.strip():
                continue
            if(line.split()[0] == '@attribute'):
                dataset.add_feature(DataReader.get_feature(line))
            if(line.split()[0] == '@data'):
                at_data_section = True
                continue
            if(at_data_section == True):
                dataset.add_instance(DataReader.get_data_instance(dataset, line))
        return dataset

    def get_feature(line):
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

    def get_data_instance(dataset, line):
        data = line.split(',')
        instance = {}
        for count, item in enumerate(data):
            feature_name = dataset.features[count]['name']
            instance[feature_name] = item.strip('\n')
        return instance