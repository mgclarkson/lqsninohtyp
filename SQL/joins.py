import re

DEBUG = False
# DEBUG = True

def joins(self):
  table_results = []
  first_tablename = self.last_table
  joining_fieldnames = self.last_selection
  if(1):
    pass
    
    # you can get the first table name by using first_tablename
    # you can get the fields that are supposed to be here by using joining_fieldnames
    
    # what should happen in SQL.py, is select will be run on Persons.LastName, Persons.FirstName, Orders.OrderNo
    # nothing will match however.
    # the data is saved a the top of the SQL.py file in the self.declarations and in select right after the selection list is parsed.
    # this is what i initialized you to have for quick access. (I kept it around for the PRINT SELECT so it came with a table and column names fyi.)
    
    # now just get regex to recognize everything after the first select. FULL JOIN... ON... [ORDER BY...]
    # parse out which fields are for which tables using a split and xxx[1] or xxx[2] (array access)
    # then everytime it matches use the algorithm similar to select to hold on to the row_result. THEN toss it into table_results.
    
    # the current select algorithm is a bit inefficient, since it's close to O(N)^3, but for now it's fine. Just keep the order to have it go smoothly in join.
    
    # Now thinking about it, the inner portion should be almost exactly like select especially if it has an order by as well.
    # DO REMEMBER: Order gets executed after self.sql_insert has been trimmed to avoid it not being at the front of the sql_insert string.






  #incorrect syntax on the JOINS call 
  else:
    raise NameError('SQL: Statement incorrect or not yet supported:\n' + self.sql_insert)

  if DEBUG: self.print_database()
  return str(table_results)