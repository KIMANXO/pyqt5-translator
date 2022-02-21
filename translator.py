from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import googletrans
import textblob

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(774, 619)
        root.setFixedSize(774,619)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("translate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        root.setWindowIcon(icon)
        root.setStyleSheet("QMainWindow{\n"
"    background-color:black\n"
"}")
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.translate = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.translate_it())
        self.translate.setGeometry(QtCore.QRect(290, 510, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.translate.setFont(font)
        self.translate.setStyleSheet("QPushButton{\n"
"    background-color : rgb(251, 255, 39);\n"
"    color : firebrick;\n"
"    border-radius : 20px \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color : firebrick;\n"
"    color: rgb(251, 255, 39)\n"
"}")
        self.translate.setObjectName("translate")
        self.org_lang = QtWidgets.QTextEdit(self.centralwidget)
        self.org_lang.setGeometry(QtCore.QRect(20, 70, 351, 381))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(14)
        font.setItalic(True)
        self.org_lang.setFont(font)
        self.org_lang.setStyleSheet("QTextEdit{\n"
"    color : rgb(251, 255, 39);\n"
"    background-color: rgb(18, 18, 18);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(251, 255, 39)\n"
"}\n"
"QTextEdit:hover {\n"
"    border: 2px solid aquamarine\n"
"}\n"
"")
        self.org_lang.setObjectName("org_lang")
        self.out_lang = QtWidgets.QTextEdit(self.centralwidget)
        self.out_lang.setGeometry(QtCore.QRect(400, 70, 351, 381))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(14)
        font.setItalic(True)
        self.out_lang.setFont(font)
        self.out_lang.setStyleSheet("QTextEdit{\n"
"    color : rgb(0, 123, 185);\n"
"    background-color: rgb(18, 18, 18);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(251, 255, 39)\n"
"}\n"
"QTextEdit:hover {\n"
"    border: 2px solid aquamarine\n"
"}\n"
"")
        self.out_lang.setObjectName("out_lang")
        self.from_lang = QtWidgets.QComboBox(self.centralwidget)
        self.from_lang.setGeometry(QtCore.QRect(20, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(14)
        font.setItalic(True)
        self.from_lang.setFont(font)
        self.from_lang.setStyleSheet("QComboBox{\n"
"    color : rgb(251, 255, 39);\n"
"    background-color: rgb(18, 18, 18);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(251, 255, 39)\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid aquamarine\n"
"}\n"
"")
        self.from_lang.setCurrentText("")
        self.from_lang.setObjectName("from_lang")
        self.to_lang = QtWidgets.QComboBox(self.centralwidget)
        self.to_lang.setGeometry(QtCore.QRect(400, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(14)
        font.setItalic(True)
        self.to_lang.setFont(font)
        self.to_lang.setStyleSheet("QComboBox{\n"
"    color : rgb(251, 255, 39);\n"
"    background-color: rgb(18, 18, 18);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(251, 255, 39)\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid aquamarine\n"
"}\n"
"")
        self.to_lang.setCurrentText("")
        self.to_lang.setObjectName("to_lang")
        root.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(root)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 24))
        self.menubar.setObjectName("menubar")
        root.setMenuBar(self.menubar)

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

        self.languages = googletrans.LANGUAGES
        self.langs = list(self.languages.values())
        self.from_lang.addItems(self.langs)
        self.to_lang.addItems(self.langs)
        self.from_lang.setCurrentText("english")
        self.to_lang.setCurrentText("arabic")

    def translate_it(self):
        for key,value in self.languages.items():
            if (value == self.from_lang.currentText()):
                from_lang_key = key
        for key,value in self.languages.items():
            if (value == self.to_lang.currentText()):
                to_lang_key = key
        inputs = textblob.TextBlob(self.org_lang.toPlainText())
        result = inputs.translate(from_lang=from_lang_key,to=to_lang_key)
        self.out_lang.setText(str(result))
    
           
    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "Translator"))
        self.translate.setText(_translate("root", "Translate ! "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
