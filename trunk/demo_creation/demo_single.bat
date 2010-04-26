@echo off

more header.txt > ..\test\%1_demo.py
echo ### %1.py2 >> ..\test\%1_demo.py 
echo ##################### >> ..\test\%1_demo.py 
echo. >> ..\test\%1_demo.py 
more ..\test\%1.py2 >> ..\test\%1_demo.py 
more spacer_1.txt >> ..\test\%1_demo.py
..\python2.py ..\test\%1.py2 ..\output.py 
more ..\output.py >> ..\test\%1_demo.py
more spacer_2.txt >> ..\test\%1_demo.py
python ..\python2.py ..\test\%1.py2 >> ..\test\%1_demo.py
