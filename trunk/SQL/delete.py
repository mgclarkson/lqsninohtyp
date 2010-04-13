import re

DEBUG = False
# DEBUG = True

def delete(self):
  ws='(\\s+)'	# white space
  delFr='(DELETE\\s+FROM)'	# deleteFrom command
  delStarFr='(DELETE\\s+\*\\s+FROM)'	# deleteStarFrom command
  where='(WHERE)' # variation 2: dropColumn
  a='(AND)' # variation 1: addColumn
  eq='(\=)' # equal sign
  tableNm='((?:[a-z][a-z0-9_]*))'	# tableName
  colNm='((?:[a-z][a-z0-9_]*))'	# columnName
  val1='((?:[a-z][a-z0-9_]*))'	# first value  
  
  rg1 = re.compile(deltStarFr+ws+tableNm,re.IGNORECASE|re.DOTALL)
  delAllRows1 = rg1.search(self.sql_insert) # DELETE * FROM (no column comparsion)
      
  rg2 = re.compile(delFr+ws+tableNm,re.IGNORECASE|re.DOTALL)
  delAllRows2 = rg2.search(self.sql_insert) # DELETE FROM (no column comparison)

  rg3 = re.compile(delFr+ws+tableNm+ws+colNm+eq+val1,re.IGNORECASE|re.DOTALL)
  delLoose = rg3.search(self.sql_insert) # DELETE FROM (one column comparison)

  #add all the crazy shit, loops, etc.
  rg4 = re.compile(delFr+ws+tableNm+ws+colNm+eq+val1+ws+a+,re.IGNORECASE|re.DOTALL)
  delTight = rg3.search(self.sql_insert) # DELETE FROM (more than one column comparison)