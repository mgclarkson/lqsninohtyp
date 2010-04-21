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
# DEBUG = True

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
        join_union_case = self.sql_insert[0:self.sql_insert.find(' ')].upper()
        if join_union_case == 'UNION':
          self.sql_insert = self.sql_insert[len(case):].strip()
          s1 = eval(s)
          s = select(self)
          s2 = eval(s)            
          if len(s1[0]) != len(s2[0]):           
            print 'SQL: each SELECT statement within the UNION must have the same number of columns.'
            s = ''
          else:
            wrongTypes = 0
            i = len(s1[0]) - 1
            while i >= 0: #iterate through the first tuple
              if not isinstance(s1[0][i], type(s2[0][i])):
                print 'SQL: each SELECT statement within the UNION must have columns of the same data types in the same order.'
                s = ''
                wrongTypes = 1 #flag indicates that elements of the two selects aren't of the same data types
                break
              i -= 1
            if not wrongTypes:
                ret = []
                for trple1 in s1:
                  ret.append(trple1) #append all triples in the first set to the output set
                for trple2 in s2:
                  found = 0
                  for addedTrple in s1:
                    if trple2 == addedTrple: #if found in both the first and second don't append it again to the output set
                      found = 1
                      break
                  if found == 0: #if not found in the second set append it to the output set
                    ret.append(trple2)
     
                x = ", ".join(map(str, ret))
                s = '[' + x + ']'              
                print s
                ##
          		## TODO: do we need to do something else with this s?  
          		## 
          		##
          		##
          		##
        elif join_union_case == 'INNER' or join_union_case == 'LEFT' or join_union_case == 'RIGHT' or join_union_case == 'FULL':
          s = joins(self)
        parent.python += s
      elif (case == 'TRUNCATE'):
        truncate(self)
      elif (case == 'DELETE'):
        delete(self)
      elif (case == 'JOINS'):
        joins(self)
      elif (case == 'UPDATE'):
        update(self)
      elif (case == 'PRINT'):
        self.sql_insert = self.sql_insert[len(case):].strip()
        parent.python += self.print_select(select(self))

      # Non-standard SQL   
      elif (case == 'DATABASEPRINT'):
        self.sql_insert = self.sql_insert[len(case):].strip()
        s = self.databaseprint()
        parent.python += s
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
        print self.sql_insert
        raise NameError('SQL: Statement incorrect or not yet supported: ' + case)
      if DEBUG: print
          
###
### Print statements for printing databases for debugs and for sql_insertion of python print statements          
###

  # Returns a string for the python file
  def databaseprint(self):
    s = 'print "Database:"\n'
    keys = self.database.keys()
    keys.sort()
    for key in keys:
      s += 'print "' + key + ':' + str(self.database[key]) + '"\n'
    s += 'print\n'
    return s
      
  # Prints onto the console
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