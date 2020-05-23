from listfile import Filelist as flist

from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
mylist=flist("pdf")
print(mylist.listfile())
