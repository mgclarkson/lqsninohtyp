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
  
  setVars='(((?:[a-z][a-z0-9_]*))(=)(\'?.*?\'?)((,\s+)(?:[a-z][a-z0-9_]*)=\'?.*?\'?)*)' #matches: column1=value, column2=value2, ...
    
  rg1 = re.compile(updateRec+ws+tableNm+ws+set+ws+setVars+ws+whereTo+ws+colNm1+eq+val1+ws+a+ws+colNm2+eq+val2,re.IGNORECASE|re.DOTALL)
  updateTight = rg1.search(self.sql_insert) # UPDATE (two column comparison)
  print updateRec+ws+tableNm+ws+set+ws+setVars+ws+whereTo+ws+colNm1+eq+val1+ws+a+ws+colNm2+eq+val2
    
  rg2 = re.compile(updateRec+ws+tableNm+ws+set+ws+setVars+ws+whereTo+ws+colNm1+eq+val1,re.IGNORECASE|re.DOTALL)
  updateLoose = rg2.search(self.sql_insert) # UPDATE (one column comparison)
  
  rg3 = re.compile(updateRec+ws+tableNm+ws+set+ws+setVars,re.IGNORECASE|re.DOTALL)
  updateAll = rg3.search(self.sql_insert) # UPDATE (one column comparison)
  
  ####  
  #update records with two matching column vals
  #### 
  if updateTight:  
    print 'updateTight'
    print len(updateTight.group(0))
    table=updateTight.group(3)
    toEval=updateTight.group(7)
    column1=updateTight.group(16)
    value1=updateTight.group(18) 
    column2=updateTight.group(22)
    value2=updateTight.group(24)
    print table
    print toEval
    print value1
    print column1
    print value2
    print column2
    
    self.sql_insert = self.sql_insert[len(updateTight.group(0)):].strip()
  
  ####  
  #update records with one matching column val
  #### 
  elif updateLoose:
    print 'updateLoose'
  
  ####  
  #update all records
  #### 
  elif updateAll:
    print 'updateAll'
  
  #incorrect syntax on the UPDATE call 
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)

  if DEBUG: self.print_database()