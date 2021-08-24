# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/plugins/object_measurement/design/3d_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from moilutils.souceIcon import ResourceIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        rs = ResourceIcon()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1210, 996)
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.OpenImage = QtWidgets.QPushButton(self.centralwidget)
        self.OpenImage.setMinimumSize(QtCore.QSize(0, 40))
        self.OpenImage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap.fromImage(rs.iconOpenImage()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenImage.setIcon(icon)
        self.OpenImage.setIconSize(QtCore.QSize(30, 30))
        self.OpenImage.setObjectName("OpenImage")
        self.horizontalLayout_60.addWidget(self.OpenImage)
        self.OpenParams = QtWidgets.QPushButton(self.centralwidget)
        self.OpenParams.setMinimumSize(QtCore.QSize(0, 40))
        self.OpenParams.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap.fromImage(rs.iconCameraParams()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenParams.setIcon(icon1)
        self.OpenParams.setIconSize(QtCore.QSize(30, 30))
        self.OpenParams.setObjectName("OpenParams")
        self.horizontalLayout_60.addWidget(self.OpenParams)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_60)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setMaximumSize(QtCore.QSize(260, 60))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #71D1BA;   \n"
"border-radius: 10px;")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(260, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_56 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_28.addWidget(self.label_56)
        self.label_status = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif Condensed")
        font.setPointSize(10)
        self.label_status.setFont(font)
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_28.addWidget(self.label_status)
        self.verticalLayout_8.addLayout(self.horizontalLayout_28)
        self.checkBox = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif Condensed")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_8.addWidget(self.checkBox)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_57 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy)
        self.label_57.setMinimumSize(QtCore.QSize(80, 40))
        self.label_57.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_29.addWidget(self.label_57)
        self.point_1_image_1 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point_1_image_1.sizePolicy().hasHeightForWidth())
        self.point_1_image_1.setSizePolicy(sizePolicy)
        self.point_1_image_1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        self.point_1_image_1.setFont(font)
        self.point_1_image_1.setObjectName("point_1_image_1")
        self.horizontalLayout_29.addWidget(self.point_1_image_1)
        self.point_2_image_1 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point_2_image_1.sizePolicy().hasHeightForWidth())
        self.point_2_image_1.setSizePolicy(sizePolicy)
        self.point_2_image_1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        self.point_2_image_1.setFont(font)
        self.point_2_image_1.setObjectName("point_2_image_1")
        self.horizontalLayout_29.addWidget(self.point_2_image_1)
        self.verticalLayout_17.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_59 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy)
        self.label_59.setMinimumSize(QtCore.QSize(80, 40))
        self.label_59.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_30.addWidget(self.label_59)
        self.point_1_image_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point_1_image_2.sizePolicy().hasHeightForWidth())
        self.point_1_image_2.setSizePolicy(sizePolicy)
        self.point_1_image_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        self.point_1_image_2.setFont(font)
        self.point_1_image_2.setObjectName("point_1_image_2")
        self.horizontalLayout_30.addWidget(self.point_1_image_2)
        self.point_2_image_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point_2_image_2.sizePolicy().hasHeightForWidth())
        self.point_2_image_2.setSizePolicy(sizePolicy)
        self.point_2_image_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(10)
        self.point_2_image_2.setFont(font)
        self.point_2_image_2.setObjectName("point_2_image_2")
        self.horizontalLayout_30.addWidget(self.point_2_image_2)
        self.verticalLayout_17.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_61 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        self.label_61.setMinimumSize(QtCore.QSize(100, 40))
        self.label_61.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_33.addWidget(self.label_61)
        self.label_distanc_config = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_distanc_config.sizePolicy().hasHeightForWidth())
        self.label_distanc_config.setSizePolicy(sizePolicy)
        self.label_distanc_config.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label_distanc_config.setFont(font)
        self.label_distanc_config.setObjectName("label_distanc_config")
        self.horizontalLayout_33.addWidget(self.label_distanc_config)
        self.verticalLayout_17.addLayout(self.horizontalLayout_33)
        self.verticalLayout_8.addLayout(self.verticalLayout_17)
        self.clear_button = QtWidgets.QPushButton(self.frame_3)
        self.clear_button.setMinimumSize(QtCore.QSize(0, 35))
        self.clear_button.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout_8.addWidget(self.clear_button)
        self.label_63 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy)
        self.label_63.setMinimumSize(QtCore.QSize(0, 40))
        self.label_63.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("background-color: #71D1BA;   \n"
"border-radius: 10px;")
        self.label_63.setFrameShape(QtWidgets.QFrame.Box)
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.verticalLayout_8.addWidget(self.label_63)
        self.label_64 = QtWidgets.QLabel(self.frame_3)
        self.label_64.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif Condensed")
        font.setPointSize(12)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.verticalLayout_8.addWidget(self.label_64)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem1)
        self.label_65 = QtWidgets.QLabel(self.frame_3)
        self.label_65.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_34.addWidget(self.label_65)
        self.delta_x = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.delta_x.setDecimals(1)
        self.delta_x.setSingleStep(0.1)
        self.delta_x.setObjectName("delta_x")
        self.horizontalLayout_34.addWidget(self.delta_x)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem3)
        self.label_66 = QtWidgets.QLabel(self.frame_3)
        self.label_66.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.horizontalLayout_35.addWidget(self.label_66)
        self.delta_y = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.delta_y.setDecimals(1)
        self.delta_y.setSingleStep(0.1)
        self.delta_y.setObjectName("delta_y")
        self.horizontalLayout_35.addWidget(self.delta_y)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem5)
        self.label_67 = QtWidgets.QLabel(self.frame_3)
        self.label_67.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_36.addWidget(self.label_67)
        self.delta_z = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.delta_z.setDecimals(1)
        self.delta_z.setSingleStep(0.1)
        self.delta_z.setObjectName("delta_z")
        self.horizontalLayout_36.addWidget(self.delta_z)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_36)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem7)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_68 = QtWidgets.QLabel(self.frame_3)
        self.label_68.setMinimumSize(QtCore.QSize(0, 30))
        self.label_68.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.horizontalLayout_37.addWidget(self.label_68)
        self.Image_size_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_size_3.sizePolicy().hasHeightForWidth())
        self.Image_size_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.Image_size_3.setFont(font)
        self.Image_size_3.setObjectName("Image_size_3")
        self.horizontalLayout_37.addWidget(self.Image_size_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_69 = QtWidgets.QLabel(self.frame_3)
        self.label_69.setMinimumSize(QtCore.QSize(0, 30))
        self.label_69.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_38.addWidget(self.label_69)
        self.ratio_image_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ratio_image_3.sizePolicy().hasHeightForWidth())
        self.ratio_image_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        self.ratio_image_3.setFont(font)
        self.ratio_image_3.setObjectName("ratio_image_3")
        self.horizontalLayout_38.addWidget(self.ratio_image_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_38)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_5.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif Condensed")
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_8.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif Condensed")
        font.setPointSize(12)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_8.addWidget(self.checkBox_6)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 120))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif Condensed")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.horizontalLayout_55.addLayout(self.verticalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_55.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #71D1BA;   \n"
"border-radius: 10px;")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem10)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Label_image_L = QtWidgets.QLabel(self.centralwidget)
        self.Label_image_L.setMinimumSize(QtCore.QSize(400, 600))
        self.Label_image_L.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Label_image_L.setText("")
        self.Label_image_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_image_L.setObjectName("Label_image_L")
        self.verticalLayout_18.addWidget(self.Label_image_L)
        self.horizontalLayout_42.addLayout(self.verticalLayout_18)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem11)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.Label_Image_R = QtWidgets.QLabel(self.centralwidget)
        self.Label_Image_R.setMinimumSize(QtCore.QSize(400, 0))
        self.Label_Image_R.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Label_Image_R.setText("")
        self.Label_Image_R.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Image_R.setObjectName("Label_Image_R")
        self.verticalLayout_19.addWidget(self.Label_Image_R)
        self.horizontalLayout_42.addLayout(self.verticalLayout_19)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_42)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem13)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif Condensed")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_43.addWidget(self.pushButton)
        spacerItem14 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem14)
        self.label_78 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif Condensed")
        font.setPointSize(14)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.horizontalLayout_43.addWidget(self.label_78)
        self.label_distance = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_distance.sizePolicy().hasHeightForWidth())
        self.label_distance.setSizePolicy(sizePolicy)
        self.label_distance.setMinimumSize(QtCore.QSize(100, 40))
        self.label_distance.setText("")
        self.label_distance.setObjectName("label_distance")
        self.horizontalLayout_43.addWidget(self.label_distance)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_43)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.horizontalLayout_55.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_55)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1210, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_image = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap.fromImage(rs.iconOpenImage()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_image.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionOpen_image.setFont(font)
        self.actionOpen_image.setObjectName("actionOpen_image")
        self.actionCamera_Parameters = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap.fromImage(rs.iconCameraParams()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCamera_Parameters.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionCamera_Parameters.setFont(font)
        self.actionCamera_Parameters.setObjectName("actionCamera_Parameters")
        self.actionExit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionMaximize.setFont(font)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionMinimize.setFont(font)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAccesibility = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionAccesibility.setFont(font)
        self.actionAccesibility.setObjectName("actionAccesibility")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionAbout_Us.setFont(font)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionWhats_New = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.actionWhats_New.setFont(font)
        self.actionWhats_New.setObjectName("actionWhats_New")
        self.actionHide_Config = QtWidgets.QAction(MainWindow)
        self.actionHide_Config.setCheckable(True)
        self.actionHide_Config.setObjectName("actionHide_Config")
        self.menuFile.addAction(self.actionOpen_image)
        self.menuFile.addAction(self.actionCamera_Parameters)
        self.menuFile.addAction(self.actionExit)
        self.menuWindow.addAction(self.actionMaximize)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAccesibility)
        self.menuHelp.addAction(self.actionAbout_Us)
        self.menuHelp.addAction(self.actionWhats_New)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Object Measurement"))
        self.label.setText(_translate("MainWindow", "Configuration"))
        self.label_56.setText(_translate("MainWindow", "Status :"))
        self.checkBox.setText(_translate("MainWindow", "Auto mode"))
        self.label_57.setText(_translate("MainWindow", "Image 1  :"))
        self.point_1_image_1.setText(_translate("MainWindow", "00"))
        self.point_2_image_1.setText(_translate("MainWindow", "00"))
        self.label_59.setText(_translate("MainWindow", "Image 2  :"))
        self.point_1_image_2.setText(_translate("MainWindow", "00"))
        self.point_2_image_2.setText(_translate("MainWindow", "00"))
        self.label_61.setText(_translate("MainWindow", "Distance :"))
        self.label_distanc_config.setText(_translate("MainWindow", "0.00"))
        self.clear_button.setText(_translate("MainWindow", "Clear !!"))
        self.label_63.setText(_translate("MainWindow", "Setting"))
        self.label_64.setText(_translate("MainWindow", "Camera related Distance:"))
        self.label_65.setText(_translate("MainWindow", "ΔX:"))
        self.label_66.setText(_translate("MainWindow", "ΔY:"))
        self.label_67.setText(_translate("MainWindow", "ΔZ:"))
        self.label_68.setText(_translate("MainWindow", "Image size : "))
        self.Image_size_3.setText(_translate("MainWindow", "(0,0)"))
        self.label_69.setText(_translate("MainWindow", "Ratio Label :"))
        self.ratio_image_3.setText(_translate("MainWindow", "0"))
        self.checkBox_5.setText(_translate("MainWindow", "Corner detection"))
        self.checkBox_6.setText(_translate("MainWindow", "Feature matching"))
        self.label_3.setText(_translate("MainWindow", "Moil Object measurment"))
        self.label_2.setText(_translate("MainWindow", "3D Measurment Using Fisheye Camera"))
        self.pushButton.setText(_translate("MainWindow", "Calculate !!!"))
        self.label_78.setText(_translate("MainWindow", "Distance:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image"))
        self.actionCamera_Parameters.setText(_translate("MainWindow", "Camera Parameters"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAccesibility.setText(_translate("MainWindow", "Accesibility"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.actionWhats_New.setText(_translate("MainWindow", "Whats New"))
        self.actionHide_Config.setText(_translate("MainWindow", "Hide Config"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
