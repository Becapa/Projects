from statistics import mode

class Node:
    def __init__(self, dataset, parent = None, branch = None):
        self.label = None
        self.children = []
        self.dataset = dataset
        self.parent = parent
        self.parent_branch = branch

    def mode_of_target_feature(self):
        target_feature_values = []
        for instance in self.dataset.instances:
            target_feature_values.append(instance[self.dataset.target_feature['name']])
        return mode(target_feature_values)

    def set_label(self, label):
        self.label = label

    def to_string(self, level = 0):
        branch = ''
        if self.parent:
            branch = self.parent_branch
        ret = '\t'*level + branch + ' - ' + self.label + '\n'
        if self.children:
            ret += '\t'*level
            for child in self.children:
                ret += child.to_string(level+1) + '\n'
        return ret
            
        
            
            

