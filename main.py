from gui import Ui
from tools import *

def create_ui():
	ui = Ui()
	name = ui.label('MoviewAll')

	name_frame = ui.widgets.QHBoxLayout()
	name_frame.addWidget(name)
	ui.place_frame(name_frame)

	ui.run()

if __name__ == '__main__':
	create_ui()