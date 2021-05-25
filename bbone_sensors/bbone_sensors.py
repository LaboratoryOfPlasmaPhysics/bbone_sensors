"""Main module."""
import requests
from serial import Serial
import socket, time
import subprocess
from .config import firmware_version_url, firmware_url, current_firmware_version, serial_port_name, serial_port_speed
from .cape_driver import start_bootloader, reset_cape, config_gpio
from . import Metric


def build_number():
    return int(requests.get(firmware_version_url.get()).text)


def download_latest_firmware():
    response = requests.get(firmware_url.get())
    fname = '/tmp/bbfw.bin'
    if response.status_code == 200:
        with open('/tmp/bbfw.bin', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024 * 16):
                if chunk:
                    f.write(chunk)
        return fname


def flash_firmware(fname):
    start_bootloader()
    cmd = ["stm32loader.py", "-p", serial_port_name.get(), "-e", "-w", "-v", fname]
    res = subprocess.run(cmd)
    reset_cape()
    return res.returncode == 0


def update_firmware():
    latest_build = build_number()
    if latest_build > int(current_firmware_version.get()):
        fname = download_latest_firmware()
        if fname:
            if flash_firmware(fname):
                current_firmware_version.set(str(latest_build))


def measurement_loop(db):
    config_gpio()
    update_firmware()
    reset_cape()
    HOSTNAME = socket.gethostname().replace(".", "_")
    uart = Serial(port=serial_port_name.get(), baudrate=int(serial_port_speed.get()))
    if uart.is_open:
        uart.readline()
        measurements = []
        last_tx = time.time()
        while True:
            measurement = uart.readline().decode().strip()
            if '#' not in measurement:
                name, value = measurement.split('\t')
                path = [HOSTNAME] + name.split('/')[:-1]
                name = name.split('/')[-1]
                measurements.append(Metric(path, name, value, int(time.time())))
                if len(measurements) > 0 and (time.time()-last_tx) > 60:
                    db.send_metrics(measurements)
                    measurements.clear()
                    last_tx = time.time()
