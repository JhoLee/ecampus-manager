import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class DialogLogin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(274, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(170, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.chk_license = QtWidgets.QCheckBox(Dialog)
        self.chk_license.setGeometry(QtCore.QRect(20, 250, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        self.chk_license.setFont(font)
        self.chk_license.setChecked(False)
        self.chk_license.setAutoRepeat(False)
        self.chk_license.setObjectName("chk_license")
        self.edit_id = QtWidgets.QLineEdit(Dialog)
        self.edit_id.setGeometry(QtCore.QRect(120, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        self.edit_id.setFont(font)
        self.edit_id.setObjectName("edit_id")
        self.edit_pw = QtWidgets.QLineEdit(Dialog)
        self.edit_pw.setGeometry(QtCore.QRect(120, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        self.edit_pw.setFont(font)
        self.edit_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_pw.setObjectName("edit_pw")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 251, 121))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setText("<html><head/><body><p align=\"justify\">본 프로그램의 사용으로 야기되는 어떠한 긍정적, 부정적 결과에 대해서도 제작자는 그 책임을 지지 않습니다.</p><p align=\"justify\">본 프로그램은 사용자 입력 정보에대한 어떠한 정보도 수집하거나 전송하지 않습니다.</p></body></html>")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "한국교통대학교 e-Campus 출석체크"))
        self.label.setText(_translate("Dialog", "학     번 : "))
        self.label_2.setText(_translate("Dialog", "비밀번호 : "))
        self.btn_login.setText(_translate("Dialog", "로그인"))
        self.chk_license.setText(_translate("Dialog", "라이선스 동의함"))
        self.btn_login.clicked.connect(self.check_validation)

    def check_validation(self):
        if self.chk_license.isChecked():
            pass
        else:
            self.show_messagebox('계속 진행하려면 라이선스에 동의해야합니다.', '경고', QMessageBox.Warning)

    @staticmethod
    def show_messagebox(message, title, icon=QMessageBox.Information):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setText(message)
        # msg_box.setInformativeText(message)
        msg_box.setWindowTitle(title)
        # msg_box.setDetailedText("The details are as follows:")
        msg_box.setStandardButtons(QMessageBox.Ok)
        retval = msg_box.exec_()
        # print("value of pressed message box button:", retval)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DialogLogin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
