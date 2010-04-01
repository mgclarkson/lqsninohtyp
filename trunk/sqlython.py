## Sources: http://www.mckoi.com/database/SQLSyntax.html
## Sources: http://txt2re.com
## Sources: http://gskinner.com/RegExr or http://gskinner.com/RegExr/desktop
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
## Capitalization of keywords. Standardize.
## 
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
  def __init__(self, parent, database, sql_insert):
    # Create class variable references
    self.parent = parent
    self.database = database
    self.sql_insert = sql_insert
    
    if DEBUG: print self.sql_insert

    while not self.sql_insert == '':
      if self.sql_insert.find(' ') > -1:
        case = self.sql_insert[0:self.sql_insert.find(' ')]
      else:
        case = self.sql_insert
      if (case == 'CREATE'):
        self.create()
      elif (case == 'ALTER'):
         self.alter()
      elif (case == 'INSERT'):
         self.insert()
      elif (case == 'TRIPLES'):
         print self.database['triples']
         s =  ", ".join(map(str, self.database['triples']))
         print s
         # print self.python
         parent.python += s
         # print self.python
         self.sql_insert = self.sql_insert[len(case):].strip()
      else:
        raise NameError('SQL: Statement incorrect or not yet supported: ' + case)
      if DEBUG: print
      
  def create(self):
    re1='(CREATE)'	# Word 1
    ws='(\\s+)'	# White Space 1
    re3='(TABLE)'	# Word 2
    re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
    re7='(\\(.*?\\(.*?\\)\\s+\\))'	# Round Braces 1
    re8='(\\(.*?\\s+\\))'	# Round Braces 1
    end = '(' + re7 + '|' + re8 + ')'

    rg = re.compile(re1+ws+re3+ws+re5+ws+end,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sql_insert)
    if m:
      table = m.group(5)
      list = m.group(7)
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
      if not table in self.database:
        self.database[table] = []
      else:
        raise NameError('SQL: Table already exists: ' + table)
      list = list[1:-1].split(',')
      for e in list:
        el = e.split()
        column = ''
        constraint = ''
        int = -1
        for i in range(len(el)):
          re9='.*?(\\(.*?\\)).*'	# Round Braces 1
          rg = re.compile(re9,re.IGNORECASE|re.DOTALL)
          m = rg.search(el[i])
          if m:
            constraint = el[i][0:el[i].find('(')]
            int = m.group(1)[1:-1]
          else:
            if column == '':
              column = el[i]
            else:
              constraint = el[i]
        # Create a column in the database with the name 'column'
        if not column in self.database[table]:
          self.database[table].append(column)
        else:
          raise NameError('SQL: Column name already exists: ' + column)
        if not table in self.database['constraints']:
          self.database['constraints'][table] = {}
        if not column in self.database['constraints'][table]:
          self.database['constraints'][table][column] = {}
        self.database['constraints'][table][column][constraint] = int
      if DEBUG: self.print_database()
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    
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

    rg = re.compile(re1+ws+re3+ws+re5+ws+re7+ws+end,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sql_insert)
    if m:
      table = m.group(5)
      value = eval(m.group(9))
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()

      columns = self.database[table]
      if not ((isinstance(value, str) and len(columns) == 1) or (len(value) == len(columns))):
        raise NameError('SQL: Statement incorrect:\n' + self.sql_insert)
        
      for i in range(len(columns)):
        if (isinstance(value, str)):
          data = value
        else:
          data = value[i]
        if not (table, columns[i], data) in self.database['triples']:
          if table in self.database['constraints'] and columns[i] in self.database['constraints'][table]:
            type = self.database['constraints'][table][columns[i]].keys()[0]
            type_val = self.database['constraints'][table][columns[i]][type]
            if type == 'VARCHAR':
              if len(data) > int(type_val):
                data = data[0:int(type_val)]
                print 'SQL: Inserted value trimmed to fit specified database limit: ' + data
            if type == 'INT':
              if not isinstance(int(data), int):
                raise NameError('SQL: Incorrect data type. Expected an INT: ' + data)
              data = int(data)
            self.database['triples'].append((table, columns[i], data))
        else:
          print 'SQL: Redundant information attempted insertion. Database not updated.'
            
      if DEBUG: self.print_database()
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    
  def print_database(self):
    print 'Database:'
    for key in self.database:
      print key, ':', self.database[key]
  
########################################################################
########################################################################
## No need to modify code below this line.
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
      index = line.find(self.sql_insertion_tag)
      if index > -1: # Handle insertion
        self.python += line[0:index]
        sql_insert = line[index + len(self.sql_insertion_tag):line.find(self.sql_insertion_end_tag)].strip()
        index = line.find(self.sql_insertion_end_tag)
        if index == -1:
          line = file.readline()
          index = line.find(self.sql_insertion_end_tag)
          while not index > -1: # Read insertion until EndTag
            sql_insert += line.strip() + ' '
            line = file.readline()
            index = line.find(self.sql_insertion_end_tag)
        # Modigy database by SQL statement
        SQL(self, self.database, sql_insert)
        self.python += line[index + len(self.sql_insertion_end_tag):]
      else: # Passively handle python text
        self.python += line
      line = file.readline()
    return self.python
        
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
    except:
      print 'Usage: sqlpython.py input [output]'
      return
      
    app = SQLinjection(arg[0])
      
    # Format the output file to have print a blank line in the terminal first
    python_code = app.run()
    
    try:
      arg.append(sys.argv[2])
      
      # Write parsed and converted code to python file
      output = open(arg[1], 'w')
      output.write(python_code)
      output.close()
    except:
      tmp = 0

    # Run new code
    exec python_code
    
########################################################################

if __name__ == '__main__':
  MainApp()