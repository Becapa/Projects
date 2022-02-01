import math

def entropy(probabilities):
    entropy = 0
    for prob in probabilities:
        prob = float(prob)
        if prob > 0:
            entropy -= prob * math.log(prob, 2)
    return entropy

if __name__ == '__main__':
    probabilites = []
    while(True):
        prob = input('Enter a probability for an event: ')
        if prob == '':
            break
        num, denom = prob.split('/')
        new_prob = float(num) / float(denom)
        probabilites.append(new_prob)
    ent = entropy(probabilites)
    print(ent)