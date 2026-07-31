import sys, json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel, QGridLayout,QComboBox, 
    QRadioButton, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from I2C_Stack import I2C_Menu
from SPI_Stack import SPI_Menu
from UART_Stack import UART_Menu
from PWM_Stack import PWM_Menu
from PCM_Stack import PCM_Menu
from GPIO_Stack import GPIO_Menu
from USB_Stack import USB_Menu
from Micro_HDMI_Stack import MicroHDMI_Menu
from Fan_Stack import Fan_Menu
from Temperature_Stack import Temperature_Menu
from WIFI_Stack import WIFI_Menu
from Ethernet_Stack import Ethernet_Menu
from Bluetooth_Stack import Bluetooth_Menu
from CSI_DSI_Stack import CSI_Menu


class Welcome_Screen(QWidget):
    def __init__(self,stack):
        super().__init__()

        wsLayout = QVBoxLayout()

        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:14px; font-weight:bold;")
        next_btn.setFixedSize(150,50)

        image = QLabel()

        pixmap = QPixmap('images/ttu_dt.png')
        pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        image.setPixmap(pixmap)

        title = QLabel("""<center>Welcome to the Raspberry Pi 5 Diagnostic Menu!<br>
                       Designed for ECE 3332<br>
                       Summer 2026</center>""")
        title.setStyleSheet("color:red; font-size:20px; font-weight:bold;")

        next_btn.clicked.connect(lambda: stack.setCurrentIndex(1))

        wsLayout.addStretch(1)
        wsLayout.addWidget(image, alignment=Qt.AlignCenter)
        wsLayout.addStretch(1)
        wsLayout.addWidget(title)
        wsLayout.addStretch(5)
        wsLayout.addWidget(next_btn, alignment=Qt.AlignCenter)
        wsLayout.addStretch(2)
        self.setLayout(wsLayout)

class Main_Menu(QWidget):
    def __init__(self, stack):
        super().__init__()

        self.CycleMode = 0
        mmLayout = QVBoxLayout()

        title = QLabel("Main Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("<center>What would you like to do?</center>")
        direction.setStyleSheet("color:black; font-size: 20px;")
        optionA = QPushButton("Continue with Previous Data")
        optionA.setStyleSheet("color:black; font-size: 14px; font-weight: bold")
        optionA.setFixedSize(210,50)

        optionB = QPushButton("Clear Data and Start Fresh")
        optionB.setStyleSheet("color:black; font-size: 14px; font-weight: bold")
        optionB.setFixedSize(210,50)

        return_btn = QPushButton("Back")
        return_btn.setStyleSheet("color:black; font-size: 14px; font-weight: bold")
        return_btn.setFixedSize(210,50)
            
        optionA.clicked.connect(self.keep_data)
        optionB.clicked.connect(self.clear_data)
        return_btn.clicked.connect(lambda: stack.setCurrentIndex(0))

        mmLayout.addWidget(title)
        mmLayout.addStretch(2)
        mmLayout.addWidget(direction)
        mmLayout.addStretch(1)
        mmLayout.addWidget(optionA, alignment=Qt.AlignCenter)
        mmLayout.addStretch(1)
        mmLayout.addWidget(optionB, alignment=Qt.AlignCenter)
        mmLayout.addStretch(1)
        mmLayout.addWidget(return_btn,alignment=Qt.AlignCenter)
        mmLayout.addStretch(1)
        self.setLayout(mmLayout)


    def keep_data(self):
        confirm = QMessageBox.question(self,"Save Data Confirmation",
                                       "<center>Are you sure you want to use previous save data?<br><br>"
                                       "Selecting yes will repopulate the tests with the<br>"
                                       "results from the last time they were run.<br><br>"
                                       "This is for reloading after connection changes.</center>",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            stack.setCurrentIndex(3)
        else:
            return
            
    def clear_data(self):
        confirm = QMessageBox.question(self, "Clear Data Confirmation",
                                       "<center>Are you sure you want to clear save data?<br><br>"
                                       "Selecting yes will reset all tests and <br>"
                                       "you will need to run them again.<br><br>"
                                       "This is for testing a new Pi from zero.</center>",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                                       )
        if confirm == QMessageBox.Yes:
            with open('GUI_Test_Results.json', 'w') as f:
                json.dump({},f)
            stack.setCurrentIndex(3)
        else:
            return

class Single_Test(QWidget):
    def __init__(self,stack):
        super().__init__()
        
        stLayout = QVBoxLayout()
        btn_layout = QHBoxLayout()

        title = QLabel("Single Test Menu")
        title.setStyleSheet("font-size: 20px; font-weight: bold; text-decoration: underline")

        direction = QLabel("<center>Please choose a test to run:</center>")
        direction.setStyleSheet("font-size:16px")

        next_btn = QPushButton("Continue")
        next_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        next_btn.setFixedSize(125,42)

        return_btn = QPushButton("Return to Main")
        return_btn.setStyleSheet("font-size:12px; font-weight:bold;")
        return_btn.setFixedSize(125,42)
        
        self.drop = QComboBox(stack)

        self.drop.addItem("I2C")
        self.drop.addItem("SPI")
        self.drop.addItem("UART")
        self.drop.addItem("PWM")
        self.drop.addItem("PCM")
        self.drop.addItem("GPIO")
        self.drop.addItem("USB Ports") 
        self.drop.addItem("Micro-HDMI Ports") 
        self.drop.addItem("Fan Controller") 
        self.drop.addItem("CPU Temperature")
        self.drop.addItem("WIFI") 
        self.drop.addItem("Ethernet") 
        self.drop.addItem("Bluetooth")         
        self.drop.addItem("CSI/DSI") 
        self.drop.setFixedSize(225,25)
        self.drop.setStyleSheet("font-size: 14px;")

        next_btn.clicked.connect(self.option_select)
        return_btn.clicked.connect(lambda: stack.setCurrentIndex(1))

        stLayout.addWidget(title)
        stLayout.addStretch()
        stLayout.addWidget(direction)
        stLayout.addWidget(self.drop, alignment = Qt.AlignCenter)
        stLayout.addStretch()

        btn_layout.addStretch(1)
        btn_layout.addWidget(return_btn)
        btn_layout.addStretch(28)
        btn_layout.addWidget(next_btn)
        btn_layout.addStretch(1)

        stLayout.addLayout(btn_layout)
        self.setLayout(stLayout)

    def option_select(self):
        option = self.drop.currentText()

        if option == "I2C":
            stack.setCurrentIndex(3)
        elif option == "SPI":
            stack.setCurrentIndex(4)
        elif option == "UART":
            stack.setCurrentIndex(5)            
        elif option == "PWM":
            stack.setCurrentIndex(6)
        elif option == "PCM":
            stack.setCurrentIndex(7)
        elif option == "GPIO":
            stack.setCurrentIndex(8)
        elif option == "USB Ports":
            stack.setCurrentIndex(9)
        elif option == "Micro-HDMI Ports":
            stack.setCurrentIndex(10)
        elif option == "Fan Controller":
            stack.setCurrentIndex(11)
        elif option == "CPU Temperature":
            stack.setCurrentIndex(12)
        elif option == "WIFI":
            stack.setCurrentIndex(13)
        elif option == "Ethernet":
            stack.setCurrentIndex(14)
        elif option == "Bluetooth":
            stack.setCurrentIndex(15)
        elif option == "CSI/DSI":
            stack.setCurrentIndex(16)

app = QApplication(sys.argv)

stack = QStackedWidget()

stack.addWidget(Welcome_Screen(stack))
stack.addWidget(Main_Menu(stack))
stack.addWidget(Single_Test(stack))
stack.addWidget(I2C_Menu(stack))
stack.addWidget(SPI_Menu(stack))
stack.addWidget(UART_Menu(stack))
stack.addWidget(PWM_Menu(stack))
stack.addWidget(PCM_Menu(stack))
stack.addWidget(GPIO_Menu(stack))
stack.addWidget(USB_Menu(stack))
stack.addWidget(MicroHDMI_Menu(stack))
stack.addWidget(Fan_Menu(stack))
stack.addWidget(Temperature_Menu(stack))
stack.addWidget(WIFI_Menu(stack))
stack.addWidget(Ethernet_Menu(stack))
stack.addWidget(Bluetooth_Menu(stack))
stack.addWidget(CSI_Menu(stack))

stack.setFixedSize(900,600)

stack.show()

sys.exit(app.exec_())