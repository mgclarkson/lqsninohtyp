@echo off
cls 

for /f %%c in (commandset.txt) do call demo_single.bat %%c

call > full.py
for /f %%c in (commandset.txt) do call more ..\test\%%c_demo.py >> full.py