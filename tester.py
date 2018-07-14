from speaker import Speaker
import time
import RPi.GPIO as GPIO


speaker = Speaker(GPIO.BCM, 23)



speaker.play('C1', 1)
speaker.play('D1', 1)
speaker.play('E1', 1)
speaker.pause(1)
speaker.play('F1', 1)
speaker.play('G1', 1)
speaker.play('A1', 1)
speaker.play('B1', 1)
speaker.play('C2', 1)