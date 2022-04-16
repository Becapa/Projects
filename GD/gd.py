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

    def error_delta(self, expected, predicted, feature_name):
        error_delta = 0
        for instance in self.dataset.instances:
            if feature_name is not None:
                error_delta += (float(expected) - predicted) * float(instance[feature_name])
            else:
                error_delta += float(expected) - predicted
        return error_delta

    def train(self):
        print(self.weights)
        count_same_sum = 0
        last_sum_sq = 0
        while count_same_sum != 100:
            sum_squared_errors = 0
            error_deltas = [0 for _ in range(len(self.dataset.features))]
            for instance in self.dataset.instances:
                expected = instance[self.dataset.target_feature['name']]
                predicted = self.predict(instance)
                error = float(expected) - predicted
                sq_error = error ** 2
                sum_squared_errors += sq_error
                error_deltas[0] = self.error_delta(expected, predicted, None)
                for i, feature in enumerate(self.dataset.features):
                    if i < len(instance)-1:
                        error_deltas[i+1] = self.error_delta(expected, predicted, feature['name'])
            sum_squared_errors/=2
            print(sum_squared_errors)
            for i in range(len(self.weights)):
                self.weights[i] = self.weights[i] + (self.alpha * error_deltas[i])
            if last_sum_sq == sum_squared_errors:
                count_same_sum += 1
            else:
                count_same_sum = 0
            last_sum_sq = sum_squared_errors
        return sum_squared_errors

if __name__ == '__main__':
    try:
        with open('datasets/Table7-1 numeric only.arff', 'r') as training_file:
            training_dataset = DataReader.parse_file_into_dataset(training_file)
        training_dataset.set_target_feature(-1)
        rate = 0.00000002
        gd = GD(training_dataset, rate)
        sse = gd.train()
        print("Final sum of squared errors:", sse)
        print("Final weights:", gd.weights)

    except EnvironmentError as e:
        print(e)
            