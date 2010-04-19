'''
  Where the SQL injection gets translated into python code.
'''
import re
from create import create
from alter import alter
from drop import drop
from insert import insert
from select import select
from truncate import truncate
from delete import delete
from joins import joins
from union import union
from update import update

DEBUG = False
DEBUG = True

class SQL:
  def __init__(self, parent, database, sql_insert):
  
    # Create class variable references
    self.parent = parent
    self.database = database
    self.sql_insert = sql_insert
    self.last_table = ''
    self.last_selection = []
    
    if DEBUG: print self.sql_insert

    # Parse the sql insert until no more characters are left
    while not self.sql_insert == '':
      if self.sql_insert.find(' ') > -1:
        case = self.sql_insert[0:self.sql_insert.find(' ')]
      else:
        case = self.sql_insert
      case = case.upper()
      if (case == 'CREATE'):
        create(self)
      elif (case == 'ALTER'):
        alter(self)
      elif (case == 'DROP'):
        drop(self)
      elif (case == 'INSERT'):
        insert(self)
      elif (case == 'SELECT'):
        s = select(self)
        parent.python += s
      elif (case == 'TRUNCATE'):
        truncate(self)
      elif (case == 'DELETE'):
        delete(self)
      elif (case == 'JOINS'):
        joins(self)
      elif (case == 'UPDATE'):
        update(self)
      elif (case == 'UNION'):
        union(self)
      elif (case == 'PRINT'):
        self.sql_insert = self.sql_insert[len(case):].strip()
        parent.python += self.print_select(select(self))

      # Non-standard SQL   
      elif (case == 'CONTENTS'):
        self.sql_insert = self.sql_insert[len(case):].strip()
        s = select(self)
        s = '[' + s.replace('[', '').replace(']', '') + ']'
        parent.python += s
      elif (case == 'TRIPLES'):
        s =  ", ".join(map(str, self.database['triples']))
        parent.python += s
        self.sql_insert = self.sql_insert[len(case):].strip()
      else:
        raise NameError('SQL: Statement incorrect or not yet supported: ' + case)
      if DEBUG: print
          
###
### Print statements for printing databases for debugs and for sql_insertion of python print statements          
###

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
  
