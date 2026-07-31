
from PyQt5.QtWidgets import ( QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel, QGridLayout,
    QLineEdit, QRadioButton, QHBoxLayout, QMessageBox,
    QButtonGroup)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QProcess
import platform
import subprocess
import json
import os

class USB_Menu(QWidget):
    def __init__(self,stack):
        super().__init__()
        usbLayout = QGridLayout()
        usb_stack = QStackedWidget()

        usb_stack.addWidget(USB_Step1(usb_stack,stack))
        usb_stack.addWidget(USB_Step2(usb_stack))
       # usb_stack.addWidget(USB_Step3(usb_stack))
        usb_stack.addWidget(USB_Final(usb_stack,stack))
        usbLayout.addWidget(usb_stack)

        self.setLayout(usbLayout)

class USB_Step1(QWidget):
    def __init__(self,usb_stack,stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       

        title = QLabel("USB Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 1: Locate the USB ports on the board<br>"
                           "which can be seen on the right. Plug in <br>"
                           "the mouse and keyboard into the 2.0 ports,<br>"
                           "and the USB sticks into the 3.0 ports.")
        direction.setFixedSize(360,260)
        direction.setStyleSheet("font-size: 18px")

        # Image Setup
        image1_holder = QLabel()
        i1pixmap = QPixmap("images/RPI_USB_Ports.jpg")
        i1pixmap = i1pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image1_holder.setPixmap(i1pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: usb_stack.setCurrentIndex(1))
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
        
    # def ReturnPage(self,stack):
    #     if Main_Menu.mode == 1:
    #         stack.setCurrentIndex(11)
    #     elif Main_Menu.mode ==2:
    #         stack.setCurrentIndex(3)

class USB_Step2(QWidget):
    def __init__(self,usb_stack):
        super().__init__()

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
       
        title = QLabel("USB Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("Step 2: Press the test button on the next <br>" 
                           "page. When pressed, a terminal will pop up<br>" 
                           "and display something similar to the image<br>"
                           "on the right. If working correctly, the <br>"
                           "peripherals should show up. The terminal<br>"
                           "can then be closed.")
        
        #label top/bottom in the image----------------------------------------------------
        
        direction.setFixedSize(360,260)
        direction.setStyleSheet("font-size: 18px")

        #Image Setup
        image2_holder = QLabel()
        i2pixmap = QPixmap("images/USB_Buses.png")
        i2pixmap = i2pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image2_holder.setPixmap(i2pixmap)

        # Page Buttons
        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        next_btn.clicked.connect(lambda: usb_stack.setCurrentIndex(2))
        return_btn.clicked.connect(lambda: usb_stack.setCurrentIndex(0))

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

        

# class USB_Step3(QWidget):
#     def __init__(self,usb_stack):
#         super().__init__()

#         V1 = QVBoxLayout()
#         H1 = QHBoxLayout()
#         H2 = QHBoxLayout()

#         title = QLabel("USB Menu")
#         title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

#         direction = QLabel("-----------------------------")
#         direction.setFixedSize(360,260)
#         direction.setStyleSheet("font-size: 18px")
        
#         # Image Setup
#         image3_holder = QLabel()
#         i3pixmap = QPixmap("images/Placeholder.png")
#         i3pixmap = i3pixmap.scaled(500,260,Qt.KeepAspectRatio, Qt.SmoothTransformation)
#         image3_holder.setPixmap(i3pixmap)

#         # Page Buttons
#         next_btn = QPushButton("Continue")
#         next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
#         next_btn.setFixedSize(125,42)

#         return_btn = QPushButton("Return")
#         return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
#         return_btn.setFixedSize(125,42)

#         next_btn.clicked.connect(lambda: usb_stack.setCurrentIndex(3))
#         return_btn.clicked.connect(lambda: usb_stack.setCurrentIndex(1))

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

class USB_Final(QWidget):
    def __init__(self,usb_stack,stack):
        super().__init__()

        self.stack = stack

        V1 = QVBoxLayout()
        H1 = QHBoxLayout()
        H2 = QHBoxLayout()
        H3 = QHBoxLayout()
        H4 = QHBoxLayout()
        H5 = QHBoxLayout()
        H6 = QHBoxLayout()
        H7 = QHBoxLayout()
        H8 = QHBoxLayout()
        H9 = QHBoxLayout()

# Widget Configurations, Button Connections ------------------------------------------------------
        menu_title = QLabel("USB Menu") 
        menu_title.setStyleSheet("font-size: 20px; font-weight: " 
                                 "bold; text-decoration: underline")

        test_btn = QPushButton("Run Test")
        test_btn.setStyleSheet("font-size: 14px")
        self.test = QProcess(self)
        test_btn.clicked.connect(self.terminal_command)
        
        direction = QLabel("<center>Record the results here:</center>") 
        direction.setStyleSheet("font-size: 16px; text-decoration: underline")
        
        # USB 2.0 Port 1
        usb2_1 = QLabel("USB 2.0 Port (Top), Bus 001") 
        usb2_1.setStyleSheet("font-size: 14px")
        self.usb2_1_device = QLabel("<center>Waiting for test...</center>")
        self.usb2_1_device.setFixedWidth(200)
        self.usb2_1_device.setStyleSheet("font-size: 14px")
        self.pass_2_1 = QRadioButton("Pass") 
        self.pass_2_1.setStyleSheet("font-size: 14px")
        self.p21flag = 0 # pass flag for 2.0 port 1
        self.fail_2_1 = QRadioButton("Fail") 
        self.fail_2_1.setStyleSheet("font-size: 14px")
        self.f21flag = 0 # fail flag for 2.0 port 1
        
        self.pass_2_1.toggled.connect(self.pass_2_1_check)
        self.fail_2_1.toggled.connect(self.fail_2_1_check)
        
        usb2_1_opt = QButtonGroup(self)
        usb2_1_opt.addButton(self.pass_2_1)
        usb2_1_opt.addButton(self.fail_2_1)

        # USB 2.0 Port 2
        usb2_2 = QLabel("USB 2.0 Port (Bottom), Bus 003") 
        usb2_2.setStyleSheet("font-size: 14px")
        self.usb2_2_device = QLabel("<center>Waiting for test...</center>")
        self.usb2_2_device.setFixedWidth(200)
        self.usb2_2_device.setStyleSheet("font-size: 14px")
        self.pass_2_2 = QRadioButton("Pass")
        self.pass_2_2.setStyleSheet("font-size: 14px")
        self.p22flag = 0
        self.fail_2_2 = QRadioButton("Fail") 
        self.fail_2_2.setStyleSheet("font-size: 14px")
        self.f22flag = 0
        
        self.pass_2_2.toggled.connect(self.pass_2_2_check)
        self.fail_2_2.toggled.connect(self.fail_2_2_check)

        usb2_2_opt = QButtonGroup(self)
        usb2_2_opt.addButton(self.pass_2_2)
        usb2_2_opt.addButton(self.fail_2_2)

        # USB 3.0 Port 1
        usb3_1 = QLabel("USB 3.0 Port (Top), Bus 004")
        usb3_1.setStyleSheet("font-size: 14px")
        self.usb3_1_device = QLabel("<center>Waiting for test...</center>")
        self.usb3_1_device.setFixedWidth(200)
        self.usb3_1_device.setStyleSheet("font-size: 14px")
        self.pass_3_1 = QRadioButton("Pass") 
        self.pass_3_1.setStyleSheet("font-size: 14px")
        self.p31flag = 0
        self.fail_3_1 = QRadioButton("Fail") 
        self.fail_3_1.setStyleSheet("font-size: 14px")
        self.f31flag = 0
        
        self.pass_3_1.toggled.connect(self.pass_3_1_check)
        self.fail_3_1.toggled.connect(self.fail_3_1_check)

        usb3_1_opt = QButtonGroup(self)
        usb3_1_opt.addButton(self.pass_3_1)
        usb3_1_opt.addButton(self.fail_3_1)

        # USB 3.0 Port 2
        usb3_2 = QLabel("USB 3.0 Port (Bottom), Bus 002") 
        usb3_2.setStyleSheet("font-size: 14px")
        self.usb3_2_device = QLabel("<center>Waiting for test...</center>")
        self.usb3_2_device.setFixedWidth(200)
        self.usb3_2_device.setStyleSheet("font-size: 14px")
        self.pass_3_2 = QRadioButton("Pass") 
        self.pass_3_2.setStyleSheet("font-size: 14px")
        self.p32flag = 0
        self.fail_3_2 = QRadioButton("Fail") 
        self.fail_3_2.setStyleSheet("font-size: 14px")
        self.f32flag = 0
        
        self.pass_3_2.toggled.connect(self.pass_3_2_check)
        self.fail_3_2.toggled.connect(self.fail_3_2_check)
        
        usb3_2_opt = QButtonGroup(self)
        usb3_2_opt.addButton(self.pass_3_2)
        usb3_2_opt.addButton(self.fail_3_2)

        # Notes
        header = QLabel("Notes:")
        header.setStyleSheet("font-size: 14px")
        self.usbNote = QLineEdit()
        self.usbNote.setMaxLength(105)
        self.usbNote.setPlaceholderText("Enter notes here (105 characters max)")
        self.usbNote.setStyleSheet("font-size: 14px")

        # Page Buttons
        next_btn = QPushButton("Save && Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)

        next_btn.clicked.connect(self.save_continue)
        return_btn.clicked.connect(lambda: usb_stack.setCurrentIndex(1))
        
# Layout Configuration ----------------------------------------------------
        # Top Title Row
        H1.addStretch(1)
        H1.addWidget(usb2_1)
        H1.addStretch(2)
        H1.addWidget(usb3_1)
        H1.addStretch(1)
        
        H2.addStretch(1)
        H2.addWidget(self.usb2_1_device)
        H2.addStretch(2)
        H2.addWidget(self.usb3_1_device)
        H2.addStretch(1)
        
        # Top Pass Row
        H3.addStretch(1)
        H3.addWidget(self.pass_2_1)
        H3.addStretch(2)
        H3.addWidget(self.pass_3_1)
        H3.addStretch(1)

        # Top Fail Row
        H4.addStretch(1)
        H4.addWidget(self.fail_2_1)
        H4.addStretch(2)
        H4.addWidget(self.fail_3_1)
        H4.addStretch(1)

        # Bottom Title Row
        H5.addStretch(1)
        H5.addWidget(usb2_2)
        H5.addStretch(2)
        H5.addWidget(usb3_2)
        H5.addStretch(1)
        
        H6.addStretch(1)
        H6.addWidget(self.usb2_2_device)
        H6.addStretch(2)
        H6.addWidget(self.usb3_2_device)
        H6.addStretch(1)

        # Bottom Pass Row
        H7.addStretch(1)
        H7.addWidget(self.pass_2_2)
        H7.addStretch(2)
        H7.addWidget(self.pass_3_2)
        H7.addStretch(1)

        # Bottom Fail Row
        H8.addStretch(1)
        H8.addWidget(self.fail_2_2)
        H8.addStretch(2)
        H8.addWidget(self.fail_3_2)
        H8.addStretch(1)

        # Page Flip Buttons
        H9.addStretch(1)
        H9.addWidget(return_btn)
        H9.addStretch(28)
        H9.addWidget(next_btn)
        H9.addStretch(1)

        # Add all rows together in a vertical layout
        V1.addWidget(menu_title)
        V1.addStretch()
        V1.addWidget(test_btn, alignment = Qt.AlignCenter)
        V1.addStretch()
        V1.addWidget(direction)
        V1.addStretch()
        V1.addLayout(H1)
        V1.addLayout(H2)
        V1.addLayout(H3)
        V1.addLayout(H4)
        V1.addStretch()
        V1.addLayout(H5)
        V1.addLayout(H6)
        V1.addLayout(H7)
        V1.addLayout(H8)
        V1.addStretch()
        V1.addWidget(header)
        V1.addWidget(self.usbNote)
        V1.addStretch()
        V1.addLayout(H9)

        self.setLayout(V1)

        usb_stack.currentChanged.connect(self.loader)
   
#Command Terminal Test Code -----------------------------------------        
    def terminal_command(self):
        os = platform.system()
        
        if os == "Windows": #For debugging GUI 
            self.terminal = "cmd.exe"
            command = ["/c", f"start cmd.exe /k set os"]
            self.test.setWorkingDirectory("C:\\")
            self.test.start(self.terminal,command)
        elif os == "Linux": #For Testing on Pi
            pftest = subprocess.run(["lsusb", "-t"], capture_output=True,text=True)

            self.busnum = 0

            for line in pftest.stdout.splitlines():
                if "Bus 001" in line:
                    self.busnum = 1
                elif "Bus 002" in line:
                    self.busnum = 2
                elif "Bus 003" in line:
                    self.busnum = 3
                elif "Bus 004" in line:
                    self.busnum = 4

                elif "|__" in line:
                    if self.busnum == 1:
                        self.pass_2_1.setChecked(True)
                    elif self.busnum == 2:
                        self.pass_3_2.setChecked(True)
                    elif self.busnum == 3:
                        self.pass_2_2.setChecked(True)
                    elif self.busnum == 4:
                        self.pass_3_1.setChecked(True)

            if not self.pass_2_1.isChecked():
                self.fail_2_1.setChecked(True)
                self.usb2_1_device.setText("<center>Device Not Found</center>")
            if not self.pass_3_1.isChecked():
                self.fail_3_1.setChecked(True)
                self.usb3_1_device.setText("<center>Device Not Found</center>")
            if not self.pass_2_2.isChecked():
                self.fail_2_2.setChecked(True)
                self.usb2_2_device.setText("<center>Device Not Found</center>")
            if not self.pass_3_2.isChecked():
                self.fail_3_2.setChecked(True)
                self.usb3_2_device.setText("<center>Device Not Found</center>")
                
            nameTest = subprocess.run(["lsusb"], capture_output=True,text=True)
                
            
            for line in nameTest.stdout.splitlines():
                if "Bus 001" in line and not "ID 1d6b:" in line:
                    self.usb2_1_device.setText(line.split(maxsplit=6)[6])
                    self.usb2_1_device.setToolTip(line.split(maxsplit=6)[6])
                elif "Bus 002" in line and not "ID 1d6b:" in line:
                    self.usb3_2_device.setText(line.split(maxsplit=6)[6])
                    self.usb3_2_device.setToolTip(line.split(maxsplit=6)[6])
                elif "Bus 003" in line and not "ID 1d6b:" in line:
                    self.usb2_2_device.setText(line.split(maxsplit=6)[6])
                    self.usb2_2_device.setToolTip(line.split(maxsplit=6)[6])
                elif "Bus 004" in line and not "ID 1d6b:" in line:
                    self.usb3_1_device.setText(line.split(maxsplit=6)[6])
                    self.usb3_1_device.setToolTip(line.split(maxsplit=6)[6])

# Fail/Pass Button Insurance Functions ------------------------------------------------       
    def pass_2_1_check(self):
        if self.pass_2_1.isChecked():
            if self.f21flag == 0:
                self.p21flag = 1
            elif self.f21flag == 1:
                chk = QMessageBox.question(self,"Change Confirmation",
                                           "Are you sure you want to edit USB 2.0 (Top)?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.p21flag = 1 
                    self.f21flag = 0
                else:
                    self.p21flag = 0
                    self.f21flag = 1
                    self.pass_2_1.setChecked(False)
                    self.fail_2_1.setChecked(True)
                    
    def fail_2_1_check(self):
        if self.fail_2_1.isChecked():
            if self.p21flag == 0:
                self.f21flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit USB 2.0 (Top)?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.f21flag = 1
                    self.p21flag = 0
                else:
                    self.f21flag = 0
                    self.p21flag = 1
                    self.fail_2_1.setChecked(False)
                    self.pass_2_1.setChecked(True)
                    
    def pass_2_2_check(self):
        if self.pass_2_2.isChecked():
            if self.f22flag == 0:
                self.p22flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit USB 2.0 (Bottom)?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.p22flag = 1
                    self.f22flag = 0
                else:
                    self.p21flag = 0
                    self.f22flag = 1
                    self.pass_2_2.setChecked(False)
                    self.fail_2_2.setChecked(True)
                    
    def fail_2_2_check(self):
        if self.fail_2_2.isChecked():
            if self.p22flag == 0:
                self.f22flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit USB 2.0 (Bottom)?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.f22flag = 1
                    self.p22flag = 0
                else:
                    self.f22flag = 0
                    self.p22flag = 1
                    self.fail_2_2.setChecked(False)
                    self.pass_2_2.setChecked(True)
        
    def pass_3_1_check(self):
        if self.pass_3_1.isChecked():
            if self.f31flag == 0:
                self.p31flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit USB 3.0 (top)?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.p31flag = 1
                    self.f31flag = 0
                else:
                    self.p31flag = 0
                    self.f31flag = 1
                    self.pass_3_1.setChecked(False)
                    self.fail_3_1.setChecked(True)
                    
    def fail_3_1_check(self):
        if self.fail_3_1.isChecked():
            if self.p31flag == 0:
                self.f31flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit USB 3.0 (top)?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.f31flag = 1
                    self.p31flag = 0
                else:
                    self.f31flag = 0
                    self.p31flag = 1
                    self.fail_3_1.setChecked(False)
                    self.pass_3_1.setChecked(True)
                    
    def pass_3_2_check(self):
        if self.pass_3_2.isChecked():
            if self.f32flag == 0:
                self.p32flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit USB 3.0 (bottom)?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.p32flag = 1
                    self.f32flag = 0
                else:
                    self.p31flag = 0
                    self.f32flag = 1
                    self.pass_3_2.setChecked(False)
                    self.fail_3_2.setChecked(True)
                    
    def fail_3_2_check(self):
        if self.fail_3_2.isChecked():
            if self.p32flag == 0:
                self.f32flag = 1
            else:
                chk = QMessageBox.question(self,"Change Confirmation", 
                                           "Are you sure you want to edit USB 3.0 (bottom)?", 
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if chk == QMessageBox.Yes:
                    self.f32flag = 1
                    self.p32flag = 0
                else:
                    self.f32flag = 0
                    self.p32flag = 1
                    self.fail_3_2.setChecked(False)
                    self.pass_3_2.setChecked(True)
                    
    def save_continue(self):
        savefile = "GUI_Test_Results.json"
        if os.path.exists(savefile):
            with open(savefile, "r") as f:
                data = json.load(f)
        else: 
            data = {}
            
        data["usb_ports"] = {
            "test": "USB Ports",
            "usb 2.0 (top)": "Pass" if self.pass_2_1.isChecked() else "Fail" if self.fail_2_1.isChecked() else "None",
            "usb 2.0 (bottom)": "Pass" if self.pass_2_2.isChecked() else "Fail" if self.fail_2_2.isChecked() else "None",
            "usb 3.0 (top)": "Pass" if self.pass_3_1.isChecked() else "Fail" if self.fail_3_1.isChecked() else "None",
            "usb 3.0 (bottom)": "Pass" if self.pass_3_2.isChecked() else "Fail" if self.fail_3_2.isChecked() else "None",
            "usbNote": self.usbNote.text()
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
            
        usb = data.get("usb_ports", {})
        
        if usb.get("usb 2.0 (top)") == "Pass":
            self.pass_2_1.setChecked(True)
        elif usb.get("usb 2.0 (top)") == "Fail":
            self.fail_2_1.setChecked(True)
        elif usb.get("usb 2.0 (top)") == "None":
            self.pass_2_1.setChecked(False)
            self.fail_2_1.setChecked(False)
            
        if usb.get("usb 2.0 (bottom)") == "Pass":
            self.pass_2_2.setChecked(True)
        elif usb.get("usb 2.0 (bottom)") == "Fail":
            self.fail_2_2.setChecked(True)
        elif usb.get("usb 2.0 (bottom)") == "None":
            self.pass_2_2.setChecked(False)
            self.fail_2_2.setChecked(False)

        if usb.get("usb 3.0 (top)") == "Pass":
            self.pass_3_1.setChecked(True)
        elif usb.get("usb 3.0 (top)") == "Fail":
            self.fail_3_1.setChecked(True)
        elif usb.get("usb 3.0 (top)") == "None":
            self.pass_3_1.setChecked(False)
            self.fail_3_1.setChecked(False)

        if usb.get("usb 3.0 (bottom)") == "Pass":
            self.pass_3_2.setChecked(True)
        elif usb.get("usb 3.0 (bottom)") == "Fail":
            self.fail_3_2.setChecked(True)
        elif usb.get("usb 3.0 (bottom)") == "None":
            self.pass_3_2.setChecked(False)
            self.fail_3_2.setChecked(False)
            
        self.usbNote.setText(usb.get("usbNote"))


    def loader(self, i):
        if i == 2:
            self.load_settings()