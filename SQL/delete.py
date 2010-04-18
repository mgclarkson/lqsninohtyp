import re

DEBUG = False
DEBUG = True

def delete(self):
  ws='(\\s+)'	# white space
  delFr='(DELETE\\s+FROM)'	# deleteFrom command
  delStarFr='(DELETE\\s+\*\\s+FROM)'	# deleteStarFrom command
  where='(WHERE)' # variation 2: dropColumn
  a='(AND)' # variation 1: addColumn
  eq='(\=)' # equal sign
  tableNm='((?:[a-z][a-z0-9_]*))'	# tableName
  colNm1='((?:[a-z][a-z0-9_]*))'	# columnName  
  val1='((?:[a-z][a-z0-9_]*))'	# first value  
  colNm2='((?:[a-z][a-z0-9_]*))'	# columnName
  val2='((?:[a-z][a-z0-9_]*))'	# first value 
  
  valShell1 = '\'' + val1 + '\''
  valShell2 = '\'' + val2 + '\''
  
  rg1 = re.compile(delStarFr+ws+tableNm,re.IGNORECASE|re.DOTALL)
  delAllRows1 = rg1.search(self.sql_insert) # DELETE * FROM (no column comparsion)
    
  rg2 = re.compile(delFr+ws+tableNm,re.IGNORECASE|re.DOTALL)
  delAllRows2 = rg2.search(self.sql_insert) # DELETE FROM (no column comparison)
  
  rg3 = re.compile(delFr+ws+tableNm+ws+where+ws+colNm1+eq+valShell1,re.IGNORECASE|re.DOTALL)
  delLoose = rg3.search(self.sql_insert) # DELETE FROM (one column comparison)
 	
  rg4 = re.compile(delFr+ws+tableNm+ws+where+ws+colNm1+eq+valShell1+ws+a+colNm2+eq+valShell2,re.IGNORECASE|re.DOTALL)
  delTight = rg3.search(self.sql_insert) # DELETE FROM (two column comparison)
  
    
  #
  # Question: is there some counter of how many records there are?
  # If there is I need to clear it for the delete all rows commands
  # or decrement it for the other two commands
  #
  #

  #delete all rows
  if delAllRows1 or delAllRows2:    
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
  
  #delete rows with one matching column val
  elif delLoose:
    table=delLoose.group(3)
    print table
    column=delLoose.group(7) #TODO: check these numbers
    print column
    value=delLoose.group(9) #TODO: check these numbers
    print value
    self.sql_insert = self.sql_insert[len(delLoose.group(0)):].strip()
    
  
  #delete rows with two matching column vals
  elif delTight:
    table=delTight.group(3)
    column1=delTight.group(7) #TODO: check these numbers
    value1=delTight.group(9) #TODO: check these numbers
    column2=delTight.group(11) #TODO: check these numbers
    value2=delTight.group(13) #TODO: check these numbers
    self.sql_insert = self.sql_insert[len(delTight.group(0)):].strip()
    
    #FIX values, remove the ' '
    #check if table is in database
    #find where column1 equals some value1
    #of those find where column2 equals value2
    #if so, remove only those rows
    #else, do nothing
    
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)

 
  if DEBUG: self.print_database()