import re

DEBUG = False
# DEBUG = True

def truncate(self):
  if DEBUG: self.print_database()
  
  re1='(^TRUNCATE)'	# Word 1
  rws='(\\s+)'	# White Space 1
  ws='(\\s*)'	# White Space 1
  re3='(TABLE)'	# Word 2
  re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1

  # Setup the regex
  rg = re.compile(re1+rws+re3+ws+re5,re.IGNORECASE|re.DOTALL)
  m = rg.search(self.sql_insert)
  
  if m:
    table=m.group(5)
    
    # Trim sql_insert
    self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
    
    if table in self.database:
      for recordNum in self.database[table]:
        # Hold the last index of the triple store
        i = len(self.database['triples']) - 1
        # Cycle until you reach the beginning
        while not i < 0:
          # Remove all triples that are in the current table
          if recordNum == self.database['triples'][i][0]:
            self.database['triples'].remove(self.database['triples'][i])
          i -= 1
      
      # Reset all references
      self.database[table + '_fields'] = []
      self.database[table] = []
      del self.database['datatypes'][table]
    else:
      print 'Table: ' + table + ' does not exist. Database unchanged.'
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
  if DEBUG: self.print_database()

