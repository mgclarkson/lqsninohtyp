import re

DEBUG = False
# DEBUG = True

def select(self):
  re1='(SELECT)'	# Word 1
  rws='(\\s+)'	# White Space 1
  ws='(\\s*)'	# White Space 1
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

