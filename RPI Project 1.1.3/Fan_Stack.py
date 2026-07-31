from PyQt5.QtWidgets import ( QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel, QGridLayout,
    QLineEdit, QRadioButton, QHBoxLayout, QMessageBox,
    QButtonGroup, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QProcess
import platform, json, os, time

class Fan_Menu(QWidget):
    def __init__(self,stack):
        super().__init__()
        fanLayout = QGridLayout()

        fan_stack = QStackedWidget()

        fan_stack.addWidget(Fan_Step1(fan_stack,stack))
        fan_stack.addWidget(Fan_Step2(fan_stack))
        fan_stack.addWidget(Fan_Final(fan_stack,stack))
        fanLayout.addWidget(fan_stack)

        self.setLayout(fanLayout)

class Fan_Step1(QWidget):
    def __init__(self,fan_stack,stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       

        title = QLabel("Fan Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 1: Locate the fan connection on<br>"
                           "the Pi 5 and plug in the fan. The fan<br>"
                           "can be seen on the next page.<br>")
        direction.setFixedSize(360,260)
        direction.setStyleSheet("font-size: 18px")

        # Image Setup
        image1_holder = QLabel()
        i1pixmap = QPixmap("images/RPI5_Fan.jpg")
        i1pixmap = i1pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image1_holder.setPixmap(i1pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: fan_stack.setCurrentIndex(1))
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

class Fan_Step2(QWidget):
    def __init__(self,fan_stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       
        title = QLabel("Fan Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 2: Once the fan is plugged in, run the <br>" 
                           "test on the next page. The fan should spin <br>"
                           "for a few seconds and then stop. Wait until <br>"
                           "the fan stops spinning to continue.")
        
        #label top/bottom in the image----------------------------------------------------
        
        direction.setFixedSize(360,260)
        direction.setStyleSheet("font-size: 18px")

        #Image Setup
        image2_holder = QLabel()
        i2pixmap = QPixmap("images/fan_plugged.jpg")
        i2pixmap = i2pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image2_holder.setPixmap(i2pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: fan_stack.setCurrentIndex(2))
        return_btn.clicked.connect(lambda: fan_stack.setCurrentIndex(0))

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

class Fan_Final(QWidget):
    def __init__(self,fan_stack,stack):
        super().__init__()

        self.stack = stack

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()

# Widget Configurations, Button Connections ------------------------------------------------------
        menu_title = QLabel("Fan Menu") 
        menu_title.setStyleSheet("font-size: 20px; font-weight: " 
                                 "bold; text-decoration: underline")
        
        test_btn = QPushButton("Run Test")
        test_btn.setStyleSheet("font-size: 14px")
        self.test = QProcess(self)
        test_btn.clicked.connect(self.terminal_command)

        self.direction = QLabel("<center>Record the results here:</center>") 
        self.direction.setStyleSheet("font-size: 16px; text-decoration: underline")
        
        # General Radio Box
        radioTitle = QLabel("Fan is Functional?") 
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
        self.fanNote = QLineEdit()
        self.fanNote.setMaxLength(105)
        self.fanNote.setPlaceholderText("Enter notes here (105 characters max)")
        self.fanNote.setStyleSheet("font-size: 14px")

        # Page Buttons
        next_btn = QPushButton("Save && Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)

        next_btn.clicked.connect(self.save_continue)
        return_btn.clicked.connect(lambda: fan_stack.setCurrentIndex(1))

        # Page Flip Buttons
        H1.addStretch(1)
        H1.addWidget(return_btn)
        H1.addStretch(28)
        H1.addWidget(next_btn)
        H1.addStretch(1)

        # Add all rows together in a vertical layout
        V1.addWidget(menu_title)
        V1.addStretch()
        V1.addWidget(test_btn, alignment = Qt.AlignCenter)        
        V1.addStretch()
        V1.addWidget(self.direction)
        V1.addStretch()
        V1.addWidget(radioTitle, alignment=Qt.AlignCenter)
        V1.addWidget(self.pass1, alignment=Qt.AlignCenter)
        V1.addWidget(self.fail1, alignment=Qt.AlignCenter)
        V1.addStretch()
        V1.addWidget(header)
        V1.addWidget(self.fanNote)
        V1.addStretch()
        V1.addLayout(H1)

        self.setLayout(V1)

        fan_stack.currentChanged.connect(self.loader)
        
# Command Terminal Test Code --------------------------------------------
    def terminal_command(self):
        os = platform.system()
        
        if os == "Windows": #For debugging GUI 
            self.terminal = "cmd.exe"
            command = ["/c", f"start cmd.exe /k set os"]
            self.test.setWorkingDirectory("C:\\")
            self.test.start(self.terminal,command)
        elif os == "Linux": #For Testing on Pi
            self.direction.setText("<center>Running Test...</center>")
            QApplication.processEvents()
            self.terminal = "x-terminal-emulator"
            command = ["-e", "bash", "-c", f"stress-ng --cpu 4 --timeout 5; exec bash"]
            self.test.start(self.terminal,command)
            time.sleep(5)
            self.direction.setText("<center>Record the results here:</center>")
            
        
# Fail/Pass Button Insurance Functions ------------------------------------------------       
    def pass1check(self):
        if self.pass1.isChecked():
            if self.failflag == 0:
                self.passflag = 1
            elif self.failflag == 1:
                chk = QMessageBox.question(self,"Change Confirmation",
                                           "Are you sure you want to edit Fan is Functional?", 
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
                                           "Are you sure you want to edit Fan is Functional?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.failflag = 1
                    self.passflag = 0
                else:
                    self.failflag = 0
                    self.passflag = 1
                    self.fail1.setChecked(False)
                    self.pass1.setChecked(True)

# asld;kfj -------------------------------------------------------------------------------------

    def save_continue(self):
        savefile = "GUI_Test_Results.json"
        if os.path.exists(savefile):
            with open(savefile, "r") as f:
                data = json.load(f)
        else: 
            data = {}
            
        data["fan_data"] = {
            "test": "Fan Connection",
            "functional": "Pass" if self.pass1.isChecked() else "Fail" if self.fail1.isChecked() else "None",
            "fanNote": self.fanNote.text()
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
            
        fan = data.get("fan_data", {})
        
        if fan.get("functional") == "Pass":
            self.pass1.setChecked(True)
        elif fan.get("functional") == "Fail":
            self.fail1.setChecked(True)
        elif fan.get("functional") == "None":
            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            
        self.fanNote.setText(fan.get("fanNote"))

    def loader(self, i):
        if i == 2:
            self.load_settings()