#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we receive data from
a QtGui.QInputDialog dialog. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""
import socket 
import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        ## Connect Button
        self.btn = QtGui.QPushButton('Connect', self)
        self.btn.move(25, 72)
        self.btn.clicked.connect(self.Connect)
        
        ## USERNAME
        self.lblUsername = QtGui.QLabel(self)
        self.lblUsername.setText("USERNAME:")
        self.lblUsername.move(25,25)
        self.txtUsername = QtGui.QLineEdit(self)
        self.txtUsername.move(100, 22)

        ## IP ADDRESS
        self.lblIPAddress = QtGui.QLabel(self)
        self.lblIPAddress.setText("IP ADDRESS:")
        self.lblIPAddress.move(25,50)
        self.txtIPAddress = QtGui.QLineEdit(self)
        self.txtIPAddress.move(100, 47)

        ##InputBox

        ##Window Settings
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Neumann Chat')
        self.show()
        
    def Connect(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.le.setText(str(text))
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()