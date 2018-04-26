class FontCreator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        gridLayout = self.createGridLayout()

        self.setLayout(gridLayout)
        self.show()

    def createGridLayout(self):
        self.containerGrid = QGridLayout()

        noticeLayout = QGridLayout()
        noticeLayout.setColumnStretch(1, 4)
        noticeLayout.setColumnStretch(2, 4)
        noticeGroupBox = QGroupBox("Grid").setLayout(noticeLayout)
        self.containerGrid.addWidget(noticeGroupBox, 0, 0)

        donate1 = QPushButton()
        donate5 = QPushButton()
        donate10 = QPushButton()
        donateLayout = QGridLayout()
        doanteLayout.addWidget(donate1, 0, 0)
        doanteLayout.addWidget(donate5, 1, 0)
        doanteLayout.addWidget(donate10, 2, 0)
        donateGroupBox = QGroupBox("Grid").setLayout(donateLayout)
        self.containerGrid.addWidget(donateGroupBox, 0, 1)

        createLayout = QGridLayout()
        createLayout.setColumnStretch(1, 4)
        createLayout.setColumnStretch(2, 4)
        createGroupBox = QGroupBox("Grid").setLayout(createLayout)
        self.containerGrid.addWidget(createGroupBox, 0, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
