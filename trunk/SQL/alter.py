import re

DEBUG = False
# DEBUG = True

def alter(self):
  ws='(\\s+)'	# white space
  altTable='(ALTER\\s+TABLE)'	# alterTable
  tableNm='((?:[a-z][a-z0-9_]*))'	# tableName
  colNm='((?:[a-z][a-z0-9_]*))'	# columnName
  dataTy='((?:[a-z][a-z0-9_]*))'	# dataType
  dataBrc='((\\(.*\\))?)' #dataTypeBrackets
  addC='(ADD)' # variation 1: addColumn
  dropC='(DROP\\s+COLUMN)' # variation 2: dropColumn
  modC='(ALTER\\s+COLUMN)' # variation 3: modifyColumn   

  rg1 = re.compile(altTable+ws+tableNm+ws+addC+ws+colNm+ws+dataTy+dataBrc,re.IGNORECASE|re.DOTALL)
  addCol = rg1.search(self.sql_insert) # ADD
      
  rg2 = re.compile(altTable+ws+tableNm+ws+dropC+ws+colNm,re.IGNORECASE|re.DOTALL)
  dropCol = rg2.search(self.sql_insert) # DROP COLUMN

  rg3 = re.compile(altTable+ws+tableNm+ws+modC+ws+colNm+ws+dataTy+dataBrc,re.IGNORECASE|re.DOTALL)
  modifyCol = rg3.search(self.sql_insert) # ALTER COLUMN

  #ALTER called with ADD 
  if addCol:
    table=addCol.group(3)
    column=addCol.group(7)
    dataType=addCol.group(9)
    int=addCol.group(10)[1:-1]
    self.sql_insert = self.sql_insert[len(addCol.group(0)):].strip()
         
    #table isn't in the database, throw error  
    if not table in self.database:
      raise NameError('SQL: Specified table doesn\'t exist:\n' + self.sql_insert)
    #column has already been created, throw error
    elif column in self.database[table+'_fields']:
      raise NameError('SQL: Cannot add column, it already exists:\n' + self.sql_insert)
    #append new column to database
    else:
      self.database[table+'_fields'].append(column)
      
    #TODO: optional check if datatype is a valid datatype
    #
    
    self.database['datatypes'][table][column] = {}
    #if the dataType has a size associated with it
    if int:
      self.database['datatypes'][table][column][dataType] = int
    else:
      self.database['datatypes'][table][column][dataType] = -1      
    
  #ALTER called with DROP COLUMN
  elif dropCol:
    table=dropCol.group(3)
    column=dropCol.group(7)
    self.sql_insert = self.sql_insert[len(dropCol.group(0)):].strip()

    #column is in the table, drop it
    if column in self.database[table + '_fields']:
      self.database[table + '_fields'].remove(column)
      for trple in self.database['triples']:
        for unique_id in self.database[table]:
          if unique_id == trple[0] and column == trple[1]:
            self.database['triples'].remove(trple)
      del self.database['datatypes'][table][column]
    #column doesn't exist, ignore
    else:
      print 'Column: ' + column + ' does not exist. Table unchanged.'

  #ALTER called with ALTER COLUMN (modify the datatype of the column)
  elif modifyCol:
    table=modifyCol.group(3)
    column=modifyCol.group(7)
    dataType=modifyCol.group(9)
    int=modifyCol.group(10)[1:-1]
    self.sql_insert = self.sql_insert[len(modifyCol.group(0)):].strip()

    #column is in the table, modify it
    if column in self.database[table + '_fields']:
      ###
      ###
      #TODO: modify the column's dataType
      print table, column, dataType, int
      if int == '':
        int = -1
      self.database['datatypes'][table][column][dataType.upper()] = int
      pass
      ###
      ###
    #column doesn't exist, ignore
    else:
      print 'Column: ' + column + ' does not exist. Table unchanged.'

    #TODO: optional check in dataType is a valid dataType
    #

  #incorrect syntax on the ALTER call 
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)

  if DEBUG: self.print_database()
