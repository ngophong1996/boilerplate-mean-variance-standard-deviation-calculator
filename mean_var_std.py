import numpy as np


def calculate(lst):

    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst).reshape(3, 3)

    # Calculate
    calculations = {
        'mean': [
            list(np.mean(arr, axis=0)),
            list(np.mean(arr, axis=1)),
            float(np.mean(arr))
        ],
        'variance': [
            list(np.var(arr, axis=0)),
            list(np.var(arr, axis=1)),
            float(np.var(arr))
        ],
        'standard deviation': [
            list(np.std(arr, axis=0)),
            list(np.std(arr, axis=1)),
            float(np.std(arr))
        ],
        'max': [
            list(np.max(arr, axis=0)),
            list(np.max(arr, axis=1)),
            int(np.max(arr))
        ],
        'min': [
            list(np.min(arr, axis=0)),
            list(np.min(arr, axis=1)),
            int(np.min(arr))
        ],
        'sum': [
            list(np.sum(arr, axis=0)),
            list(np.sum(arr, axis=1)),
            int(np.sum(arr))
        ]

    }

    return calculations
