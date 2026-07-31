from PyQt5.QtWidgets import ( QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel, QGridLayout,
    QLineEdit, QRadioButton, QHBoxLayout, QMessageBox,
    QButtonGroup)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QProcess
import platform
import json
import os


class MicroHDMI_Menu(QWidget):
    def __init__(self,stack):
        super().__init__()
        mhdmiLayout = QGridLayout()

        mhdmi_stack = QStackedWidget()

        mhdmi_stack.addWidget(MicroHDMI_Step1(mhdmi_stack,stack))
        mhdmi_stack.addWidget(MicroHDMI_Step2(mhdmi_stack))
        #mhdmi_stack.addWidget(MicroHDMI_Step3(mhdmi_stack))
        mhdmi_stack.addWidget(MicroHDMI_Final(mhdmi_stack,stack))
        mhdmiLayout.addWidget(mhdmi_stack)

        self.setLayout(mhdmiLayout)

class MicroHDMI_Step1(QWidget):
    def __init__(self,mhdmi_stack,stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       
       

        title = QLabel("Micro-HDMI Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 1: Position yourself near a monitor and <br>"
                           "locate the micro-HDMI ports on the board.<br>"
                           "They will be labeled HDMI0 and HDMI1.<br>")
        direction.setFixedSize(360,260)
        direction.setStyleSheet("font-size: 18px")

        # Image Setup
        image1_holder = QLabel()
        i1pixmap = QPixmap("images/mhdmi_ports.jpg")
        i1pixmap = i1pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image1_holder.setPixmap(i1pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: mhdmi_stack.setCurrentIndex(1))
        return_btn.clicked.connect(lambda: stack.setCurrentIndex(3))

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

class MicroHDMI_Step2(QWidget):
    def __init__(self,mhdmi_stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       
        title = QLabel("Micro-HDMI Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 2: Begin by plugging in the micro-HDMI<br>" 
                           "to HDMI adapter into the monitor and plug <br>" 
                           "the other end into HDMI0. If the port is <br> " 
                           "working, then the monitor will display the <br>"
                           "Pi 5 desktop screen. Repeat this for HDMI1 <br>"
                           "and record results on the next page.<br>")
        
        #label top/bottom in the image----------------------------------------------------
        
        direction.setFixedSize(360,260)
        direction.setStyleSheet("font-size: 18px")

        #Image Setup
        image2_holder = QLabel()
        i2pixmap = QPixmap("images/rpi_desktop.png")
        i2pixmap = i2pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image2_holder.setPixmap(i2pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: mhdmi_stack.setCurrentIndex(2))
        return_btn.clicked.connect(lambda: mhdmi_stack.setCurrentIndex(0))

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

# class MicroHDMI_Step3(QWidget):
#     def __init__(self,mhdmi_stack):
#         super().__init__()

#         V1 = QVBoxLayout()
#         H1 = QHBoxLayout()
#         H2 = QHBoxLayout()

#         title = QLabel("Micro-HDMI Menu")
#         title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

#         direction = QLabel("Step 3: ----------------------------------<br>" 
#                            "------------------------------------------<br>"
#                            "----------------------------------------- <br>")
#         direction.setFixedSize(360,500)
#         direction.setStyleSheet("font-size: 18px")
        
#         # Image Setup
#         image3_holder = QLabel()
#         i3pixmap = QPixmap("images/placeholder.png")
#         i3pixmap = i3pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
#         image3_holder.setPixmap(i3pixmap)

#         # Page Buttons
#         next_btn = QPushButton("Continue")
#         next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
#         next_btn.setFixedSize(125,42)

#         return_btn = QPushButton("Return")
#         return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
#         return_btn.setFixedSize(125,42)

#         next_btn.clicked.connect(lambda: mhdmi_stack.setCurrentIndex(3))
#         return_btn.clicked.connect(lambda: mhdmi_stack.setCurrentIndex(1))

#         # Step and Image Row
#         H1.addStretch()
#         H1.addWidget(direction)
#         H1.addStretch()
#         H1.addWidget(image3_holder)
#         H1.addStretch()

#         # Page Button Row
#         H2.addStretch(1)
#         H2.addWidget(return_btn)
#         H2.addStretch(28)
#         H2.addWidget(next_btn)
#         H2.addStretch(1)

#         # Combined Layout
#         V1.addWidget(title)
#         V1.addStretch()
#         V1.addLayout(H1)
#         V1.addStretch()
#         V1.addLayout(H2)
#         self.setLayout(V1)

class MicroHDMI_Final(QWidget):
    def __init__(self,mhdmi_stack,stack):
        super().__init__()
        
        self.stack = stack

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
        H3 = QHBoxLayout()
        H7 = QHBoxLayout()

# Widget Configurations, Button Connections ------------------------------------------------------
        menu_title = QLabel("Micro-HDMI Menu") 
        menu_title.setStyleSheet("font-size: 20px; font-weight: " 
                                 "bold; text-decoration: underline")

        direction = QLabel("<center>Record the results here:</center>") 
        direction.setStyleSheet("font-size: 16px; text-decoration: underline")
        
        # General Radio Box
        radioTitle = QLabel("HDMI0 Displays?") 
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
        
        # General Radio Box
        radioTitle2 = QLabel("HDMI1 Displays?") 
        radioTitle2.setStyleSheet("font-size: 14px")
        self.pass2 = QRadioButton("Pass") 
        self.pass2.setStyleSheet("font-size: 14px")
        self.pass2flag = 0 
        self.fail2 = QRadioButton("Fail") 
        self.fail2.setStyleSheet("font-size: 14px")
        self.fail2flag = 0 
        
        self.pass2.toggled.connect(self.pass2check)
        self.fail2.toggled.connect(self.fail2check)
        
        radio2_opt = QButtonGroup(self)
        radio2_opt.addButton(self.pass2)
        radio2_opt.addButton(self.fail2)

        # Notes
        header = QLabel("Notes:")
        header.setStyleSheet("font-size: 14px")
        self.mhdmiNote = QLineEdit()
        self.mhdmiNote.setMaxLength(105)
        self.mhdmiNote.setPlaceholderText("Enter notes here (105 characters max)")
        self.mhdmiNote.setStyleSheet("font-size: 14px")

        # Page Buttons
        next_btn = QPushButton("Save && Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)

       # next_btn.clicked.connect(lambda: stack.setCurrentIndex(3))
        next_btn.clicked.connect(self.save_continue)
        return_btn.clicked.connect(lambda: mhdmi_stack.setCurrentIndex(1))
        
# Layout Configuration ----------------------------------------------------
        # Top Title Row
        H1.addStretch(1)
        H1.addWidget(radioTitle)
        H1.addStretch(2)
        H1.addWidget(radioTitle2)
        H1.addStretch(1)
        
        # Top Pass Row
        H2.addStretch(1)
        H2.addWidget(self.pass1)
        H2.addStretch(2)
        H2.addWidget(self.pass2)
        H2.addStretch(1)

        # Top Fail Row
        H3.addStretch(1)
        H3.addWidget(self.fail1)
        H3.addStretch(2)
        H3.addWidget(self.fail2)
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
        V1.addWidget(direction)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addLayout(H2)
        V1.addLayout(H3)
        V1.addStretch()
        V1.addWidget(header)
        V1.addWidget(self.mhdmiNote)
        V1.addStretch()
        V1.addLayout(H7)

        self.setLayout(V1)
        
        mhdmi_stack.currentChanged.connect(self.loader)
        
# Fail/Pass Button Insurance Functions ------------------------------------------------       
    def pass1check(self):
        if self.pass1.isChecked():
            if self.failflag == 0:
                self.passflag = 1
            elif self.failflag == 1:
                chk = QMessageBox.question(self,"Change Confirmation",
                                           "Are you sure you want to edit HDMI0 Display?", 
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
                                           "Are you sure you want to edit HDMI0 Display?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.failflag = 1
                    self.passflag = 0
                else:
                    self.failflag = 0
                    self.passflag = 1
                    self.fail1.setChecked(False)
                    self.pass1.setChecked(True)
                    
    def pass2check(self):
        if self.pass2.isChecked():
            if self.fail2flag == 0:
                self.pass2flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit HDMI1 Display?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.pass2flag = 1
                    self.fail2flag = 0
                else:
                    self.pass2flag = 0
                    self.fail2flag = 1
                    self.pass2.setChecked(False)
                    self.fail2.setChecked(True)
                    
    def fail2check(self):
        if self.fail2.isChecked():
            if self.pass2flag == 0:
                self.fail2flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit HDMI1 Display?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.fail2flag = 1
                    self.pass2flag = 0
                else:
                    self.fail2flag = 0
                    self.pass2flag = 1
                    self.fail2.setChecked(False)
                    self.pass2.setChecked(True)
# JSON save/load ----------------------------------------------------------------------------------------                    
    def save_continue(self):
        savefile = "GUI_Test_Results.json"
        if os.path.exists(savefile):
            with open(savefile, "r") as f:
                data = json.load(f)
        else: 
            data = {}
            
        data["micro_HDMI"] = {
            "test": "Micro-HDMI Ports",
            "hdmi0": "Pass" if self.pass1.isChecked() else "Fail" if self.fail1.isChecked() else "None",
            "hdmi1": "Pass" if self.pass2.isChecked() else "Fail" if self.fail2.isChecked() else "None",
            "mhdmiNote": self.mhdminote.text()
        }
        
        with open(savefile, "w") as f:
            json.dump(data, f, indent=4)
            
        self.stack.setCurrentIndex(3)
        
    def load_settings(self):
        savefile = "GUI_Test_Results.json"
        if not os.path.exists(savefile):
            return
        
        with open(savefile, "r") as f:
            data = json.load(f)
            
        mhdmi = data.get("micro_HDMI", {})
        
        if mhdmi.get("hdmi0") == "Pass":
            self.pass1.setChecked(True)
        elif mhdmi.get("hdmi0") == "Fail":
            self.fail1.setChecked(True)
        elif mhdmi.get("hdmi0") == "None":
            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            
        if mhdmi.get("hdmi1") == "Pass":
            self.pass2.setChecked(True)
        elif mhdmi.get("hdmi1") == "Fail":
            self.fail2.setChecked(True)
        elif mhdmi.get("hdmi1") == "None":
            self.pass2.setChecked(False)
            self.fail2.setChecked(False)
            
        self.mhdmiNote.setText(mhdmi.get("mhdmiNote"))

    def loader(self, i):
        if i == 2:
            self.load_settings()