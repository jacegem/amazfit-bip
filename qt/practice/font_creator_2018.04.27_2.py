import sys

from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QGridLayout, QGroupBox, QWidget, QFileDialog, QLabel, QLineEdit, QMessageBox, QSpinBox, QPushButton)

from qt.button import Button


class FontCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 300
        self.initUI()
        self.center()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumWidth(self.width)
        self.setMinimumHeight(self.height)

        self.setLayout(self.createGridLayout())

        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    # Open an image file.
    def open_file(self):
        # Select the file dialog design.
        dialog_style = QFileDialog.DontUseNativeDialog
        dialog_style |= QFileDialog.DontUseCustomDirectoryIcons

        self.file_chosen = QFileDialog.getExistingDirectory(self, 'Open working directory', '.', QFileDialog.ShowDirsOnly)
        # Open the file dialog to select an image file.
        # self.file_chosen, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
        #                                                   "TTF (*.ttf)",
        #                                                   options=dialog_style)

        # Show the path of the file chosen.
        if self.file_chosen:
            self.lbl.setText(self.file_chosen)
            # Change the text on the label to display the file path chosen.
        else:
            self.lbl.setText("No file was selected. Please select an image.")
            # Change the text on the label to say that "No file was selected. Please select an image."
            # This 'else' statement is used to catch the case where the user presses 'Cancel' after opening the file dialog,
            # which will close the file dialog without choosing any file, even if they had already previously chosen a file
            # from previously opening the file dialog.

    def textchanged(self, text):
        print("contents of text box: " + text)
        try:
            number = int(text)
        except Exception:
            QMessageBox.about(self, 'Error', 'Input can only be a number')
            pass

    def createGridLayout(self):
        containerGrid = QGridLayout()

        noticeLayout = QGridLayout()
        noticeLayout.setColumnStretch(1, 4)
        noticeLayout.setColumnStretch(2, 4)

        noticeGroupBox = QGroupBox("Notice")
        noticeGroupBox.setLayout(noticeLayout)
        containerGrid.addWidget(noticeGroupBox, 0, 0)

        donate1 = Button('$1')
        donate1.setToolTip('donate $1')
        donate1.clicked.connect(self.open_file)

        donate5 = Button('$5')
        donate10 = Button('$10')
        donateLayout = QGridLayout()
        donateLayout.addWidget(donate1, 0, 0)
        donateLayout.addWidget(donate5, 1, 0)
        donateLayout.addWidget(donate10, 2, 0)
        donateGroupBox = QGroupBox("Donate")
        donateGroupBox.setLayout(donateLayout)
        containerGrid.addWidget(donateGroupBox, 0, 1)

        createGroupBox = QGroupBox("Create")
        createLayout = QGridLayout()
        # Create a label which displays the path to our chosen file

        self.lbl = QLineEdit('No file selected')
        self.lbl.setDisabled(True)
        createLayout.addWidget(self.lbl, 1, 0, 1, 3)

        btn_select_ttf = QPushButton('Select TTF file')
        btn_select_ttf.clicked.connect(self.open_file)
        createLayout.addWidget(btn_select_ttf, 1, 3, 1, 2)

        createLayout.addWidget(QLabel('Margin-Top:'), 2, 0)
        sb_margin_top = QSpinBox()
        sb_margin_top.setMinimum(-99)
        createLayout.addWidget(sb_margin_top, 2, 1)

        createLayout.addWidget(QLabel('Margin-Left:'), 2, 3)
        sb_margin_left = QSpinBox()
        sb_margin_left.setMinimum(-99)
        createLayout.addWidget(sb_margin_left, 2, 4)

        self.lb_directory = QLineEdit('No Directory selected')
        self.lb_directory.setDisabled(True)
        createLayout.addWidget(self.lb_directory, 3, 0, 1, 3)

        btn_select_folder = QPushButton('Select ft Directory')
        btn_select_folder.clicked.connect(self.select_folder)
        createLayout.addWidget(btn_select_folder, 1, 3, 1, 2)

        btn_create = Button('Font File Create')
        btn_create.clicked.connect(self.font_create)
        createLayout.addWidget(btn_create, 3, 0, 1, 5)

        createGroupBox.setLayout(createLayout)
        containerGrid.addWidget(createGroupBox, 0, 2)

        return containerGrid

    def select_file(self):
        pass
    
    def select_folder(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    creator = FontCreator()
    sys.exit(app.exec_())
