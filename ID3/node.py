from statistics import mode

class Node:
    def __init__(self, dataset, parent = None):
        self.label = None
        self.children = []
        self.dataset = dataset
        self.parent = parent
        self.mode = self.mode_of_target_feature()

    def mode_of_target_feature(self):
        target_feature_values = []
        for instance in self.dataset.instances:
            target_feature_values.append(list(instance.values())[-1])
        return mode(target_feature_values)

    def set_label(self, label):
        self.label = label

    def build(self):
        if(self.dataset.targets_are_the_same()):
            node = Node(self.dataset, self.parent)
            node.set_label(self.dataset.targets_are_the_same())
            return Node
        elif(self.dataset.get_num_instances() == 0):
            node = Node(self.dataset, self.parent)
            node.set_label(self.parent.mode_of_target_feature)
            return node
        elif(self.dataset.features_is_empty()):
            node = Node(self.dataset, self.parent)
            node.set_label(self.dataset.get_mode_for_target_feature())
            return node
        else:
            best = self.dataset.get_feature_of_max_info_gain()
            node = Node(self.dataset)
            node.set_label(best)
            datasets = self.dataset.partition_on_feature(best)
            for dataset in datasets:
                self.children.append(Node(dataset, node))
            return node



