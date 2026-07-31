from PyQt5.QtWidgets import ( QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel, QGridLayout,
    QLineEdit, QRadioButton, QHBoxLayout, QMessageBox,
    QButtonGroup, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QProcess
import platform, json, os
import test_files.i2c_file as i2c_file

class I2C_Menu(QWidget):
    def __init__(self,stack):
        super().__init__()
        i2cLayout = QGridLayout()

        i2c_stack = QStackedWidget()

        i2c_stack.addWidget(I2C_Step1(i2c_stack,stack))
        i2c_stack.addWidget(I2C_Step2(i2c_stack))
        i2c_stack.addWidget(I2C_Step3(i2c_stack))
        i2c_stack.addWidget(I2C_Final(i2c_stack,stack))
        i2cLayout.addWidget(i2c_stack)

        self.setLayout(i2cLayout)

class I2C_Step1(QWidget):
    def __init__(self,i2c_stack,stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       

        title = QLabel("I2C Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 1: ----------------------------<br>"
                           "------------------------------------<br>"
                           "------------------------------------<br>")
        direction.setFixedSize(360,500)
        direction.setStyleSheet("font-size: 18px")

        # Image Setup
        image1_holder = QLabel()
        i1pixmap = QPixmap("images/placeholder.png")
        i1pixmap = i1pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image1_holder.setPixmap(i1pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: i2c_stack.setCurrentIndex(1))
        return_btn.clicked.connect(lambda: stack.setCurrentIndex(2))

        # Step and Image Row
        H1.addStretch()
        H1.addWidget(direction)
        H1.addStretch()
        H1.addWidget(image1_holder)
        H1.addStretch()

        # Page Button Row
        H2.addStretch(1)
        H2.addWidget(return_btn)
        H2.addStretch(28)
        H2.addWidget(next_btn)
        H2.addStretch(1)

        # Combined Layout
        V1.addWidget(title)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addStretch()
        V1.addLayout(H2)
        self.setLayout(V1)

class I2C_Step2(QWidget):
    def __init__(self,i2c_stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       
        title = QLabel("I2C Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 2: ------------------------------------<br>" 
                           "--------------------------------------------<br>"
                           "-------------------------------------------.")
        
        #label top/bottom in the image----------------------------------------------------
        
        direction.setFixedSize(360,500)
        direction.setStyleSheet("font-size: 18px")

        #Image Setup
        image2_holder = QLabel()
        i2pixmap = QPixmap("images/placeholder.png")
        i2pixmap = i2pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image2_holder.setPixmap(i2pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: i2c_stack.setCurrentIndex(2))
        return_btn.clicked.connect(lambda: i2c_stack.setCurrentIndex(0))

        # Step and Image Row
        H1.addStretch()
        H1.addWidget(direction)
        H1.addStretch()
        H1.addWidget(image2_holder)
        H1.addStretch()

        # Page Button Row
        H2.addStretch(1)
        H2.addWidget(return_btn)
        H2.addStretch(28)
        H2.addWidget(next_btn)
        H2.addStretch(1)

        # Combined Layout
        V1.addWidget(title)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addStretch()
        V1.addLayout(H2)
        self.setLayout(V1)

class I2C_Step3(QWidget):
    def __init__(self,i2c_stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()

        title = QLabel("I2C Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 3: ----------------------------------<br>" 
                           "------------------------------------------<br>"
                           "----------------------------------------- <br>")
        direction.setFixedSize(360,500)
        direction.setStyleSheet("font-size: 18px")
        
        # Image Setup
        image3_holder = QLabel()
        i3pixmap = QPixmap("images/placeholder.png")
        i3pixmap = i3pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image3_holder.setPixmap(i3pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)

        next_btn.clicked.connect(lambda: i2c_stack.setCurrentIndex(3))
        return_btn.clicked.connect(lambda: i2c_stack.setCurrentIndex(1))

        # Step and Image Row
        H1.addStretch()
        H1.addWidget(direction)
        H1.addStretch()
        H1.addWidget(image3_holder)
        H1.addStretch()

        # Page Button Row
        H2.addStretch(1)
        H2.addWidget(return_btn)
        H2.addStretch(28)
        H2.addWidget(next_btn)
        H2.addStretch(1)

        # Combined Layout
        V1.addWidget(title)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addStretch()
        V1.addLayout(H2)
        self.setLayout(V1)

class I2C_Final(QWidget):
    def __init__(self,i2c_stack,stack):
        super().__init__()

        self.stack = stack

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
        H3 = QHBoxLayout()
        H7 = QHBoxLayout()

# Widget Configurations, Button Connections ------------------------------------------------------
        menu_title = QLabel("I2C Menu") 
        menu_title.setStyleSheet("font-size: 20px; font-weight: " 
                                 "bold; text-decoration: underline")

        test_btn = QPushButton("Run Test")
        test_btn.setStyleSheet("font-size: 14px")
        # self.test = QProcess(self)
        test_btn.clicked.connect(self.test_function)

        self.direction = QLabel("<center>Record the results here:</center>") 
        self.direction.setStyleSheet("font-size: 16px; text-decoration: underline")
        
        # General Radio Box
        radioTitle = QLabel("I2C (GPIO 2,3)") 
        radioTitle.setStyleSheet("font-size: 14px")
        self.pass1 = QRadioButton("Pass") 
        self.pass1.setStyleSheet("font-size: 14px")
        self.passflag = 0 
        self.fail1 = QRadioButton("Fail") 
        self.fail1.setStyleSheet("font-size: 14px")
        self.failflag = 0 
        
        self.pass1.toggled.connect(self.pass1check)
        self.fail1.toggled.connect(self.fail1check)
        
        radio1_opt = QButtonGroup(self)
        radio1_opt.addButton(self.pass1)
        radio1_opt.addButton(self.fail1)
        
        # # General Radio Box
        # radioTitle2 = QLabel("Radio Title 2") 
        # radioTitle2.setStyleSheet("font-size: 14px")
        # self.pass2 = QRadioButton("Pass") 
        # self.pass2.setStyleSheet("font-size: 14px")
        # self.pass2flag = 0 
        # self.fail2 = QRadioButton("Fail") 
        # self.fail2.setStyleSheet("font-size: 14px")
        # self.fail2flag = 0 
        
        # self.pass2.toggled.connect(self.pass2check)
        # self.fail2.toggled.connect(self.fail2check)
        
        # radio2_opt = QButtonGroup(self)
        # radio2_opt.addButton(self.pass2)
        # radio2_opt.addButton(self.fail2)

        # Notes
        header = QLabel("Notes:")
        header.setStyleSheet("font-size: 14px")
        self.i2cNote = QLineEdit()
        self.i2cNote.setMaxLength(105)
        self.i2cNote.setPlaceholderText("Enter notes here (105 characters max)")
        self.i2cNote.setStyleSheet("font-size: 14px")

        # Page Buttons
        next_btn = QPushButton("Save && Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)

        next_btn.clicked.connect(self.save_continue)
        return_btn.clicked.connect(lambda: i2c_stack.setCurrentIndex(2))
        
# Layout Configuration ----------------------------------------------------
        # Top Title Row
        H1.addStretch(1)
        H1.addWidget(radioTitle)
        # H1.addStretch(2)
        # H1.addWidget(radioTitle2)
        H1.addStretch(1)
        
        # Top Pass Row
        H2.addStretch(1)
        H2.addWidget(self.pass1)
        # H2.addStretch(2)
        # H2.addWidget(self.pass2)
        H2.addStretch(1)

        # Top Fail Row
        H3.addStretch(1)
        H3.addWidget(self.fail1)
        # H3.addStretch(2)
        # H3.addWidget(self.fail2)
        H3.addStretch(1)

        # Page Flip Buttons
        H7.addStretch(1)
        H7.addWidget(return_btn)
        H7.addStretch(28)
        H7.addWidget(next_btn)
        H7.addStretch(1)

        # Add all rows together in a vertical layout
        V1.addWidget(menu_title)
        V1.addStretch()
        V1.addWidget(test_btn, alignment=Qt.AlignCenter)
        V1.addStretch()
        V1.addWidget(self.direction)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addLayout(H2)
        V1.addLayout(H3)
        V1.addStretch()
        V1.addWidget(header)
        V1.addWidget(self.i2cNote)
        V1.addStretch()
        V1.addLayout(H7)

        self.setLayout(V1)

        i2c_stack.currentChanged.connect(self.loader)
        
# Fail/Pass Button Insurance Functions ------------------------------------------------       
    def pass1check(self):
        if self.pass1.isChecked():
            if self.failflag == 0:
                self.passflag = 1
            elif self.failflag == 1:
                chk = QMessageBox.question(self,"Change Confirmation",
                                           "Are you sure you want to edit I2C (GPIO 2,3)?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.passflag = 1 
                    self.failflag = 0
                else:
                    self.passflag = 0
                    self.failflag = 1
                    self.pass1.setChecked(False)
                    self.fail1.setChecked(True)
                    
    def fail1check(self):
        if self.fail1.isChecked():
            if self.passflag == 0:
                self.failflag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit I2C (GPIO 2,3)?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.failflag = 1
                    self.passflag = 0
                else:
                    self.failflag = 0
                    self.passflag = 1
                    self.fail1.setChecked(False)
                    self.pass1.setChecked(True)
                    
    # def pass2check(self):
    #     if self.pass2.isChecked():
    #         if self.fail2flag == 0:
    #             self.pass2flag = 1
    #         else:
    #             chk = QMessageBox.question(self,"Change Confirmation", 
    #                                        "Are you sure you want to edit Radio Title 2?", 
    #                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #             if chk == QMessageBox.Yes:
    #                 self.pass2flag = 1
    #                 self.fail2flag = 0
    #             else:
    #                 self.pass2flag = 0
    #                 self.fail2flag = 1
    #                 self.pass2.setChecked(False)
    #                 self.fail2.setChecked(True)
                    
    # def fail2check(self):
    #     if self.fail2.isChecked():
    #         if self.pass2flag == 0:
    #             self.fail2flag = 1
    #         else:
    #             chk = QMessageBox.question(self,"Change Confirmation", 
    #                                        "Are you sure you want to edit Radio Title 2?", 
    #                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #             if chk == QMessageBox.Yes:
    #                 self.fail2flag = 1
    #                 self.pass2flag = 0
    #             else:
    #                 self.fail2flag = 0
    #                 self.pass2flag = 1
    #                 self.fail2.setChecked(False)
    #                 self.pass2.setChecked(True)

    def test_function(self):
        
        self.direction.setText("<center>Running Test...</center>")
        QApplication.processEvents()
            
        self.pass1.setChecked(False)
        self.fail1.setChecked(False)
        # self.pass2.setChecked(False)
        # self.fail2.setChecked(False)

        i2c_file.test_i2c()        
        self.direction.setText("<center>Record the results here:</center>")

# JSON save/load ----------------------------------------------------------------------------------------
    def save_continue(self):
        savefile = "GUI_Test_Results.json"
        if os.path.exists(savefile):
            with open(savefile, "r") as f:
                data = json.load(f)
        else: 
            data = {}
            
        data["i2c_data"] = {
            "test": "I2C Communication",
            "i2c": "Pass" if self.pass1.isChecked() else "Fail" if self.fail1.isChecked() else "None",
#            "RadioTitle2": "Pass" if self.pass2.isChecked() else "Fail" if self.fail2.isChecked() else "None",
            "i2cNote": self.i2cNote.text()
        }
        
        with open(savefile, "w") as f:
            json.dump(data, f, indent=4)
            
        self.stack.setCurrentIndex(2)
            
    def load_settings(self):
        savefile = "GUI_Test_Results.json"
        if not os.path.exists(savefile):
            return
        
        with open(savefile, "r") as f:
            data = json.load(f)
            
        i2c = data.get("i2c_data", {})
        
        if i2c.get("i2c") == "Pass":
            self.pass1.setChecked(True)
        elif i2c.get("i2c") == "Fail":
            self.fail1.setChecked(True)
        elif i2c.get("i2c") == "None":
            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            
        # if i2c.get("RadioTitle2") == "Pass":
        #     self.pass2.setChecked(True)
        # elif i2c.get("RadioTitle2") == "Fail":
        #     self.fail2.setChecked(True)
        # elif i2c.get("RadioTitle2") == "None":
        #     self.pass2.setChecked(False)
        #     self.fail2.setChecked(False)
            
        self.i2cNote.setText(i2c.get("i2cNote"))

    def loader(self, i):
        if i == 3:
            self.load_settings()