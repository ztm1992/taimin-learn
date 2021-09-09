import numpy as np
from collections import Counter


def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


class KNN:
    def __init__(self, k):
        self.k = k
    
    def fit(self, X, y):
        self.X = X
        self.y = np.array(y)

    def predict(self, x):
        dist_score = np.linalg.norm(x - self.X, axis=1)
        sort_index = np.argsort(dist_score)
        counter = Counter(self.y[sort_index][:self.k])
        label, _ = counter.most_common(1)[0]
        return label


if __name__ == "__main__":
    model = KNN(10)
    group, labels = createDataSet()
    print(type(group))
    print(labels)
    model.fit(group, labels)
    res = model.predict(np.array([0, 0]))
    print(res)