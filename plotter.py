import matplotlib.pyplot as plt
import re

def Plotter(min_value, max_value, function_string):
    e = None
    try:
        function_string = sanitize_string(function_string)
    except ValueError as e:
        return [], [], e
    x_axis = []
    y_axis = []
    for i in range(min_value, max_value+1):
        x_axis.append(i)
        y_axis.append(eval(function_string, {"x": i}))
    plt.plot(x_axis, y_axis)
    plt.show()
    return x_axis, y_axis, e

def sanitize_string(function_string):
    for expression in re.findall('[a-zA-Z_]+', function_string):
        if expression != 'x':
            raise ValueError(
                f"{expression} is not supported or is not a valid expression."
            )
    function_string = function_string.replace('^', '**')
    return function_string