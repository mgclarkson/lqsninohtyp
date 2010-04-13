import re

DEBUG = False
# DEBUG = True

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
      del self.database['datatypes'][table][column]
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
      del self.database['datatypes'][table]
    else:
      print 'Table: ' + table + ' does not exist. Database unchanged.'
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
  if DEBUG: self.print_database()
    
