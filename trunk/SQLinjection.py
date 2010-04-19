from SQL.SQL import *

class SQLinjection:
  def __init__(self):
    # Read from 'sql:' to ':sql'
    self.sql_insertion_tag = 'sql:'
    self.sql_insertion_end_tag = self.sql_insertion_tag[-1:] + self.sql_insertion_tag[0:-1]
    self.database = {}
    self.database['triples'] = []
    self.database['datatypes'] = {}
    self.database['valid_datatypes'] = ['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']
    self.database['current_record'] = 0
    self.python = ''
    
  def run(self, code):
    self.python = ''
    code = code.splitlines(True)
    i = 0
    while i < len(code): # Read each line and identify sql insertions
      line = code[i]
      index = line.find(self.sql_insertion_tag)
      if index > -1: # Handle insertion
        self.python += line[0:index]
        sql_insert = line[index + len(self.sql_insertion_tag):line.find(self.sql_insertion_end_tag)].strip() + ' '
        commented_sql_insert = line[line.find(self.sql_insertion_tag) - 1: line.find(self.sql_insertion_tag)] == '#'
        index = line.find(self.sql_insertion_end_tag)
        if index == -1:
          i += 1
          line = code[i]
          index = line.find(self.sql_insertion_end_tag)
          while not index > -1: # Read insertion until EndTag
            sql_insert += line.strip() + ' '
            i += 1
            line = code[i]
            index = line.find(self.sql_insertion_end_tag)
        # Modify database by SQL statement
        if not commented_sql_insert:
          SQL(self, self.database, sql_insert.strip())
        self.python += line[index + len(self.sql_insertion_end_tag):]
      else: # Passively handle python text
        self.python += line
      i += 1
    return self.python
