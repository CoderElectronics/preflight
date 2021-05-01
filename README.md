![](targets/img/logo.png)
# Preflight Beta

Preflight is a tool to repair, backup, or reset your racing drone's configuration in the easiest way possible. Simply download the app, and select your Prebuilt FPV drone model to reset your config.
<br><br>
We are working with companies that sell FPV racing drones to unify all of the configuration work neccesary to keep you up in the air! 

## Requirements to Compile
1. Node.js and NPM<br>
2. Python3 and Pip3<br>
## Compiling

Just run the `deploy.bat` file to create the EXE and deploy the static content to surge.
<br>

If you just want to compile the EXE (the best option), open the app directory and install all the required dependencies. Then run pyinstaller to make the EXE.
```bash
npm i -g surge
pip3 install -r app\requirements.txt
build.bat
```
<br>

This will put a release executable in the `app/dist/` folder. Once you are done, To clean the build environment, run `clean.bat`


## Supported Firmware
- Betaflight <br>
- Cleanflight <br>
- iNav <br>
- Butterflight <br>
- Betaflight <br>
- Emuflight <br>
- FalcoX <br>
- Kiss / Fettec (Not implemented yet) <br>