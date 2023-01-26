from plotter import *
import pytest
import numpy as np


def test_string_sanitization_correct_string():
    # Test that the string is sanitized correctly
    string = "x^2"
    assert sanitize_string(string) == "x**2"

def test_string_sanitization_unsupported_variable():
    # Test that unsupported variables raise an error
    string = "x^2+2*y"
    with pytest.raises(ValueError):
        sanitize_string(string)

def test_string_sanitization_unsupported_operator():
    # Test that unsupported operators raise an error
    string = "x^2+2%y"
    with pytest.raises(ValueError):
        sanitize_string(string)

def test_string_compilation_correct_string():
    # Test that the string is compiled correctly
    string = "x**2"
    assert compile_function_string(string) == compile(string, '<string>', 'eval')

def test_string_compilation_unsupported_variable():
    # Test that unsupported variables raise an error in the compilation
    string = "x**2+2*y"
    with pytest.raises(ValueError):
        compile_function_string(string)

def test_plotter_correct_string():
    # Test that the plotter works correctly
    min_value = 0
    max_value = 10
    function_string = "x**2"
    x_axis, y_axis, figure, e = Plotter(min_value, max_value, function_string)
    assert e == None

def test_plotter_unsupported_variable():
    # Test that unsupported variables raise an error in the main Plotter function
    min_value = 0
    max_value = 10
    function_string = "x**2+2*y"
    x_axis, y_axis, figure, e = Plotter(min_value, max_value, function_string)
    assert e != None

def test_plotter_unsupported_operator():
    # Test that unsupported operators raise an error in the main Plotter function
    min_value = 0
    max_value = 10
    function_string = "x**2+2%y"
    x_axis, y_axis, figure, e = Plotter(min_value, max_value, function_string)
    assert e != None

def test_plotter_min_value_greater_than_max_value():
    # Test that min value greater than max value raises an error in the main Plotter function
    min_value = 10
    max_value = 0
    function_string = "x**2"
    x_axis, y_axis, figure, e = Plotter(min_value, max_value, function_string)
    assert e != None

def test_plotter_max_value_too_big():
    # Test that max value too big raises an error in the main Plotter function
    min_value = 0
    max_value = 10
    function_string = "x**2"
    x_axis, y_axis, figure, e = Plotter(min_value, max_value, function_string, max_gb=0)
    assert e != None

def test_plotter_correct_output_x_axis():
    # Test that the plotter outputs the correct X-axis values
    min_value = 0
    max_value = 10
    function_string = "x**2"
    x_axis, y_axis, figure, e = Plotter(min_value, max_value, function_string)
    np.testing.assert_array_equal(x_axis, np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def test_plotter_correct_output_y_axis():
    # Test that the plotter outputs the correct Y-axis values
    min_value = 0
    max_value = 10
    function_string = "x**2"
    x_axis, y_axis, figure, e = Plotter(min_value, max_value, function_string)
    np.testing.assert_array_equal(y_axis, np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))