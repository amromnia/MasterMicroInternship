from plotter import *
import numpy as np

def main():
    try:
        min_value = float(input("Enter the minimum value: "))
        max_value = float(input("Enter the maximum value: "))
        function_string = input("Enter the function: ")
    except ValueError:
        print("Invalid Input, Input Valid Number or Function")
        return
    if min_value>max_value:
        print("Min Value Must Be Smaller Than Max Value!")
        return
    if max_value*np.dtype(np.float64).itemsize>2e9:
        print("Max Value Too Big, Needs more than 2 gigabytes!")
        return
    x, y, e= Plotter(min_value, max_value, function_string)
    if e is not None:
        print(e)
        return
    print(x, y)

if __name__ == '__main__':
    main()