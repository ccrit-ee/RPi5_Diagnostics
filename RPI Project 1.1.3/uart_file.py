import serial
import time
from PyQt5.QtWidgets import QMessageBox

uart_result = None

# Pop-up Functions

def show_success():
    QMessageBox.information(None, "UART Test Complete",
                            "✓ UART test completed successfully!\n\n"
                            "All 4 messages sent and received correctly.\n"
                            "Pi GPIO 14 TX → CP2102 → GPIO 15 RX verified.\n",
                            QMessageBox.Ok)

def show_failure(sent, received):
    QMessageBox.critical(None, "UART Test Failed",
                         f"✗ UART test failed!\n\n"
                         f"Sent:     {sent}\n"
                         f"Received: {received}\n\n"
                         "Check:\n"
                         "• GPIO 14 TX → CP2102 RX\n"
                         "• GPIO 15 RX → CP2102 TX\n"
                         "• GND connected",
                         QMessageBox.Ok)


def show_port_error(port):
    QMessageBox.warning(None, "Port Not Found",
                        f"✗ Could not open {port}\n\n"
                        "Check that:\n"
                        "• CP2102 is plugged into Pi USB\n"
                        "• UART is enabled (raspi-config)\n"
                        "• No other program is using the port",
                        QMessageBox.Ok)

#  UART test 

def run_uart_test():
    global uart_result

    # Pi's onboard UART
    PI_UART   = '/dev/ttyAMA0'
    # CP2102 over USB
    CP2102    = '/dev/ttyUSB0'

    test_messages = [
        "UART test 25%",
        "UART test 50%",
        "UART test 75%",
        "UART test 100%"
    ]

    # Open Pi UART (GPIO 14 TX, GPIO 15 RX)
    try:
        pi_uart = serial.Serial(
            port=PI_UART,
            baudrate=9600,
            timeout=1
        )
    except serial.SerialException:
        uart_result = "Error"
        show_port_error(PI_UART)
        return

    # Open CP2102 (receives from Pi TX, sends back to Pi RX)
    try:
        cp2102 = serial.Serial(
            port=CP2102,
            baudrate=9600,
            timeout=1
        )
    except serial.SerialException:
        pi_uart.close()
        uart_result = "Error"
        show_port_error(CP2102)
        return

    print("Starting Pi UART test...\n")
    print(f"Pi TX (GPIO 14) → CP2102 RX")
    print(f"CP2102 TX       → Pi RX (GPIO 15)\n")
    print(f"{'Message':<20} {'Sent':<16} {'Received':<16} {'Result'}")
    print("-" * 65)

    all_passed = True

    for message in test_messages:
        # Pi sends out GPIO 14 TX
        pi_uart.write(message.encode())
        time.sleep(0.1)

        # CP2102 reads what Pi sent (arrived on CP2102 RX)
        # then echoes it back out CP2102 TX → Pi GPIO 15 RX
        cp2102_received = cp2102.read(len(message)).decode(errors='replace')
        cp2102.write(cp2102_received.encode())
        time.sleep(0.1)

        # Pi reads what came back on GPIO 15 RX
        pi_received = pi_uart.read(len(message)).decode(errors='replace')

        passed = message == pi_received
        if not passed:
            all_passed = False

        status = "PASS ✓" if passed else "FAIL ✗"
        print(f"{message:<20} {message:<16} {pi_received:<16} {status}")

        if not passed:
            pi_uart.close()
            cp2102.close()
            uart_result = "False"
            show_failure(message, pi_received)
            return

        time.sleep(1)

    pi_uart.close()
    cp2102.close()
    print("\nAll tests passed.")
    uart_result = "True"
    show_success()
