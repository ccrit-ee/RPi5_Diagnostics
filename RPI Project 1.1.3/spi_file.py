import spidev
import time
import tkinter as tk
from tkinter import messagebox

# ── Config ─────────────────────────────────────────────────
SPI_BUS   = 0        # SPI0
SPI_CS    = 0        # CE0  -> GPIO 8/9/10/11
SPI_SPEED = 1350000  # 1.35 MHz

HIGH_CH   = 0        # CH0 tied to 3.3V  -> expect near 1023
LOW_CH    = 1        # CH1 tied to GND   -> expect near 0

HIGH_MIN  = 1000     # CH0 must read at least this (near full-scale)
LOW_MAX   = 25       # CH1 must read at most this (near zero)
SAMPLES   = 10       # average this many reads per channel to cut noise


# ── SPI read (same transaction as the reference code) ──────
def read_channel(spi, channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((adc[1] & 3) << 8) + adc[2]

def read_avg(spi, channel, n=SAMPLES):
    vals = [read_channel(spi, channel) for _ in range(n)]
    for _ in vals:
        time.sleep(0.005)
    return sum(vals) // len(vals), vals


# ── Popups ─────────────────────────────────────────────────
def show_pass(details):
    root = tk.Tk(); root.withdraw()
    messagebox.showinfo(
        "SPI Test Complete",
        "\u2713 SPI test passed!\n\n"
        "MCP3008 responded correctly on SPI0 (CE0).\n"
        "GPIO 8/9/10/11 verified end-to-end.\n\n"
        f"{details}"
    )
    root.destroy()

def show_fail(details):
    root = tk.Tk(); root.withdraw()
    messagebox.showerror(
        "SPI Test Failed",
        "\u2717 SPI test failed!\n\n"
        f"{details}\n\n"
        "Check:\n"
        "\u2022 SCLK \u2192 GPIO 11 (pin 23)\n"
        "\u2022 DIN  \u2192 GPIO 10 (pin 19)\n"
        "\u2022 DOUT \u2192 GPIO 9  (pin 21)\n"
        "\u2022 CS   \u2192 GPIO 8  (pin 24)\n"
        "\u2022 VDD/VREF \u2192 3.3V, AGND/DGND \u2192 GND\n"
        "\u2022 CH0 \u2192 3.3V, CH1 \u2192 GND (test inputs)\n"
        "\u2022 SPI enabled in raspi-config"
    )
    root.destroy()

def show_bus_error(err):
    root = tk.Tk(); root.withdraw()
    messagebox.showerror(
        "SPI Bus Not Available",
        f"\u2717 Could not open SPI bus {SPI_BUS}.{SPI_CS}\n\n"
        f"{err}\n\n"
        "Check that:\n"
        "\u2022 SPI is enabled (raspi-config \u2192 Interface \u2192 SPI)\n"
        "\u2022 /dev/spidev0.0 exists (ls /dev/spi*)\n"
        "\u2022 No other program is using the bus"
    )
    root.destroy()


# ── Test ───────────────────────────────────────────────────
def test_spi():
    print("Running SPI test via MCP3008 ADC...\n")

    # ── Open the bus ───────────────────────────────────────
    try:
        spi = spidev.SpiDev()
        spi.open(SPI_BUS, SPI_CS)
        spi.max_speed_hz = SPI_SPEED
    except Exception as e:
        print(f"Failed to open SPI bus: {e}")
        show_bus_error(e)
        return

    # ── Test 1: CH0 (tied 3.3V) reads high ─────────────────
    high_val, high_raw = read_avg(spi, HIGH_CH)
    high_ok = high_val >= HIGH_MIN
    print(f"CH0 (3.3V) reads high:  {'PASS \u2713' if high_ok else 'FAIL \u2717'}  "
          f"(got {high_val}, need \u2265 {HIGH_MIN})")

    # ── Test 2: CH1 (tied GND) reads low ───────────────────
    low_val, low_raw = read_avg(spi, LOW_CH)
    low_ok = low_val <= LOW_MAX
    print(f"CH1 (GND)  reads low:   {'PASS \u2713' if low_ok else 'FAIL \u2717'}  "
          f"(got {low_val}, need \u2264 {LOW_MAX})")

    # ── Test 3: bus is not stuck ───────────────────────────
    # A dead MISO line returns the SAME value on every read of both
    # channels. If CH0 and CH1 differ, the chip is really converting.
    distinct = abs(high_val - low_val) > 100
    print(f"Channels distinct:      {'PASS \u2713' if distinct else 'FAIL \u2717'}  "
          f"(\u0394 = {abs(high_val - low_val)})")

    spi.close()

    all_passed = high_ok and low_ok and distinct

    # ── Console breakdown ──────────────────────────────────
    def volts(raw):
        return (raw / 1023.0) * 3.3

    print("\nReading breakdown:")
    print(f"{'Channel':<10} {'Expect':<10} {'Raw':<8} {'Voltage'}")
    print("-" * 40)
    print(f"{'CH0':<10} {'~1023':<10} {high_val:<8} {volts(high_val):.3f}V")
    print(f"{'CH1':<10} {'~0':<10} {low_val:<8} {volts(low_val):.3f}V")

    print(f"\nOverall: {'PASS \u2713' if all_passed else 'FAIL \u2717'}")

    # ── Popup ──────────────────────────────────────────────
    details = (
        f"CH0 (3.3V): raw {high_val}  ->  {volts(high_val):.3f}V  "
        f"{'\u2713' if high_ok else '\u2717'}\n"
        f"CH1 (GND):  raw {low_val}  ->  {volts(low_val):.3f}V  "
        f"{'\u2713' if low_ok else '\u2717'}\n"
        f"Channel spread: {abs(high_val - low_val)}  "
        f"{'\u2713' if distinct else '\u2717'}"
    )

    if all_passed:
        show_pass(details)
    else:
        show_fail(details)


# test_spi()