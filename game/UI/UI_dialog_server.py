# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_layout/dialog_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 216)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 160, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(50, 50, 161, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(50, 110, 161, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 40, 91, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_25 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_25.setObjectName("radioButton_25")
        self.verticalLayout.addWidget(self.radioButton_25)
        self.radioButton_55 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_55.setObjectName("radioButton_55")
        self.verticalLayout.addWidget(self.radioButton_55)
        self.radioButton_85 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_85.setObjectName("radioButton_85")
        self.verticalLayout.addWidget(self.radioButton_85)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "имя сервера"))
        self.label_2.setText(_translate("Dialog", "пароль"))
        self.radioButton_25.setText(_translate("Dialog", "25x25"))
        self.radioButton_55.setText(_translate("Dialog", "55x55"))
        self.radioButton_85.setText(_translate("Dialog", "85x85"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
