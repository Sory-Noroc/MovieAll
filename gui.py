# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui:

	def __init__(self):

		self.app = QtWidgets.QApplication(sys.argv)
		self.mw = QtWidgets.QMainWindow()

		self.mw.setObjectName("mw")
		self.mw.resize(800, 600)

		self.centralwidget = QtWidgets.QWidget(self.mw)
		self.centralwidget.setObjectName("centralwidget")
		self.mw.setCentralWidget(self.centralwidget)

		self.menubar = QtWidgets.QMenuBar(self.mw)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")

		self.mw.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(self.mw)
		self.statusbar.setObjectName("statusbar")
		self.mw.setStatusBar(self.statusbar)

	def run(self):
		self.mw.show()
		sys.exit(self.app.exec_())


if __name__ == "__main__":
	ui = Ui()
	ui.run()