import sys
from PySide2.QtWidgets import *
from plotter import Plotter
import matplotlib

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mathematical Function Plotter")
        self.button = QPushButton("Plot")
        self.button.clicked.connect(self.plot_function)
        self.setCentralWidget(self.button)
        self.function_input = QLineEdit()
        self.min_input = QLineEdit()
        self.max_input = QLineEdit()
        self.function_label = QLabel("Function")
        self.min_label = QLabel("Minimum Value")
        self.max_label = QLabel("Maximum Value")
        self.error_label = QLabel()
        self.plot_canvas = FigureCanvasQTAgg(Figure())
        layout = QVBoxLayout()
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.min_label)
        layout.addWidget(self.min_input)
        layout.addWidget(self.max_label)
        layout.addWidget(self.max_input)
        layout.addWidget(self.button)
        layout.addWidget(self.error_label)
        layout.addWidget(self.plot_canvas)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    def plot_function(self):
        if self.inputs_empty():
            self.error_label.setText("Inputs Cannot Be Empty")
            self.plot_canvas.figure.clear()
            return
        try:
            function_string = self.function_input.text()
            min_value = float(self.min_input.text())
            max_value = float(self.max_input.text())
            _, _, figure, err1 = Plotter(min_value, max_value, function_string)
            if err1 is not None:
                self.error_label.setText(str(err1))
                return
            self.plot_canvas.figure.clear()
            self.plot_canvas.figure = figure
            self.plot_canvas.draw()
            self.error_label.setText("")
        except Exception as e:
            self.error_label.setText(str(e))
            self.plot_canvas.figure.clear()
            return
    def inputs_empty(self):
        return self.function_input.text() == "" or self.min_input.text() == "" or self.max_input.text() == ""


def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
