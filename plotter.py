import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import re
import numpy as np

def Plotter(min_value, max_value, function_string, max_gb=1):
    e = None
    max_gb_val = max_gb*1e9
    if min_value>=max_value:
        e = "Min Value Must Be Smaller Than Max Value!"
        return [], [], Figure(), ValueError(e)
    if (max_value-min_value+1)*np.dtype(np.float64).itemsize>max_gb_val:
        e = f"Max Value Too Big, Needs more than {max_gb} gigabytes to store!"
        return [], [], Figure(), ValueError(e)
    try:
        function_string = sanitize_string(function_string)
        compiled_function = compile_function_string(function_string)
    except ValueError as e:
        return [], [], Figure(), e

    try:
        x_axis = np.arange(min_value, max_value+1, dtype=np.float64)
        applied_function = np.vectorize(lambda x: eval(compiled_function, {'x': x, 'X': x, '__builtins__': {}}, {}), otypes=[np.float64])
        y_axis = applied_function(x_axis)
    except Exception as e:
        return [], [], Figure(), e
    figure = plt.figure()
    plt.plot(x_axis, y_axis)
    return x_axis, y_axis, figure, e

def sanitize_string(function_string):
    function_string = function_string.replace(' ', '')
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
