import pytestqt
from GUI import *
from PySide2 import QtCore
from plotter import *

def test_gui(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)

def test_gui_correct_string(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)
    qtbot.keyClicks(window.function_input, "x**2")
    qtbot.keyClicks(window.min_input, "0")
    qtbot.keyClicks(window.max_input, "10")
    qtbot.wait(1000)
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.wait(1000)
    assert(window.error_label.text() == "")

def test_gui_unsupported_variable(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)
    qtbot.keyClicks(window.function_input, "x%2+2*y")
    qtbot.keyClicks(window.min_input, "0")
    qtbot.keyClicks(window.max_input, "10")
    qtbot.wait(1000)
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.wait(1000)
    assert window.error_label.text() == "y is not supported or is not a valid variable (Only X functions are supported)."

def test_gui_unsupported_operator(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)
    qtbot.keyClicks(window.function_input, "x**2+2%x")
    qtbot.keyClicks(window.min_input, "0")
    qtbot.keyClicks(window.max_input, "10")
    qtbot.wait(1000)
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.wait(1000)
    assert window.error_label.text() == "% is not supported or is not a valid operator."

def test_gui_min_value_greater_than_max_value(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait(1000)
    qtbot.keyClicks(window.function_input, "x**2")
    qtbot.keyClicks(window.min_input, "10")
    qtbot.keyClicks(window.max_input, "0")
    qtbot.wait(1000)
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.wait(1000)
    assert window.error_label.text() == "Min Value Must Be Smaller Than Max Value!"
