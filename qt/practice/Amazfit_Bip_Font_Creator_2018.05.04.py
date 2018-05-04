import configparser
import os
import sys
import webbrowser

from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QApplication, QDesktopWidget, QGroupBox, QWidget, QFileDialog, QLabel, QLineEdit, QMessageBox,
                             QSpinBox, QPushButton, QStyleFactory, QHBoxLayout, QVBoxLayout, QCheckBox, QProgressBar)

from qt.bip_font_creator import FontCreator
from qt.button import DonateButton, FullButton


# from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings


class AmazfitBipFontCreator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Amazfit Bip - Font Creator (v0.1)'
        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 300

        self.lbl_ttf = None  # Font file name
        self.chk_delete_bmp = None  # option delete bmp
        self.chk_overwrite_bmp = None
        self.lbl_prog = None
        self.progress = None
        self.sb_margin_top = None
        self.sb_margin_left = None

        self.initUI()
        self.center()

        if hasattr(sys, '_MEIPASS'):
            # self.root_path = os.path.dirname(sys.executable)
            self.root_path = os.path.dirname(sys.argv[0])
        else:
            self.root_path = os.path.dirname(os.path.abspath(__file__))

        self.config = configparser.ConfigParser()
        self.config_file_name = os.path.join(self.root_path, 'config.ini')
        print('config_file_name: ', self.config_file_name)
        self.config.read(self.config_file_name)

        try:
            self.config_ttf = self.config['PATH']['ttf']
            self.lbl_ttf.setText(self.config_ttf)
        except:
            print('error ini')

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

        widget = QWidget()
        widget.setLayout(self.get_layout())

        self.setCentralWidget(widget)

        icon = QIcon(self.resource_path('assets/font.png'))
        self.setWindowIcon(icon)
        self.show()

    def get_notice_box(self):
        notice_box = QVBoxLayout()

        web = QWebEngineView(self)
        # web.setUrl(QUrl('https://jacegem.github.io/amazfit-bip'))
        web.load(QUrl('https://jacegem.github.io/amazfit-bip'))
        notice_box.addWidget(web)

        # notice_group = QGroupBox("Notice")
        # notice_box.addWidget(notice_group)
        return notice_box

    def get_donate_box(self):
        donate_box = QHBoxLayout()

        btn_home = QPushButton('Visit Homepage')
        btn_home.clicked.connect(self.open_home)
        donate_box.addWidget(btn_home)

        donate_group = QGroupBox("Donate")
        donate_layout = QHBoxLayout()
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

        # TTF 선택 라벨, 버튼
        row_ttf = QHBoxLayout()

        self.lbl_ttf = QLineEdit('No file selected')
        self.lbl_ttf.setDisabled(True)
        self.lbl_ttf.setMinimumWidth(300)
        row_ttf.addWidget(self.lbl_ttf)

        btn_ttf = QPushButton('Select TTF file')
        btn_ttf.clicked.connect(lambda: self.select_file(self.lbl_ttf))
        row_ttf.addWidget(btn_ttf)

        # margin-top, margin-left
        row_margin = QHBoxLayout()
        row_margin.addWidget(QLabel('Margin-Top:'))
        self.sb_margin_top = QSpinBox()
        self.sb_margin_top.setMinimum(-99)
        row_margin.addWidget(self.sb_margin_top)

        row_margin.addWidget(QLabel('Margin-Left:'))
        self.sb_margin_left = QSpinBox()
        self.sb_margin_left.setMinimum(-99)
        row_margin.addWidget(self.sb_margin_left)

        # 옵션들
        row_option = QHBoxLayout()
        self.chk_delete_bmp = QCheckBox('Delete BMP files')
        self.chk_delete_bmp.setChecked(True)
        row_option.addWidget(self.chk_delete_bmp)
        self.chk_overwrite_bmp = QCheckBox('Overwrite BMP files')
        row_option.addWidget(self.chk_overwrite_bmp)

        # create 버튼
        row_create = QHBoxLayout()
        self.btn_create = FullButton('''Font File Create
        
        *.ft file will be created in the ft sub-folder'''
                                     )
        self.btn_create.clicked.connect(self.create_font)
        row_create.addWidget(self.btn_create)

        # 전체 순서 결정
        create_layout.addLayout(row_ttf)
        create_layout.addLayout(row_margin)
        create_layout.addLayout(row_option)
        create_layout.addLayout(row_create)

        # set layer
        create_group.setLayout(create_layout)
        create_box.addWidget(create_group)
        return create_box

    def get_layout(self):

        layout = QVBoxLayout()

        hbox_content = QHBoxLayout()
        # hbox_content.addLayout(self.get_notice_box())

        vbox_create = QVBoxLayout()
        vbox_create.addLayout(self.get_create_box())
        vbox_create.addLayout(self.get_donate_box())
        hbox_content.addLayout(vbox_create)

        hbox_progress = QHBoxLayout()
        self.lbl_prog = QLabel('Done')
        hbox_progress.addWidget(self.lbl_prog)
        self.progress = QProgressBar()
        self.progress.setMaximum(100)
        self.progress.setMinimum(0)
        hbox_progress.addWidget(self.progress)

        layout.addLayout(hbox_content)
        layout.addLayout(hbox_progress)
        return layout

    def select_file(self, target):
        # Select the file dialog design.
        dialog_style = QFileDialog.DontUseNativeDialog
        dialog_style |= QFileDialog.DontUseCustomDirectoryIcons

        # Open the file dialog to select an image file.
        file_chosen, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "TTF (*.ttf)")

        # Show the path of the file chosen.
        if file_chosen:
            target.setText(file_chosen)
        else:
            target.setText("No file was selected. Please select an TTF.")

    def select_folder(self, target):
        dialog_style = QFileDialog.DontUseNativeDialog
        dialog_style |= QFileDialog.DontUseCustomDirectoryIcons

        file_chosen = QFileDialog.getExistingDirectory(self, 'Open working directory', '.', QFileDialog.ShowDirsOnly)

        if file_chosen:
            target.setText(file_chosen)
        else:
            target.setText("No file was selected. Please select an image.")

    def create_font(self):
        print('run test from main')
        font_path = self.lbl_ttf.text()
        delete_bmp = self.chk_delete_bmp.isChecked()
        overwrite_bmp = self.chk_overwrite_bmp.isChecked()
        margin_top = self.sb_margin_top.text()
        margin_left = self.sb_margin_left.text()

        if not font_path.lower().endswith('.ttf'):
            msg_box = QMessageBox()
            msg_box.setText("Please Select TTF File")
            msg_box.exec()
            return

        self.config['PATH'] = {}
        self.config['PATH']['ttf'] = font_path
        with open(self.config_file_name, 'w') as configfile:
            self.config.write(configfile)

        self.btn_create.setEnabled(False)
        self.set_progress_text('Start!')

        font_creator_thread = FontCreator(font_path, margin_top, margin_left, delete_bmp, overwrite_bmp, self.root_path, self)
        font_creator_thread.set_progress_text.connect(self.set_progress_text)
        font_creator_thread.set_progress.connect(self.set_progress)
        font_creator_thread.done.connect(self.create_done)
        font_creator_thread.start()

    @pyqtSlot(str)
    def set_progress_text(self, text):
        self.lbl_prog.setText(text)

    def open_home(self):
        webbrowser.open('https://jacegem.github.io/amazfit-bip')

    @pyqtSlot()
    def create_done(self):
        self.set_progress_text('Finished')
        self.set_progress(1, 1)
        self.btn_create.setEnabled(True)
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Font Creator')
        msg_box.setText('Finished')
        # TODO: 완료 메시지 보이기, 폴더 열기 링크 제공 [Open Explorer] [OK]
        msg_box.addButton(QPushButton('OK'), QMessageBox.NoRole)
        # msg_box.addButton(QPushButton('Open File'), QMessageBox.YesRole)
        # msg_box.buttonClicked.connect(self.button_click)
        msg_box.exec()

    @pyqtSlot(int, int)
    def set_progress(self, current, end):
        val = current / end * 100
        self.progress.setValue(int(val))

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    print('Currently used style:', app.style().metaObject().className())
    print('Available styles:', QStyleFactory.keys())
    creator = AmazfitBipFontCreator()
    sys.exit(app.exec_())


    # changed
