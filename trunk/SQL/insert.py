import re

DEBUG = False
# DEBUG = True

def insert(self):
  re1='(INSERT)'	# Word 1
  rws='(\\s+)'	# White Space 1
  ws='(\\s*)'	# White Space 1
  re3='(INTO)'	# Word 2
  re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
  re7='(VALUES)'	# Word 3
  re9='(\\(.*?\\))'	# Round Braces 1
  braceCSVbrace='((\()(.*?),(.*)(\)))'
  end = '(' + re9 + '|' + braceCSVbrace + ')'

  # Setup regex
  rg = re.compile(re1+rws+re3+ws+re5+rws+re7+ws+end,re.IGNORECASE|re.DOTALL)
  m = rg.search(self.sql_insert)
  if m:
    table = m.group(5)
    
    # Grab a hold of all Values to insert
    toEval = m.group(9)
    # Replace all ,, with , '', up to three spaces in distance
    toEval = toEval.replace('(,', '(\'\', ').replace('( ,', '(\'\', ').replace('(  ,', '(\'\', ')
    toEval = toEval.replace(',,', ', \'\',').replace(', ,', ', \'\',').replace(',  ,', ', \'\',')
    toEval = toEval.replace(',)', ', \'\')').replace(', )', ', \'\')').replace(',  )', ', \'\')')
    # Use python to evaluate this string into a python list
    value = eval(toEval)
    
    # Trim sql_insert
    self.sql_insert = self.sql_insert[len(m.group(0)):].strip()

    fieldnames = self.database[table + '_fields']
    
    # Check to make sure the at the number of elements in the insertion value matches the length of the current length of fields
    if not ((isinstance(value, str) and len(fieldnames) == 1) or (len(value) == len(fieldnames))):
      raise NameError('SQL: Length of insertion does not match the length of the fields :\n' + m.group(0))
      
    # Check to see that record does not already exist
    for j in self.database[table]:
      # Start with a fresh record in the form of a list since tuples are immutable
      record = []
      for record_data in self.database['triples']:
        if record_data[0] == j:
          # Add values to the record
          record.append(record_data[2])
      # Compare them.
      if tuple(record) == value:
        print 'SQL: Redundant information attempted insertion. Database not updated.'
        return
      
    # Commence record adding
    self.database['current_record'] += 1
    for i in range(len(fieldnames)):
      if (isinstance(value, str)):
        data = value
      else:
        data = value[i]
        
      # Verifies data is consistent with datatype assigned
      if table in self.database['datatypes'] and fieldnames[i] in self.database['datatypes'][table]:
        type = self.database['datatypes'][table][fieldnames[i]].keys()[0]
        type_val = self.database['datatypes'][table][fieldnames[i]][type]
        
        if type == 'VARCHAR':
          if len(data) > int(type_val):
            print 'SQL: Inserted value trimmed to fit specified database limit: ' + data[:int(type_val)] + ' from: ' + data
            data = data[:int(type_val)]
            
        elif type == 'INT':
          if data == '':
            data = None
          elif not isinstance(data, int):
            raise NameError('SQL: Incorrect data type. Expected an INT: ' + data)
            
        elif type == 'CHAR':
          if len(data) == 1:
            data = ord(data)
          else:
            raise NameError('SQL: Incorrect data type. Expected a CHAR: ' + data)
            
        elif type == 'TEXT':
          if len(data) > 255:
            print 'SQL: Inserted value trimmed to fit specified database limit: ' + data[:255] + ' from: ' + data
            data = data[:int(type_val)]
            
        elif type == 'BIT':
          if lower(data) == 'null':
            data = None
          if not (data == 1 or data == 0):
            raise NameError('SQL: Incorrect data type. Expected a BIT: ' + data)
            
        elif type == 'BIGINT':
          if not isinstance(data, int):
            raise NameError('SQL: Incorrect data type. Expected an BIGINT: ' + data)
          if data > 9223372036854775807 or data < -9223372036854775808:
            raise NameError('SQL: Datasize for BIGINT exceeded: ' + data)
            
        elif type == 'REAL':
          if isinstance(data, int):
            data = float(data)
          if not isinstance(data, float):
            raise NameError('SQL: Incorrect data type. Expected an REAL: ' + data)
            
        # Not implemented yet
        elif type == 'DATE':
          data = data
        elif type == 'TIME':
          data = data
        elif type == 'DATETIME':
          data = data
      
      # Do the actual append for the current piece of data
      self.database['triples'].append((self.database['current_record'], fieldnames[i], data))
      
      # Update the table to hace the recordNum
      if not self.database['current_record'] in self.database[table]:
        self.database[table].append(self.database['current_record'])
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
  if DEBUG: self.print_database()
  
