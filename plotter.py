import matplotlib.pyplot as plt
import re
import numpy as np

def Plotter(min_value, max_value, function_string):
    e = None
    try:
        function_string = sanitize_string(function_string)
        compiled_function = compile_function_string(function_string)
    except ValueError as e:
        return [], [], e

    try:
        x_axis = np.arange(min_value, max_value+1, dtype=np.float64)
        applied_function = np.vectorize(lambda x: eval(compiled_function, {'x': x, 'X': x, '__builtins__': {}}, {}), otypes=[np.float64])
        y_axis = applied_function(x_axis)
    except Exception as e:
        return [], [], e
    plt.plot(x_axis, y_axis)
    plt.show()
    return x_axis, y_axis, e

def sanitize_string(function_string):
    for variable in re.findall('[a-zA-Z_]+', function_string):
        if variable != 'x' and variable != 'X':
            raise ValueError(
                f"{variable} is not supported or is not a valid variable (Only X functions are supported)."
            )
    function_string = function_string.replace('^', '**')
    return function_string

def compile_function_string(function_string):
    compiled_function = compile(function_string, '<string>', 'eval')
    for name in compiled_function.co_names:
        if name != "x" and name != "X":
            raise ValueError(
                f"{name} is not supported or is not a valid variable (Only X functions are supported)."
            )
    return compiled_function