# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui:
	''' The GUI that holds all the widgets that the User will interact with '''

	def __init__(self):
		''' Initializes the GUI and '''

		self.app = QtWidgets.QApplication(sys.argv)
		self.mw = QtWidgets.QMainWindow()
		self.mw.resize(800, 600)

		self.centralwidget = QtWidgets.QWidget(self.mw)
		self.mw.setCentralWidget(self.centralwidget)

		self.centralframe = QtWidgets.QVBoxLayout()

	def place_frame(self, frame):
		''' 
		Places the provided frame on the central window.
		frame -> QBoxLayout 
		'''
		widget = QtWidgets.QWidget()
		widget.setLayout(frame)
		self.centralframe.addWidget(widget)

	def run(self):
		self.mw.show()
		sys.exit(self.app.exec_())


if __name__ == "__main__":
	ui = Ui()
	ui.run()