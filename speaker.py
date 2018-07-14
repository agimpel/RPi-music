import time
import RPi.GPIO as GPIO


class Speaker:

    pin = False

    # frequency data (Hz)
    frequencies = {
        'C0': 130.81,
        'C0X': 138.59,
        'D0': 146.83,
        'D0X': 155.56,
        'E0': 164.81,
        'F0': 174.61,
        'F0X': 185.00,
        'G0': 196.00,
        'G0X': 207.65,
        'A0': 220.00,
        'A0X': 233.08,
        'B0': 246.94,
        'C1': 261.63,
        'C1X': 277.18,
        'D1': 293.66,
        'D1X': 311.13,
        'E1': 329.63,
        'F1': 349.23,
        'F1X': 369.99,
        'G1': 391.00,
        'G1X': 415.30,
        'A1': 440.00,
        'A1X': 466.16,
        'B1': 493.88,
        'C2': 523.25,
        'C2X': 554.37,
        'D2': 587.33,
        'D2X': 622.25,
        'E2': 659.26,
        'F2': 698.46,
        'F2X': 739.99,
        'G2': 783.99,
        'G2X': 830.61,
        'A2': 880.00,
        'A2X': 923.33,
        'B2': 987.77,
        'C3': 1046.50
    }


    # speed of music
    bpm = 120 # beats per minute
    speed = 0.5 # seconds per beat

    # pause after every note
    note_pause = 0.05

    # current frequency
    frequency = 440.00

    # current duty cycle
    dutycycle = 0
    note_dc = 1
    pause_dc = 0
    

    def __init__(self, mode, pin):
        GPIO.setmode(mode)
        GPIO.setup(pin, GPIO.OUT)
        self.pin = GPIO.PWM(pin, self.frequency)
        self.pin.start(self.dutycycle)

    
    def __del__(self):
        self.pin.stop()
        GPIO.cleanup()


    def set_bpm(self, bpm):
        self.bpm = bpm
        self.speed = 60/bpm


    def play(self, note, duration):
        self.dutycycle = self.note_dc
        self.frequency = self.frequencies[note]
        self.pin.ChangeDutyCycle(self.dutycycle)
        self.pin.ChangeFrequency(self.frequency)
        time.sleep(duration*4*self.speed - self.note_pause)
        self.pause(self.note_pause)

    
    def pause(self, duration):
        self.dutycycle = self.pause_dc
        self.pin.ChangeDutyCycle(self.dutycycle)
        time.sleep(duration*4*self.speed)