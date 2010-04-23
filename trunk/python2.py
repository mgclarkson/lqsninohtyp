#!/usr/bin/env python

## Sources: http://www.w3schools.com/sql/default.asp
## Sources: http://www.mckoi.com/database/SQLSyntax.html
## Sources: http://txt2re.com/index-python.php3
## Sources: http://gskinner.com/RegExr
## Sources: http://gskinner.com/RegExr/desktop
##
## Goal:
## To use SQL injection within python using RDL building techniques on dictionaries
## and to perform additional sample operations on top of the full python library and the usual subset of SQL:
##   if i in sql:[table]:sql  == if i in sql:CONTENTS SELECT * FROM table:sql -J
##   if i in sql:[table][COLUMN]:sql == if i in sql:CONTENTS SELECT column FROM table:sql -J
##   
##   for i in sql:[table][COLUMN]:sql == for i in sql:SELECT column FROM table:sql -J
##   for i in sql:[table]:sql  == for i in sql:SELECT * FROM table:sql -J
##   
##   for i in sql:TRIPLES:sql -J
##   for i in sql:CONTENTS SELECT * FROM table:sql -J
##   
##   print sql:PRINT SELECT * FROM table:sql -J
##   
##   USING STANDARD PYTHON COMMAND LINE FOR LINE BY LINE EVAL (...SHOULD BLOW HIM AWAY) - J
##   USING PIPE USAGE - J
##   
##  COMMANDS:
##    CREATE TABLE -J
##    DROP INDEX -J
##    DROP TABLE -J
##    INSERT -J                     ---second form not implemented
##    SELECT -J
##    SELECT DISTINCT -J
##    SELECT WHERE -J
##    TRUNCATE TABLE -J
##    ALTER TABLE -M
##    UPDATE -M
##    DELETE -M
##    JOIN -M'll do
##    UNION -M
##    ORDER BY in SELECT -J
##    TOP in SELECT -J'll do
##    IN in WHERE -M'll do
##    BETWEEN in WHERE -M'll do
##    WILDCARDS? in WHERE
##    ALIAS?
##    SELECT INTO
##    CONSTRAINTS(6) in CREATE -??
##    CREATE INDEX
##    DROP INDEX
##    INCREMENT in CREATE & INSERT
##    VIEWS?
##    NULL in WHERE & INSERT
##    
##  DATATYPES in INSERT (CREATE already implemented -J):
##    varchar(n)
##    text
##    bit
##    bigint
##    real
##    
##  NOT IMPLEMETING:
##    CREATE DB
##    DATES()
##    LIKE in WHERE
##    
##  NOTES:
##  Between, In, and Like SQL operators are not yet implemented in WHERE.
##  
## URGENT:
## None Currently
## 
## TO FIX:
## Stop erroring out due to blankness in print select
## Get all demos to be good... like update.
## 
## DONE:
## Create+ white space -J
## Redirect CommandGUI -J
## Catch KeyboardInterrupt -J
## Handle line breaks as spaces and don't strip those -J
## Inline tags -J
## Multiple sql statements in a tag -J
## Capitalization of keywords. Standardize. -J
## Find reason for slow WHERE processing -J
## Accept more than 3 vars in create (no error, following INSERT code was messed up) -J
## 
## TO RUN: -J
##   Windows:
##    python2.py file.py2
##    python2.py --console
##  Linux:
##    setup.py
##      then:
##        file.py2        (No need for python2.py)
##    python2.py file.py2
##    python2.py --console
##    cat file.py2 | python2.py
##    python2.py < file.py2
## 
## 
## 

import sys
from CommandGUI import *
from SQLinjection import *

DEBUG = False
# DEBUG = True

########################################################################

class Python2:
  def __init__(self):
    
    # Handle a piped in file and run python2 and exit
    if not sys.stdin.isatty():
      code = ''
      for s in sys.stdin.readlines():
        code += s
      app = SQLinjection()
      python_code = app.run(code)    
      exec python_code
      sys.exit()
    
    # Check command line arguments
    arg = sys.argv[1:]
    if len(arg) == 0 or len(arg) > 2:
      print 'Usage: \tsqlpython.py inputFile [converted_output_file]'
      print '\tsqlpython.py --console'
      print
      print 'Linux (additional):'
      print '\t"code" | sqlpython.py'
      print '\tsqlpython.py < file'
      print
      print 'Run setup.py in Linux to allow for automatic file execution. \n(For code in the same directory as python2.py.)'
      return
    
    # If argument is console, run the python2 console
    if arg[0] == '-console' or arg[0] == '--console':
      CommandGUI()
    else: # Get the filename and read the python2 code
      file = open(arg[0],'r')
      code = file.read()
      app = SQLinjection()
      python_code = app.run(code)    
      file.close()
      try:
        # Write parsed and converted code to python file
        output = open(arg[1], 'w')
        output.write(python_code)
        output.close()
      except:
        tmp = 0

      # Run new code
      exec python_code
    
if __name__ == '__main__':
  Python2()
  
