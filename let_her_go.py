from speaker import Speaker
import time
import RPi.GPIO as GPIO


speaker = Speaker(GPIO.BCM, 23)

speaker.set_bpm(140)

speaker.pause(2)

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
speaker.play('B1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#10
speaker.play('G1', 1/4)
speaker.play('G1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 1/4)

#11
speaker.pause(1/2)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#12
speaker.play('A1', 1/4)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)
speaker.play('B1', 1/4)
speaker.play('A1', 1/8)
speaker.play('A1', 1/8)

#13
speaker.play('G1', 1/2)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#14-15
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('G1', 6/8)
speaker.pause(1/2)

#16
speaker.pause(1)

#17
speaker.pause(1/4)
speaker.play('B1', 1/8)
speaker.play('B1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#18
speaker.play('G1', 1/4)
speaker.play('G1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 1/8)
speaker.play('E1', 1/8)
speaker.play('G1', 1/4)

#19
speaker.pause(1/2)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#20
speaker.play('A1', 1/4)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)
speaker.play('B1', 1/4)
speaker.play('A1', 1/8)
speaker.play('A1', 1/8)

#21
speaker.play('G1', 1/2)
speaker.play('A1', 1/8)
speaker.play('B1', 1/8)
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)

#22
speaker.play('A1', 1/8)
speaker.play('G1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('G1', 6/8)








