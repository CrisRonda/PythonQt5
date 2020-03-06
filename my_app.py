#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import  uic, QtWidgets
 
qtCreatorFile = "calculadoraDesk.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.btn_calc.clicked.connect(self.calculate_discount)
    def calculate_discount(self):
        price = int(self.inp_price.toPlainText())
        discount = (self.sb_discount.value())
        total = ((100-discount)/100)*price
        label_total_str= "Debes pagar: "+str(total)
        self.inp_total.setText(label_total_str)
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())