import os, sys, serial, time

# Preflight v1.0 - Betaflight rmc control scheme
# by: Ari Stehney
#
# Compatible with iNav, Emuflight, Betaflight, Cleanflight, and Butterflight

def readConfig(fc):
    configText = ""
    fc.write("#\r".encode())
    ln = 0
    nd = 0
    while True:
        data = fc.readline()[:-2] #the last bit gets rid of the new-line chars

        if data:
            ln += 1
            if ln == 1:
                fc.write("diff all\r".encode())
            
            if ln >= 3:
                configText += (data.decode("utf-8")+"\n")
                if configText.endswith("\nsave\n"):
                    fc.write("save\r".encode())
                    break
                    
    return configText

def writeConfig(fc, config):
    fc.write("#\r".encode())
    config = config+"\n"
    ln = 0
    connection = True
    while connection:
        data = fc.readline()[:-2] #the last bit gets rid of the new-line chars

        if data:
            ln += 1
            if ln == 1:
                fc.write(config.encode())
                break