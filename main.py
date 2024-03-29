# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from tools import *
import sys


class Ui(QtWidgets.QMainWindow):
	''' The Vertical Layed GUI that holds all the widgets that the User will interact with '''

	app = QtWidgets.QApplication(sys.argv)  # Firstly, an Application is needed

	def __init__(self, width=800, height=150, *args, **kwargs):
		''' Initializes the GUI and it's properties '''

		super().__init__()
		# self.policy = QtWidgets.QSizePolicy.Ignored
		self.resize(width, height)
		submit_key = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter), self)
		submit_key.activated.connect(self.submit)

		self.cw = QtWidgets.QWidget(self)
		self.setCentralWidget(self.cw)
		self.setWindowTitle("MovieAll")

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

		self.name = QtWidgets.QLabel(self.cw)
		self.name.setFont(QtGui.QFont('Arial', 20))
		self.name.setAlignment(QtCore.Qt.AlignCenter)
		self.name.setText('<font color=blue>MoviewAll</font>')
		self.centralframe.addWidget(self.name)

		input_frame = QtWidgets.QHBoxLayout()
		self.label = QtWidgets.QLabel(self.cw)
		self.entry = QtWidgets.QLineEdit(self.cw)
		self.combo = QtWidgets.QComboBox(self.cw)
		self.submitb = QtWidgets.QPushButton(self.cw)
		self.submitb.clicked.connect(self.submit)
		self.submitb.setText('Submit')
		self.submitb.setMaximumWidth(200)

		# Placing the widgets
		input_frame.addWidget(self.label)
		input_frame.addWidget(self.entry)
		input_frame.addWidget(self.combo)
		self.place_frame(input_frame)
		self.centralframe.addWidget(self.submitb, alignment=QtCore.Qt.AlignCenter)
		self.name.adjustSize()

		self.combo.addItems(criterias.keys())

	def search(self, keyword, *args, **kwargs):
		''' Gets invoked when the search button gets clicked '''
		query = self.entry.text()
		self.entry.clear()
		# movie_links = search_movies(here_goes_criteria_from_checkbox, query)

	def submit(self, *args, **kwargs):
		''' Gets activated when the user searches for a movie, saving what was found to the database '''
		
		search = self.entry.text()
		if search:
			combo_crit = self.combo.currentText()
			links = search_movies(criterias[combo_crit], search)

			data_found = []
			for link in links:
				# title, rating, summary, year
				info_dict = get_movie_info(link=link)
				data_found.append(info_dict)
			print(data_found)
		
	def run(self, *args, **kwargs):
		self.create_widgets()
		self.show()
		sys.exit(self.app.exec_())


if __name__ == "__main__":
	ui = Ui()
	ui.run()