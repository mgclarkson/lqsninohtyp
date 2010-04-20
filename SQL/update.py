import re

DEBUG = False
DEBUG = True

def update(self):
  ws='(\\s+)'	# white space
  updateRec='(^UPDATE)'	
  set='(SET)'	
  whereTo='(WHERE)' 
  a='(AND)'
  eq='(=)'
  tableNm='((?:[a-z][a-z0-9_]*))'	# tableName
  colNm1='((?:[a-z][a-z0-9_]*))'	# columnName  
  val1='((?:\'?[a-z0-9_]*\'?))'	# first value  
  colNm2='((?:[a-z][a-z0-9_]*))'	# columnName
  val2='((?:\'?[a-z0-9_]*\'?))'	# first value   
  
  setVars='((?:[a-z][a-z0-9_]*)(=)(\'?([a-z0-9_])+\'?))(((,\s+)(?:[a-z][a-z0-9_]*)=(\'?([a-z0-9_])+\'?))*)' #matches: column1=value, column2=value2, ...
    
  rg1 = re.compile(updateRec+ws+tableNm+ws+set+ws+setVars+ws+whereTo+ws+colNm1+eq+val1+ws+a+ws+colNm2+eq+val2,re.IGNORECASE|re.DOTALL)
  updateTight = rg1.search(self.sql_insert) # UPDATE (two column comparison)
    
  rg2 = re.compile(updateRec+ws+tableNm+ws+set+ws+setVars+ws+whereTo+ws+colNm1+eq+val1,re.IGNORECASE|re.DOTALL)
  updateLoose = rg2.search(self.sql_insert) # UPDATE (one column comparison)
  
  rg3 = re.compile(updateRec+ws+tableNm+ws+set+ws+setVars,re.IGNORECASE|re.DOTALL)
  updateAll = rg3.search(self.sql_insert) # UPDATE (no column comparison-be cautious!)
  
  ####  
  #update records with two matching column vals
  #### 
  if updateTight:  
    table=updateTight.group(3)
    toEval=updateTight.group(7) + updateTight.group(11)
    column1=updateTight.group(19) #match these two columns with these two values
    value1=updateTight.group(21) 
    column2=updateTight.group(25)
    value2=updateTight.group(27)    
    self.sql_insert = self.sql_insert[len(updateTight.group(0)):].strip()
    
    listOfCols = []
    listOfValues = []
    #put the different values and column names into an array
    remComma = toEval.split(',')    
    for i in remComma:
      remEq = i.strip().split('=')
      listOfCols.append(remEq[0])
      listOfValues.append(eval(remEq[1])) 
      
    print listOfCols
    print listOfValues
    
    value1 = eval(value1) #handle the different possible value types
    value2 = eval(value2)
    if not isinstance(value1, int):
      value1 = value1.replace('\'', '') #strip the opening and closing quotes for the value of string
    if not isinstance(value2, int):
      value2 = value2.replace('\'', '')
    
    foundIds = [] #list of to-be-updated indexes
    for unique_id in self.database[table]: #acquire the appropriate unique_id's: those for this table
      i = len(self.database['triples']) - 1
      while i >= 0: #go through all triples starting at the last trying to match to first value
        if unique_id == self.database['triples'][i][0] and column1 == self.database['triples'][i][1] and value1 == self.database['triples'][i][2]:
          k = len(self.database['triples']) - 1
          while k >= 0: #go through all triples starting at the last trying to match to second value
            if unique_id == self.database['triples'][k][0] and column2 == self.database['triples'][k][1] and value2 == self.database['triples'][k][2]:
              foundIds.append(unique_id) #if the columns and values match, add it to the update list
            k -= 1
        i -= 1
    
    col = 0
    while col < len(listOfCols): #go through each of the source cols in the update command
      if listOfCols[col] in self.database[table + '_fields']:
        for fId in foundIds: #iterate through to-be-updated list
          i = len(self.database['triples']) - 1
          while i >= 0:
            if fId == self.database['triples'][i][0] and listOfCols[col] == self.database['triples'][i][1]:
              self.database['triples'][i] = [fId, listOfCols[col], listOfValues[col]] #update the values of the triples             
            i -= 1
      else:
        print 'Column: ' + listOfCols[col] + ' does not exist.'
      col += 1       
      
  
  
  ####  
  #update records with one matching column val
  #### 
  elif updateLoose:
    table=updateLoose.group(3)
    toEval=updateLoose.group(7) + updateLoose.group(11)
    column1=updateLoose.group(19) #match this columns with this value
    value1=updateLoose.group(21)   
    self.sql_insert = self.sql_insert[len(updateLoose.group(0)):].strip()
    
    listOfCols = []
    listOfValues = []
    #put the different values and column names into an array
    remComma = toEval.split(',')    
    for i in remComma:
      remEq = i.strip().split('=')
      listOfCols.append(remEq[0])
      listOfValues.append(eval(remEq[1])) 
      
    print listOfCols
    print listOfValues
    
    value1 = eval(value1) #handle the different possible value types
    if not isinstance(value1, int):
      value1 = value1.replace('\'', '') #strip the opening and closing quotes for the value if string  
    
    foundIds = [] #list of to-be-updated indexes
    for unique_id in self.database[table]: #acquire the appropriate unique_id's: those for this table
      i = len(self.database['triples']) - 1
      while i >= 0: #go through all triples starting at the last
        if unique_id == self.database['triples'][i][0] and column1 == self.database['triples'][i][1] and value1 == self.database['triples'][i][2]:
          foundIds.append(unique_id) #if the column and data match, add it to the update list            
        i -= 1
    
    col = 0
    while col < len(listOfCols): #go through each of the source cols in the update command
      if listOfCols[col] in self.database[table + '_fields']:
        for fId in foundIds: #iterate through to-be-updated list
          i = len(self.database['triples']) - 1
          while i >= 0:
            if fId == self.database['triples'][i][0] and listOfCols[col] == self.database['triples'][i][1]:
              self.database['triples'][i] = [fId, listOfCols[col], listOfValues[col]] #update the values of the triples             
            i -= 1
      else:
        print 'Column: ' + listOfCols[col] + ' does not exist.'
      col += 1       
      
  
  ####  
  #update all records
  #### 
  elif updateAll:
    table=updateAll.group(3)
    toEval=updateAll.group(7) + updateAll.group(11)
    self.sql_insert = self.sql_insert[len(updateAll.group(0)):].strip()
    
    listOfCols = []
    listOfValues = []
    #put the different values and column names into an array
    remComma = toEval.split(',')    
    for i in remComma:
      remEq = i.strip().split('=')
      listOfCols.append(remEq[0])
      listOfValues.append(eval(remEq[1])) 

    col = 0
    while col < len(listOfCols):
      if listOfCols[col] in self.database[table + '_fields']:
        for unique_id in self.database[table]:
          i = len(self.database['triples']) - 1
          while i >= 0:
            if unique_id == self.database['triples'][i][0] and listOfCols[col] == self.database['triples'][i][1]:
              self.database['triples'][i] = [unique_id, listOfCols[col], listOfValues[col]]              
            i -= 1
      else:
        print 'Column: ' + listOfCols[col] + ' does not exist.'
      col += 1      
  
  #incorrect syntax on the UPDATE call 
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)

  if DEBUG: self.print_database()