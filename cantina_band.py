from speaker import Speaker
import time
import RPi.GPIO as GPIO


speaker = Speaker(GPIO.BCM, 23)

speaker.set_bpm(260)

speaker.pause(2)

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
speaker.play('F1', 3/8)
speaker.play('D1', 4/8)
speaker.pause(1/8)

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
speaker.play('C2', 1/8)
speaker.play('A1X', 1/4)
speaker.play('A1', 2/8)
speaker.play('G1', 3/8)

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

#11
speaker.play('C2', 1/4)
speaker.play('C2', 3/8)
speaker.play('F1', 1/8)
speaker.play('G1', 1/4)

#12
speaker.play('F1', 3/8)
speaker.play('D1', 4/8)
speaker.pause(1/8)

#13
speaker.play('D1', 1/2)
speaker.play('F1', 1/2)

#14
speaker.play('A1', 1/2)
speaker.play('C2', 1/2)

#15-16
speaker.play('D2X', 1/4)
speaker.play('D2', 1/4)
speaker.play('G1X', 1/8)
speaker.play('A1', 1/4)
speaker.play('F1', 1/4)
speaker.pause(7/8)

#17
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.pause(1/4)

#18
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.pause(1/4)

#19-20
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('C2X', 1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 4/8)
speaker.play('F1', 5/8)

#21
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.pause(1/4)

#22
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.pause(1/4)

#23-24
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('C2X', 1/8)
speaker.play('D2', 1/4)
speaker.play('C2', 4/8)
speaker.play('E1', 5/8)

#25
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.pause(1/4)

#26
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('D2', 1/4)
speaker.pause(1/4)

#27-28
speaker.pause(1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 1/8)
speaker.play('C2X', 1/8)
speaker.play('D2', 1/4)
speaker.play('A1', 4/8)
speaker.play('F1', 5/8)

#29
speaker.pause(1/4)
speaker.play('A1X', 1/4)
speaker.pause(1/4)
speaker.play('B1', 1/4)

#30
speaker.play('C2X', 1/8)
speaker.play('D2', 3/8)
speaker.play('F1', 5/8)

#31-32
speaker.play('D1', 1/8)
speaker.play('F1', 1/8)
speaker.play('A1X', 1/8)
speaker.play('D2', 1/8)
speaker.play('G1X', 1/8)
speaker.play('A1', 1/4)
speaker.play('F1', 5/8)
