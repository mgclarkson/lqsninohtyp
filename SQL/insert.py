import re

DEBUG = False
DEBUG = True

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
        
      if table in self.database['datatypes'] and columns[i] in self.database['datatypes'][table]:
        type = self.database['datatypes'][table][columns[i]].keys()[0]
        type_val = self.database['datatypes'][table][columns[i]][type]
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
  
