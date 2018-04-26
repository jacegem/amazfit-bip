import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox, QGridLayout, QGroupBox, QDialog,
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy)


class FontCreator(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        # windowLayout = QVBoxLayout()
        # windowLayout.addWidget(self.horizontalGroupBox)

        self.setLayout(self.containerGrid)
        self.show()


    def createGridLayout(self):
        self.containerGrid = QGridLayout()

        noticeLayout = QGridLayout()
        noticeLayout.setColumnStretch(1, 4)
        noticeLayout.setColumnStretch(2, 4)

        noticeGroupBox = QGroupBox("Notice")
        noticeGroupBox.setLayout(noticeLayout)
        self.containerGrid.addWidget(noticeGroupBox, 0, 0)

        donate1 = QPushButton('$1')
        sizePolicy = QSizePolicy()
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        # sizePolicy.setHorizontalStretch(1)
        # sizePolicy.setWidthForHeight(True)
        donate1.setSizePolicy(sizePolicy)

        donate5 = QPushButton('$5')
        donate10 = QPushButton('$10')
        donateLayout = QGridLayout()
        donateLayout.addWidget(donate1, 0, 0)
        donateLayout.addWidget(donate5, 1, 0)
        donateLayout.addWidget(donate10, 2, 0)
        donateGroupBox = QGroupBox("Donate")
        donateGroupBox.setLayout(donateLayout)
        self.containerGrid.addWidget(donateGroupBox, 0, 1)

        createLayout = QGridLayout()
        createLayout.setColumnStretch(1, 4)
        createLayout.setColumnStretch(2, 4)
        createGroupBox = QGroupBox("Create")
        createGroupBox.setLayout(createLayout)
        self.containerGrid.addWidget(createGroupBox, 0, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    creator = FontCreator()
    sys.exit(app.exec_())
