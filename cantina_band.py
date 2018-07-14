from speaker import Speaker
import time
import RPi.GPIO as GPIO


speaker = Speaker(GPIO.BCM, 23)

speaker.set_bpm(150)

#1
speaker.play('A1', 1/4)
speaker.play('D2', 1/4)
speaker.play('A1', 1/4)
speaker.play('D2', 1/4)

#2
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.pause(1/8)
speaker.play('G1X', 1/8)
speaker.play('A1', 1/4)

#3
speaker.play('A1', 1/8)
speaker.play('G1X', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)
speaker.pause(1/8)
speaker.play('F1X', 1/8)
speaker.play('G1', 1/4)

#4
speaker.play('F1', 1/2)
speaker.play('D1', 1/2)

#5
speaker.play('A1', 1/4)
speaker.play('D2', 1/4)
speaker.play('A1', 1/4)
speaker.play('D2', 1/4)

#6
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.pause(1/8)
speaker.play('G1X', 1/8)
speaker.play('A1', 1/4)

#7
speaker.play('G1', 1/4)
speaker.play('G1', 1/4)
speaker.pause(1/8)
speaker.play('F1X', 1/8)
speaker.play('G1', 1/8)

#8
speaker.play('C2', 1/4)
speaker.play('A1X', 1/4)
speaker.play('G1', 1/4)
speaker.play('F1X', 1/4)

#9
speaker.play('A1', 1/4)
speaker.play('D2', 1/4)
speaker.play('A1', 1/4)
speaker.play('D2', 1/4)

#10
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.pause(1/8)
speaker.play('G1X', 1/8)
speaker.play('A1', 1/4)














