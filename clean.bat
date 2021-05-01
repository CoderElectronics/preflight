@echo off
rmdir /Q /S "app\build"
rmdir /Q /S "app\dist"
rmdir /Q /S "app\__pycache__"

del /Q /S "targets\downloads\*.exe"