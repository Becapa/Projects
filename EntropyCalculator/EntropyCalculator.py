import math

def entropy(counts):
    denom = sum(counts)
    entropy = 0
    for num in counts:
        prob = num/denom
        if prob > 0:
            entropy -= prob * math.log(prob, 2)
    return entropy

if __name__ == '__main__':
    counts = []
    while(True):
        count = input('Enter a count for an event: ')
        if count == '':
            break
        counts.append(int(count))
    ent = entropy(counts)
    print("The entropy for this set of counts is:", ent)