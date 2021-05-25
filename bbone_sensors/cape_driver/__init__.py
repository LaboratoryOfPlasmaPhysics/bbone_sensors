import time

try:
    import Adafruit_BBIO.GPIO as GPIO
except ImportError:
    class GPIO:
        OUT = None
        HIGH = None
        LOW = None

        @staticmethod
        def setup(*args):
            pass

        @staticmethod
        def output(*args):
            pass

RESET_PIN = "P9_15"
BOOT0_PIN = "P9_23"


def config_gpio():
    GPIO.setup(BOOT0_PIN, GPIO.OUT)
    GPIO.output(BOOT0_PIN, GPIO.LOW)
    GPIO.setup(RESET_PIN, GPIO.OUT)


def reset_cape():
    GPIO.output(BOOT0_PIN, GPIO.LOW)
    GPIO.output(RESET_PIN, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(RESET_PIN, GPIO.HIGH)


def start_bootloader():
    GPIO.output(BOOT0_PIN, GPIO.HIGH)
    GPIO.output(RESET_PIN, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(RESET_PIN, GPIO.HIGH)
    time.sleep(0.01)
