# https://stackoverflow.com/questions/42887955/how-to-download-files-using-pyqt5-webenginewidgets
#
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import *

app = QtWidgets.QApplication(sys.argv)
w = QWebEngineView()
# w.page().fullScreenRequested.connect(QWebEngineFullScreenRequest.accept)
w.load(QtCore.QUrl('https://google.com'))
# w.showMaximized()
app.exec_()
