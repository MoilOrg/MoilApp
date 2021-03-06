# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help_moilApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(922, 701)
        Help.setMinimumSize(QtCore.QSize(0, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../My/MoilApp.v.3/MoilApp/src/github/Moildev-apps/src/assets/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Help.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Help)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(Help)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-color: rgb(66, 69, 183);\n"
"background-color: #71D1BA;\n"
"border-radius: 10px;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        self.scrollArea.setMinimumSize(QtCore.QSize(700, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 681))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(66, 69, 183);\n"
"background-color: #71D1BA;\n"
"border-radius: 10px;")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setSearchPaths([])
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "MoilApp Help"))
        self.label_2.setText(_translate("Help", "Index"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Help", "MoilApp"))
        item = self.listWidget.item(1)
        item.setText(_translate("Help", "Plugin"))
        item = self.listWidget.item(2)
        item.setText(_translate("Help", "Multiple View"))
        item = self.listWidget.item(3)
        item.setText(_translate("Help", "Axis Controller"))
        item = self.listWidget.item(4)
        item.setText(_translate("Help", "Object Measurement"))
        item = self.listWidget.item(5)
        item.setText(_translate("Help", "Read more .."))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Help", "Label Apps"))
        self.textBrowser.setHtml(_translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">MoilApp</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Moildev-Apps is a software to process fisheye image with the result panorama view and Anypoint view. The panoramic view may present a horizontal view in a specific immersed environment to meet the common human visual perception, while the Anypoint view is an image that has been undistorted in a certain area according to the input coordinates.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">In addition, this software is also developed for various applications in industry and vehicle security systems. images from anypoint and panoramic views will be further processed such as middle level and high-level processing.</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/Moilapp.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Explanation</span>:</p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">MenuBar</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:24px;\">This is container stores various button     </p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">File</span>    </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:24px;\">File contains <span style=\" font-weight:600;\"> </span>Load image, Load video, Open cam, Cam Parameter, Record Video, Save Image, and Exit    </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Window</span>    </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:24px;\">Window contains  Maximize and Minimize    </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Apps</span>    </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:24px;\">Apps contains <span style=\" font-weight:600;\"> </span>Add, Open, Delete, Create and Help for Add-Ons    </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Help</span>    </li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:24px;\">Help contains<span style=\" font-weight:600;\">  </span>About Apps, About Us and Accesibility</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Name of Application</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This part will give information about app name </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Source of Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">The source button consists of 3 buttons, the first and second button are to Load Images and  Load Videos from the directory and the third button is to open the camera in real time which can choose USB Cam or Web Cam. </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Rotate Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Rotate your image right and left 10 degree</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Zoom Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Zoom in or Zoom out your image and provide information of zoom ratio percentage </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Saving Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Save Image and Record Video</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Add-Ons</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Add-Ons will provide information, install, remove and open Add-Ons application</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Application Name/ Information  of Camera</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This part will first show the name of the MoilApp application but when open the image it will change to camera information on the image used</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">View Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">There are 3 view buttons, the first is Normal View which corresponds to the original image, Anypoint which point can see all sides of the image and Panorama which makes the image a panorama</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Help Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Help button will givr information about MoilApp and Moil-lab</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Support Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This button will show other tools that help in processing anypoint and panoramic images</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Result window</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Showing the resulting image after processing, this is the main image viewer </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Image saved viewer</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This will contain the image frame saved and allow to show it again in the result image viewer</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Video Controller</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This will contain some important tools for the video controller such as the previous button, play/pause button, skip button, stop button, slider time, and recent time viewer of the video</p>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Original Image View</span></li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Showing the original image frame and keep it to show the difference before and after processing</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
import help_moilapp_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Help = QtWidgets.QWidget()
    ui = Ui_Help()
    ui.setupUi(Help)
    Help.show()
    sys.exit(app.exec_())
