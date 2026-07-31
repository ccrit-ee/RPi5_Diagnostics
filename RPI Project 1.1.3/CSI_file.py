import subprocess
import os
import tkinter as tk
from tkinter import messagebox

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

def test_camera():
    print("Running Camera Module 3 tests...\n")

    results = {
        "detected": False,
        "capture": False,
        "image_valid": False,
        "resolution": "Unknown",
        "error": None
    }

    # ── Test 1: Camera detected ────────────────────────────
    # rpicam-hello --list-cameras lists all detected cameras
    stdout, stderr = run_command(['rpicam-hello', '--list-cameras'])
    output_lower = stdout.lower()
    no_camera_found = 'no cameras available' in output_lower
    detected = ('imx708' in output_lower) and not no_camera_found
    results["detected"] = detected

    print(f"Camera detected:   {'PASS ✓' if detected else 'FAIL ✗'}")
    print(f"Detection output:  {stdout}")

    if not detected:
        results["error"] = (
            "Camera not detected\n\n"
            "Check:\n"
            "• Ribbon cable fully seated\n"
            "• Blue side of ribbon faces USB-C Power port\n"
            "• Camera enabled in raspi-config\n"
            "• Pi was rebooted after enabling"
        )
        show_popup(results)
        return

    # ── Test 2: Capture a frame ────────────────────────────
    image_path = '/tmp/camera_test.jpg'

    # Remove old test image if it exists
    if os.path.exists(image_path):
        os.remove(image_path)

    # Capture a single frame
    stdout, stderr = run_command([
        'rpicam-still',
        '-o', image_path,
        '--timeout', '2000',  # 2 second timeout
        '--nopreview'
    ])

    capture_ok = os.path.exists(image_path)
    results["capture"] = capture_ok
    print(f"Frame captured:    {'PASS ✓' if capture_ok else 'FAIL ✗'}")

    if not capture_ok:
        results["error"] = (
            "Camera detected but capture failed\n\n"
            "Check:\n"
            "• Camera lens cap removed\n"
            "• Adequate lighting\n"
            "• Try: rpicam-still -o test.jpg"
        )
        show_popup(results)
        return

    # ── Test 3: Image is valid ─────────────────────────────
    file_size = os.path.getsize(image_path)
    image_valid = file_size > 10000  # Valid image should be well over 10KB
    results["image_valid"] = image_valid

    print(f"Image valid:       {'PASS ✓' if image_valid else 'FAIL ✗'}")
    print(f"File size:         {file_size / 1024:.1f} KB")

    # ── Get resolution from image ──────────────────────────
    try:
        import struct, imghdr
        with open(image_path, 'rb') as f:
            data = f.read(24)
        # Pull resolution from JPEG header
        stdout, _ = run_command(['identify', image_path])
        if 'x' in stdout:
            for part in stdout.split():
                if 'x' in part and part.replace('x', '').isdigit():
                    results["resolution"] = part
                    break
    except:
        results["resolution"] = f"{file_size / 1024:.1f} KB captured"

    show_popup(results)

# ── Popup ──────────────────────────────────────────────────

def show_popup(results):
    all_passed = results["detected"] and results["capture"] and results["image_valid"]

    summary = (
        f"Camera Detected:   {'✓ Yes' if results['detected'] else '✗ No'}\n"
        f"Frame Captured:    {'✓ Yes' if results['capture'] else '✗ No'}\n"
        f"Image Valid:       {'✓ Yes' if results['image_valid'] else '✗ No'}\n"
        f"Resolution/Size:   {results['resolution']}"
    )

    root = tk.Tk()
    root.withdraw()

    if all_passed:
        messagebox.showinfo(
            "Camera Test Complete",
            f"✓ Camera Module 3 test passed!\n\n"
            f"{summary}"
        )
    else:
        messagebox.showerror(
            "Camera Test Failed",
            f"✗ Camera test failed\n\n"
            f"{summary}\n\n"
            f"{results['error'] if results['error'] else ''}"
        )

    root.destroy()

# test_camera()