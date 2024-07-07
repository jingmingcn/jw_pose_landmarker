# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 269)
        self.file_ok = QtWidgets.QPushButton(Form)
        self.file_ok.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.file_ok.setObjectName("file_ok")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(14, 5, 361, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_file_path_label = QtWidgets.QLabel(self.layoutWidget)
        self.show_file_path_label.setStyleSheet("")
        self.show_file_path_label.setObjectName("show_file_path_label")
        self.horizontalLayout_2.addWidget(self.show_file_path_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_path_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_path_label.sizePolicy().hasHeightForWidth())
        self.file_path_label.setSizePolicy(sizePolicy)
        self.file_path_label.setMinimumSize(QtCore.QSize(0, 20))
        self.file_path_label.setObjectName("file_path_label")
        self.horizontalLayout.addWidget(self.file_path_label)
        self.choice_file_path_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_file_path_button.sizePolicy().hasHeightForWidth())
        self.choice_file_path_button.setSizePolicy(sizePolicy)
        self.choice_file_path_button.setObjectName("choice_file_path_button")
        self.horizontalLayout.addWidget(self.choice_file_path_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 180, 291, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.radioButton_mp3 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_mp3.setEnabled(False)
        self.radioButton_mp3.setObjectName("radioButton_mp3")
        self.horizontalLayout_3.addWidget(self.radioButton_mp3)
        self.radioButton_wav = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_wav.setEnabled(False)
        self.radioButton_wav.setObjectName("radioButton_wav")
        self.horizontalLayout_3.addWidget(self.radioButton_wav)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 130, 291, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.radioButton_mp4 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_mp4.setObjectName("radioButton_mp4")
        self.horizontalLayout_4.addWidget(self.radioButton_mp4)
        self.radioButton_avi = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_avi.setObjectName("radioButton_avi")
        self.horizontalLayout_4.addWidget(self.radioButton_avi)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "初始化配置"))
        self.file_ok.setText(_translate("Form", "确认"))
        self.label.setText(_translate("Form", "音视频格式选择"))
        self.show_file_path_label.setText(_translate("Form", "当前文件保存路径:"))
        self.file_path_label.setText(_translate("Form", "C:"))
        self.choice_file_path_button.setText(_translate("Form", "选择文件保存路径"))
        self.label_3.setText(_translate("Form", "音频格式"))
        self.radioButton_mp3.setText(_translate("Form", "mp3"))
        self.radioButton_wav.setText(_translate("Form", "wav"))
        self.label_2.setText(_translate("Form", "视频格式"))
        self.radioButton_mp4.setText(_translate("Form", "mp4"))
        self.radioButton_avi.setText(_translate("Form", "avi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
