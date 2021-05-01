# Preflight Beta

Preflight is a tool to repair or reset your racing drone's configuration in the easiest way possible. Simply download the app, and select your FPV drone model to reset your config.
<Br>
We work with companies that sell FPV racing drones to unify all of the configuration work neccesary to keep you up in the air! This is where all of the configs are stored, checkout our github page for more details.

## Compiling

Just run the `build.bat` file to create the EXE and deploy the static content to surge.
<br>

If you just want to compile the EXE (the best option), open the app directory and install all the required dependencies. Then run pyinstaller to make the EXE.
```bash
npm i -g surge
pip3 install -r app\requirements.txt
pyinstaller --onefile preflight-beta.spec
```