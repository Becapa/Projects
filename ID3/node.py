class Node:
    def __init__(self, dataset, parent):
        self.label = ''
        self.children = []
        self.dataset = dataset
        self.parent = parent

    def mode_of_target_feature(self):
        #TODO: Implement
        return 0