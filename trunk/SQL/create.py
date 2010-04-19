import re

DEBUG = False
# DEBUG = True

def create(self):
  re1='(CREATE)'	# Word 1
  rws='(\\s+)'	# White Space 1
  ws='(\\s*)'	# White Space 1
  re3='(TABLE)'	# Word 2
  re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
  re7='(\\(.*?\\(.*?\\)\\s+\\))'	# Round Braces 1
  re8='(\\(.*?\\s+\\))'	# Round Braces 1
  end = '(' + re7 + '|' + re8 + ')'

  # Set up the regex
  rg = re.compile(re1+rws+re3+rws+re5+ws+end,re.IGNORECASE|re.DOTALL)
  m = rg.search(self.sql_insert)
  if m: # If regex was matched
    table = m.group(5)
    list = m.group(7)
    
    # Trim sql_insert
    self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
    
    # Create the structure for the new table
    if not table in self.database:
      self.database[table] = []
      self.database[table + '_fields'] = []
    else: # Throw an error if the table already exists in the structure.
      raise NameError('SQL: Table already exists: ' + table)
      
    # Remove outside parens from list string    
    list = list[1:-1].split(',')
    
    # Loop over each field
    for e in list:
      # Split the fieldname from the datatype
      el = e.split()
      fieldname = ''
      datatype = ''
      datatypevalue = -1
      
      # Loop over all splits (Could be simpler. Sorry.)
      for i in range(len(el)):
        re9='.*?(\\(.*?\\)).*'	# Round Braces 1
        rg = re.compile(re9,re.IGNORECASE|re.DOTALL)
        m = rg.search(el[i])
        
        if not m: # No braces present in current element
          # Assign fieldname if none.
          if fieldname == '':
            fieldname = el[i]
          # Assign datatype otherwise
          else:
            datatype = el[i]
        else:
          # Assign the datatype and datatypevalue
          datatype = el[i][0:el[i].find('(')]
          datatypevalue = m.group(1)[1:-1]
      # Add fieldname
      if not fieldname in self.database[table + '_fields']:
        self.database[table + '_fields'].append(fieldname)
      else:
        raise NameError('SQL: Field name already exists: ' + fieldname)
        
      # Initialize the datatypes structure
      if not table in self.database['datatypes']:
        self.database['datatypes'][table] = {}
      if not fieldname in self.database['datatypes'][table]:
        self.database['datatypes'][table][fieldname] = {}
      
      # Set the datatypes value
      self.database['datatypes'][table][fieldname][datatype.upper()] = datatypevalue
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
  if DEBUG: self.print_database()
