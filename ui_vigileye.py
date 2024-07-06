# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vigileyeUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################



from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
    QRadioButton, QSizePolicy, QStackedWidget, QTextEdit,QHeaderView,
    QVBoxLayout, QWidget)
import sys
import threading
from PySide6.QtMultimedia import (QCamera, QCameraDevice, QMediaDevices, QMediaCaptureSession)
from PySide6.QtMultimediaWidgets import (QVideoWidget)

from inference import InferencePipeline
from inference.core.interfaces.stream.sinks import render_boxes

import threading

# pipeline = None
# def run_api_code(self):

#     # Initialize the inference pipeline
#     pipeline = InferencePipeline.init(
#         model_id="cds-gc5yj/4",
#         api_key="rOHmhOAmDW8U4OSb21Vy",
#         video_reference=0,  # Path to video, device id (int, usually 0 for built-in webcams), or RTSP stream URL
#         confidence=0.70,
#         iou_threshold=0.4,
#         video_source_properties={
#             "frame_width": 1280.0,
#             "frame_height": 720.0,
#             "fps": 30.0,
#         },
#         on_prediction=render_boxes
#     )
    
#     # Start the pipeline and wait for it to finish
#     pipeline.start()
#     pipeline.join()


# def stop_api_code(self):
#         pipeline = InferencePipeline.init(
#             model_id="cds-gc5yj/4",
#             api_key="rOHmhOAmDW8U4OSb21Vy",
#             video_reference=0,  # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
#             on_prediction=render_boxes
#         )
#         pipeline.start()
#         pipeline.join()

#         if pipeline:
#             pipeline._stop()
#             pipeline._camera_restart_ongoing()
#             pipeline.terminate() # Assuming the InferencePipeline class has a stop method
#             pipeline.join()  # Wait for the pipeline to finish
#             pipeline = None

# class CameraWidget(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Set up the layout for this widget
#         self.layout = QVBoxLayout(self)

#         # Create a video widget to display the camera feed
#         self.video_widget = QVideoWidget()
#         self.layout.addWidget(self.video_widget)

#         # Get the default camera device
#         self.camera_device = QMediaDevices.defaultVideoInput()

#         # Create the camera and set the video widget as the viewfinder
#         self.camera = QCamera(self.camera_device)
#         self.capture_session = QMediaCaptureSession()
#         self.capture_session.setCamera(self.camera)
#         self.capture_session.setVideoOutput(self.video_widget)

#         # Start the camera
#         self.camera.start()
        



class Ui_MainWindow(object):
        
    def signupHandler(self):
        print("I am here")
       # get_user_info() 

    def run_api_code(self):
     self.pipeline = InferencePipeline.init(
        model_id="cds-gc5yj/4",
        api_key="rOHmhOAmDW8U4OSb21Vy",
        video_reference=0,
        on_prediction=render_boxes,
        max_fps=10,
        confidence=0.70,
        iou_threshold=0.4,
        video_source_properties={
             "frame_width": 1280.0,
             "frame_height": 720.0,
             "fps": 30.0,
        },
     )
     self.pipeline.start()


    def stop_api_code(self):
        self.pipeline.terminate() 

    pipeline2 = None
    def setupUi(self, MainWindow):
        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        MainWindow.resize(900, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 271, 851))
        self.sidebar.setStyleSheet(u"QWidget{\n"
"		background-color: rgb(0, 31, 63);\n"
"}\n"
"QPushButton {\n"
"        color:white;\n"
"		text-align:centre;\n"
"		border:none;\n"
"		border-top-left-radius:10px;\n"
"		border-bottom-left-radius:10px;\n"
"		border-bottom-right-radius:10px;\n"
"		border-top-right-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#111d88;\n"
"	font-weight:bold;\n"
"}")
        self.label = QLabel(self.sidebar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 150, 70))
        self.label.setPixmap(QPixmap(u"vigileye_logo-removebg.png"))
        self.label.setScaledContents(True)
        
        self.layoutWidget = QWidget(self.sidebar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 280, 151, 281))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_button = QPushButton(self.layoutWidget)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.home_button.setCheckable(True)
        self.home_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_button)

        #self.dashboard_button = QPushButton(self.layoutWidget)
        #self.dashboard_button.setObjectName(u"dashboard_button")
#         self.dashboard_button.setStyleSheet(u"QPushButton{\n"
# "	color:white;\n"
# "	height:30px;\n"
# "	border:none;\n"
# "}")
        #self.dashboard_button.setCheckable(True)
        #self.dashboard_button.setAutoExclusive(True)

        #self.verticalLayout.addWidget(self.dashboard_button)

        self.profiles_button = QPushButton(self.layoutWidget)
        self.profiles_button.setObjectName(u"profiles_button")
        self.profiles_button.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.profiles_button.setCheckable(True)
        self.profiles_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profiles_button)

        #self.favourites_button = QPushButton(self.layoutWidget)
        #self.favourites_button.setObjectName(u"favourites_button")
#         self.favourites_button.setStyleSheet(u"QPushButton{\n"
# "	color:white;\n"
# "	height:30px;\n"
# "	border:none;\n"
# "}")
        #self.favourites_button.setCheckable(True)
        #self.favourites_button.setAutoExclusive(True)

        #self.verticalLayout.addWidget(self.favourites_button)

        self.add_camera_button = QPushButton(self.layoutWidget)
        self.add_camera_button.setObjectName(u"add_camera_button")
        self.add_camera_button.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.add_camera_button.setCheckable(True)
        self.add_camera_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.add_camera_button)

        self.layoutWidget1 = QWidget(self.sidebar)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 720, 91, 106))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.login_button = QPushButton(self.layoutWidget1)
#         self.login_button.setObjectName(u"login_button")
#         self.login_button.setStyleSheet(u"QPushButton{\n"
# "	color:white;\n"
# "	height:30px;\n"
# "	border:none;\n"
# "}")
#         self.login_button.setCheckable(True)
#         self.login_button.setAutoExclusive(True)

#         self.verticalLayout_2.addWidget(self.login_button)

        self.settings_button = QPushButton(self.layoutWidget1)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.settings_button.setCheckable(True)
        self.settings_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_button)

        self.support_button = QPushButton(self.layoutWidget1)
        self.support_button.setObjectName(u"support_button")
        self.support_button.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.support_button.setCheckable(True)
        self.support_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.support_button)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(230, 0, 1366, 768))
        self.stackedWidget.setMaximumSize(QSize(1234567, 12345678))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"\n"
"")
        self.signup = QWidget()
        self.signup.setObjectName(u"signup")
        self.widget_3 = QWidget(self.signup)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 871, 861))
        font = QFont()
        font.setPointSize(10)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(80, 100, 261, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_14.setFont(font1)
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(80, 140, 171, 31))
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 260, 141, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_16.setFont(font2)
        self.pushButton_14 = QPushButton(self.widget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(40, 550, 101, 28))
        font3 = QFont()
        font3.setPointSize(9)
        self.pushButton_14.setFont(font3)
        self.pushButton_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_14.clicked.connect(self.signupHandler)
        self.lineEdit_5 = QLineEdit(self.widget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(70, 290, 301, 31))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(40, 290, 31, 31))
        self.label_17.setPixmap(QPixmap(u"email-icon-vector-illustration-1816079832.jpg"))
        self.label_17.setScaledContents(True)
        self.label_18 = QLabel(self.widget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 340, 101, 16))
        self.label_18.setFont(font)
        self.lineEdit_6 = QLineEdit(self.widget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(70, 370, 301, 31))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_19 = QLabel(self.widget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(40, 370, 31, 31))
        self.label_19.setPixmap(QPixmap(u"lock-icon-vector-illustration-2972797813.jpg"))
        self.label_19.setScaledContents(True)
        self.layoutWidget_3 = QWidget(self.widget_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(550, 30, 271, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_20)

        self.pushButton_15 = QPushButton(self.layoutWidget_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.pushButton_15.setFont(font4)
        self.pushButton_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.pushButton_15)

        self.label_21 = QLabel(self.widget_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(40, 190, 141, 16))
        self.label_21.setFont(font2)
        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(80, 220, 301, 31))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_22 = QLabel(self.widget_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 220, 41, 31))
        self.label_22.setPixmap(QPixmap(u"user-profile-icon-free-vector-658200527.jpg"))
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(self.widget_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(40, 420, 151, 21))
        self.label_23.setFont(font)
        self.lineEdit_8 = QLineEdit(self.widget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(70, 450, 301, 31))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_24 = QLabel(self.widget_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(40, 450, 31, 31))
        self.label_24.setPixmap(QPixmap(u"lock-icon-vector-illustration-2972797813.jpg"))
        self.label_24.setScaledContents(True)
        self.layoutWidget_4 = QWidget(self.widget_3)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(40, 500, 131, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.layoutWidget_4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_4.addWidget(self.checkBox_2)

        self.label_25 = QLabel(self.layoutWidget_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_25)

        # self.stackedWidget.addWidget(self.signup)
        # self.login = QWidget()
        # self.login.setObjectName(u"login")
        # self.widget_2 = QWidget(self.login)
        # self.widget_2.setObjectName(u"widget_2")
        # self.widget_2.setGeometry(QRect(0, 0, 871, 861))
        # self.widget_2.setFont(font)
        # self.widget_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        # self.label_2 = QLabel(self.widget_2)
        # self.label_2.setObjectName(u"label_2")
        # self.label_2.setGeometry(QRect(80, 100, 261, 31))
        # self.label_2.setFont(font1)
        # self.label_3 = QLabel(self.widget_2)
        # self.label_3.setObjectName(u"label_3")
        # self.label_3.setGeometry(QRect(80, 150, 171, 31))
        # self.label_4 = QLabel(self.widget_2)
        # self.label_4.setObjectName(u"label_4")
        # self.label_4.setGeometry(QRect(50, 220, 141, 16))
        # self.label_4.setFont(font2)
        # self.pushButton_8 = QPushButton(self.widget_2)
        # self.pushButton_8.setObjectName(u"pushButton_8")
        # self.pushButton_8.setGeometry(QRect(50, 510, 101, 28))
        # self.pushButton_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        # self.lineEdit = QLineEdit(self.widget_2)
        # self.lineEdit.setObjectName(u"lineEdit")
        # self.lineEdit.setGeometry(QRect(80, 250, 301, 31))
        # self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        # self.label_5 = QLabel(self.widget_2)
        # self.label_5.setObjectName(u"label_5")
        # self.label_5.setGeometry(QRect(50, 250, 31, 31))
        # self.label_5.setPixmap(QPixmap(u"email-icon-vector-illustration-1816079832.jpg"))
        # self.label_5.setScaledContents(True)
        # self.label_6 = QLabel(self.widget_2)
        # self.label_6.setObjectName(u"label_6")
        # self.label_6.setGeometry(QRect(50, 340, 101, 16))
        # self.label_6.setFont(font)
        # self.lineEdit_2 = QLineEdit(self.widget_2)
        # self.lineEdit_2.setObjectName(u"lineEdit_2")
        # self.lineEdit_2.setGeometry(QRect(80, 370, 301, 31))
        # self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        # self.label_8 = QLabel(self.widget_2)
        # self.label_8.setObjectName(u"label_8")
        # self.label_8.setGeometry(QRect(50, 370, 31, 31))
        # self.label_8.setPixmap(QPixmap(u"lock-icon-vector-illustration-2972797813.jpg"))
        # self.label_8.setScaledContents(True)
        # self.label_9 = QLabel(self.widget_2)
        # self.label_9.setObjectName(u"label_9")
        # self.label_9.setGeometry(QRect(240, 410, 141, 21))
        # self.layoutWidget_2 = QWidget(self.widget_2)
        # self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        # self.layoutWidget_2.setGeometry(QRect(580, 30, 251, 41))
        # self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        # self.horizontalLayout.setObjectName(u"horizontalLayout")
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # #self.label_10 = QLabel(self.layoutWidget_2)
        # self.label_10.setObjectName(u"label_10")
        # self.label_10.setFont(font3)

        # self.horizontalLayout.addWidget(self.label_10)

        # self.pushButton_9 = QPushButton(self.layoutWidget_2)
        # self.pushButton_9.setObjectName(u"pushButton_9")
        # self.pushButton_9.setFont(font4)
        # self.pushButton_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        # self.horizontalLayout.addWidget(self.pushButton_9)

        # self.layoutWidget2 = QWidget(self.widget_2)
        # self.layoutWidget2.setObjectName(u"layoutWidget2")
        # self.layoutWidget2.setGeometry(QRect(50, 450, 135, 22))
        # self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        # self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        # self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.checkBox = QCheckBox(self.layoutWidget2)
        # self.checkBox.setObjectName(u"checkBox")

        #self.horizontalLayout_2.addWidget(self.checkBox)

        # self.label_7 = QLabel(self.layoutWidget2)
        # self.label_7.setObjectName(u"label_7")
        # self.label_7.setFont(font3)

        #self.horizontalLayout_2.addWidget(self.label_7)

        #self.stackedWidget.addWidget(self.login)

        self.home1 = QWidget()
        self.home1.setObjectName(u"home")
        self.stackedWidget.addWidget(self.home1)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.label_96 = QLabel(self.home1)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(70, 70, 81, 31))
        self.label_113 = QLabel(self.home1)
        self.label_113.setObjectName(u"label 113")
        self.label_113.setGeometry(QRect(70, 115, 841, 21))
        
        self.widget_totalusers = QWidget(self.home1)
        self.widget_totalusers.setGeometry(70,200,471,51)
        self.widget_totalusers.setObjectName("widget_totalusers")
        self.widget_totalusers.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 1px solid black;
    border-radius: 10px;
""")
        font70 = QFont()
        font70.setBold(True)

        self.label_117 = QLabel(self.widget_totalusers)
        self.label_117.setObjectName(u"label 117")
        self.label_117.setGeometry(QRect(440, 20, 450, 16))
        self.label_117.setFont(font70)
        self.label_117.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 1px solid black;
""")
        

        self.label_114 = QLabel(self.widget_totalusers)
        self.label_114.setObjectName(u"label 114")
        self.label_114.setGeometry(QRect(20, 20, 200, 16))
        self.label_114.setFont(font70)
        self.label_114.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 0px solid black;
""")
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Total Users:", None))

        self.widget_cameras = QWidget(self.home1)
        self.widget_cameras.setGeometry(70,261,471,51)
        self.widget_cameras.setObjectName("widget_cameras")
        self.widget_cameras.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 1px solid black;
    border-radius: 10px;
""")
        self.label_115 = QLabel(self.widget_cameras)
        self.label_115.setObjectName(u"label 115")
        self.label_115.setGeometry(QRect(20, 20, 200, 16))
        self.label_115.setFont(font70)
        self.label_115.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 0px solid black;
""")
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Total Cameras:", None))

        self.label_116 = QLabel(self.widget_cameras)
        self.label_116.setObjectName(u"label 116")
        self.label_116.setGeometry(QRect(440, 20, 450, 16))
        self.label_116.setFont(font70)
        self.label_116.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 1px solid black;
""")
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"2", None))
        
        

        font69 = QFont()
        font69.setPointSize(12)
        font69.setBold(True)
        self.label_113.setFont(font69)
        font5 = QFont()
        font5.setPointSize(14)
        self.label_96.setFont(font5)
        self.label_97 = QLabel(self.home1)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(70, 150, 81, 21))
        self.label_97.setFont(font3)
        self.label_camfeed = QLabel(self.home1)
        self.label_camfeed.setObjectName(u"label_camfeed")
        self.label_camfeed.setGeometry(QRect(70, 380, 81, 21))
        self.label_camfeed.setFont(font3)
        self.label_camfeed.setText(QCoreApplication.translate("MainWindow", u"Camera Feed", None))
        self.label_webcam = QLabel(self.home1)
        self.label_webcam.setObjectName(u"label_rstp")
        self.label_webcam.setGeometry(QRect(70, 450, 150, 21))
        self.label_webcam.setFont(font69)
        self.label_webcam.setText(QCoreApplication.translate("MainWindow", u"Webcam : ", None))
        self.label_rstp = QLabel(self.home1)
        self.label_rstp.setObjectName(u"label_rstp")
        self.label_rstp.setGeometry(QRect(400, 450, 150, 21))
        self.label_rstp.setFont(font69)
        self.label_rstp.setText(QCoreApplication.translate("MainWindow", u"IP Camera : ", None))
        self.pushButton_startcam = QPushButton(self.home1)
        self.pushButton_startcam.setObjectName(u"pushButton_startcam")
        self.pushButton_startcam.setGeometry(QRect(70, 500, 93, 28))
        
        self.pushButton_startcam.clicked.connect(self.run_api_code)
        self.pushButton_startcam.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n")
        
        self.pushButton_stopcam = QPushButton(self.home1)
        self.pushButton_stopcam.setObjectName(u"pushButton_startcam")
        self.pushButton_stopcam.setGeometry(QRect(70, 570, 93, 28))
        self.pushButton_stopcam.clicked.connect(self.stop_api_code)
        self.pushButton_stopcam.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n")
        

        self.pushButton_rstp = QPushButton(self.home1)
        self.pushButton_rstp.setObjectName(u"pushButton_startcam")
        self.pushButton_rstp.setGeometry(QRect(400, 528, 93, 28))
        self.pushButton_rstp.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n")
        self.pushButton_rstp.setText(QCoreApplication.translate("MainWindow", u"Add IP : ", None))

        
        self.label_104 = QLabel(self.home)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(70, 380, 111, 21))
        self.label_104.setFont(font)
        self.widget = QWidget(self.home)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 170, 3311, 181))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setMaximumSize(QSize(1677, 16777215))
        self.widget1.setStyleSheet(u"background-color: rgb(188, 188, 188);\n"
"")
        self.label_98 = QLabel(self.widget1)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(20, 10, 81, 16))
        self.label_101 = QLabel(self.widget1)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(640, 10, 41, 16))

        self.verticalLayout_5.addWidget(self.widget1)

        self.widget_20 = QWidget(self.widget)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setStyleSheet(u"background-color: rgb(188, 188, 188);\n"
"")
        self.label_99 = QLabel(self.widget_20)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(20, 10, 91, 16))
        self.label_102 = QLabel(self.widget_20)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(640, 10, 41, 16))

        self.verticalLayout_5.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setStyleSheet(u"background-color: rgb(188, 188, 188);\n"
"")
        self.label_100 = QLabel(self.widget_21)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(20, 10, 151, 16))
        self.label_103 = QLabel(self.widget_21)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(640, 10, 41, 16))

        self.verticalLayout_5.addWidget(self.widget_21)

        self.widget2 = QWidget(self.home)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(620, 370, 179, 31))
        self.horizontalLayout_15 = QHBoxLayout(self.widget2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_14 = QLineEdit(self.widget2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_15.addWidget(self.lineEdit_14)

        self.pushButton_5 = QPushButton(self.widget2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font6 = QFont()
        font6.setPointSize(8)
        self.pushButton_5.setFont(font6)
        icon = QIcon()
        icon.addFile(u"search icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.pushButton_5)

        self.widget3 = QWidget(self.home)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(60, 430, 731, 171))
        self.horizontalLayout_16 = QHBoxLayout(self.widget3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_105 = QLabel(self.widget3)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMaximumSize(QSize(500, 16777215))
        self.label_105.setPixmap(QPixmap(u"emp1.jpg"))
        self.label_105.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_105)

        self.label_106 = QLabel(self.widget3)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMaximumSize(QSize(500, 16777215))
        self.label_106.setPixmap(QPixmap(u"emp2.jpg"))
        self.label_106.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_106)

        self.label_107 = QLabel(self.widget3)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMaximumSize(QSize(500, 16777215))
        self.label_107.setPixmap(QPixmap(u"emp3.jpg"))
        self.label_107.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_107)

        self.label_108 = QLabel(self.widget3)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMaximumSize(QSize(500, 16777215))
        self.label_108.setPixmap(QPixmap(u"emp4.jpg"))
        self.label_108.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_108)

        self.widget4 = QWidget(self.home)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(60, 610, 741, 23))
        self.horizontalLayout_17 = QHBoxLayout(self.widget4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_109 = QLabel(self.widget4)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_109)

        self.label_110 = QLabel(self.widget4)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_110)

        self.label_111 = QLabel(self.widget4)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_111)

        self.label_112 = QLabel(self.widget4)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_112)

        #self.stackedWidget.addWidget(self.home)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.widget_4 = QWidget(self.dashboard)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 871, 851))
        self.widget_4.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 50, 180, 41))
        font7 = QFont()
        font7.setPointSize(15)
        self.label_11.setFont(font7)
        
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(70, 190, 261, 171))
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        #self.camera_widget = CameraWidget()
        
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(470, 190, 261, 171))
        self.widget_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(470, 460, 261, 171))
        self.widget_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(70, 460, 261, 171))
        self.widget_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.widget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(500, 60, 231, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_16 = QPushButton(self.widget_4)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(740, 60, 93, 28))
        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(460, 60, 31, 31))
        self.label_28.setPixmap(QPixmap(u"search icon.png"))
        self.label_28.setScaledContents(True)
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(150, 370, 111, 31))
        font8 = QFont()
        font8.setPointSize(12)
        self.label_12.setFont(font8)
        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(550, 370, 111, 31))
        self.label_13.setFont(font8)
        self.label_27 = QLabel(self.widget_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(150, 640, 111, 31))
        self.label_27.setFont(font8)
        self.label_26 = QLabel(self.widget_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(540, 630, 111, 31))
        self.label_26.setFont(font8)
        self.stackedWidget.addWidget(self.dashboard)
        self.profiles = QWidget()
        self.profiles.setObjectName(u"profiles")
        self.widget_9 = QWidget(self.profiles)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(0, 0, 841, 871))
        self.widget_9.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        
        self.widget_9 = QWidget(self.profiles)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(-1, -1, 841, 841))
        self.layoutWidget_5 = QWidget(self.widget_9)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(100, 300, 7071, 5061))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.layoutWidget_5)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        if (self.tableWidget.rowCount() < 7):
            self.tableWidget.setRowCount(7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 200)  # Adjust the width of column 0
        self.tableWidget.setColumnWidth(1, 200)  # Adjust the width of column 1
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Email"])
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.refresh_btn = QPushButton(self.layoutWidget_5)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.verticalLayout_3.addWidget(self.refresh_btn)
        #self.refresh_btn.clicked.connect(self.profilesdata)
        self.widget_totalusers1 = QWidget(self.profiles)
        self.widget_totalusers1.setGeometry(70,200,471,51)
        self.widget_totalusers1.setObjectName("widget_totalusers1")
        self.widget_totalusers1.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 1px solid black;
    border-radius: 10px;
""")
        font70 = QFont()
        font70.setBold(True)

        self.label_1177 = QLabel(self.widget_totalusers1)
        self.label_1177.setObjectName(u"label_1177")
        self.label_1177.setGeometry(QRect(440, 20, 450, 16))
        self.label_1177.setFont(font70)
        self.label_1177.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 1px solid black;
""")
        

        self.label_1144 = QLabel(self.widget_totalusers1)
        self.label_1144.setObjectName(u"label_1144")
        self.label_1144.setGeometry(QRect(20, 20, 200, 16))
        self.label_1144.setFont(font70)
        self.label_1144.setStyleSheet("""
    background-color: rgb(188, 188, 188);
    border: 0px solid black;
""")
        self.label_1144.setText(QCoreApplication.translate("MainWindow", u"Total Users:", None))
        
        self.label_966 = QLabel(self.profiles)
        self.label_966.setObjectName(u"label_966")
        self.label_966.setGeometry(QRect(70, 70, 81, 31))
        self.label_966.setText(QCoreApplication.translate("MainWindow", u"Profiles", None))
        self.label_966.setFont(font5)



        self.stackedWidget.addWidget(self.profiles)
        self.favourites = QWidget()
        self.favourites.setObjectName(u"favourites")
        self.widget_15 = QWidget(self.favourites)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(0, 0, 841, 851))
        self.widget_15.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.label_55 = QLabel(self.widget_15)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(50, 50, 151, 41))
        self.label_55.setFont(font8)
        self.label_56 = QLabel(self.widget_15)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(50, 120, 55, 16))
        self.label_56.setFont(font)
        self.layoutWidget_16 = QWidget(self.widget_15)
        self.layoutWidget_16.setObjectName(u"layoutWidget_16")
        self.layoutWidget_16.setGeometry(QRect(90, 760, 661, 20))
        
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.layoutWidget_16)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_57)

        self.label_58 = QLabel(self.layoutWidget_16)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_58)

        self.label_59 = QLabel(self.layoutWidget_16)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_59)

        self.label_60 = QLabel(self.layoutWidget_16)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_60)

        self.layoutWidget_17 = QWidget(self.widget_15)
        self.layoutWidget_17.setObjectName(u"layoutWidget_17")
        self.layoutWidget_17.setGeometry(QRect(90, 420, 661, 20))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.layoutWidget_17)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_61)

        self.label_62 = QLabel(self.layoutWidget_17)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_62)

        self.label_63 = QLabel(self.layoutWidget_17)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_63)

        self.label_64 = QLabel(self.layoutWidget_17)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_64)

        self.layoutWidget_18 = QWidget(self.widget_15)
        self.layoutWidget_18.setObjectName(u"layoutWidget_18")
        self.layoutWidget_18.setGeometry(QRect(80, 320, 671, 97))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_18)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.layoutWidget_18)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setPixmap(QPixmap(u"stealing.PNG"))
        self.label_65.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_65)

        self.label_66 = QLabel(self.layoutWidget_18)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setPixmap(QPixmap(u"shoplifting.PNG"))
        self.label_66.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_66)

        self.label_67 = QLabel(self.layoutWidget_18)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setPixmap(QPixmap(u"robbery.PNG"))
        self.label_67.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_67)

        self.label_68 = QLabel(self.layoutWidget_18)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setPixmap(QPixmap(u"shooting.PNG"))
        self.label_68.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_68)

        self.layoutWidget_19 = QWidget(self.widget_15)
        self.layoutWidget_19.setObjectName(u"layoutWidget_19")
        self.layoutWidget_19.setGeometry(QRect(90, 460, 661, 131))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_19)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.layoutWidget_19)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setPixmap(QPixmap(u"explosion.PNG"))
        self.label_69.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_69)

        self.label_70 = QLabel(self.layoutWidget_19)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setPixmap(QPixmap(u"fighting.PNG"))
        self.label_70.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_70)

        self.label_71 = QLabel(self.layoutWidget_19)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setPixmap(QPixmap(u"road accidents.PNG"))
        self.label_71.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_71)

        self.label_72 = QLabel(self.layoutWidget_19)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setPixmap(QPixmap(u"burglary.PNG"))
        self.label_72.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_72)

        self.layoutWidget_20 = QWidget(self.widget_15)
        self.layoutWidget_20.setObjectName(u"layoutWidget_20")
        self.layoutWidget_20.setGeometry(QRect(90, 600, 671, 20))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.layoutWidget_20)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_73)

        self.label_74 = QLabel(self.layoutWidget_20)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_74)

        self.label_75 = QLabel(self.layoutWidget_20)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_75)

        self.label_76 = QLabel(self.layoutWidget_20)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_76)

        self.layoutWidget_21 = QWidget(self.widget_15)
        self.layoutWidget_21.setObjectName(u"layoutWidget_21")
        self.layoutWidget_21.setGeometry(QRect(90, 630, 661, 121))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_21)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.layoutWidget_21)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setPixmap(QPixmap(u"assault.PNG"))
        self.label_77.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_77)

        self.label_78 = QLabel(self.layoutWidget_21)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setPixmap(QPixmap(u"arson.PNG"))
        self.label_78.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_78)

        self.label_79 = QLabel(self.layoutWidget_21)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setPixmap(QPixmap(u"arrest.PNG"))
        self.label_79.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_79)

        self.label_80 = QLabel(self.layoutWidget_21)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setPixmap(QPixmap(u"abuse.PNG"))
        self.label_80.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_80)

        self.layoutWidget3 = QWidget(self.widget_15)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(560, 120, 239, 30))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_9 = QLineEdit(self.layoutWidget3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.lineEdit_9)

        self.pushButton_18 = QPushButton(self.layoutWidget3)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_11.addWidget(self.pushButton_18)

        self.stackedWidget.addWidget(self.favourites)
        self.add_camera = QWidget()
        self.add_camera.setObjectName(u"add_camera")
        self.widget_16 = QWidget(self.add_camera)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(0, 0, 861, 851))
        self.widget_16.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.label_81 = QLabel(self.widget_16)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(50, 70, 151, 41))
        self.label_81.setStyleSheet("color: rgb(0, 0, 0);") 
        font10 = QFont()
        font10.setPointSize(13)
        self.label_81.setFont(font10)
        
        
        self.lineEdit_10 = QLineEdit(self.widget_16)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(90, 330, 311, 51))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter RSTP URL", None))

        self.pipeline2 = None
        def run_api_url():
                url_of_rstp = self.lineEdit_10.text()   
                self.pipeline2 = InferencePipeline.init(
                        model_id="cds-gc5yj/4",
                        api_key="rOHmhOAmDW8U4OSb21Vy",
                        video_reference=url_of_rstp,
                        on_prediction=render_boxes,
                        max_fps=10,
                        confidence=0.70,
                        iou_threshold=0.4,
                        video_source_properties={
                        "frame_width": 1280.0,
                        "frame_height": 720.0,
                        "fps": 30.0,
                        },
                )
                self.pipeline2.start()
        def stop_api_url():
            if self.pipeline2 is not None:
                self.pipeline2.terminate()
                self.pipeline2 = None
        
#         self.label_83 = QLabel(self.widget_16)
#         self.label_83.setObjectName(u"label_83")
#         self.label_83.setGeometry(QRect(50, 340, 31, 31))
#         self.label_83.setPixmap(QPixmap(u"74_Connection_Error_communication_internet_disconnect_network_global_issues_repository_lost_no_service-512-3869570745.png"))
#         self.label_83.setScaledContents(True)
        
        self.pushButton_19 = QPushButton(self.widget_16)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(200, 420, 93, 28))
        self.pushButton_19.clicked.connect(stop_api_url)
        self.pushButton_19.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n")
        self.pushButton_696 = QPushButton(self.widget_16)
        self.pushButton_696.setObjectName(u"pushButton_696")
        self.pushButton_696.setGeometry(QRect(100, 420, 93, 28))
        self.pushButton_696.clicked.connect(run_api_url)
        self.pushButton_696.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n")
        
#         self.pushButton_697 = QPushButton(self.widget_16)
#         self.pushButton_697.setObjectName(u"pushButton_697")
#         self.pushButton_697.setGeometry(QRect(100, 420, 93, 28))
#         self.pushButton_697.clicked.connect(stop_api_code)
#         self.pushButton_697.setStyleSheet(u"background-color: black;\n"
# "color: white;\n"
# "border-radius: 10px;\n")
       

        
#         self.layoutWidget_22 = QWidget(self.widget_16)
#         self.layoutWidget_22.setObjectName(u"layoutWidget_22")
#         self.layoutWidget_22.setGeometry(QRect(532, 90, 271, 30))
#         self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_22)
#         self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
#         self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        


        
        self.stackedWidget.addWidget(self.add_camera)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")

        self.settings1 = QWidget()
        self.settings1.setObjectName(u"settings")
        
        self.widget_18 = QWidget(self.settings)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(0, 0, 841, 851))
        self.widget_18.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.widget_188 = QWidget(self.settings1)
        self.widget_188.setObjectName(u"widget_18")
        self.widget_188.setGeometry(QRect(0, 0, 841, 851))
        self.widget_188.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.email_4 = QLineEdit(self.widget_188)
        self.email_4.setObjectName(u"email_4")
        self.email_4.setGeometry(QRect(50, 260, 281, 31))
        self.email_4.setFocusPolicy(Qt.ClickFocus)
        self.email_4.setContextMenuPolicy(Qt.PreventContextMenu)
        self.email_4.setStyleSheet(u"")
        self.email_4.setFrame(True)
        self.email_4.setEchoMode(QLineEdit.Normal)
        self.email_4.setCursorPosition(0)
        self.email_4.setAlignment(Qt.AlignCenter)
        self.email_4.setDragEnabled(False)
        self.email_4.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.email_4.setClearButtonEnabled(True)
        self.email_4.setInputMask("")
        self.email_4.setText("")
        self.email_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Name", None))
        self.label_86 = QLabel(self.widget_188)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(70, 70, 81, 31))
        self.label_14 = QLabel(self.widget_188)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(50, 230, 111, 16))
        font161 = QFont()
        font161.setPointSize(8)
        font161.setBold(False)
        self.label_14.setFont(font161)
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"NEW NAME", None))
        self.email_5 = QLineEdit(self.widget_188)
        self.email_5.setObjectName(u"email_5")
        self.email_5.setGeometry(QRect(50, 350, 281, 31))
        self.email_5.setFocusPolicy(Qt.ClickFocus)
        self.email_5.setContextMenuPolicy(Qt.PreventContextMenu)
        self.email_5.setStyleSheet(u"")
        self.email_5.setFrame(True)
        self.email_5.setEchoMode(QLineEdit.Normal)
        self.email_5.setCursorPosition(0)
        self.email_5.setAlignment(Qt.AlignCenter)
        self.email_5.setDragEnabled(False)
        self.email_5.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.email_5.setClearButtonEnabled(True)
        self.email_5.setInputMask("")
        self.email_5.setText("")
        self.email_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your name verification code....", None))
        self.label_18 = QLabel(self.widget_188)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 320, 200, 16))
        self.label_18.setFont(font161)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"ENTER NAME VERIFICATION CODE", None))
        self.password_5 = QLineEdit(self.widget_188)
        self.password_5.setObjectName(u"password_5")
        self.password_5.setGeometry(QRect(50, 440, 281, 31))
        self.password_5.setFocusPolicy(Qt.ClickFocus)
        self.password_5.setContextMenuPolicy(Qt.PreventContextMenu)
        self.password_5.setStyleSheet(u"")
        self.password_5.setFrame(True)
        self.password_5.setEchoMode(QLineEdit.Password)
        self.password_5.setCursorPosition(0)
        self.password_5.setAlignment(Qt.AlignCenter)
        self.password_5.setDragEnabled(False)
        self.password_5.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.password_5.setClearButtonEnabled(True)
        self.password_5.setInputMask("")
        self.password_5.setText("")
        self.password_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your new password...", None))
        self.label_19 = QLabel(self.widget_188)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 410, 150, 16))
        self.label_19.setFont(font161)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"NEW PASSWORD", None))
        self.email_55 = QLineEdit(self.widget_188)
        self.email_55.setObjectName(u"email_55")
        self.email_55.setGeometry(QRect(50, 530, 281, 31))
        self.email_55.setFocusPolicy(Qt.ClickFocus)
        self.email_55.setContextMenuPolicy(Qt.PreventContextMenu)
        self.email_55.setStyleSheet(u"")
        self.email_55.setFrame(True)
        self.email_55.setEchoMode(QLineEdit.Normal)
        self.email_55.setCursorPosition(0)
        self.email_55.setAlignment(Qt.AlignCenter)
        self.email_55.setDragEnabled(False)
        self.email_55.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.email_55.setClearButtonEnabled(True)
        self.email_55.setInputMask("")
        self.email_55.setText("")
        self.email_55.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your Password verification code....", None))
        self.label_1818 = QLabel(self.widget_188)
        self.label_1818.setObjectName(u"label_18")
        self.label_1818.setGeometry(QRect(50, 500, 200, 16))
        self.label_1818.setFont(font161)
        self.label_1818.setText(QCoreApplication.translate("MainWindow", u"ENTER PASSWORD VERIFICATION CODE", None))

        self.pushButton_21 = QPushButton(self.widget_188)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(360, 440, 121, 31))
        self.pushButton_21.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n"
"                                 ")
        self.pushButton_22 = QPushButton(self.widget_188)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(360, 260, 121, 31))
        self.pushButton_22.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n"
"                                 ")
        self.pushButton_23 = QPushButton(self.widget_188)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(360, 350, 121, 31))
        self.pushButton_23.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n"
"                                 ")
        self.pushButton_233 = QPushButton(self.widget_188)
        self.pushButton_233.setObjectName(u"pushButton_233")
        self.pushButton_233.setGeometry(QRect(360, 530, 121, 31))
        self.pushButton_233.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;\n"
"                                 ")
        self.pushButton_24 = QPushButton(self.widget_188)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(50, 610, 101, 31))
        self.pushButton_24.setStyleSheet(u"background-color: rgb(54, 0, 147);\n"
"color: rgb(255, 255, 255);")
        self.label_666 = QLabel(self.widget_188)
        self.label_666.setObjectName(u"label_666")
        self.label_666.setGeometry(QRect(50, 580, 500, 16))
        #self.label_666.setFont(font1)
        font11 = QFont()
        font11.setPointSize(13)
        font11.setBold(True)
        self.label_86.setFont(font5)
        self.label_87 = QLabel(self.widget_18)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(100, 260, 141, 31))
        self.lineEdit_12 = QLineEdit(self.widget_18)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(100, 300, 111, 31))
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_88 = QLabel(self.widget_18)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(220, 310, 91, 16))
        self.label_88.setStyleSheet(u"")
        self.layoutWidget_23 = QWidget(self.widget_18)
        self.layoutWidget_23.setObjectName(u"layoutWidget_23")
        self.layoutWidget_23.setGeometry(QRect(100, 350, 291, 31))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_23)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_89 = QLabel(self.layoutWidget_23)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_13.addWidget(self.label_89)

        self.radioButton_2 = QRadioButton(self.layoutWidget_23)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_13.addWidget(self.radioButton_2)

        self.label_90 = QLabel(self.widget_18)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(100, 390, 141, 31))
        self.lineEdit_13 = QLineEdit(self.widget_18)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(100, 420, 111, 41))
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_91 = QLabel(self.widget_18)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(220, 440, 91, 16))
        self.label_91.setStyleSheet(u"")
        
        self.layoutWidget_24 = QWidget(self.widget_18)
        self.layoutWidget_24.setObjectName(u"layoutWidget_24")
        self.layoutWidget_24.setGeometry(QRect(100, 210, 291, 31))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget_24)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_92 = QLabel(self.layoutWidget_24)
        self.label_92.setObjectName(u"label_92")

        self.horizontalLayout_14.addWidget(self.label_92)

        self.radioButton = QRadioButton(self.layoutWidget_24)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_14.addWidget(self.radioButton)

        self.stackedWidget.addWidget(self.settings1)
        self.support = QWidget()
        self.support.setObjectName(u"support")
        self.widget_19 = QWidget(self.support)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(0, 0, 841, 841))
        self.widget_19.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.label_93 = QLabel(self.widget_19)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(50, 80, 121, 41))
        self.label_93.setFont(font5)
        self.label_94 = QLabel(self.widget_19)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(0, 240, 629, 51))
        self.label_94.setFont(font8)
        self.label_94.setAlignment(Qt.AlignCenter)
        self.label_94.setWordWrap(True)
        self.label_95 = QLabel(self.widget_19)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(0, 280, 629, 31))
        self.label_95.setStyleSheet(u"")
        self.label_95.setAlignment(Qt.AlignCenter)
        self.label_95.setWordWrap(True)
        self.stackedWidget.addWidget(self.support)
        font322 = QFont()
        font322.setPointSize(13)
        font322.setBold(True)
        self.label_955 = QLabel(self.widget_19)
        self.label_955.setObjectName(u"label_95")
        self.label_955.setGeometry(QRect(0, 320, 629, 31))
        self.label_955.setStyleSheet(u"")
        self.label_955.setAlignment(Qt.AlignCenter)
        self.label_955.setWordWrap(True)
        self.label_955.setFont(font322)
        self.stackedWidget.addWidget(self.support)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        #self.dashboard_button.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.profiles_button.setText(QCoreApplication.translate("MainWindow", u"Profiles", None))
        #self.favourites_button.setText(QCoreApplication.translate("MainWindow", u"Favourites", None))
        self.add_camera_button.setText(QCoreApplication.translate("MainWindow", u"Add Camera", None))
        #self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.support_button.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        #self.label_14.setText(QCoreApplication.translate("MainWindow", u"Create New User", None))
        # self.label_15.setText(QCoreApplication.translate("MainWindow", u"Enter your user details here", None))
        # self.label_16.setText(QCoreApplication.translate("MainWindow", u"EMAIL ADDRESS", None))
        # self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Sign Up ", None))
        # self.label_17.setText("")
        # self.label_18.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        # self.label_19.setText("")
        # self.label_20.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        # self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        # self.label_21.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        # self.label_22.setText("")
        # self.label_23.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.label_24.setText("")
        self.checkBox_2.setText("")
        # self.label_25.setText(QCoreApplication.translate("MainWindow", u"Remember me ", None))
        # self.label_2.setText(QCoreApplication.translate("MainWindow", u"Log into VigilEye", None))
        # self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter your login details here", None))
        # self.label_4.setText(QCoreApplication.translate("MainWindow", u"EMAIL ADDRESS", None))
        # self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Login ", None))
        # self.label_5.setText("")
        # self.label_6.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        # self.label_8.setText("")
        # self.label_9.setText(QCoreApplication.translate("MainWindow", u"Forgot Password ?", None))
        # self.label_10.setText(QCoreApplication.translate("MainWindow", u"Don't have an account", None))
        # self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        # self.checkBox.setText("")
        # self.label_7.setText(QCoreApplication.translate("MainWindow", u"Remember me ?", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Online Users", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Total Users", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Total Cameras", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"168", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Total Crimes Detected", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.pushButton_5.setText("")
        self.label_105.setText("")
        self.label_106.setText("")
        self.label_107.setText("")
        self.label_108.setText("")
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Julie ", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Sam", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Jack", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"John", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_28.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Camera 3", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Camera 4", None))
        
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Favourites", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Assault", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Arson", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Arrest", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Abuse", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Stealing", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Shoplifting", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Robbery", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Shooting", None))
        self.label_65.setText("")
        self.label_66.setText("")
        self.label_67.setText("")
        self.label_68.setText("")
        self.label_69.setText("")
        self.label_70.setText("")
        self.label_71.setText("")
        self.label_72.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Explosion", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Fighting ", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Road Accidents", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Burglary", None))
        self.label_77.setText("")
        self.label_78.setText("")
        self.label_79.setText("")
        self.label_80.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Add camera", None))
        # self.label_83.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_startcam.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stopcam.setText(QCoreApplication.translate("MainWindow", u"Stop", None))


        self.pushButton_696.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        #self.pushButton_697.setText(QCoreApplication.translate("MainWindow", u"Stop Webcam", None))

        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Set time Manually", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Ex. 23:30:29", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Set date automatically", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Set date Manually", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Ex. 23:30:29", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Change Name", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Verify for Name", None))
        self.pushButton_233.setText(QCoreApplication.translate("MainWindow", u"Verify for Password", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Set Time zone automatically", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Need Help?", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Email your query at", None))
        self.label_955.setText(QCoreApplication.translate("MainWindow", u"vigileyemanagement@outlook.com", None))

        
        
    # retranslateUi

