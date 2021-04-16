# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui:
	''' The Vertical Layed GUI that holds all the widgets that the User will interact with '''

	def __init__(self, width=800, height=600):
		''' Initializes the GUI and it's properties '''

		self.app = QtWidgets.QApplication(sys.argv)
		self.mw = QtWidgets.QMainWindow()
		self.mw.resize(width, height)

		self.widgets = QtWidgets

		self.centralwidget = self.widgets.QWidget(self.mw)
		self.mw.setCentralWidget(self.centralwidget)

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

	def button(self, connect_func):
		''' Creates and places a button, also connects it to a function(clicked)'''
		button = self.widgets.QPushButton(self.centralwidget)
		button.clicked.connect(connect_func)

		return button

	def run(self):
		self.mw.show()
		sys.exit(self.app.exec_())


if __name__ == "__main__":
	ui = Ui()
	ui.run()