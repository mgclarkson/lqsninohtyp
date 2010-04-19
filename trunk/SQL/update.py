import re

DEBUG = False
# DEBUG = True

def update(self):
  ws='(\\s+)'	# white space
  updateRec='(UPDATE)'	
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
  print updateRec+ws+tableNm+ws+set+ws+setVars+ws+whereTo+ws+colNm1+eq+val1+ws+a+ws+colNm2+eq+val2
    
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
    
  
  #incorrect syntax on the UPDATE call 
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)

  if DEBUG: self.print_database()