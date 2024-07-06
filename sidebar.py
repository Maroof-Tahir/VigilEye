from ui import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        
        
        
        
        self.pushButton_2.clicked.connect(self.switch_to_login)
        self.pushButton_7.clicked.connect(self.switch_to_signup)
        self.pushButton_forget.clicked.connect(self.switch_to_forget)
        self.pushButton_6969.clicked.connect(self.switch_to_login)
   
    
    def switch_to_login(self):
        self.stackedWidget.setCurrentIndex(0)
        
    
        
    def switch_to_signup(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_forget(self):
        self.stackedWidget.setCurrentIndex(2)
        
        
    

