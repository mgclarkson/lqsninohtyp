## Sources: http://www.mckoi.com/database/SQLSyntax.html
## Goal:
## To use SQL injection within python using RDL building techniques on dictionaries
## and to perform additional sample operations on top of the full python library and the usual subset of SQL:
##   if sql:[TABLE]:
##   if i in sql:[TABLE][COLUMN]:
##   for i in sql:[TABLE][COLUMN]:
##   for i in sql:[TABLE]:
##   print sql:[TABLE]
##   
## FIX:
## Handle line breaks as spaces and don't strip those
## Inline tags
## Multiple sql statements in a tag
## 
## 

import sys
import os
import subprocess
import re

DEBUG = True

########################################################################

'''
  Where the SQL injection gets translated into python code.
'''

class SQL:
  def __init__(self, database, sql_insert):
    # Create class variable references
    self.database = database
    self.sql_insert = sql_insert
    
    if DEBUG: print self.sql_insert

    while not self.sql_insert == '':
      case = self.sql_insert[0:self.sql_insert.find(' ')]
      if (case == 'CREATE'):
        self.create()
      elif (case == 'ALTER'):
         self.alter()
      elif (case == 'INSERT'):
         self.insert()
      else:
        raise NameError('SQL statement incorrect or not yet supported: ' + case)
      print
      
  def create(self):
    re1='(CREATE)'	# Word 1
    ws='(\\s+)'	# White Space 1
    re3='(TABLE)'	# Word 2
    var='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
    re7='(\\()'	# Any Single Character 1
    re11='(VARCHAR)'	# Word 3
    re12='(\\()'	# Any Single Character 2
    re13='(\\d+)'	# Integer Number 1
    re14='.*?'	# Non-greedy match on filler
    re16='(\\))'	# Any Single Character 3

    rg = re.compile(re1+ws+re3+ws+var+ws+re7+ws+var+ws+re11+re12+re13+re14+ws+re16,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sql_insert)
    if m:
      table=m.group(5)
      column=m.group(9)
      varchar=m.group(11)
      int=m.group(13)
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()

      # Create a column in the database with the name 'column'
      self.database[table] = []
      self.database[table].append(column)
      
      # Create VARCHAR constraint
      if varchar == 'VARCHAR':
        if not table in self.database['constraints']:
          self.database['constraints'][table] = {}
        if not column in self.database['constraints'][table]:
          self.database['constraints'][table][column] = {}
        self.database['constraints'][table][column][varchar] = int
      if DEBUG: self.print_database()
    else:
      raise NameError('SQL statement incorrect or not yet supported:\n' + self.sql_insert)
    
  def alter(self):
    print 'ALTER'
    
  def insert(self):
    re1='(INSERT)'	# Word 1
    ws='(\\s+)'	# White Space 1
    re3='(INTO)'	# Word 2
    re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
    re7='(VALUES)'	# Word 3
    re9='(\\(.*?\\))'	# Round Braces 1
    braceCSVbrace='((\()(.*?),(.*)(\)))'
    end = '(' + re9 + '|' + braceCSVbrace + ')'
    remainder='.*?'

    rg = re.compile(re1+ws+re3+ws+re5+ws+re7+ws+end+remainder,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sql_insert)
    if m:
      table = m.group(5)
      value = eval(m.group(9))
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()

      columns = self.database[table]
      for column in columns:
        self.database['triples'].append((table, column, value))
      if DEBUG: self.print_database()
    else:
      raise NameError('SQL statement incorrect or not yet supported:\n' + self.sql_insert)
    
  def print_database(self):
    print 'Database:'
    for key in self.database:
      print key, ':', self.database[key]
  
########################################################################
########################################################################
## No need to modify code below this line.
## EDIT: UNTIL INLINE SQL INJECTION QUERIES ARE HANDLED. EG (FOR LOOPS)
########################################################################
########################################################################

'''
  No need to change any of this code.
  Merely handles SQLinjection tags and passes them to the SQL class.
'''

class SQLinjection:
  def __init__(self, filename):
    # Read from 'sql:' to ':sql'
    self.sql_insertion_tag = 'sql:'
    self.sql_insertion_end_tag = self.sql_insertion_tag[-1:] + self.sql_insertion_tag[0:-1]
    self.filename = filename
    self.database = {}
    self.database['triples'] = []
    self.database['constraints'] = {}
    self.python = ''
    
  def run(self):
    file = open(self.filename,'r')
    line = file.readline()
    
    while line: # Read each line and identify sql insertions
      if self.isBeginTag(line): # Handle insertion
        sql_insert = ''
        line = file.readline()
        while not self.isEndTag(line): # Read insertion until EndTag
          sql_insert += line.strip() + ' '
          line = file.readline()
        # Modigy database by SQL statement
        SQL(self.database, sql_insert)
      else: # Passively handle python text
        self.python = self.python + line
      line = file.readline()
    return self.python
      
  # Helper function for if SQLinjection has begun
  def isBeginTag(self, line):
    if line.strip()[0:len(self.sql_insertion_tag)] == self.sql_insertion_tag:
      return True
  
  # Helper function for if SQLinjection has ended
  def isEndTag(self, line):
    if line.strip()[0:len(self.sql_insertion_end_tag)] == self.sql_insertion_end_tag:
      return True
        
########################################################################

'''
  No need to modify any of this code.
  Main function: 
    Run SQLinjection parser on argv[1]. 
    Write code to argv[2].
    Run argv[2].
'''

class MainApp:
  def __init__(self):
    # Run custom script for identifiying SQLinjections
    arg = []
    try:
      arg.append(sys.argv[1])
      arg.append(sys.argv[2])
    except:
      print 'Usage: sqlpython.py input output'
      return
    app = SQLinjection(arg[0])
      
    # Format the output file to have print a blank line in the terminal first
    python_code = '# clear new terminal line \nprint \n\n' + app.run()
    
    # Write parsed and converted code to python file
    output = open(arg[1], 'w')
    output.write(python_code)
    output.close()
    
    # Run new code
    child = subprocess.Popen("python output.py")
    
########################################################################

if __name__ == '__main__':
  MainApp()