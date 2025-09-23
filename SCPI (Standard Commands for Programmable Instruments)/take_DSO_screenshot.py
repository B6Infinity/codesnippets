#!/usr/bin/env python3
"""
Screenshot grabber for Tektronix TBS2000B via USBTMC (/dev/usbtmc0).
Saves PNG screenshots with timestamped filenames.
"""

import datetime
import time

USB_DEVICE = "/dev/usbtmc0"

def query(dev, command, retries=3, delay=0.1):
    """Send SCPI query and return response (text). Retries if timeout occurs."""
    for attempt in range(retries):
        try:
            dev.write((command + "\n").encode())
            dev.flush()
            time.sleep(delay)  # let scope prepare reply
            return dev.read(4096).decode(errors="ignore").strip()
        except TimeoutError:
            if attempt < retries - 1:
                print(f"[WARN] Timeout on '{command}', retrying ({attempt+1}/{retries})...")
                continue
            raise

def write(dev, command):
    """Send SCPI command without expecting a response"""
    dev.write((command + "\n").encode())
    dev.flush()

def read_binary(dev, chunk_size=4096):
    """Read binary data until EOF, show progress"""
    chunks = []
    total = 0
    while True:
        try:
            chunk = dev.read(chunk_size)
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if total % (100*1024) < chunk_size:  # every ~100 KB
                print(f"[LOG] Received {total/1024:.1f} KB...")
        except Exception:
            break
    return b"".join(chunks)

if __name__ == "__main__":
    try:
        with open(USB_DEVICE, "r+b", buffering=0) as dev:
            print("[LOG] Identifying oscilloscope...")
            idn = query(dev, "*IDN?")
            print("[LOG] Connected to:", idn)

            # Configure screenshot
            write(dev, "HARDCOPY:FORMAT PNG")

            # Trigger screenshot
            write(dev, "HARDCOPY START")

            # Read binary PNG data
            print("[LOG] Reading screenshot binary data...")
            data = read_binary(dev)

            # Save with timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/screenshot_{timestamp}.png"
            with open(filename, "wb") as f:
                f.write(data)

            print(f"[LOG] Screenshot saved as {filename}")

    except PermissionError:
        print(f"[ERROR] Permission denied accessing {USB_DEVICE}.")
        print("Run with 'sudo' or add a udev rule for user access.")
