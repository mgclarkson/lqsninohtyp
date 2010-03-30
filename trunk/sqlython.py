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

DEBUG = True

########################################################################

'''
  Where the SQL injection gets translated into python code.
'''

class SQL:
  def __init__(self, database, sql_insert):
    if DEBUG: print sql_insert

    # Create reference for database within SQL Class
    self.database = database
    
    # Find SQL Command
    case = sql_insert[0:sql_insert.find(' ')]
    sql_insert = sql_insert[sql_insert.find(' '):].strip()
    
    # Match SQL Command and begin parsing
    if (case == 'CREATE'):
      self.create(sql_insert)
    elif (case == 'ALTER'):
       self.alter(sql_insert)
    elif (case == 'INSERT'):
       self.insert(sql_insert)
    else:
      print 'NON-IMPLEMENTED SQL INSERTION: ' + case
    print
      
  # CREATE
  def create(self, sql_insert):
    item, sql_insert = self.parse(sql_insert, ' ')
    if item == 'TABLE':
      # Create a table in the database with the name 'item_name'
      item_name, sql_insert = self.parse(sql_insert, ' ')
      self.database[item_name] = {}
      
      # Create a column in the database with the name 'column'
      column, sql_insert = self.parse(sql_insert, ' ')
      self.database[item_name] = []
      self.database[item_name].append(column[1:])
      
      # ERROR: Assumes constraint to exist. (Runs on looking for '('.) FIX! Only for demo purpose.
      constraint_type, sql_insert = self.parse(sql_insert, '(')
      
      if not constraint_type == '': # If constraints exist
        # Create special '_constraints' table
        self.database[item_name + '_' + column[1:] + '_constraints'] = {}
        
        # Create VARCHAR constraint
        if constraint_type == 'VARCHAR':
          constraint_arg, sql_insert = self.parse(sql_insert, ')')
          self.database[item_name + '_' + column[1:] + '_constraints'][constraint_type] = constraint_arg[1:]
          
      if DEBUG: self.print_database()
    
  # ALTER
  def alter(self, sql_insert):
    print 'ALTER'
    
  # INSERT
  def insert(self, sql_insert):
    # Parse statement
    keyword, sql_insert = self.parse(sql_insert, ' ')
    table, sql_insert = self.parse(sql_insert, ' ')
    keyword, sql_insert = self.parse(sql_insert, ' ')
    value, sql_insert = self.parse(sql_insert, ')')
    value = value[1:].strip('\'')
    
    # Get column names for RDF
    columns = self.database[table]
    
    # Append the triple to the database
    self.database['triples'].append((table, columns[0], value))
    
    if DEBUG: self.print_database()
    
  # Helper method for continous parsing
  def parse(self, sql_insert, symbol):
    item = sql_insert[0:sql_insert.find(symbol)]
    sql_insert = sql_insert[sql_insert.find(symbol):].strip()
    return (item, sql_insert)
    
  def print_database(self):
    print 'Database:'
    for key in self.database:
      print key, ':', self.database[key]
  
########################################################################
########################################################################
## No need to modify code below this line.
## EDIT: UNTIL INLINE SQL INJECTION QUERIES ARE HANDLED. EG FOR LOOPS
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
    self.python = ''
    
  def run(self):
    file = open(self.filename,'r')
    line = file.readline()
    
    while line: # Read each line and identify sql insertions
      if self.isBeginTag(line): # Handle insertion
        sql_insert = ''
        line = file.readline()
        while not self.isEndTag(line): # Read insertion until EndTag
          sql_insert += line.strip()
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