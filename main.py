# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from tools import *
import sys


class Ui(QtWidgets.QMainWindow):
	''' The Vertical Layed GUI that holds all the widgets that the User will interact with '''

	app = QtWidgets.QApplication(sys.argv)  # Firstly, an Application is needed

	def __init__(self, width=800, height=600, *args, **kwargs):
		''' Initializes the GUI and it's properties '''

		super().__init__()
		# self.policy = QtWidgets.QSizePolicy.Ignored
		self.resize(width, height)

		self.cw = QtWidgets.QWidget(self)
		self.setCentralWidget(self.cw)
		self.setWindowTitle("MoviewAll")

		self.centralframe = QtWidgets.QVBoxLayout()
		self.cw.setLayout(self.centralframe)
		self.widgets = dict()  # For the widgets in each frame

	def place_frame(self, frame, *args, **kwargs):
		''' 
		Places the provided frame on the central window.
		frame -> QBoxLayout 
		'''
		widget = QtWidgets.QWidget()
		widget.setLayout(frame)
		self.centralframe.addWidget(widget)

	def create_widgets(self, *args, **kwargs):
		''' Creates all the widgets needed fot our app '''

		self.widgets['name'] = QtWidgets.QLabel(self.cw)
		self.widgets['name'].setFont(QtGui.QFont('Arial', 20))
		self.widgets['name'].setAlignment(QtCore.Qt.AlignCenter)
		self.widgets['name'].setText('<font color=blue>MoviewAll</font>')
		self.centralframe.addWidget(self.widgets['name'])

		input_frame = QtWidgets.QHBoxLayout()
		self.widgets['label'] = QtWidgets.QLabel(self.cw)
		self.widgets['entry'] = QtWidgets.QLineEdit(self.cw)
		self.widgets['combo'] = QtWidgets.QComboBox(self.cw)
		self.widgets['entry'].setAlignment(QtCore.Qt.AlignCenter)

		# Placing the widgets
		for w in list(self.widgets.values())[1:]:  # Skipping 'name' as we have already placed it
			input_frame.addWidget(w)
		self.place_frame(input_frame)
		self.widgets['name'].adjustSize()

		self.widgets['list'] = QtWidgets.QListWidget(self.cw)
		self.centralframe.addWidget(self.widgets['list'])

		self.widgets['combo'].addItems(criterias.keys())

	def search(self, keyword, *args, **kwargs):
		''' Gets invoked when the search button gets clicked '''
		query = self.widgets['entry'].text()
		self.widgets['entry'].clear()
		# movie_links = search_movies(here_goes_criteria_from_checkbox, query)

	def run(self, *args, **kwargs):
		self.create_widgets()
		self.show()
		sys.exit(self.app.exec_())


if __name__ == "__main__":
	ui = Ui()
	ui.run()