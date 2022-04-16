from datareader import DataReader
from random import uniform

class GD:
    def __init__(self, dataset, rate):
        self.dataset = dataset
        self.alpha = rate
        self.weights = self.init_weights()
    
    def init_weights(self):
        return [uniform(-0.2, 0.2) for _ in range(len(self.dataset.features))]

    def predict(self, instance):
        predicted_value = self.weights[0]
        for i, (key, value) in enumerate(instance.items()):
            if i < len(instance)-1:
                predicted_value += self.weights[i+1] * float(value)
        return predicted_value

    def sq_error(self, target_value, predicted_value):
        return (float(target_value) - predicted_value) ** 2


    def train(self):
        instance = self.dataset.instances[0]
        print("target value:",instance[self.dataset.target_feature['name']], "predicted value:", self.predict(instance))
        error = self.sq_error(instance[self.dataset.target_feature['name']], self.predict(instance))
        return error


if __name__ == '__main__':
    try:
        with open('datasets/Table7-1 numeric only.arff', 'r') as training_file:
            training_dataset = DataReader.parse_file_into_dataset(training_file)
        training_dataset.set_target_feature(-1)
        rate = 0.002
        gd = GD(training_dataset, rate)
        sse = gd.train()
        print("Final sum of squared errors:", sse)
        print("Final weights:", gd.weights)


    except EnvironmentError as e:
        print(e)
            