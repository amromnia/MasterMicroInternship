import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import re
import numpy as np

# Main function, invokes all other functions to compile the mathematical function then plots it and returns the x and y axis and the figure,
# if an error occurs it returns the error alongside empty x and y axis and an empty figure

# min_value: The minimum value of the x axis
# max_value: The maximum value of the x axis
# function_string: The mathematical function to plot
# max_gb: The maximum amount of gigabytes to use for the x and y axis
# returns: x_axis, y_axis, figure, e

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
        # The vectorize function is used to apply the compiled function to the x axis
        applied_function = np.vectorize(lambda x: eval(compiled_function, {'x': x, 'X': x, '__builtins__': {}}, {}), otypes=[np.float64])
        y_axis = applied_function(x_axis)
    except Exception as e:
        return [], [], Figure(), e
    figure = plt.figure()
    plt.plot(x_axis, y_axis)
    return x_axis, y_axis, figure, e

# Sanitizes the function string by removing spaces and checking for unsupported variables and operators using regex
def sanitize_string(function_string):
    function_string = function_string.replace(' ', '')
    for variable in re.findall('[a-zA-Z_]+', function_string):
        if variable != 'x' and variable != 'X':
            raise ValueError(
                f"{variable} is not supported or is not a valid variable (Only X functions are supported)."
            )
    for operator in re.findall('[^a-zA-Z0-9_]+', function_string):
        if operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '^' and operator != '(' and operator != ')' and operator != '.' and operator != '**' and operator != '//':
            raise ValueError(
                f"{operator} is not supported or is not a valid operator."
            )
    function_string = function_string.replace('^', '**')
    return function_string

# Compiles the function string into a python code object and checks for unsupported variables
def compile_function_string(function_string):
    compiled_function = compile(function_string, '<string>', 'eval')
    for name in compiled_function.co_names:
        if name != "x" and name != "X":
            raise ValueError(
                f"{name} is not supported or is not a valid variable (Only X functions are supported)."
            )
    return compiled_function
