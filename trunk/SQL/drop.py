import re

DEBUG = False
# DEBUG = True

def drop(self):
  re1='(DROP)'	# Variable Name 1
  rws='(\\s+)'	# White Space 1
  ws='(\\s*)'	# White Space 1
  re3='(INDEX)'	# Variable Name 2
  re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 3
  re7='(ON)'	# Word 1
  re9='((?:[a-z][a-z0-9_]*))'	# Variable Name 4
  re32='(TABLE)'	# Word 2
  
  # Set up regex's
  rg1 = re.compile(re1+rws+re3+ws+re5+rws+re7+ws+re9,re.IGNORECASE|re.DOTALL)
  drop_field = rg1.search(self.sql_insert)

  rg2 = re.compile(re1+rws+re32+ws+re5,re.IGNORECASE|re.DOTALL)
  drop_table = rg2.search(self.sql_insert)
  
  # If dropping field:
  if drop_field:
    fieldname=drop_field.group(5)
    table=drop_field.group(9)
    self.sql_insert = self.sql_insert[len(drop_field.group(0)):].strip()
    
    if fieldname in self.database[table + '_fields']:
      self.database[table + '_fields'].remove(fieldname)
      
      # Loop through all the triples and remove the triples where the recordNum and fieldname match
      for trple in self.database['triples']:
        for recordNum in self.database[table]:
          if recordNum == trple[0] and fieldname == trple[1]:
            self.database['triples'].remove(trple)
      # Delete the fieldname from being referenced
      del self.database['datatypes'][table][fieldname]
    else:
      print 'Field: ' + fieldname + ' does not exist. Table unchanged.'

  # If dropping table:
  elif drop_table:
    table=drop_table.group(5)
    self.sql_insert = self.sql_insert[len(drop_table.group(0)):].strip()
    
    if table in self.database:
      # Loop through all the triples and remove the triples where the recordNum match
      for recordNum in self.database[table]:
        # Hold the last index of the triple store
        i = len(self.database['triples']) - 1
        # Cycle until you reach the beginning
        while not i < 0:
          # Remove all triples that are in the current table
          if recordNum == self.database['triples'][i][0]:
            self.database['triples'].remove(self.database['triples'][i])
          i -= 1
      # Remove all traces of the table
      del self.database[table + '_fields']
      del self.database[table]
      del self.database['datatypes'][table]
    else:
      print 'Table: ' + table + ' does not exist. Database unchanged.'
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
  if DEBUG: self.print_database()
    
