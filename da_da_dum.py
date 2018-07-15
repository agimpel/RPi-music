from speaker import Speaker
import time
import RPi.GPIO as GPIO


speaker = Speaker(GPIO.BCM, 23)

speaker.set_bpm(400)
speaker.set_notepause(0.01)

speaker.pause(1)

#1
speaker.play('C2', 1/16)
speaker.play('C2X', 1/16)
speaker.play('D2', 1/8)
speaker.pause(3/4)

#2
speaker.play('B1', 1/4)
speaker.play('F2', 1/4)
speaker.pause(1/4)
speaker.play('F2', 1/4)

#3
speaker.play('F2', 1/3)
speaker.play('E2', 1/3)
speaker.play('D2', 1/3)

#4
speaker.play('C2', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/4)
speaker.play('E1', 1/4)

#5
speaker.play('C1', 1/4)











