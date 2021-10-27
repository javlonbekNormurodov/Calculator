#Calculator
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Calculator")
        Dialog.resize(201, 301)
        self.btn_zero = QtWidgets.QPushButton(Dialog)
        self.btn_zero.setGeometry(QtCore.QRect(0, 250, 101, 51))
        self.btn_zero.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_equal = QtWidgets.QPushButton(Dialog)
        self.btn_equal.setGeometry(QtCore.QRect(100, 250, 101, 51))
        self.btn_equal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_one = QtWidgets.QPushButton(Dialog)
        self.btn_one.setGeometry(QtCore.QRect(0, 200, 51, 51))
        self.btn_one.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_one.setObjectName("btn_one")
        self.btn_two = QtWidgets.QPushButton(Dialog)
        self.btn_two.setGeometry(QtCore.QRect(50, 200, 51, 51))
        self.btn_two.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);")
        self.btn_two.setObjectName("btn_two")
        self.btn_three = QtWidgets.QPushButton(Dialog)
        self.btn_three.setGeometry(QtCore.QRect(100, 200, 51, 51))
        self.btn_three.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);")
        self.btn_three.setObjectName("btn_three")
        self.btn_plus = QtWidgets.QPushButton(Dialog)
        self.btn_plus.setGeometry(QtCore.QRect(150, 200, 51, 51))
        self.btn_plus.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_four = QtWidgets.QPushButton(Dialog)
        self.btn_four.setGeometry(QtCore.QRect(0, 150, 51, 51))
        self.btn_four.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);")
        self.btn_four.setObjectName("btn_four")
        self.btn_five = QtWidgets.QPushButton(Dialog)
        self.btn_five.setGeometry(QtCore.QRect(50, 150, 51, 51))
        self.btn_five.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_five.setObjectName("btn_five")
        self.btn_six = QtWidgets.QPushButton(Dialog)
        self.btn_six.setGeometry(QtCore.QRect(100, 150, 51, 51))
        self.btn_six.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_six.setObjectName("btn_six")
        self.btn_minus = QtWidgets.QPushButton(Dialog)
        self.btn_minus.setGeometry(QtCore.QRect(150, 150, 51, 51))
        self.btn_minus.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_seven = QtWidgets.QPushButton(Dialog)
        self.btn_seven.setGeometry(QtCore.QRect(0, 100, 51, 51))
        self.btn_seven.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_seven.setObjectName("btn_seven")
        self.btn_eight = QtWidgets.QPushButton(Dialog)
        self.btn_eight.setGeometry(QtCore.QRect(50, 100, 51, 51))
        self.btn_eight.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_eight.setObjectName("btn_eight")
        self.btn_nine = QtWidgets.QPushButton(Dialog)
        self.btn_nine.setGeometry(QtCore.QRect(100, 100, 51, 51))
        self.btn_nine.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_nine.setObjectName("btn_nine")
        self.divide = QtWidgets.QPushButton(Dialog)
        self.divide.setGeometry(QtCore.QRect(150, 100, 51, 51))
        self.divide.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);")
        self.divide.setObjectName("divide")
        self.btn_ce = QtWidgets.QPushButton(Dialog)
        self.btn_ce.setGeometry(QtCore.QRect(0, 50, 71, 51))
        self.btn_ce.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_ce.setObjectName("btn_ce")
        self.btn_c = QtWidgets.QPushButton(Dialog)
        self.btn_c.setGeometry(QtCore.QRect(70, 50, 81, 51))
        self.btn_c.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_c.setObjectName("btn_c")
        self.btn_multiply = QtWidgets.QPushButton(Dialog)
        self.btn_multiply.setGeometry(QtCore.QRect(150, 50, 51, 51))
        self.btn_multiply.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_multiply.setObjectName("btn_multiply")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(6, 10, 191, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.add_functions()
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.btn_zero.setText(_translate("Dialog", "0"))
        self.btn_equal.setText(_translate("Dialog", "="))
        self.btn_one.setText(_translate("Dialog", "1"))
        self.btn_two.setText(_translate("Dialog", "2"))
        self.btn_three.setText(_translate("Dialog", "3"))
        self.btn_plus.setText(_translate("Dialog", "+"))
        self.btn_four.setText(_translate("Dialog", "4"))
        self.btn_five.setText(_translate("Dialog", "5"))
        self.btn_six.setText(_translate("Dialog", "6"))
        self.btn_minus.setText(_translate("Dialog", "-"))
        self.btn_seven.setText(_translate("Dialog", "7"))
        self.btn_eight.setText(_translate("Dialog", "8"))
        self.btn_nine.setText(_translate("Dialog", "9"))
        self.divide.setText(_translate("Dialog", "/"))
        self.btn_ce.setText(_translate("Dialog", "CE"))
        self.btn_c.setText(_translate("Dialog", "C"))
        self.btn_multiply.setText(_translate("Dialog", "*"))
        self.label.setText(_translate("Dialog", "0"))
    def add_functions(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_equal.clicked.connect(self.results)
        self.btn_one.clicked.connect(lambda: self.write_number(self.btn_one.text()))
        self.btn_two.clicked.connect(lambda: self.write_number(self.btn_two.text()))
        self.btn_three.clicked.connect(lambda: self.write_number(self.btn_three.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_four.clicked.connect(lambda: self.write_number(self.btn_four.text()))
        self.btn_five.clicked.connect(lambda: self.write_number(self.btn_five.text()))
        self.btn_six.clicked.connect(lambda: self.write_number(self.btn_six.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_seven.clicked.connect(lambda: self.write_number(self.btn_seven.text()))
        self.btn_eight.clicked.connect(lambda: self.write_number(self.btn_eight.text()))
        self.btn_nine.clicked.connect(lambda: self.write_number(self.btn_nine.text()))
        self.divide.clicked.connect(lambda: self.write_number(self.divide.text()))
        self.btn_ce.clicked.connect(self.clear)
        self.btn_c.clicked.connect(self.clear_last)
        self.btn_multiply.clicked.connect(lambda: self.write_number(self.btn_multiply.text()))
    
    def write_number(self,number):
        if(self.label.text() == '0'):
            self.label.setText(number)
        else:
            self.label.setText(self.label.text() + number)
    def results(self):
        res = eval(self.label.text())
        self.label.setText(str(res))
        
    def clear(self):
        self.label.setText("")
    def clear_last(self):
        a = self.label.text()
        self.label.setText(a[:-1])
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
