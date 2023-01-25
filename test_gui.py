import pytestqt
from GUI import *
from PySide2 import QtCore
from plotter import *

def test_gui(qtbot):
    # Test that the GUI works correctly
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)

def test_gui_correct_string(qtbot):
    # Test that the GUI works correctly
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)
    #qt bot enter text into input
    qtbot.keyClicks(window.function_input, "x**2")
    qtbot.keyClicks(window.min_input, "0")
    qtbot.keyClicks(window.max_input, "10")
    qtbot.wait(1000)
    #qt bot click button
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.wait(1000)
    assert(window.error_label.text() == "")

def test_gui_unsupported_variable(qtbot):
    # Test that the GUI works correctly
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)
    #qt bot enter text into input
    qtbot.keyClicks(window.function_input, "x%2+2*y")
    qtbot.keyClicks(window.min_input, "0")
    qtbot.keyClicks(window.max_input, "10")
    qtbot.wait(1000)
    #qt bot click button
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.wait(1000)
    assert window.error_label.text() == "y is not supported or is not a valid variable (Only X functions are supported)."

def test_gui_unsupported_operator(qtbot):
    # Test that the GUI works correctly
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)
    #qt bot enter text into input
    qtbot.keyClicks(window.function_input, "x**2+2%x")
    qtbot.keyClicks(window.min_input, "0")
    qtbot.keyClicks(window.max_input, "10")
    qtbot.wait(1000)
    #qt bot click button
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.wait(1000)
    assert window.error_label.text() == "% is not supported or is not a valid operator."

def test_gui_min_value_greater_than_max_value(qtbot):
    # Test that the GUI works correctly
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)
    #qt bot enter text into input
    qtbot.keyClicks(window.function_input, "x**2")
    qtbot.keyClicks(window.min_input, "10")
    qtbot.keyClicks(window.max_input, "0")
    qtbot.wait(1000)
    #qt bot click button
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.wait(1000)
    assert window.error_label.text() == "Min Value Must Be Smaller Than Max Value!"
