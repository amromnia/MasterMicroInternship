from plotter import *
import numpy as np

def main():
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))
    function_string = input("Enter the function: ")
    x, y, e= Plotter(min_value, max_value, function_string)
    if e is not None:
        print(e)
        return
    print(x, y)

if __name__ == '__main__':
    main()