from PyQt5.QtWidgets import ( QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel, QGridLayout,
    QLineEdit, QRadioButton, QHBoxLayout, QMessageBox,
    QButtonGroup,QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QProcess
import json, os, subprocess, platform

class WIFI_Menu(QWidget):
    def __init__(self,stack):
        super().__init__()
        wifiLayout = QGridLayout()

        wifi_stack = QStackedWidget()

        wifi_stack.addWidget(WIFI_Step1(wifi_stack,stack))
        wifi_stack.addWidget(WIFI_Step2(wifi_stack))
        # wifi_stack.addWidget(WIFI_Step3(wifi_stack))
        wifi_stack.addWidget(WIFI_Final(wifi_stack,stack))
        wifiLayout.addWidget(wifi_stack)

        self.setLayout(wifiLayout)

class WIFI_Step1(QWidget):
    def __init__(self,wifi_stack,stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       

        title = QLabel("WIFI Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 1: Connect to the internet by clicking<br>"
                           "the WIFI icon in the top right of the      <br>"
                           "desktop and select the appropriate network.<br>")
        direction.setFixedSize(360,260)
        direction.setStyleSheet("font-size: 18px")

        # Image Setup
        image1_holder = QLabel()
        i1pixmap = QPixmap("images/RPi5_WIFI.png")
        i1pixmap = i1pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image1_holder.setPixmap(i1pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: wifi_stack.setCurrentIndex(1))
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

class WIFI_Step2(QWidget):
    def __init__(self,wifi_stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       
        title = QLabel("WIFI Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 2: Press the test button on the next   <br>" 
                           "page and a command terminal will open with  <br>"
                           "results similar to the ones in the image to <br>"
                           "the right. To pass, 4 packets must be     <br>"
                           "successfuly transmit and recieved with 0% <br>"
                           "packet loss.")
        
        #label top/bottom in the image----------------------------------------------------
        
        direction.setFixedSize(360,260)
        direction.setStyleSheet("font-size: 18px")

        #Image Setup
        image2_holder = QLabel()
        i2pixmap = QPixmap("images/WIFI_Terminal.png")
        i2pixmap = i2pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image2_holder.setPixmap(i2pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: wifi_stack.setCurrentIndex(2))
        return_btn.clicked.connect(lambda: wifi_stack.setCurrentIndex(0))

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

# class WIFI_Step3(QWidget):
#     def __init__(self,wifi_stack):
#         super().__init__()

#         V1 = QVBoxLayout()
#         H1 = QHBoxLayout()
#         H2 = QHBoxLayout()

#         title = QLabel("WIFI Menu")
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

#         next_btn.clicked.connect(lambda: wifi_stack.setCurrentIndex(3))
#         return_btn.clicked.connect(lambda: wifi_stack.setCurrentIndex(1))

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

class WIFI_Final(QWidget):
    def __init__(self,wifi_stack,stack):
        super().__init__()

        self.stack = stack

        V1 = QVBoxLayout()
        V2 = QVBoxLayout()
        V3 = QVBoxLayout()
        V4 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
        H3 = QHBoxLayout()
        H7 = QHBoxLayout()

# Widget Configurations, Button Connections ------------------------------------------------------
        menu_title = QLabel("WIFI Menu") 
        menu_title.setStyleSheet("font-size: 20px; font-weight: " 
                                 "bold; text-decoration: underline")

        test_btn = QPushButton("Run Test")
        test_btn.setStyleSheet("font-size: 14px")
        self.test = QProcess(self)
        test_btn.clicked.connect(self.terminal_command)

        self.direction = QLabel("<center>Record the results here:</center>") 
        self.direction.setStyleSheet("font-size: 16px; text-decoration: underline")
        
        # General Radio Box
        self.radioTitle = QLabel("   Transmit:") 
        self.radioTitle.setStyleSheet("font-size: 14px")
        self.pass1 = QRadioButton("Pass") 
        self.pass1.setStyleSheet("font-size: 14px")
        self.passflag = 0 
        self.fail1 = QRadioButton("Fail   ") 
        self.fail1.setStyleSheet("font-size: 14px")
        self.failflag = 0 
        
        self.pass1.toggled.connect(self.pass1check)
        self.fail1.toggled.connect(self.fail1check)
        
        radio1_opt = QButtonGroup(self)
        radio1_opt.addButton(self.pass1)
        radio1_opt.addButton(self.fail1)
        
        # General Radio Box
        self.radioTitle2 = QLabel("    Received:") 
        self.radioTitle2.setStyleSheet("font-size: 14px")
        self.pass2 = QRadioButton("Pass") 
        self.pass2.setStyleSheet("font-size: 14px")
        self.pass2flag = 0 
        self.fail2 = QRadioButton("Fail   ") 
        self.fail2.setStyleSheet("font-size: 14px")
        self.fail2flag = 0 
        
        self.pass2.toggled.connect(self.pass2check)
        self.fail2.toggled.connect(self.fail2check)
        
        radio2_opt = QButtonGroup(self)
        radio2_opt.addButton(self.pass2)
        radio2_opt.addButton(self.fail2)

        # General Radio Box
        self.radioTitle3 = QLabel("Packet Loss:") 
        self.radioTitle3.setStyleSheet("font-size: 14px")
        self.pass3 = QRadioButton("Pass") 
        self.pass3.setStyleSheet("font-size: 14px")
        self.pass3flag = 0 
        self.fail3 = QRadioButton("Fail ") 
        self.fail3.setStyleSheet("font-size: 14px")
        self.fail3flag = 0 
        
        self.pass3.toggled.connect(self.pass2check)
        self.fail3.toggled.connect(self.fail2check)
        
        radio3_opt = QButtonGroup(self)
        radio3_opt.addButton(self.pass3)
        radio3_opt.addButton(self.fail3)

        # Notes
        header = QLabel("Notes:")
        header.setStyleSheet("font-size: 14px")
        self.wifiNote = QLineEdit()
        self.wifiNote.setMaxLength(105)
        self.wifiNote.setPlaceholderText("Enter notes here (105 characters max)")
        self.wifiNote.setStyleSheet("font-size: 14px")

        # Page Buttons
        next_btn = QPushButton("Save && Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)

        next_btn.clicked.connect(self.save_continue)
        return_btn.clicked.connect(lambda: wifi_stack.setCurrentIndex(1))
        
# Layout Configuration ----------------------------------------------------
        # Top Title Row
        H1.addStretch(1)
        H1.addWidget(self.radioTitle)
        H1.addStretch(1)
        H1.addWidget(self.radioTitle2)
        H1.addStretch(1)
        H1.addWidget(self.radioTitle3)
        H1.addStretch(1)
        
        # Top Pass Row
        H2.addStretch(1)
        H2.addWidget(self.pass1)
        H2.addStretch(1)
        H2.addWidget(self.pass2)
        H2.addStretch(1)
        H2.addWidget(self.pass3)
        H2.addStretch(1)

        # Top Fail Row
        H3.addStretch(1)
        H3.addWidget(self.fail1)
        H3.addStretch(1)
        H3.addWidget(self.fail2)
        H3.addStretch(1)
        H3.addWidget(self.fail3)
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
        V1.addWidget(test_btn, alignment = Qt.AlignCenter)        
        V1.addStretch()
        V1.addWidget(self.direction)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addLayout(H2)
        V1.addLayout(H3)
        V1.addStretch()
        V1.addWidget(header)
        V1.addWidget(self.wifiNote)
        V1.addStretch()
        V1.addLayout(H7)

        self.setLayout(V1)

        wifi_stack.currentChanged.connect(self.loader)

# Command Terminal Test Code --------------------------------------------
    def terminal_command(self):
        os = platform.system()

        self.pass1.setChecked(False)
        self.fail1.setChecked(False)

        
        if os == "Windows": #For debugging GUI 
            self.terminal = "cmd.exe"
            command = ["/c", f"start cmd.exe /k set os"]
            self.test.setWorkingDirectory("C:\\")
            self.test.start(self.terminal,command)
        elif os == "Linux": #For Testing on Pi
            self.direction.setText("<center>Running Test...</center>")
            QApplication.processEvents()

            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            self.pass2.setChecked(False)
            self.fail2.setChecked(False)
            self.pass3.setChecked(False)
            self.fail3.setChecked(False)
            self.radioTitle.setText("   Transmit:")
            self.radioTitle2.setText("    Received:")
            self.radioTitle3.setText("Packet Loss:")

            self.terminal = "x-terminal-emulator"
            command = ["-e", "bash", "-c", f"ping -c 4 google.com; exec bash"]
            self.test.start(self.terminal,command)
            bgtest = subprocess.run(["ping","-c", "4", "google.com"], capture_output=True, text=True)

            for line in bgtest.stdout.splitlines():
                if "transmitted" in line and "received" in line:
                    self.radioTitle.setText(f"   Transmit: {line.split()[0]}")
                    self.radioTitle2.setText(f"    Received: {line.split()[3]}")
                    self.radioTitle3.setText(f"Packet Loss: {line.split()[5]}")

            if "4 packets transmitted" in bgtest.stdout:
                self.pass1.setChecked(True)
            else:
                self.fail1.setChecked(True)

            if "4 received" in bgtest.stdout:
                self.pass2.setChecked(True)
            else:
                self.fail2.setChecked(True)

            if " 0% packet loss" in bgtest.stdout:
                self.pass3.setChecked(True)
            else: 
                self.fail3.setChecked(True)

            self.direction.setText("<center>Record the results here:</center>")
        
# Fail/Pass Button Insurance Functions ------------------------------------------------       
    def pass1check(self):
        if self.pass1.isChecked():
            if self.failflag == 0:
                self.passflag = 1
            elif self.failflag == 1:
                chk = QMessageBox.question(self,"Change Confirmation",
                                           "Are you sure you want to edit Packets Transmit?", 
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
                                           "Are you sure you want to edit Packets Transmit?",
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
                                           "Are you sure you want to edit Received?", 
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
                                           "Are you sure you want to edit Received?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.fail2flag = 1
                    self.pass2flag = 0
                else:
                    self.fail2flag = 0
                    self.pass2flag = 1
                    self.fail2.setChecked(False)
                    self.pass2.setChecked(True)

    def pass3check(self):
        if self.pass3.isChecked():
            if self.fail3flag == 0:
                self.pass3flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit 0% Packet Loss?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.pass3flag = 1
                    self.fail3flag = 0
                else:
                    self.pass3flag = 0
                    self.fail3flag = 1
                    self.pass3.setChecked(False)
                    self.fail3.setChecked(True)
                    
    def fail3check(self):
        if self.fail3.isChecked():
            if self.pass3flag == 0:
                self.fail3flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit 0% Packet Loss?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.fail3flag = 1
                    self.pass3flag = 0
                else:
                    self.fail3flag = 0
                    self.pass3flag = 1
                    self.fail3.setChecked(False)
                    self.pass3.setChecked(True)

# JSON save/load ----------------------------------------------------------------------------------------------                    

    def save_continue(self):
        savefile = "GUI_Test_Results.json"
        if os.path.exists(savefile):
            with open(savefile, "r") as f:
                data = json.load(f)
        else: 
            data = {}
            
        data["wifi_data"] = {
            "test": "WIFI",
            "transmit": "Pass" if self.pass1.isChecked() else "Fail" if self.fail1.isChecked() else "None",
            "received": "Pass" if self.pass2.isChecked() else "Fail" if self.fail2.isChecked() else "None",
            "packet loss": "Pass" if self.pass3.isChecked() else "Fail" if self.fail3.isChecked() else "None",
            "wifiNote": self.wifiNote.text()
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
            
        wifi = data.get("wifi_data", {})
        
        if wifi.get("transmit") == "Pass":
            self.pass1.setChecked(True)
        elif wifi.get("transmit") == "Fail":
            self.fail1.setChecked(True)
        elif wifi.get("transmit") == "None":
            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            
        if wifi.get("received") == "Pass":
            self.pass2.setChecked(True)
        elif wifi.get("received") == "Fail":
            self.fail2.setChecked(True)
        elif wifi.get("received") == "None":
            self.pass2.setChecked(False)
            self.fail2.setChecked(False)

        if wifi.get("packet loss") == "Pass":
            self.pass3.setChecked(True)
        elif wifi.get("packet loss") == "Fail":
            self.fail3.setChecked(True)
        elif wifi.get("packet loss") == "None":
            self.pass3.setChecked(False)
            self.fail3.setChecked(False)
            
        self.wifiNote.setText(wifi.get("wifiNote"))

    def loader(self, i):
        if i == 2:
            self.load_settings()