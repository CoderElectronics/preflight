import os, sys, platform, serial, time, eel, eel.browsers, requests, glob, json
from sys import platform as plat

# Preflight v1.0 - one click FPV drone config application
# by: Ari Stehney
#
# Compatible with iNav, Emuflight, Betaflight, and Butterflight

eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')

import fw.btfl as btfl
import fw.fettec as kiss_fettec
import fw.kiss as kiss_vanilla
import fw.falcox as falcox

configTargets = {
    "BTFL": btfl,
    "FLKX": falcox,
    "FKIS": kiss_fettec,
    "KISS": kiss_vanilla
}

releaseurl = "https://preflight-dl.surge.sh/targets/tr.json"
confbaseurl = "https://preflight-dl.surge.sh/targets/"

"""
def press():
    comport = serial.Serial('COM4', 115200, timeout=.8)
    config = configTargets["Betaflight"].readConfig(comport)
    print(config)

"""
# eel init
eel.init('web')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

# main web ui actions
@eel.expose
def action_readconfig(com, target):
    try:
        comport = serial.Serial(com, 115200, timeout=.8)
        config = configTargets[target].readConfig(comport)
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        return -1
    else:
        return config
    

@eel.expose
def action_scanports():
    return json.dumps(serial_ports())

@eel.expose
def action_driverinstall():
    if plat == "linux" or plat == "linux2":
        # Linux, Nothing to do here....
        return 1
    elif plat == "darwin":
        # OSX, Nothing to do here....
        return 1
    elif plat == "win32":
        # Windows driver stuff
        os.startfile(resource_path("fw/bin/impulserc-drivers.exe"))
        return 0

@eel.expose
def action_getrelease():
    try:
        response = requests.get(releaseurl)
        response.raise_for_status()

    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        return "-1"
    else:
        return response.text
        print('Success!')

@eel.expose
def action_writeconfig(com, target, targurl):
    vbase = confbaseurl+targurl
    try:
        response = requests.get(vbase)
        response.raise_for_status()

    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        return -1
    else:
        try:
            comport = serial.Serial(com, 115200, timeout=.8)
            configTargets[target].writeConfig(comport, response.text)
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
            return -1
        else:
            return 0

@eel.expose
def action_writecustomconfig(com, target, confscript):
    try:
        comport = serial.Serial(com, 115200, timeout=.8)
        configTargets[target].writeConfig(comport, confscript)
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        return -1
    else:
        return 0

# actually start eel webui

eel.start('index.html', size=(600, 600), mode='custom', cmdline_args=[resource_path('node_modules/electron/dist/electron'), resource_path(".")])  # Start