import sys
import os

from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QGridLayout, QGroupBox, QWidget, QFileDialog, QLabel, QLineEdit, QMessageBox, QSpinBox,
                             QPushButton, QStyleFactory, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon

from qt.button import DonateButton, FullButton
from qt.ttf2bmp import *


class FontCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Amazfit Bip - Font Creator (v0.0.1)'
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

        self.setLayout(self.get_layout())
        icon = QIcon(resource_path('assets/font.png'))
        self.setWindowIcon(icon)
        self.show()

    # Open an image file.
    def open_file(self, ):
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
            self.lb_ttf_file.setText(self.file_chosen)
            # Change the text on the label to display the file path chosen.
        else:
            self.lb_ttf_file.setText("No file was selected. Please select an image.")
            # Change the text on the label to say that "No file was selected. Please select an image."
            # This 'else' statement is used to catch the case where the user presses 'Cancel' after opening the file dialog,
            # which will close the file dialog without choosing any file, even if they had already previously chosen a file
            # from previously opening the file dialog.

    def get_notice_box(self):
        notice_box = QVBoxLayout()
        notice_group = QGroupBox("Notice")
        notice_box.addWidget(notice_group)
        return notice_box

    def get_donate_box(self):
        donate_box = QVBoxLayout()
        donate_group = QGroupBox("Donate")
        donate_layout = QVBoxLayout()
        donate_layout.addWidget(DonateButton(1))
        donate_layout.addWidget(DonateButton(5))
        donate_layout.addWidget(DonateButton(10))
        donate_group.setLayout(donate_layout)
        donate_box.addWidget(donate_group)
        return donate_box

    def get_create_box(self):
        create_box = QVBoxLayout()
        create_group = QGroupBox('Create')
        create_layout = QVBoxLayout()

        layout_ttf = QHBoxLayout()

        lbl_ttf = QLineEdit('No file selected')
        lbl_ttf.setDisabled(True)
        lbl_ttf.setMinimumWidth(300)
        layout_ttf.addWidget(lbl_ttf)

        btn_ttf = QPushButton('Select TTF file')
        btn_ttf.clicked.connect(lambda: self.select_file(lbl_ttf))
        layout_ttf.addWidget(btn_ttf)

        create_layout.addLayout(layout_ttf)
        create_group.setLayout(create_layout)
        create_box.addWidget(create_group)
        return create_box

    def get_layout(self):
        whole_box = QHBoxLayout()

        whole_box.addLayout(self.get_notice_box())
        whole_box.addLayout(self.get_donate_box())
        whole_box.addLayout(self.get_create_box())

        return whole_box

    def createGridLayout(self):
        containerGrid = QGridLayout()

        noticeLayout = QGridLayout()
        noticeGroupBox = QGroupBox("Notice")
        noticeGroupBox.setLayout(noticeLayout)
        containerGrid.addWidget(noticeGroupBox, 0, 0)

        donate1 = DonateButton(1)
        donate5 = DonateButton(5)
        donate10 = DonateButton(10)

        donateLayout = QGridLayout()
        donateLayout.addWidget(donate1, 0, 0)
        donateLayout.addWidget(donate5, 1, 0)
        donateLayout.addWidget(donate10, 2, 0)
        donateGroupBox = QGroupBox("Donate")
        donateGroupBox.setLayout(donateLayout)
        containerGrid.addWidget(donateGroupBox, 0, 1)

        createGroupBox = QGroupBox("Create")
        createLayout = QGridLayout()

        self.lb_ttf_file = QLineEdit('No file selected')
        self.lb_ttf_file.setDisabled(True)
        self.lb_ttf_file.setMinimumWidth(300)
        createLayout.addWidget(self.lb_ttf_file, 1, 0, 1, 3)

        btn_select_ttf = QPushButton('Select TTF file')
        btn_select_ttf.clicked.connect(lambda: self.select_file(self.lb_ttf_file))
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
        btn_select_folder.clicked.connect(lambda: self.select_folder(self.lb_directory))
        createLayout.addWidget(btn_select_folder, 3, 3, 1, 2)

        btn_create = FullButton('Font File Create')
        btn_create.clicked.connect(self.create_font)
        createLayout.addWidget(btn_create, 4, 0, 1, 5)

        createGroupBox.setLayout(createLayout)
        containerGrid.addWidget(createGroupBox, 0, 2)

        return containerGrid

    def select_file(self, target):
        # Select the file dialog design.
        dialog_style = QFileDialog.DontUseNativeDialog
        dialog_style |= QFileDialog.DontUseCustomDirectoryIcons

        # Open the file dialog to select an image file.
        self.file_chosen, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                          "TTF (*.ttf)",
                                                          options=dialog_style)

        # Show the path of the file chosen.
        if self.file_chosen:
            target.setText(self.file_chosen)
            # Change the text on the label to display the file path chosen.
        else:
            target.setText("No file was selected. Please select an image.")
            # Change the text on the label to say that "No file was selected. Please select an image."
            # This 'else' statement is used to catch the case where the user presses 'Cancel' after opening the file dialog,
            # which will close the file dialog without choosing any file, even if they had already previously chosen a file
            # from previously opening the file dialog.
        pass

    def select_folder(self, target):
        dialog_style = QFileDialog.DontUseNativeDialog
        dialog_style |= QFileDialog.DontUseCustomDirectoryIcons

        self.file_chosen = QFileDialog.getExistingDirectory(self, 'Open working directory', '.', QFileDialog.ShowDirsOnly)

        if self.file_chosen:
            target.setText(self.file_chosen)
        else:
            target.setText("No file was selected. Please select an image.")

    def create_font(self):
        print('run test from main')
        runtest()
        create_bmp_range('..\\font\\d2.ttf')


        # TODO: 필요한 정보가 있는지 확인한다.
        # 폰트파일, 압축해제폴더, 패킹파일위치, 패킹파일명,
        # self.font_path
        # self.bmp_path
        # self.pack_path
        # self.pack_file_name
        # # 옵션, BMP 폴더 삭제, 기존 파일 덮어쓰기
        # self.delete_bmp_folder
        # self.overwrite_bmp_file

        # TODO: run thread, and disable other buttons.
        # TODO: when it finished, enable buttons.


        #     self.showdialog()
        #
        # def showdialog(self):
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Information)
        #
        #     msg.setText("Start to creat Font file for Amazfit bip")
        #     msg.setInformativeText("This is additional information")
        #     msg.setWindowTitle("MessageBox demo")
        #     msg.setDetailedText("The details are as follows:")
        #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #     msg.buttonClicked.connect(self.msgbtn)
        #
        #     retval = msg.exec_()
        #     print("value of pressed message box button:", retval)
        #
        # def msgbtn(self, i):
        #     print("Button pressed is:", i.text())


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    print('Currently used style:', app.style().metaObject().className())
    print('Available styles:', QStyleFactory.keys())
    creator = FontCreator()
    sys.exit(app.exec_())
