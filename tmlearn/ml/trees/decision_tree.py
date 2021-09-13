from typing import Dict, List

import numpy as np


def calc_shannon_entropy(dataset: List[str]):
    labels = [vec[-1] for vec in dataset]
    num_entries = len(labels)
    label_count: Dict[str, int] = {}
    for label in labels:
        label_count[label] = label_count.get(label, 0) + 1
    shannon_entropy = 0.0
    for label in label_count:
        prob = label_count[label] / num_entries
        shannon_entropy -= prob * np.log2(prob)
    return shannon_entropy


def split_dataset(dataset, axis, value):
    res = []
    for feature_vec in dataset:
        if feature_vec[axis] == value:
            res.append(
                feature_vec[:axis] + feature_vec[axis+1:]
            )
    return res


def choose_best_feature(dataset):
    num_features = len(dataset[0]) - 1
    base_entropy = calc_shannon_entropy(dataset)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        current_entropy = 0.0
        feature_list = [vec[i] for vec in dataset]
        values = np.unique(feature_list)
        for value in values:
            subset = split_dataset(dataset, i, value)
            prob = len(subset) / len(dataset)
            current_entropy += prob * calc_shannon_entropy(subset)
        info_gain = base_entropy - current_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature




if __name__ == '__main__':
    dataset = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ]
    print(
        choose_best_feature(
            dataset
            )
    )