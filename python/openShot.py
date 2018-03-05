from Qt import QtGui
from Qt import QtCore
from Qt import QtWidgets

import openShot_version

__version__ = openShot_version.nuke_openShot_version()

class Panel(QtWidgets.QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        label = QtWidgets.QLabel()
        label.setText("Episode")

        comboBox = QtWidgets.QComboBox()
        comboBox.addItem("")

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(label)
        hLayout.addWidget(comboBox)
        
        self.setLayout(hLayout)

def main():
    main.panel = Panel()
    main.panel.show()