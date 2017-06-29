import numpy as np


def function_1(seq, sub):
    return [i for i in range(len(seq) - len(sub)) if seq[i:i+len(sub)] == sub]


def function_2(seq, sub):
    target = np.dot(sub, sub)
    candidates = np.where(np.correlate(seq, sub, mode='valid') == target)[0]
    check = candidates[:, np.newaxis] + np.arange(len(sub))
    mask = np.all((np.take(seq, check) == sub), axis=-1)
    return candidates[mask]
