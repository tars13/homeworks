import sys
import sqlite3
from PyQt5 import QtWidgets, QtGui

class Course(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.db_course()
        self.init_ui()

    def db_course(self):
        connection = sqlite3.connect("course.db")
        self.cursor = connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS registration_info (Name TEXT, Surname TEXT, Email TEXT, Gender TEXT, City TEXT)")

        connection.commit()

    def init_ui(self):
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("pycoders2.png"))
        self.name_title = QtWidgets.QLabel("Name:")
        self.name = QtWidgets.QLineEdit()
        self.surname_title = QtWidgets.QLabel("Surname:")
        self.surname = QtWidgets.QLineEdit()
        self.e_mail_title = QtWidgets.QLabel("Email:")
        self.e_mail = QtWidgets.QLineEdit()

        self.gender = QtWidgets.QLabel("Gender:")
        self.male = QtWidgets.QRadioButton("Male")
        self.female = QtWidgets.QRadioButton("Female")

        self.city_title = QtWidgets.QLabel("City:")
        self.city = QtWidgets.QLineEdit()

        self.send = QtWidgets.QPushButton("Send")
        self.cancel = QtWidgets.QPushButton("Cancel")

        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.logo)
        v_box.addWidget(self.name_title)
        v_box.addWidget(self.name)
        v_box.addWidget(self.surname_title)
        v_box.addWidget(self.surname)
        v_box.addWidget(self.e_mail_title)
        v_box.addWidget(self.e_mail)
        v_box.addWidget(self.gender)
        v_box.addWidget(self.male)
        v_box.addWidget(self.female)
        v_box.addWidget(self.city_title)
        v_box.addWidget(self.city)
        v_box.addStretch()
        v_box.addWidget(self.send)
        v_box.addWidget(self.cancel)
        v_box.addStretch()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setGeometry(450,150,500,500)
        self.setWindowTitle("Application Form")
        self.send.clicked.connect(self.info_record)
        self.cancel.clicked.connect(self.cancel_space)
        self.show()

    def cancel_space(self):
        self.name.clear()
        self.surname.clear()
        self.e_mail.clear()
        self.city.clear()
    def info_record(self):
        name = self.name.text()
        surname = self.surname.text()
        email = self.e_mail.text()
        if self.male.isChecked() == True:
            gender = "Male"
        elif self.female.isChecked() == True:
            gender = "Female"
        city = self.city.text()
        connection = sqlite3.connect("course.db")
        self.cursor = connection.cursor()
        self.cursor.execute("INSERT INTO registration_info VALUES(?,?,?,?,?)",(name,surname,email,gender,city))
        connection.commit()
        QtWidgets.qApp.quit()



app = QtWidgets.QApplication(sys.argv)

course = Course()

sys.exit(app.exec_())