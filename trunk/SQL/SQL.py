'''
  Where the SQL injection gets translated into python code.
'''
import re

DEBUG = False
# DEBUG = True

class SQL:
  def __init__(self, parent, database, sql_insert):
  
    # Create class variable references
    self.parent = parent
    self.database = database
    self.sql_insert = sql_insert
    self.last_table = ''
    self.last_selection = []
    
    if DEBUG: print self.sql_insert

    # Parse the sql insert until no more characters are left
    while not self.sql_insert == '':
      if self.sql_insert.find(' ') > -1:
        case = self.sql_insert[0:self.sql_insert.find(' ')]
      else:
        case = self.sql_insert
      case = case.upper()
      if (case == 'CREATE'):
        self.create()
      elif (case == 'ALTER'):
        self.alter()
      elif (case == 'DROP'):
        self.drop()
      elif (case == 'INSERT'):
        self.insert()
      elif (case == 'SELECT'):
        s = self.select()
        parent.python += s
      elif (case == 'TRUNCATE'):
        self.truncate()
      elif (case == 'PRINT'):
        self.sql_insert = self.sql_insert[len(case):].strip()
        parent.python += self.print_select(self.select())

      # Non-standard SQL   
      elif (case == 'CONTENTS'):
        self.sql_insert = self.sql_insert[len(case):].strip()
        s = self.select()
        s = '[' + s.replace('[', '').replace(']', '') + ']'
        parent.python += s
      elif (case == 'TRIPLES'):
        s =  ", ".join(map(str, self.database['triples']))
        parent.python += s
        self.sql_insert = self.sql_insert[len(case):].strip()
      else:
        raise NameError('SQL: Statement incorrect or not yet supported: ' + case)
      if DEBUG: print
      
  def create(self):
    re1='(CREATE)'	# Word 1
    ws='(\\s+)'	# White Space 1
    re3='(TABLE)'	# Word 2
    re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
    re7='(\\(.*?\\(.*?\\)\\s+\\))'	# Round Braces 1
    re8='(\\(.*?\\s+\\))'	# Round Braces 1
    end = '(' + re7 + '|' + re8 + ')'

    rg = re.compile(re1+ws+re3+ws+re5+ws+end,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sql_insert)
    if m:
      table = m.group(5)
      fields = table + '_fields'
      list = m.group(7)
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
      if not table in self.database:
        self.database[table] = []
        self.database[fields] = []
      else:
        raise NameError('SQL: Table already exists: ' + table)
      list = list[1:-1].split(',')
      for e in list:
        el = e.split()
        column = ''
        datatype = ''
        int = -1
        for i in range(len(el)):
          re9='.*?(\\(.*?\\)).*'	# Round Braces 1
          rg = re.compile(re9,re.IGNORECASE|re.DOTALL)
          m = rg.search(el[i])
          if m:
            datatype = el[i][0:el[i].find('(')]
            int = m.group(1)[1:-1]
          else:
            if column == '':
              column = el[i]
            else:
              datatype = el[i]
        # Create a column in the database with the name 'column'
        # ###
        # ###
        # ###
        # Check this with J: why no '_fields'?
        # ###
        # ###
        if not column in self.database[fields]:
          self.database[fields].append(column)
        else:
          raise NameError('SQL: Column name already exists: ' + column)
        if not table in self.database['datatypes']:
          self.database['datatypes'][table] = {}
        if not column in self.database['datatypes'][table]:
          self.database['datatypes'][table][column] = {}
        self.database['datatypes'][table][column][datatype.upper()] = int
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    if DEBUG: self.print_database()
      
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
    
  def drop(self):
    re1='(DROP)'	# Variable Name 1
    ws='(\\s+)'	# White Space 1
    re3='(INDEX)'	# Variable Name 2
    re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 3
    re7='(ON)'	# Word 1
    re9='((?:[a-z][a-z0-9_]*))'	# Variable Name 4
    re32='(TABLE)'	# Word 2
    
    rg1 = re.compile(re1+ws+re3+ws+re5+ws+re7+ws+re9,re.IGNORECASE|re.DOTALL)
    drop_field = rg1.search(self.sql_insert)

    rg2 = re.compile(re1+ws+re32+ws+re5,re.IGNORECASE|re.DOTALL)
    drop_table = rg2.search(self.sql_insert)
    
    if drop_field:
      column=drop_field.group(5)
      table=drop_field.group(9)
      self.sql_insert = self.sql_insert[len(drop_field.group(0)):].strip()
      
      if column in self.database[table + '_fields']:
        self.database[table + '_fields'].remove(column)
        for trple in self.database['triples']:
          for unique_id in self.database[table]:
            if unique_id == trple[0] and column == trple[1]:
              self.database['triples'].remove(trple)
        del self.database['datatypes'][table][column]
      else:
        print 'Field: ' + column + ' does not exist. Table unchanged.'
    elif drop_table:
      table=drop_table.group(5)
      self.sql_insert = self.sql_insert[len(drop_table.group(0)):].strip()
      
      if table in self.database:
        for unique_id in self.database[table]:
          for trple in self.database['triples']:
            if unique_id == trple[0]:
              self.database['triples'].remove(trple)
        del self.database[table + '_fields']
        del self.database[table]
        del self.database['datatypes'][table]
      else:
        print 'Table: ' + table + ' does not exist. Database unchanged.'
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    if DEBUG: self.print_database()
      
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
    
  def select(self):
    re1='(SELECT)'	# Word 1
    ws='(\\s+)'	# White Space 1
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

  def truncate(self):
    re1='(TRUNCATE)'	# Word 1
    ws='(\\s+)'	# White Space 1
    re3='(TABLE)'	# Word 2
    re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1

    rg = re.compile(re1+ws+re3+ws+re5,re.IGNORECASE|re.DOTALL)
    m = rg.search(self.sql_insert)
    if m:
      table=m.group(5)
      self.sql_insert = self.sql_insert[len(m.group(0)):].strip()
      
      if table in self.database:
        for unique_id in self.database[table]:
          for trple in self.database['triples']:
            if unique_id == trple[0]:
              self.database['triples'].remove(trple)
        self.database[table + '_fields'] = []
        self.database[table] = []
        del self.database['datatypes'][table]
      else:
        print 'Table: ' + table + ' does not exist. Database unchanged.'
    else:
      raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)
    if DEBUG: self.print_database()
  
  def print_database(self):
    print 'Database:'
    keys = self.database.keys()
    keys.sort()
    for key in keys:
      print key, ':', self.database[key]
      
  def print_select(self, s):
    width = 17
    toReturn = 'print \'' + self.last_table + ':\'\n'
    toReturn += self.print_horz_rule(s, width)
    
    toReturn += 'print \'|'
    for col in self.last_selection:
      toReturn +=  str('').ljust(2) + str(col).ljust(width - 3) + '|'
    toReturn += '\'\n'
    toReturn += self.print_horz_rule(s, width)
    
    for row in eval(s):
      toReturn += 'print \'|'
      for col in row:
        toReturn +=  str('').ljust(2) + str(col).ljust(width - 3) + '|'
      toReturn += '\'\n'
    toReturn += self.print_horz_rule(s, width)
    return toReturn
        
  def print_horz_rule(self, s, width):
    toReturn = 'print \'|'
    for i in range(len(eval(s)[0])):
      toReturn += str('').ljust(width, '-')
    toReturn += '\'\n'
    return toReturn
  
