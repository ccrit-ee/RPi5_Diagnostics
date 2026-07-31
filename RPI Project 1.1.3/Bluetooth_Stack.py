
from PyQt5.QtWidgets import ( QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel, QGridLayout,
    QLineEdit, QRadioButton, QHBoxLayout, QMessageBox,
    QButtonGroup,QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QProcess

import platform, json, os

class Bluetooth_Menu(QWidget):
    def __init__(self,stack):
        super().__init__()
        btLayout = QGridLayout()

        bt_stack = QStackedWidget()

        bt_stack.addWidget(Bluetooth_Step1(bt_stack,stack))
        # bt_stack.addWidget(Bluetooth_Step2(bt_stack))
        # bt_stack.addWidget(Bluetooth_Step3(bt_stack))
        bt_stack.addWidget(Bluetooth_Final(bt_stack,stack))
        btLayout.addWidget(bt_stack)

        self.setLayout(btLayout)

class Bluetooth_Step1(QWidget):
    def __init__(self,bt_stack,stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       

        title = QLabel("Bluetooth Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 1: To test the bluetooth ensure   <br>"
                           "there is a phone or other device with  <br>"
                           "bluetooth enabled nearby. Run the test <br>"
                           "on the next page. The results should   <br>"
                           "be something similar to the image on   <br>"
                           "the right.")
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
        
        next_btn.clicked.connect(lambda: bt_stack.setCurrentIndex(1))
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

# class Bluetooth_Step2(QWidget):
#     def __init__(self,bt_stack):
#         super().__init__()

#         V1 = QVBoxLayout()
#         H1 = QHBoxLayout()
#         H2 = QHBoxLayout()
       
#         title = QLabel("Bluetooth Menu")
#         title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

#         direction = QLabel("Step 2: ------------------------------------<br>" 
#                            "--------------------------------------------<br>"
#                            "-------------------------------------------.")
        
#         #label top/bottom in the image----------------------------------------------------
        
#         direction.setFixedSize(360,500)
#         direction.setStyleSheet("font-size: 18px")

#         #Image Setup
#         image2_holder = QLabel()
#         i2pixmap = QPixmap("images/placeholder.png")
#         i2pixmap = i2pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
#         image2_holder.setPixmap(i2pixmap)

#         # Page Buttons
#         next_btn = QPushButton("Continue")
#         next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
#         next_btn.setFixedSize(125,42)

#         return_btn = QPushButton("Return")
#         return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
#         return_btn.setFixedSize(125,42)
        
#         next_btn.clicked.connect(lambda: bt_stack.setCurrentIndex(2))
#         return_btn.clicked.connect(lambda: bt_stack.setCurrentIndex(0))

#         # Step and Image Row
#         H1.addStretch()
#         H1.addWidget(direction)
#         H1.addStretch()
#         H1.addWidget(image2_holder)
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

# class Bluetooth_Step3(QWidget):
#     def __init__(self,bt_stack):
#         super().__init__()

#         V1 = QVBoxLayout()
#         H1 = QHBoxLayout()
#         H2 = QHBoxLayout()

#         title = QLabel("Bluetooth Menu")
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

#         next_btn.clicked.connect(lambda: bt_stack.setCurrentIndex(3))
#         return_btn.clicked.connect(lambda: bt_stack.setCurrentIndex(1))

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

class Bluetooth_Final(QWidget):
    def __init__(self,bt_stack,stack):
        super().__init__()

        self.stack = stack

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
        H3 = QHBoxLayout()
        H7 = QHBoxLayout()

# Widget Configurations, Button Connections ------------------------------------------------------
        menu_title = QLabel("Bluetooth Menu") 
        menu_title.setStyleSheet("font-size: 20px; font-weight: " 
                                 "bold; text-decoration: underline")
        
        test_btn = QPushButton("Run Test")
        test_btn.setStyleSheet("font-size: 14px")
        self.test = QProcess(self)
        test_btn.clicked.connect(self.terminal_command)

        self.direction = QLabel("<center>Record the results here:</center>") 
        self.direction.setStyleSheet("font-size: 16px; text-decoration: underline")
        
        # General Radio Box
        radioTitle = QLabel("Bluetooth Devices Paired?") 
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

        # Notes
        header = QLabel("Notes:")
        header.setStyleSheet("font-size: 14px")
        self.btNote = QLineEdit()
        self.btNote.setMaxLength(105)
        self.btNote.setPlaceholderText("Enter notes here (105 characters max)")
        self.btNote.setStyleSheet("font-size: 14px")

        # Page Buttons
        next_btn = QPushButton("Save && Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)

        next_btn.clicked.connect(self.save_continue)
        return_btn.clicked.connect(lambda: bt_stack.setCurrentIndex(0))
        
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
        # V1.addWidget(test_btn, alignment = Qt.AlignCenter)
        # V1.addStretch()
        V1.addWidget(self.direction)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addLayout(H2)
        V1.addLayout(H3)
        V1.addStretch()
        V1.addWidget(header)
        V1.addWidget(self.btNote)
        V1.addStretch()
        V1.addLayout(H7)

        self.setLayout(V1)

        bt_stack.currentChanged.connect(self.loader)
        
#Command Terminal Test Code -----------------------------------------        
    def terminal_command(self):
        os = platform.system()
        
        if os == "Windows": #For debugging GUI 
            self.terminal = "cmd.exe"
            command = ["/c", f"start cmd.exe /k set os"]
            self.test.setWorkingDirectory("C:\\")
            self.test.start(self.terminal,command)
        elif os == "Linux": #For Testing on Pi
            self.terminal = "x-terminal-emulator"
            command = ["-e", "bash", "-c", f"bluetoothctl; exec bash"]
            self.test.start(self.terminal,command)

            self.direction.setText("<center>Running Test...</center>")
            QApplication.processEvents()

            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            #put test code here
            self.direction.setText("<center>Record the results here:</center>")
        
# Fail/Pass Button Insurance Functions ------------------------------------------------       
    def pass1check(self):
        if self.pass1.isChecked():
            if self.failflag == 0:
                self.passflag = 1
            elif self.failflag == 1:
                chk = QMessageBox.question(self,"Change Confirmation",
                                           "Are you sure you want to edit Bluetooth Devices Detected?", 
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
                                           "Are you sure you want to edit Bluetooth Devices Detected?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.failflag = 1
                    self.passflag = 0
                else:
                    self.failflag = 0
                    self.passflag = 1
                    self.fail1.setChecked(False)
                    self.pass1.setChecked(True)


# JSON save/load ----------------------------------------------------------------------------------------
    def save_continue(self):
        savefile = "GUI_Test_Results.json"
        if os.path.exists(savefile):
            with open(savefile, "r") as f:
                data = json.load(f)
        else: 
            data = {}
            
        data["bt_data"] = {
            "test": "Bluetooth Pairing",
            "connection": "Pass" if self.pass1.isChecked() else "Fail" if self.fail1.isChecked() else "None",
            # "RadioTitle2": "Pass" if self.pass2.isChecked() else "Fail" if self.fail2.isChecked() else "None",
            # "RadioTitle3": "Pass" if self.pass3.isChecked() else "Fail" if self.fail3.isChecked() else "None",
            "btNote": self.btNote.text()
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
            
        bt = data.get("bt_data", {})
        
        if bt.get("connection") == "Pass":
            self.pass1.setChecked(True)
        elif bt.get("connection") == "Fail":
            self.fail1.setChecked(True)
        elif bt.get("connection") == "None":
            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            
        # if bt.get("RadioTitle2") == "Pass":
        #     self.pass2.setChecked(True)
        # elif bt.get("RadioTitle2") == "Fail":
        #     self.fail2.setChecked(True)
        # elif bt.get("RadioTitle2") == "None":
        #     self.pass2.setChecked(False)
        #     self.fail2.setChecked(False)

        # if bt.get("RadioTitle3") == "Pass":
        #     self.pass3.setChecked(True)
        # elif bt.get("RadioTitle3") == "Fail":
        #     self.fail3.setChecked(True)
        # elif bt.get("RadioTitle3") == "None":
        #     self.pass3.setChecked(False)
        #     self.fail3.setChecked(False)
            
        self.btNote.setText(bt.get("btNote"))

    def loader(self,i):
        if i == 1:
            self.load_settings()

