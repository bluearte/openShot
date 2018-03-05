from PySide.QtGui import *
from PySide.QtCore import *

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        label = QLabel()
        label.setText("Episode")

        comboBox = QComboBox()
        comboBox.addItem("")

        hLayout = QHBoxLayout()
        hLayout.addWidget(label)
        hLayout.addWidget(comboBox)
        
        self.setLayout(hLayout)

panel = Panel()
panel.show()