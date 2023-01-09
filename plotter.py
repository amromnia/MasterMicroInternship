import matplotlib.pyplot as plt
import re
import numpy as np

def Plotter(min_value, max_value, function_string):
    e = None
    try:
        function_string = sanitize_string(function_string)
    except ValueError as e:
        return [], [], e

    try:
        x_axis = np.arange(min_value, max_value+1, dtype=np.float64)
        applied_function = np.vectorize(lambda x: eval(function_string, {"x": x}), otypes=[np.float64])
        y_axis = applied_function(x_axis)
    except Exception as e:
        return [], [], e
    plt.plot(x_axis, y_axis)
    plt.show()
    return x_axis, y_axis, e

def sanitize_string(function_string):
    for variable in re.findall('[a-zA-Z_]+', function_string):
        if variable != 'x':
            raise ValueError(
                f"{variable} is not supported or is not a valid variable (Only X functions are supported)."
            )
    function_string = function_string.replace('^', '**')
    return function_string