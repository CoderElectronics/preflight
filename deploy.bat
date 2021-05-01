@echo off

clean

cd app
pyinstaller --onefile preflight-beta.spec
xcopy dist ..\targets\downloads
cd ..

cd targets
surge .
cd ..