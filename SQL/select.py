import re

DEBUG = False
# DEBUG = True

def select(self):
  re1='(^SELECT)'	# Word 1
  rws='(\\s+)'	# White Space 1
  ws='(\\s*)'	# White Space 1
  # re2='((?:[a-z][a-z0-9_]*,?\\s*)*|\*)'	THIS MAKES IT LAG....
  re2='(.*?)'	# Variable Name 1
  re3='(FROM)'	# Word 2
  re4='((?:[a-z][a-z0-9_]*))'	# Variable Name 1

  re12='(^SELECT\\s+DISTINCT)'	# Word 1
  
  re13='(^WHERE)'	# Word 1
  re53='(.?.?)'	# Variable Name 2
  re43='((\()?(\'?([a-z0-9_])+\'?)((,)\s+(\'?([a-z0-9_])+\'?))*(\))?)'	# Variable Name 1
  
  re14='(^ORDER)'	# Word 1
  re24='(BY)'	# Word 1
  re34='((?:[a-z0-9_]*))'
  re44='((ASC|DESC)?)'
  
  # Setup the different regex's
  rg = re.compile(re1+ws+re2+ws+re3+ws+re4,re.IGNORECASE|re.DOTALL)
  m = rg.search(self.sql_insert)
  
  rg = re.compile(re12+ws+re2+ws+re3+ws+re4,re.IGNORECASE|re.DOTALL)
  distinct = rg.search(self.sql_insert)
  
  rgwhere = re.compile(re13+ws+re4+ws+re53+ws+re43,re.IGNORECASE|re.DOTALL)
  
  rgorder = re.compile(re14+rws+re24+ws+re34+ws+re44,re.IGNORECASE|re.DOTALL)
  
  # If caught by regex
  if m or distinct:
    # Trim sql_insert to size
    if distinct:
      selection = distinct.group(3)
      table = distinct.group(7)
      self.sql_insert = self.sql_insert[len(distinct.group(0)):].strip()
    elif m:
      selection = m.group(3)
      table = m.group(7)
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
      
    where = rgwhere.search(self.sql_insert)
    if where:
      comparison_fieldname=where.group(3)
      operator=where.group(5)
      value=where.group(7)
      # Trim sql_insert to size
      self.sql_insert = self.sql_insert[len(where.group(0)):].strip()
      
    order = rgorder.search(self.sql_insert)
    if order:
      orderField = order.group(5)
      orderOrder = order.group(7).upper()
      # Trim sql_insert to size
      self.sql_insert = self.sql_insert[len(order.group(0)):].strip()
      
    if selection == '*':
      selection = self.database[table + '_fields']
      selection_list = selection
    else:
      selection_list = selection.split(',')
    
    # For SQL.py
    self.last_table = table
    self.last_selection = selection_list
      
    table_results = []
    row_results = {}
    orderNum = -1
    # Look at all the triples
    for trple in self.database['triples']:
      # Look at all the recordNums in the table to select from
      for recordNum in self.database[table]:
        # If the triple is of that table:... else: loop at next triple
        if recordNum == trple[0]:
          # Cycle through all the fieldnames in the list of fields that are to be selected
          for fieldname in selection_list:
            # Check if this fieldname in this trple is in the selection_list
            if fieldname.strip() == trple[1]:
              
              # Initalize return structure for this recordNum
              if not recordNum in row_results:
                row_results[recordNum] = []
                
              # If order regex is found on this fieldname, hold onto the number for later.
              if order and trple[1] == orderField:
                orderNum = len(row_results[recordNum])
                
              # Add all elements if no where clause
              if not where:
                row_results[recordNum].append(trple[2])
              # Add only the elements where where clause matches if where clause exists
              else:
                # If we're looking at the triple that decides the comparison:
                if trple[1] == comparison_fieldname:
                  # Use python to evaluate the comparison
                  if operator == 'IN':
                    if trple[1] == comparison_fieldname:
                      if trple[2] in eval(value):      
                         row_results[recordNum].append(trple[2])
                  elif operator == 'BETWEEN':
                    print 'between'
                  elif operator == 'LIKE':
                    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
                  elif eval(str(trple[2]) + ' ' + operator + ' ' +  str(value)):
                    # The comparison is allowed, so continue to add data
                    row_results[recordNum].append(trple[2])
                  else:
                    # Block access to adding any more tuples since the comparison did not match
                    row_results[recordNum] = None
                elif not row_results[recordNum] == None:
                  # Add tuples to the row_results until comparision is made and makes the final decision
                  row_results[recordNum].append(trple[2])
    
    # Move all non-Nones from the row_results into the table_results
    for recordNum in row_results:
      if not row_results[recordNum] == None:
        table_results.append(row_results[recordNum])
        
    # Order the select if order clause was used
    if order:
      table_results = sorted(table_results, key=lambda sortBy: sortBy[orderNum])
      # Reverse the order if 'DESC'
      if orderOrder == 'DESC':
        table_results.reverse()
        
    # If distinct clause, remove duplicates from the return table
    if distinct:
      noDupes = [] 
      [noDupes.append(i) for i in table_results if not noDupes.count(i)] 
      table_results = noDupes
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
  if DEBUG: print table_results
  return str(table_results)

