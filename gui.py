# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui(QtWidgets.QMainWindow):
	''' The Vertical Layed GUI that holds all the widgets that the User will interact with '''

	app = QtWidgets.QApplication(sys.argv)  # Firstly, an Application is needed

	def __init__(self, width=800, height=600):
		''' Initializes the GUI and it's properties '''

		super().__init__()
		self.resize(width, height)

		self.widgets = QtWidgets

		self.centralwidget = self.widgets.QWidget(self)
		self.setCentralWidget(self.centralwidget)

		self.centralframe = self.widgets.QVBoxLayout()
		self.centralwidget.setLayout(self.centralframe)

	def place_frame(self, frame):
		''' 
		Places the provided frame on the central window.
		frame -> QBoxLayout 
		'''
		widget = QtWidgets.QWidget()
		widget.setLayout(frame)
		self.centralframe.addWidget(widget)

	def label(self, text):
		''' Creates a label and writes the provided text to it '''
		label = self.widgets.QLabel(self.centralwidget)
		label.setText(text)

		return label

	def button(self, connect_func):
		''' Creates and places a button, also connects it to a function(clicked)'''
		button = self.widgets.QPushButton(self.centralwidget)
		button.clicked.connect(connect_func)

		return button

	def run(self):
		self.show()
		sys.exit(self.app.exec_())


if __name__ == "__main__":
	ui = Ui()
	ui.run()