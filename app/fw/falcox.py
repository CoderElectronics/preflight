import os, sys, serial, time

# Preflight v1.0 - FalcoX rmc control scheme
# by: Ari Stehney
#
# Compatible with FalcoX

def readConfig(fc):
    configText = ""
    ln = 0
    nd = 0
    while True:
        data = fc.readline()[:-2] #the last bit gets rid of the new-line chars

        if data:
            ln += 1
            if ln == 1:
                fc.write("dump\r".encode())
            
            if ln >= 3:
                configText += (data.decode("utf-8")+"\n")
                if configText.endswith("\nsave\n"):
                    break
                    
    return configText

def writeConfig(fc, config):
    config = config+"\n"
    fc.write(config.encode())
    fc.write("\nsave\n".encode())