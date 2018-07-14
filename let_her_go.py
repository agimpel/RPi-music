from speaker import Speaker
import time
import RPi.GPIO as GPIO


speaker = Speaker(GPIO.BCM, 23)

speaker.set_bpm(140)

#0
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#1-2
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 3/8)
speaker.play('E1', 1/4)
speaker.play('B1', 5/8)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#3
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 3/8)
speaker.play('E1', 1/8)
speaker.play('B1', 1/4)

#4
speaker.play('A1', 1/2)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#5
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 3/8)
speaker.play('E1', 1/4)
speaker.play('G1', 1/8)

#6-7
speaker.play('D2', 1/8)
speaker.play('B1', 3/8)
speaker.play('G1', 1/8)
speaker.play('A1', 1/4)
speaker.play('B1', 9/8)

#8
speaker.pause(1/2)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#1-2
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 3/8)
speaker.play('E1', 1/4)
speaker.play('B1', 5/8)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#3
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 3/8)
speaker.play('E1', 1/8)
speaker.play('B1', 1/4)

#4
speaker.play('A1', 1/2)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#5
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 3/8)
speaker.play('E1', 1/4)
speaker.play('G1', 1/8)

#6-7
speaker.play('D2', 1/8)
speaker.play('B1', 3/8)
speaker.play('G1', 1/8)
speaker.play('A1', 1/4)
speaker.play('B1', 9/8)

#9
speaker.pause(1/4)














