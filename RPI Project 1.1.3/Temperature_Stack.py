from PyQt5.QtWidgets import ( QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel, QGridLayout,
    QLineEdit, QRadioButton, QHBoxLayout, QMessageBox,
    QButtonGroup, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QProcess
import platform, time, subprocess, json, os

class Temperature_Menu(QWidget):
    def __init__(self,stack):
        super().__init__()
        hsLayout = QGridLayout()

        hs_stack = QStackedWidget()

        hs_stack.addWidget(Temperature_Step1(hs_stack,stack))
        # hs_stack.addWidget(Temperature_Step2(hs_stack))
        hs_stack.addWidget(Temperature_Final(hs_stack,stack))
        hsLayout.addWidget(hs_stack)

        self.setLayout(hsLayout)

class Temperature_Step1(QWidget):
    def __init__(self,hs_stack,stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       

        title = QLabel("Temperature Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 1: This test will check the CPU<br>"
                           "temp to ensure that it is within the<br>"
                           "expected ranges idling and under stress.<br>" 
                           "Expected temperatures are below 55'C when<br>" 
                           "idling and below 65'C when stressed.")
        direction.setFixedSize(360,260)
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
        
        next_btn.clicked.connect(lambda: hs_stack.setCurrentIndex(1))
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

# class Temperature_Step2(QWidget):
#     def __init__(self,hs_stack):
#         super().__init__()

#         V1 = QVBoxLayout()
#         H1 = QHBoxLayout()
#         H2 = QHBoxLayout()
       
#         title = QLabel("Temperature Menu")
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
        
#         next_btn.clicked.connect(lambda: hs_stack.setCurrentIndex(2))
#         return_btn.clicked.connect(lambda: hs_stack.setCurrentIndex(0))

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

class Temperature_Final(QWidget):
    def __init__(self,hs_stack,stack):
        super().__init__()
        
        self.stack = stack

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
        H3 = QHBoxLayout()
        H7 = QHBoxLayout()

# Widget Configurations, Button Connections ------------------------------------------------------
        menu_title = QLabel("Temperature Menu") 
        menu_title.setStyleSheet("font-size: 20px; font-weight: " 
                                 "bold; text-decoration: underline")
        
        test_btn = QPushButton("Run Test")
        test_btn.setStyleSheet("font-size: 14px")
        self.test = QProcess(self)
        test_btn.clicked.connect(self.terminal_command)

        self.direction = QLabel("<center>Record the results here:</center>") 
        self.direction.setStyleSheet("font-size: 16px; text-decoration: underline")
        
        # General Radio Box
        self.radioTitle = QLabel("Idle Temp:") 
        self.radioTitle.setStyleSheet("font-size: 14px")
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
        self.radioTitle2 = QLabel("Stress Temp:") 
        self.radioTitle2.setStyleSheet("font-size: 14px")
        self.pass2 = QRadioButton("Pass") 
        self.pass2.setStyleSheet("font-size: 14px")
        self.pass2flag = 0 
        self.fail2 = QRadioButton("Fail") 
        self.fail2.setStyleSheet("font-size: 14px")
        self.fail2flag = 0 
        
        self.pass2.toggled.connect(self.pass2check)
        self.fail2.toggled.connect(self.fail2check)
        
        radio1_opt = QButtonGroup(self)
        radio1_opt.addButton(self.pass2)
        radio1_opt.addButton(self.fail2)

        # Notes
        header = QLabel("Notes:")
        header.setStyleSheet("font-size: 14px")
        self.heatNote = QLineEdit()
        self.heatNote.setMaxLength(105)
        self.heatNote.setPlaceholderText("Enter notes here (105 characters max)")
        self.heatNote.setStyleSheet("font-size: 14px")

        # Page Buttons
        next_btn = QPushButton("Save && Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)

        next_btn.clicked.connect(self.save_continue)
        return_btn.clicked.connect(lambda: hs_stack.setCurrentIndex(1))
        
# Layout Configuration ----------------------------------------------------
        # Top Title Row
        H1.addStretch(1)
        H1.addWidget(self.radioTitle)
        H1.addStretch(2)
        H1.addWidget(self.radioTitle2)
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
        V1.addWidget(test_btn, alignment = Qt.AlignCenter)        
        V1.addStretch()
        V1.addWidget(self.direction)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addLayout(H2)
        V1.addLayout(H3)
        V1.addStretch()
        V1.addWidget(header)
        V1.addWidget(self.heatNote)
        V1.addStretch()
        V1.addLayout(H7)

        self.setLayout(V1)

        hs_stack.currentChanged.connect(self.loader)

# Command Terminal Test Code --------------------------------------------
    def terminal_command(self):
        os = platform.system()
        
        if os == "Windows": #For debugging GUI 
            self.terminal = "cmd.exe"
            command = ["/c", f"start cmd.exe /k set os"]
            self.test.setWorkingDirectory("C:\\")
            self.test.start(self.terminal,command)
        elif os == "Linux": #For Testing on Pi
            # self.terminal = "x-terminal-emulator"
            # command = ["-e", "bash", "-c", f"stress-ng --cpu 4 --timeout 5; exec bash"]
            # self.test.start(self.terminal,command)
            self.direction.setText("<center>Running Test...</center>")
            QApplication.processEvents()

            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            self.pass2.setChecked(False)
            self.fail2.setChecked(False)
            self.radioTitle.setText("Idle Temp:")
            self.radioTitle.setText("Stress Temp:")

            idleTest = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True, text=True)
            idleResult = idleTest.stdout.strip()
            idleTemp = idleResult.replace("temp=","").replace("'C","")
            idleTempInt = float(idleTemp)
            self.radioTitle.setText(f"Idle Temp:{idleTempInt}'C")
            if idleTempInt <= 55:
                self.pass1.setChecked(True)
            else:
                self.fail1.setChecked(True)
            
            time.sleep(0.1)

            subprocess.run(["stress-ng", "--cpu", "4", "--timeout", "5"], capture_output=True, text=True)

            time.sleep(4)

            stressTest = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True, text=True)
            stressResult = stressTest.stdout.strip()
            stressTemp = stressResult.replace("temp=","").replace("'C","")
            stressTempInt = float(stressTemp)
            self.radioTitle2.setText(f"Stress Temp:{stressTempInt}'C")
            if stressTempInt <= 65:
                self.pass2.setChecked(True)
            else:
                self.fail2.setChecked(True)

            self.direction.setText("<center>Record the results here:</center>")

                

# Fail/Pass Button Insurance Functions ------------------------------------------------       
    def pass1check(self):
        if self.pass1.isChecked():
            if self.failflag == 0:
                self.passflag = 1
            elif self.failflag == 1:
                chk = QMessageBox.question(self,"Change Confirmation",
                                           "Are you sure you want to edit Idle Temp?", 
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
                                           "Are you sure you want to edit Idle Temp?",
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
                                           "Are you sure you want to edit Stress Temp?", 
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
                                           "Are you sure you want to edit Stress Temp?", 
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
            
        data["temp_data"] = {
            "test": "Temperature Check",
            "idle": "Pass" if self.pass1.isChecked() else "Fail" if self.fail1.isChecked() else "None",
            "stressed": "Pass" if self.pass2.isChecked() else "Fail" if self.fail2.isChecked() else "None",
            "heatNote": self.heatNote.text()
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
            
        heat = data.get("temp_data", {})
        
        if heat.get("idle") == "Pass":
            self.pass1.setChecked(True)
        elif heat.get("idle") == "Fail":
            self.fail1.setChecked(True)
        elif heat.get("idle") == "None":
            self.pass1.setChecked(False)
            self.fail1.setChecked(False)
            
        if heat.get("stressed") == "Pass":
            self.pass2.setChecked(True)
        elif heat.get("stressed") == "Fail":
            self.fail2.setChecked(True)
        elif heat.get("stressed") == "None":
            self.pass2.setChecked(False)
            self.fail2.setChecked(False)
            
        self.heatNote.setText(heat.get("heatNote"))

    def loader(self, i):
        if i == 1:
            self.load_settings()