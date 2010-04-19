import re

DEBUG = False
#DEBUG = True

def delete(self):
  ws='(\\s+)'	# white space
  delFr='(DELETE\\s+FROM)'	# deleteFrom command
  delStarFr='(DELETE\\s+\*\\s+FROM)'	# deleteStarFrom command
  whereTo='(WHERE)' 
  a='(AND)' 
  eq='(=)' # equal sign
  tableNm='((?:[a-z][a-z0-9_]*))'	# tableName
  colNm1='((?:[a-z][a-z0-9_]*))'	# columnName  
  val1='((?:\'?[a-z0-9_]*\'?))'	# first value  
  colNm2='((?:[a-z][a-z0-9_]*))'	# columnName
  val2='((?:\'?[a-z0-9_]*\'?))'	# first value 
  
  rg4 = re.compile(delFr+ws+tableNm+ws+whereTo+ws+colNm1+eq+val1+ws+a+ws+colNm2+eq+val2,re.IGNORECASE|re.DOTALL)
  delTight = rg4.search(self.sql_insert) # DELETE FROM (two column comparison)
    
  rg3 = re.compile(delFr+ws+tableNm+ws+whereTo+ws+colNm1+eq+val1,re.IGNORECASE|re.DOTALL)
  delLoose = rg3.search(self.sql_insert) # DELETE FROM (one column comparison)
  
  rg1 = re.compile(delStarFr+ws+tableNm,re.IGNORECASE|re.DOTALL)
  delAllRows1 = rg1.search(self.sql_insert) # DELETE * FROM (no column comparsion)
    
  rg2 = re.compile(delFr+ws+tableNm,re.IGNORECASE|re.DOTALL)
  delAllRows2 = rg2.search(self.sql_insert) # DELETE FROM (no column comparison)  
    
  ####  
  #delete rows with two matching column vals
  ####  
  if delTight:
    table=delTight.group(3)
    column1=delTight.group(7)
    value1=delTight.group(9) 
    column2=delTight.group(13)
    value2=delTight.group(15)     
    self.sql_insert = self.sql_insert[len(delTight.group(0)):].strip()
    
    if not table in self.database:
      print 'Table: ' + table + ' does not exist. Database unchanged.'
    elif not column1 in self.database[table + '_fields']:
      print 'Column: ' + column1 + ' does not exist in table: ' + table + '.  Database unchanged.'
    elif not column2 in self.database[table + '_fields']:
      print 'Column: ' + column2 + ' does not exist in table: ' + table + '.  Database unchanged.'
    else:
      value1 = eval(value1) #handle the different possible value types
      value2 = eval(value2) 
      if not isinstance(value1, int):
        value1 = value1.replace('\'', '') #strip the opening and closing quotes for the value if string     
      if not isinstance(value2, int):
        value2 = value2.replace('\'', '') #strip the opening and closing quotes for the value if string 
      
      foundIds = [] #list of to-be-delete indexes
      for unique_id in self.database[table]:
        i = len(self.database['triples']) - 1
        while i >= 0:
          if unique_id == self.database['triples'][i][0] and column1 == self.database['triples'][i][1] and value1 == self.database['triples'][i][2]:
            k = len(self.database['triples']) - 1
            while k >= 0:
              if unique_id == self.database['triples'][k][0] and column2 == self.database['triples'][k][1] and value2 == self.database['triples'][k][2]:
                foundIds.append(unique_id) #if the columns and datas match, add it to the delete list
                break
              k -= 1
          i -= 1
      
      for index in foundIds: #go through delete list and remove all of its elements triple database        
        j = len(self.database['triples']) - 1
        while j >= 0:
          if index == self.database['triples'][j][0]:           
            self.database['triples'].remove(self.database['triples'][j])           
          j -= 1
        for element in self.database[table]: #after removing the triple, remove the indexes from the 'table' table
          if element == index:
            self.database[table].remove(element)
  
  ####          
  #delete rows with one matching column val
  ####  
  elif delLoose:    
    table=delLoose.group(3)   
    column=delLoose.group(7) 
    value=delLoose.group(9)
    self.sql_insert = self.sql_insert[len(delLoose.group(0)):].strip()

    if not table in self.database:
      print 'Table: ' + table + ' does not exist. Database unchanged.'
    elif not column in self.database[table + '_fields']:
      print 'Column: ' + column + ' does not exist in table: ' + table + '.  Database unchanged.'
    else:
      value = eval(value) #handle the different possible value types
      if not isinstance(value, int):
        value = value.replace('\'', '') #strip the opening and closing quotes for the value if string     
      
      foundIds = [] #list of to-be-delete indexes
      for unique_id in self.database[table]:
        i = len(self.database['triples']) - 1
        while i >= 0:
          if unique_id == self.database['triples'][i][0] and column == self.database['triples'][i][1] and value == self.database['triples'][i][2]:
            foundIds.append(unique_id) #if the column and data match, add it to the delete list            
          i -= 1
      
      for index in foundIds: #go through delete list and remove all of its elements triple database        
        j = len(self.database['triples']) - 1
        while j >= 0:
          if index == self.database['triples'][j][0]:
            self.database['triples'].remove(self.database['triples'][j])           
          j -= 1
        for element in self.database[table]: #after removing the triple, remove the indexes from the 'table' table
          if element == index:
            self.database[table].remove(element)
  
  ####     
  #delete all rows
  ####  
  elif delAllRows1 or delAllRows2:    
    if delAllRows1:
      table=delAllRows1.group(3)
      self.sql_insert = self.sql_insert[len(delAllRows1.group(0)):].strip()
    else:
      table=delAllRows2.group(3)
      self.sql_insert = self.sql_insert[len(delAllRows2.group(0)):].strip()
    
    if table in self.database:
      for unique_id in self.database[table]:
        i = len(self.database['triples']) - 1
        while not i == 0:
          if unique_id == self.database['triples'][i][0]:
            self.database['triples'].remove(self.database['triples'][i])
          i -= 1
      self.database[table] = []
    else:
      print 'Table: ' + table + ' does not exist. Database unchanged.'
    
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)

 
  if DEBUG: self.print_database()