#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­
# Purpose: Script to check TXT connection and sounds.
# Date: 06­09­2018
# Author: M. Vogelaar
#
# Remarks: This script should play sounds available to the TXT.
# Note that a next sound can only be played when the first one
# is finished. Therefore we check in a loop if the sound
# was ended. Setting a volume works only when the connection
# is in 'direct mode'.
# Tested: Python 3, Ubuntu 16.04, Windows 10
#­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­

import ftrobopy
import sys

# plc = ftrobopy.ftrobopy("192.168.7.2")
plc = ftrobopy.ftrobopy("192.168.1.208")

print("Nombre del controlador: ", plc.getDevicename())
print("Version: ", plc.getVersionNumber())

for i in range(1,27):
    plc.play_sound(i, repeat=1, volume=10)
    while not plc.sound_finished():
        pass

