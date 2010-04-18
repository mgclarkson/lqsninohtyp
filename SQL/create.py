import re

DEBUG = False
# DEBUG = True

def create(self):
  re1='(CREATE)'	# Word 1
  rws='(\\s+)'	# White Space 1
  ws='(\\s*)'	# White Space 1
  re3='(TABLE)'	# Word 2
  re5='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
  re7='(\\(.*?\\(.*?\\)\\s+\\))'	# Round Braces 1
  re8='(\\(.*?\\s+\\))'	# Round Braces 1
  end = '(' + re7 + '|' + re8 + ')'

  rg = re.compile(re1+rws+re3+rws+re5+ws+end,re.IGNORECASE|re.DOTALL)
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
