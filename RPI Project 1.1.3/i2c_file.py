import smbus2
import time
import tkinter as tk
from tkinter import messagebox

# 24LC256 I2C address with A0/A1/A2 tied to GND
EEPROM_ADDRESS = 0x50
TEST_VALUE     = "08062001"  # Stored as 8 bytes, one per character
MEM_ADDRESS    = 0x00

def write_eeprom(bus, mem_addr, text):
    for i, char in enumerate(text):
        high_byte = ((mem_addr + i) >> 8) & 0xFF
        low_byte  = (mem_addr + i) & 0xFF
        bus.write_i2c_block_data(EEPROM_ADDRESS, high_byte, [low_byte, ord(char)])
        time.sleep(0.01)  # 10ms write cycle per byte

def read_eeprom(bus, mem_addr, length):
    result = ""
    for i in range(length):
        high_byte = ((mem_addr + i) >> 8) & 0xFF
        low_byte  = (mem_addr + i) & 0xFF
        bus.write_i2c_block_data(EEPROM_ADDRESS, high_byte, [low_byte])
        time.sleep(0.01)
        byte = bus.read_byte(EEPROM_ADDRESS)
        result += chr(byte)
    return result

def show_popup(passed, details):
    root = tk.Tk()
    root.withdraw()

    if passed:
        messagebox.showinfo(
            "I2C Test Complete",
            f"✓ I2C test passed!\n\n"
            f"{details}"
        )
    else:
        messagebox.showerror(
            "I2C Test Failed",
            f"✗ I2C test failed!\n\n"
            f"{details}\n\n"
            "Check:\n"
            "• SDA → GPIO 2 (pin 3)\n"
            "• SCL → GPIO 3 (pin 5)\n"
            "• VCC → 3.3V\n"
            "• A0/A1/A2/WP → GND\n"
            "• I2C enabled in raspi-config"
        )

    root.destroy()

def show_not_found():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "I2C Device Not Found",
        "✗ EEPROM not detected on I2C bus\n\n"
        "Expected address: 0x50\n\n"
        "Check:\n"
        "• All wiring connections\n"
        "• I2C enabled (raspi-config)\n"
        "• Run: i2cdetect -y 1"
    )
    root.destroy()

def test_i2c():
    print("Running I2C test via 24LC256 EEPROM...\n")

    try:
        bus = smbus2.SMBus(1)
    except Exception as e:
        print(f"Failed to open I2C bus: {e}")
        show_not_found()
        return

    # ── Test 1: Device detected ────────────────────────────
    try:
        bus.read_byte(EEPROM_ADDRESS)
        detected = True
    except OSError:
        detected = False

    print(f"Device detected (0x50): {'PASS ✓' if detected else 'FAIL ✗'}")

    if not detected:
        bus.close()
        show_not_found()
        return

    # ── Test 2: Write 8 bytes ──────────────────────────────
    try:
        write_eeprom(bus, MEM_ADDRESS, TEST_VALUE)
        write_ok = True
    except Exception as e:
        write_ok = False
        print(f"Write error: {e}")

    print(f"Write value ({TEST_VALUE}): {'PASS ✓' if write_ok else 'FAIL ✗'}")

    # ── Test 3: Read 8 bytes back ──────────────────────────
    try:
        read_value = read_eeprom(bus, MEM_ADDRESS, len(TEST_VALUE))
        read_ok = True
    except Exception as e:
        read_ok = False
        read_value = None
        print(f"Read error: {e}")

    print(f"Read value back:        {'PASS ✓' if read_ok else 'FAIL ✗'}")

    # ── Test 4: Values match ───────────────────────────────
    match = read_value == TEST_VALUE
    print(f"Values match:           {'PASS ✓' if match else 'FAIL ✗'}")
    print(f"Expected: {TEST_VALUE}  Got: {read_value}")

    # ── Print byte by byte breakdown ──────────────────────
    print("\nByte breakdown:")
    print(f"{'Address':<12} {'Char':<8} {'ASCII'}")
    print("-" * 32)
    for i, char in enumerate(TEST_VALUE):
        print(f"0x{(MEM_ADDRESS + i):02X}         '{char}'      {ord(char)}")

    bus.close()

    all_passed = detected and write_ok and read_ok and match

    details = (
        f"Device detected (0x50): {'✓ Yes' if detected else '✗ No'}\n"
        f"Write succeeded:        {'✓ Yes' if write_ok else '✗ No'}\n"
        f"Read succeeded:         {'✓ Yes' if read_ok else '✗ No'}\n"
        f"Values match:           {'✓ Yes' if match else '✗ No'}\n\n"
        f"Expected: {TEST_VALUE}\n"
        f"Got:      {read_value if read_value else 'Nothing'}"
    )

    show_popup(all_passed, details)

# test_i2c()