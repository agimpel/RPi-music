from speaker import Speaker
import time
import RPi.GPIO as GPIO


speaker = Speaker(GPIO.BCM, 23)

speaker.set_bpm(160)

#intro for speed
speaker.play('C1', 1/8)
speaker.pause(1/8)
speaker.play('C1', 1/8)
speaker.pause(1/8)
speaker.play('C1', 1/8)
speaker.pause(1/8)
speaker.play('C1', 1/8)
speaker.pause(1/8)


#1-4
speaker.pause(4)

#5
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)

#6
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)

#7
speaker.play('E1', 1/4)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)

#8
speaker.play('A1', 1/4)
speaker.play('G1', 1/4)
speaker.play('G1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)

#9
speaker.play('E1', 1/8)
speaker.play('E1', 1/4)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)
speaker.pause(1/8)
speaker.play('D1', 1/8)

#10
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/4)

#11
speaker.play('D1', 1/8)
speaker.play('D1', 1/8)
speaker.play('D1', 1/4)
speaker.play('D1', 1/4)
speaker.play('B0', 1/8)

#12
speaker.play('A0', 1/8)
speaker.play('G0', 1/8)
speaker.play('E0', 1/8)
speaker.play('E0', 1/8)
speaker.play('E0', 3/8)

#13
speaker.pause(1/8)
speaker.play('G1', 1/2)
speaker.play('F1X', 1/2)

#14
speaker.play('E1', 1/2)
speaker.play('D1', 1/2)

#15
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/2)

#16
speaker.pause(1)

#17
speaker.play('G1', 1/2)
speaker.play('F1X', 1/2)

#18
speaker.play('E1', 1/2)
speaker.play('D1', 1/2)

#19
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/2)

#20
speaker.pause(1)

#21
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)

#22
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)

#23
speaker.play('E1', 1/4)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/4)
speaker.play('E1', 1/8)

#24
speaker.play('A1', 1/4)
speaker.play('G1', 1/4)
speaker.play('G1', 1/8)
speaker.play('B0', 1/8)
speaker.play('D1', 1/4)

#25
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)
speaker.pause(1/8)
speaker.play('D1', 1/8)

#26
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/4)

#27
speaker.play('D1', 1/8)
speaker.play('D1', 1/8)
speaker.play('D1', 1/4)
speaker.play('D1', 1/4)
speaker.play('B0', 1/4)

#28
speaker.play('A0', 1/8)
speaker.play('G0', 1/8)
speaker.play('E0', 1/4)
speaker.play('E0', 1/4)
speaker.pause(1/4)

#29
speaker.play('G1', 1/2)
speaker.play('F1X', 1/2)

#30
speaker.play('E1', 1/2)
speaker.play('D1', 1/2)

#31
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/2)

#32
speaker.pause(1)

#33
speaker.play('G1', 1/2)
speaker.play('F1X', 1/2)

#34
speaker.play('E1', 1/2)
speaker.play('D1', 1/2)

#35
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/2)

#36
speaker.pause(1)

#37
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)

#38
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)

#39
speaker.play('E1', 1/4)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/8)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)

#40
speaker.play('A1', 1/4)
speaker.play('G1', 1/4)
speaker.play('G1', 1/8)
speaker.play('B0', 1/8)
speaker.play('D1', 1/4)

#41
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)
speaker.play('D1', 1/8)
speaker.play('E1', 1/4)
speaker.pause(1/4)

#42
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.play('D1', 1/4)

#43
speaker.play('D1', 1/8)
speaker.play('D1', 1/8)
speaker.play('D1', 1/8)
speaker.play('D1', 1/8)
speaker.play('D1', 1/8)
speaker.play('D1', 1/8)
speaker.play('B0', 1/4)

#44
speaker.play('A0', 1/8)
speaker.play('G0', 1/8)
speaker.play('E0', 1/4)
speaker.play('E0', 1/4)
speaker.pause(1/4)

#45
speaker.play('G1', 1/2)
speaker.play('F1X', 1/2)

#46
speaker.play('E1', 1/2)
speaker.play('D1', 1/2)

#47
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/2)

#48
speaker.pause(1)

#49
speaker.play('G1', 1/2)
speaker.play('F1X', 1/2)

#50
speaker.play('E1', 1/2)
speaker.play('D1', 1/2)

#51
speaker.play('E1', 1/4)
speaker.play('E1', 1/4)
speaker.pause(1/2)

#52
speaker.pause(1)







