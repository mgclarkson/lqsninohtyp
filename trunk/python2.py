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
##    INSERT -J
##    SELECT -J
##    SELECT DISTINCT -J
##    SELECT WHERE -J
##    TRUNCATE TABLE -J
##    ALTER TABLE
##    UPDATE 
##    DELETE
##    JOINS(4)
##    UNION 
##    INSERT INTO
##    WHERE (AND | OR) in WHERE -J'll do
##    ORDER BY in SELECT -J'll do
##    TOP in SELECT -J'll do
##    LIKE in WHERE -J'll do
##    IN in WHERE -J'll do
##    BETWEEN in WHERE -J'll do
##    WILDCARDS? in WHERE
##    ALIAS?
##    SELECT INTO
##    CONSTRAINTS(6) in CREATE -J'll do
##    CREATE INDEX
##    DROP INDEX
##    INCREMENT in CREATE & INSERT -J'll do
##    VIEWS?
##    NULL in WHERE & INSERT -J'll do
##    
##  DATATYPES in INSERT (CREATE already implemented -J):
##    char(n)
##    text
##    bit
##    bigint
##    real
##    date?
##    time?
##    datetime?
##    
##  NOT IMPLEMETING:
##    CREATE DB
##    DATES()
##    
##  NOTES:
##  Between, In, and Like SQL operators are not yet implemented in WHERE.
##  
## URGENT:
## None Currently
## 
## TO FIX:
## Catch KeyboardInterrupt
## Redirect CommandGUI
## Create+ white space
## 
## DONE:
## Handle line breaks as spaces and don't strip those -J
## Inline tags -J
## Multiple sql statements in a tag -J
## Capitalization of keywords. Standardize. -J
## Find reason for slow WHERE processing -J
## Accept more than 3 vars in create (no error, following INSERT code was messed up) -J
## 
## 
## 

import sys
import os
import subprocess
import re

DEBUG = False
# DEBUG = True

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
    self.last_table = ''
    self.last_selection = []
    
    if DEBUG: print self.sql_insert

    while not self.sql_insert == '':
      if self.sql_insert.find(' ') > -1:
        case = self.sql_insert[0:self.sql_insert.find(' ')]
      else:
        case = self.sql_insert
      case = case.upper()
      if (case == 'CREATE'):
        self.create()
      elif (case == 'ALTER'):
        self.alter()
      elif (case == 'DROP'):
        self.drop()
      elif (case == 'INSERT'):
        self.insert()
      elif (case == 'SELECT'):
        s = self.select()
        parent.python += s
      elif (case == 'TRUNCATE'):
        self.truncate()
      elif (case == 'PRINT'):
        self.sql_insert = self.sql_insert[len(case):].strip()
        parent.python += self.print_select(self.select())

      # Non-standard SQL   
      elif (case == 'CONTENTS'):
        self.sql_insert = self.sql_insert[len(case):].strip()
        s = self.select()
        s = '[' + s.replace('[', '').replace(']', '') + ']'
        parent.python += s
      elif (case == 'TRIPLES'):
        s =  ", ".join(map(str, self.database['triples']))
        parent.python += s
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
      fields = table + '_fields'
      list = m.group(7)
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
      if not table in self.database:
        self.database[table] = []
        self.database[fields] = []
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
        if not column in self.database[fields]:
          self.database[fields].append(column)
        else:
          raise NameError('SQL: Column name already exists: ' + column)
        if not table in self.database['constraints']:
          self.database['constraints'][table] = {}
        if not column in self.database['constraints'][table]:
          self.database['constraints'][table][column] = {}
        self.database['constraints'][table][column][constraint.upper()] = int
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    if DEBUG: self.print_database()
      
  def alter(self):
    re1='(ALTER)'	# Word 1
    ws='(\\s+)'	# White Space
    re3='(TABLE)'	# Word 2
    
    re5='((?:[a-z][a-z0-9_]*))'	# tableName
    re6='((?:[a-z][a-z0-9_]*))'	# columnName
    re7='((?:[a-z][a-z0-9_]*))'	# dataType
    
    addc='(ADD)'	# Word 3
    dropc='(DROP\\s+COLUMN)' # Word 3
    alterc='(ALTER\\s+COLUMN)' # Word 3
    
    rg = re.compile(re1+ws+re3+ws+re5+ws+addc+ws+re6+ws+re7,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sqlinsert)
    
    rg = re.compile(re1+ws+re3+ws+re5+ws+dropc+ws+re6,re.IGNORECASE|re.DOTALL)
    dc = rg.search(self.sqlinsert)
    
    rg = re.compile(re1+ws+re3+ws+re5+ws+alterc+ws+re6+ws+re7,re.IGNORECASE|re.DOTALL)
    ac = rg.search(self.sqlinsert)
    
    if m:
      table=m.group(11)
      ##TODO
    elif dc:
      table=dc.group(9)
      ##TODO
    elif ac:
      table=ac.group(11)
      #TODO
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
  

  def drop(self):
    re1='(DROP)'	# Variable Name 1
    ws='(\\s+)'	# White Space 1
    re3='(INDEX)'	# Variable Name 2
    re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 3
    re7='(ON)'	# Word 1
    re9='((?:[a-z][a-z0-9_]*))'	# Variable Name 4
    re32='(TABLE)'	# Word 2
    
    rg1 = re.compile(re1+ws+re3+ws+re5+ws+re7+ws+re9,re.IGNORECASE|re.DOTALL)
    drop_field = rg1.search(self.sql_insert)

    rg2 = re.compile(re1+ws+re32+ws+re5,re.IGNORECASE|re.DOTALL)
    drop_table = rg2.search(self.sql_insert)
    
    if drop_field:
      column=drop_field.group(5)
      table=drop_field.group(9)
      self.sql_insert = self.sql_insert[len(drop_field.group(0)):].strip()
      
      if column in self.database[table + '_fields']:
        self.database[table + '_fields'].remove(column)
        for trple in self.database['triples']:
          for unique_id in self.database[table]:
            if unique_id == trple[0] and column == trple[1]:
              self.database['triples'].remove(trple)
        del self.database['constraints'][table][column]
      else:
        print 'Field: ' + column + ' does not exist. Table unchanged.'
    elif drop_table:
      table=drop_table.group(5)
      self.sql_insert = self.sql_insert[len(drop_table.group(0)):].strip()
      
      if table in self.database:
        for unique_id in self.database[table]:
          for trple in self.database['triples']:
            if unique_id == trple[0]:
              self.database['triples'].remove(trple)
        del self.database[table + '_fields']
        del self.database[table]
        del self.database['constraints'][table]
      else:
        print 'Table: ' + table + ' does not exist. Database unchanged.'
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    if DEBUG: self.print_database()
      
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
      toEval = m.group(9)
      toEval = toEval.replace('(,', '(\'\', ').replace('( ,', '(\'\', ').replace('(  ,', '(\'\', ')
      toEval = toEval.replace(',,', ', \'\',').replace(', ,', ', \'\',').replace(',  ,', ', \'\',')
      toEval = toEval.replace(',)', ', \'\')').replace(', )', ', \'\')').replace(',  )', ', \'\')')
      value = eval(toEval)
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()

      columns = self.database[table + '_fields']
      if not ((isinstance(value, str) and len(columns) == 1) or (len(value) == len(columns))):
        raise NameError('SQL: Statement incorrect:\n' + m.group(0))
        
      for j in self.database[table]:
        record = []
        for record_data in self.database['triples']:
          if record_data[0] == j:
            record.append(record_data[2])
        if tuple(record) == value:
          print 'SQL: Redundant information attempted insertion. Database not updated.'
          return
        
      self.database['current_record'] += 1
      for i in range(len(columns)):
        if (isinstance(value, str)):
          data = value
        else:
          data = value[i]
          
        if table in self.database['constraints'] and columns[i] in self.database['constraints'][table]:
          type = self.database['constraints'][table][columns[i]].keys()[0]
          type_val = self.database['constraints'][table][columns[i]][type]
          if type == 'VARCHAR':
            if len(data) > int(type_val):
              print 'SQL: Inserted value trimmed to fit specified database limit: ' + data[0:int(type_val)] + ' from: ' + data
              data = data[0:int(type_val)]
          elif type == 'INT':
            if data == '':
              data = None
            elif not isinstance(int(data), int):
              raise NameError('SQL: Incorrect data type. Expected an INT: ' + data)
              data = int(data)
          elif type == 'CHAR':
            data = data
          elif type == 'TEXT':
            data = data
          elif type == 'BIT':
            data = data
          elif type == 'BIGINT':
            data = data
          elif type == 'REAL':
            data = data
          elif type == 'DATE':
            data = data
          elif type == 'TIME':
            data = data
          elif type == 'DATETIME':
            data = data
          self.database['triples'].append((self.database['current_record'], columns[i], data))
          if not self.database['current_record'] in self.database[table]:
            self.database[table].append(self.database['current_record'])
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    if DEBUG: self.print_database()
    
  def select(self):
    re1='(SELECT)'	# Word 1
    ws='(\\s+)'	# White Space 1
    # re2='((?:[a-z][a-z0-9_]*,?\\s*)*|\*)'	THIS MAKES IT LAG....
    re2='(.*?)'	# Variable Name 1
    re3='(FROM)'	# Word 2
    re4='((?:[a-z][a-z0-9_]*))'	# Variable Name 1

    re12='(SELECT\\s+DISTINCT)'	# Word 1
    
    re13='(WHERE)'	# Word 1
    re53='(.?.?)'	# Variable Name 2
    re43='((?:[a-z0-9_]*))'	# Variable Name 1
    
    rg = re.compile(re1+ws+re2+ws+re3+ws+re4,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sql_insert)
    
    rg = re.compile(re12+ws+re2+ws+re3+ws+re4,re.IGNORECASE|re.DOTALL)
    distinct = rg.search(self.sql_insert)
    
    rg = re.compile(re13+ws+re4+ws+re53+ws+re43,re.IGNORECASE|re.DOTALL)
    where = rg.search(self.sql_insert)
    
    if m or distinct:
      if distinct:
        selection = distinct.group(3)
        table = distinct.group(7)
        self.sql_insert = self.sql_insert[len(distinct.group(0)):].strip()
      elif m:
        selection = m.group(3)
        table = m.group(7)
        self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
        
      if where:
        comp_column=where.group(3)
        operator=where.group(5)
        value=where.group(7)
        self.sql_insert = self.sql_insert[len(where.group(0)):].strip()
        
      if selection == '*':
        selection = self.database[table + '_fields']
      if isinstance(selection, str):
        selection_list = selection.split(',')
      else:
        selection_list = selection
      self.last_table = table
      self.last_selection = selection_list
        
      table_results = []
      row_results = {}
      for trple in self.database['triples']:
        for unique_id in self.database[table]:
          if unique_id == trple[0]:
            for column in selection_list:
              if column.strip() == trple[1]:
                if not unique_id in row_results:
                  row_results[unique_id] = []
                if not where:
                  row_results[unique_id].append(trple[2])
                else:
                  if trple[1] == comp_column:
                    if eval(str(trple[2]) + ' ' + operator + ' ' +  str(value)):
                      row_results[unique_id].append(trple[2])
                    else:
                      row_results[unique_id] = None
                  elif not row_results[unique_id] == None:
                    row_results[unique_id].append(trple[2])
      for unique_id in row_results:
        if not row_results[unique_id] == None:
          table_results.append(row_results[unique_id])
      if distinct:
        noDupes = [] 
        [noDupes.append(i) for i in table_results if not noDupes.count(i)] 
        table_results = noDupes
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    if DEBUG: print table_results
    return str(table_results)

  def truncate(self):
    re1='(TRUNCATE)'	# Word 1
    ws='(\\s+)'	# White Space 1
    re3='(TABLE)'	# Word 2
    re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1

    rg = re.compile(re1+ws+re3+ws+re5,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sql_insert)
    if m:
      table=m.group(5)
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
      
      if table in self.database:
        for unique_id in self.database[table]:
          for trple in self.database['triples']:
            if unique_id == trple[0]:
              self.database['triples'].remove(trple)
        self.database[table + '_fields'] = []
        self.database[table] = []
        del self.database['constraints'][table]
      else:
        print 'Table: ' + table + ' does not exist. Database unchanged.'
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    if DEBUG: self.print_database()
  
  def print_database(self):
    print 'Database:'
    keys = self.database.keys()
    keys.sort()
    for key in keys:
      print key, ':', self.database[key]
      
  def print_select(self, s):
    width = 17
    toReturn = 'print \'' + self.last_table + ':\'\n'
    toReturn += self.print_horz_rule(s, width)
    
    toReturn += 'print \'|'
    for col in self.last_selection:
      toReturn +=  str('').ljust(2) + str(col).ljust(width - 3) + '|'
    toReturn += '\'\n'
    toReturn += self.print_horz_rule(s, width)
    
    for row in eval(s):
      toReturn += 'print \'|'
      for col in row:
        toReturn +=  str('').ljust(2) + str(col).ljust(width - 3) + '|'
      toReturn += '\'\n'
    toReturn += self.print_horz_rule(s, width)
    return toReturn
        
  def print_horz_rule(self, s, width):
    toReturn = 'print \'|'
    for i in range(len(eval(s)[0])):
      toReturn += str('').ljust(width, '-')
    toReturn += '\'\n'
    return toReturn
  
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
  def __init__(self):
    # Read from 'sql:' to ':sql'
    self.sql_insertion_tag = 'sql:'
    self.sql_insertion_end_tag = self.sql_insertion_tag[-1:] + self.sql_insertion_tag[0:-1]
    self.database = {}
    self.database['triples'] = []
    self.database['constraints'] = {}
    self.database['current_record'] = 0
    self.python = ''
    
  def run(self, code):
    self.python = ''
    code = code.splitlines(True)
    i = 0
    while i < len(code): # Read each line and identify sql insertions
      line = code[i]
      index = line.find(self.sql_insertion_tag)
      if index > -1: # Handle insertion
        self.python += line[0:index]
        sql_insert = line[index + len(self.sql_insertion_tag):line.find(self.sql_insertion_end_tag)].strip() + ' '
        commented_sql_insert = line[line.find(self.sql_insertion_tag) - 1: line.find(self.sql_insertion_tag)] == '#'
        index = line.find(self.sql_insertion_end_tag)
        if index == -1:
          i += 1
          line = code[i]
          index = line.find(self.sql_insertion_end_tag)
          while not index > -1: # Read insertion until EndTag
            sql_insert += line.strip() + ' '
            i += 1
            line = code[i]
            index = line.find(self.sql_insertion_end_tag)
        # Modigy database by SQL statement
        if not commented_sql_insert:
          SQL(self, self.database, sql_insert.strip())
        self.python += line[index + len(self.sql_insertion_end_tag):]
      else: # Passively handle python text
        self.python += line
      i += 1
    return self.python
        
########################################################################

class CommandGUI:
  def __init__(self):
    print 'Python 2: The SQL (r100:39, Apr 26 2010, 14:00:00)'
    print 'Type "help()", "copyright()", "credits()", or "license()" for more information.'
    app = SQLinjection()
    while True:
      # python_code = '\
# def copyright():\n\
  # copyright()\n\
  # print \'\\nCopyright (c) 2010 Matthew Clarkson and Joaquin Casares.\'\n\
  # print \'All Rights Reserved.\'\n\
# def credits():\n\
  # credits()\n\
  # print \'\\n    SQL implementation by Matthew Clarkson and Joaquin Casares.\'\n'
      try:
        temp = raw_input('>>> ')
        if temp.strip()[-1:] == ':':
          looppython_code = 'spacer'
          temp += '\n'
          while not looppython_code.strip() == '':
            looppython_code = raw_input('... ')
            temp += looppython_code + '\n'
        try:
          python_code = app.run(temp)
          exec python_code
        except Exception as e:
          print type(e).__name__ + ':',
          print e
      except KeyboardInterrupt:
        print '\nGoodbye.\n'
        return
      except EOFError:
        print 'Goodbye.\n'
        return

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
    
    if not sys.stdin.isatty():
      code = ''
      for s in sys.stdin.readlines():
        code += s
      app = SQLinjection()
      python_code = app.run(code)    
      exec python_code
      sys.exit()
    
    arg = []
    try:
      arg.append(sys.argv[1])
    except:
      print 'Usage: \tsqlpython.py inputFile [converted_output_file]'
      print '\tsqlpython.py --console'
      print '\t"code" | sqlpython.py'
      print '\tsqlpython.py < "code"'
      return
    
    if arg[0] == '-console' or arg[0] == '--console':
      CommandGUI()
    else:
      file = open(arg[0],'r')
      code = file.read()
      app = SQLinjection()
      python_code = app.run(code)    
      file.close()
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