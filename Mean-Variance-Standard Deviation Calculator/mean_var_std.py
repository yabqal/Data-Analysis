import numpy as np

def calculate(list):
    array = np.array(list)
    if len(array) < 9:
        raise ValueError("List must contain nine numbers.")
    array = np.reshape( array, (3, 3))

    calculations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    for key, func in calculations.items():
        calculations[key] = [
            func(array, axis=0).tolist(),
            func(array, axis=1).tolist(),
            func(array.flatten()).tolist()
        ]


    return calculations