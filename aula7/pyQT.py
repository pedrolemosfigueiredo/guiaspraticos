# -*- coding: utf-8 -*-
# autor: Pedro Figueiredo
# data: 04/11/2013

import sys
from PyQt4 import QtGui
class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__(); self.initUI()
        pass
    def initUI(self):
        eact = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        tact = QtGui.QAction(QtGui.QIcon('exit.png'), '&Treta', self)
        eact.setShortcut('Ctrl+Q')
        eact.setStatusTip('Exit application')
        eact.triggered.connect(QtGui.qApp.quit)
        tact.triggered.connect(treta)
        self.statusBar()
        mb = self.menuBar(); fm = mb.addMenu('&File')
        fm.addAction(tact); fm.addAction(eact)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Menubar'); self.show()
        pass
    pass
def treta():
    print 'TRETA'
    pass
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
if __name__ == '__main__': main()
