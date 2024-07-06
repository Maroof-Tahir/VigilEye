from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
    QRadioButton, QSizePolicy, QStackedWidget, QTextEdit,QHeaderView,
    QVBoxLayout, QWidget)
import sys
from ui import Ui_MainWindow
from sidebar import MySideBar
from sidebar2 import MySideBar2
import mysql.connector as myconn
import re
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stack = QStackedWidget()
        self.sideBar1 = MySideBar()
        self.sideBar2 = MySideBar2()
        self.stack.addWidget(self.sideBar1)
        self.stack.addWidget(self.sideBar2)
        self.stack.setStyleSheet("color: rgb(0, 0, 0);")

        self.setCentralWidget(self.stack)

        # Connect buttons to methods
        self.sideBar1.pushButton_6.clicked.connect(self.register_def)
        self.sideBar1.pushButton.clicked.connect(self.login_Def)
        self.sideBar2.pushButton_24.clicked.connect(self.show_sideBar1)
        self.sideBar1.pushButton_69696.clicked.connect(self.generate_and_send)
        self.sideBar1.pushButton_696.clicked.connect(self.ran_chk)
        self.sideBar2.pushButton_22.clicked.connect(self.generate_and_send_for_name_update)
        self.sideBar2.pushButton_23.clicked.connect(self.ran_chk_for_name_update)
        self.sideBar2.pushButton_21.clicked.connect(self.generate_and_send_for_password_update)
        self.sideBar2.pushButton_233.clicked.connect(self.ran_chk_for_name_password)


        #self.stack.setCurrentIndex(1)

    def show_sideBar1(self):
        self.stack.setCurrentWidget(self.sideBar1)

    def show_sideBar2(self):
        self.stack.setCurrentWidget(self.sideBar2)
        
    def forget_password(self):
        Email = self.sideBar1.email_verify.text()
        mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))   # Email verification while loging in or signing up
        result = mycursor.fetchone()
        self.send_email_password(result[2],Email,result[0])
        

    numr=None
    def generate_and_send(self):
        Email = self.sideBar1.email_verify.text()
        mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))   # Email verification while loging in or signing up
        result = mycursor.fetchone()
        if result:
            self.numr = random.randint(100000, 999999)
            print(f'Generated Number: {self.numr}')
            #self.label.setText(f'Generated Number: {number}')
            self.send_email_code(self.numr,result[0])
        else:
            self.sideBar1.label_66.setText("Email does'nt exist! please sign up")
            self.sideBar1.label_66.setStyleSheet("color: red;")

    def ran_chk(self):
        num_input = self.sideBar1.password_verify.text()
        if num_input.strip():
            num_input = int(num_input)
            if num_input == self.numr:
                self.forget_password()
                self.sideBar1.label_66.setText("Password sent successfully!")
                self.sideBar1.label_66.setStyleSheet("color: green;")
            else:
                print("Code Not Match")
                self.sideBar1.label_66.setText("Code Not Match")
                self.sideBar1.label_66.setStyleSheet("color: red;")
        else:
            print("input empty")


    def send_email_code(self, numbers_str,name):
        sender_email = 'vigileyemanagement@outlook.com'
        sender_password = 'vigileye123'
        recipient_email = self.sideBar1.email_verify.text()
        subject = 'Welcome to VigilEye - Your Verification Code Inside'
        body = f"Dear {name},\nWelcome to VigilEye!\nWe are thrilled to have you join us. VigilEye is dedicated to providing the highest level of security for your peace of mind.\n\nTo complete your signup or update your details, please use the verification code below:\nVerification Code: {numbers_str}\n\nThank you for choosing VigilEye. If you have any questions or need assistance, feel free to reach out to our support team.\n\nBest regards,\nTeam VigilEye"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.outlook.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            print(f'Email sent successfully!\nGenerated Numbers: {numbers_str}')
            self.sideBar1.label_66.setText("Email sent successfully!")
            self.sideBar1.label_66.setStyleSheet("color: green;")
            #self.label.setText(f'Email sent successfully!\nGenerated Numbers: {numbers_str}')
        except Exception as e:
            print(f'Failed to send email. Error: {str(e)}')
            #self.label.setText(f'Failed to send email. Error: {str(e)}')
    


    def send_email_password(self, numbers_str, email , name):
        sender_email = 'vigileyemanagement@outlook.com'
        sender_password = 'vigileye123'
        recipient_email = self.sideBar1.email_verify.text()
        subject = 'Welcome to VigilEye - Your Password Inside'
        body = f"Dear {name},\nWelcome to VigilEye!\nWe are thrilled to have you join us. VigilEye is dedicated to providing the highest level of security for your peace of mind.\n\nTo complete your login for email: {email}, please find your password below:\nPassword: {numbers_str}\n\nThank you for choosing VigilEye. If you have any questions or need assistance, feel free to reach out to our support team.\n\nBest regards,\nTeam VigilEye"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.outlook.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            print(f'Email sent successfully!\nGenerated Numbers: {numbers_str}')
            self.sideBar1.label_66.setText("Email sent successfully!")
            self.sideBar1.label_66.setStyleSheet("color: green;")


            #self.label.setText(f'Email sent successfully!\nGenerated Numbers: {numbers_str}')
        except Exception as e:
            print(f'Failed to send email. Error: {str(e)}')
            #self.label.setText(f'Failed to send email. Error: {str(e)}')

    def profilesdata_count(self):
    
    # Connect to the database
        mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
        mycursor = mydb.cursor()

    # Execute the query to count the total number of users
        mycursor.execute("SELECT COUNT(*) FROM login")
        result = mycursor.fetchone()

    # Fetch the count and update the label
        total_users = result[0]  # result[0] contains the count
        self.sideBar2.label_117.setText(str(total_users))
        self.sideBar2.label_1177.setText(str(total_users))
    numr_name = None
    def generate_and_send_for_name_update(self):
        Email = self.sideBar1.email.text()
        mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))   # Email verification while loging in or signing up
        result = mycursor.fetchone()
        self.numr_name = random.randint(100000, 999999)
        print(f'Generated Number: {self.numr_name}')
        #self.label.setText(f'Generated Number: {number}')
        self.send_email_code_update(self.numr_name,result[0])
            


    def ran_chk_for_name_update(self):
        num_input = self.sideBar2.email_5.text()
        if num_input.strip():
            num_input = int(num_input)
            if num_input == self.numr_name:
                self.data_update_name()
            else:
                print("Code Not Match")
                self.sideBar2.label_666.setText("Code not match")
                self.sideBar2.label_666.setStyleSheet("color: red;")
        else:
            print("input empty")

    numr_password = None
    def generate_and_send_for_password_update(self):
        Email = self.sideBar1.email.text()
        mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))   # Email verification while loging in or signing up
        result = mycursor.fetchone()
        self.numr_password = random.randint(100000, 999999)
        print(f'Generated Number: {self.numr_password}')
        #self.label.setText(f'Generated Number: {number}')
        self.send_email_code_password(self.numr_password,result[0])
            


    def ran_chk_for_name_password(self):
        num_input = self.sideBar2.email_55.text()
        if num_input.strip():
            num_input = int(num_input)
            if num_input == self.numr_password:
                self.data_update_password()
            else:
                print("Code Not Match")
                self.sideBar2.label_666.setText("Code not match")
                self.sideBar2.label_666.setStyleSheet("color: red;")
        else:
            print("input empty")
    def send_email_code_password(self, numbers_str,name):
        sender_email = 'vigileyemanagement@outlook.com'
        sender_password = 'vigileye123'
        recipient_email = self.sideBar1.email.text()
        subject = 'Welcome to VigilEye - Your Verification Code Inside'
        body = f"Dear {name},\nWelcome to VigilEye!\nWe are thrilled to have you join us. VigilEye is dedicated to providing the highest level of security for your peace of mind.\n\nTo complete your signup or update your details, please use the verification code below:\nVerification Code: {numbers_str}\n\nThank you for choosing VigilEye. If you have any questions or need assistance, feel free to reach out to our support team.\n\nBest regards,\nTeam VigilEye"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.outlook.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            print(f'Email sent successfully!\nGenerated Numbers: {numbers_str}')
            self.sideBar2.label_666.setText("Email sent successfully!")
            self.sideBar2.label_666.setStyleSheet("color: green;")
            #self.label.setText(f'Email sent successfully!\nGenerated Numbers: {numbers_str}')
        except Exception as e:
            print(f'Failed to send email. Error: {str(e)}')
            #self.label.setText(f'Failed to send email. Error: {str(e)}')

    def send_email_code_update(self, numbers_str,name):
        sender_email = 'vigileyemanagement@outlook.com'
        sender_password = 'vigileye123'
        recipient_email = self.sideBar1.email.text()
        subject = 'Welcome to VigilEye - Your Verification Code Inside'
        body = f"Dear {name},\nWelcome to VigilEye!\nWe are thrilled to have you join us. VigilEye is dedicated to providing the highest level of security for your peace of mind.\n\nTo complete your signup or update your details, please use the verification code below:\nVerification Code: {numbers_str}\n\nThank you for choosing VigilEye. If you have any questions or need assistance, feel free to reach out to our support team.\n\nBest regards,\nTeam VigilEye"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.outlook.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            print(f'Email sent successfully!\nGenerated Numbers: {numbers_str}')
            self.sideBar2.label_666.setText("Email sent successfully!")
            self.sideBar2.label_666.setStyleSheet("color: green;")
            #self.label.setText(f'Email sent successfully!\nGenerated Numbers: {numbers_str}')
        except Exception as e:
            print(f'Failed to send email. Error: {str(e)}')
            #self.label.setText(f'Failed to send email. Error: {str(e)}')
    def data_update_name(self):
        Email = self.sideBar1.email.text()
        mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
        mycursor = mydb.cursor()
    
        # Fetch user details based on email
        mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))
        result = mycursor.fetchone()
    
        if result:
            new_name = self.sideBar2.email_4.text()
        
            if new_name:
                # Update user name
                update_query = "UPDATE login SET name=%s WHERE email=%s"
                mycursor.execute(update_query, (new_name, Email))
                mydb.commit()
        
                print("User name updated successfully.")
                self.sideBar2.label_666.setText("User name updated successfully.")
                self.sideBar2.label_666.setStyleSheet("color: green;")
                self.sideBar2.label_113.setText(f"Welcome, {result[0]}!")  # Assuming result[0] is the name column
                self.sideBar2.label_113.setStyleSheet("color: black;")
            else:
                self.sideBar2.label_666.setText("Name field is empty")
                self.sideBar2.label_666.setStyleSheet("color: red;")
        else:
            print("User not found.")
            self.sideBar2.label_666.setText("User not found.")
            
    # def data_update_email(self):
    #         Email = self.sideBar1.email.text()
    #         mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
    #         mycursor = mydb.cursor()
    
    #         # Fetch user details based on email
    #         mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))
    #         result = mycursor.fetchone()
    #         new_email = self.sideBar2.email_5.text()
    #         if result:
                
        
    #             # Update user name
    #             update_query = "UPDATE login SET email=%s WHERE email=%s"
    #             mycursor.execute(update_query, (new_email, Email))
    #             mydb.commit()
    #             self.sideBar2.label_666.setText("User email updated successfully.")
    #             print("User email updated successfully.")
    #         else:
    #             self.sideBar2.label_666.setText("User not found.")
    #             print("User not found.")
    #         Email = new_email

    def data_update_password(self):
            Email = self.sideBar1.email.text()
            mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
            mycursor = mydb.cursor()
    
            # Fetch user details based on email
            mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))
            result = mycursor.fetchone()
    
            if result:

                new_password = self.sideBar2.password_5.text()
                if new_password:
                    if len(new_password) >= 8:
                        # Update user name
                        update_query = "UPDATE login SET password=%s WHERE email=%s"
                        mycursor.execute(update_query, (new_password, Email))
                        mydb.commit()
                        self.sideBar2.label_666.setText("User password updated successfully.")
                        self.sideBar2.label_666.setStyleSheet("color: green;")

                        print("User password updated successfully.")
                    else:
                        self.sideBar2.label_666.setText("Password should be at least 8 characters long. Registration aborted.")
                        self.sideBar2.label_666.setStyleSheet("color: red;")
                else:
                    self.sideBar2.label_666.setText("Password field is empty!")
                    self.sideBar2.label_666.setStyleSheet("color: red;")
            else:
                self.sideBar2.label_666.setText("User not found.")
                self.sideBar2.label_666.setStyleSheet("color: red;")
                print("User not found.")

    def profilesdata(self):
        
        #table_name=login
        mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
        mycursor = mydb.cursor()                       # Data for profiles table
        mycursor.execute("SELECT * FROM login ")
            
        result = mycursor.fetchall()
        
        self.sideBar2.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.sideBar2.tableWidget.insertRow(row_number)
                
            for column_number, data in enumerate(row_data):
                self.sideBar2.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def login_Def(self):
        try:
            Email = self.sideBar1.email.text()
            Password = self.sideBar1.password.text()
            mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))   # Email verification while loging in or signing up
            result = mycursor.fetchone()
            
            if result:
                if result[2] == Password:  # result[2] is the password column in the database
                    self.show_sideBar2()
                    # Set welcome message in label_113
                    self.sideBar2.label_113.setText(f"Welcome, {result[0]}!")  # Assuming result[0] is the name column
                    self.sideBar2.label_113.setStyleSheet("color: black;")  # Optionally set the text color
                    self.profilesdata()
                    self.profilesdata_count()
                    #self.sideBar2.pushButton_23.clicked.connect(self.data_update_email)
                    self.sideBar1.label_6.setText("")


                else:
                    self.sideBar1.label_6.setText("Password not correct")
                    self.sideBar1.label_6.setStyleSheet("color: red;")
                    self.sideBar1.label_5.setText("")
            else:
                self.sideBar1.label_5.setText("Wrong email address")
                self.sideBar1.label_5.setStyleSheet("color: red;")
                self.sideBar1.label_6.setText("")
        except myconn.Error as err:
            print(f"Error: {err}")



    def register_def(self):
        try:
            Name = self.sideBar1.email_5.text()
            Email = self.sideBar1.email_4.text()
            Password = self.sideBar1.password_4.text()
            Confirm_pass = self.sideBar1.password_5.text()
        
            # Check if email is a proper email format
            if not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
                self.sideBar1.label_query.setText("Invalid email format. Registration aborted.")
                self.sideBar1.label_query.setStyleSheet("color: red;")
                print("Invalid email format. Registration aborted.")
                return
        
            # Check if password length is at least 8 characters
            if len(Password) < 8:
                self.sideBar1.label_query.setText("Password should be at least 8 characters long. Registration aborted.")
                self.sideBar1.label_query.setStyleSheet("color: red;")
                print("Password should be at least 8 characters long. Registration aborted.")
                return

            mydb = myconn.connect(host="34.135.144.211", user="root", password="", database="vigileye")
            mycursor = mydb.cursor()
        
            # Check if the email already exists
            mycursor.execute("SELECT * FROM login WHERE email=%s", (Email,))
            result = mycursor.fetchone()

            if result:
                self.sideBar1.label_query.setText("Email already exists. Registration aborted.")
                self.sideBar1.label_query.setStyleSheet("color: red;")
                print("Email already exists. Registration aborted.")
            else:
                if Password == Confirm_pass:
                    # Insert new user into the database
                    mycursor.execute("INSERT INTO login (name, email, password) VALUES (%s, %s, %s)", (Name, Email, Password))
                    mydb.commit()
                    self.sideBar1.label_query.setText("Registration successful.")
                    self.sideBar1.label_query.setStyleSheet("color: green;")
                    print("Registration successful.")
                else:
                    self.sideBar1.label_query.setText("Passwords do not match.")
                    self.sideBar1.label_query.setStyleSheet("color: red;")
                    print("Passwords do not match.")

        except myconn.Error as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
