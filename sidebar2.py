from ui_vigileye import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        
        
        
        #self.dashboard_button.clicked.connect(self.switch_to_dashboard)
        self.home_button.clicked.connect(self.switch_to_home)
        self.add_camera_button.clicked.connect(self.switch_to_add_camera)
        self.settings_button.clicked.connect(self.switch_to_settings)
        #self.login_button.clicked.connect(self.switch_to_login)
        self.profiles_button.clicked.connect(self.switch_to_profiles)
        self.pushButton_rstp.clicked.connect(self.switch_to_add_camera)
        #self.favourites_button.clicked.connect(self.switch_to_favourites)
        self.support_button.clicked.connect(self.switch_to_support)
        #self.pushButton_15.clicked.connect(self.switch_to_login)
        #self.pushButton_9.clicked.connect(self.switch_to_signup)
        
    # def switch_to_dashboard(self):
    #     self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_home(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def switch_to_add_camera(self):
        self.stackedWidget.setCurrentIndex(4)
    
    def switch_to_settings(self):
        self.stackedWidget.setCurrentIndex(5)
    
    # def switch_to_login(self):
    #     self.stackedWidget.setCurrentIndex(1)
        
    def switch_to_profiles(self):
        self.stackedWidget.setCurrentIndex(2)
        
    # def switch_to_favourites(self):
    #     self.stackedWidget.setCurrentIndex(5)
    
    def switch_to_support(self):
        self.stackedWidget.setCurrentIndex(6)
        
    # def switch_to_signup(self):
    #     self.stackedWidget.setCurrentIndex(0)
        
        
    

