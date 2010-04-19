=======================================================
#####################
### Original Python2 File:
### select.py  
#####################  
  
for i in range(10):
  print i,
print

sql:
  CREATE TABLE Customers ( 
    name VARCHAR(100) ,
    last VARCHAR(15),
    phone int
  )
  INSERT INTO Customers VALUES ('Phil', 'Cannata', 7735647)
  INSERT INTO Customers VALUES ('Matthew', 'Clarkson', 9875643)
  INSERT INTO Customers VALUES ('Joaquin', 'Casares', 3451878)
  INSERT INTO Customers VALUES ('Joaquin', 'Joaquin', 9345879)
  INSERT INTO Customers VALUES ('Joaquin', 'Joaquin', 5123789)
  INSERT INTO Customers VALUES ('Joaquin', 'Guadalupe', 8845748)
:sql

print 'What follows gets sent to the actual python code.'
print 'Not the output window.'
sql:
  SELECT DISTINCT name, last FROM Customers
:sql
sql:
  SELECT DISTINCT name FROM Customers
:sql
sql:
  SELECT name, last, phone FROM Customers
:sql
sql:
  SELECT name, last, phone FROM Customers WHERE phone > 6001234
:sql
sql:
  SELECT name, last, phone FROM Customers WHERE phone <> 7735647
:sql
print '----------------------------------------------------------------------------'

print
sql: PRINT SELECT * FROM Customers 
      ORDER BY name asc
:sql
print

print
sql: PRINT SELECT * FROM Customers 
      ORDER BY last desc
:sql
print

print 'All rows: '
for a in sql:SELECT * FROM Customers:sql :
  print a,
print '\n'

print 'All phone numbers: '
for a in sql:SELECT phone FROM Customers:sql :
  print a,
print '\n'

print 7735647 in sql:CONTENTS SELECT phone FROM Customers:sql
print 7735647 in sql:CONTENTS SELECT * FROM Customers:sql
print

for i in sql:CONTENTS SELECT * FROM Customers:sql:
  print i,
print '\n'

sql: DATABASEPRINT :sql

sql:PRINT SELECT * FROM Customers:sql

=======================================================
### Converted Python File:

for i in range(10):
  print i,
print



print 'What follows gets sent to the actual python code.'
print 'Not the output window.'
[['Phil', 'Cannata'], ['Matthew', 'Clarkson'], ['Joaquin', 'Casares'], ['Joaquin', 'Joaquin'], ['Joaquin', 'Guadalupe']]
[['Phil'], ['Matthew'], ['Joaquin']]
[['Phil', 'Cannata', 7735647], ['Matthew', 'Clarkson', 9875643], ['Joaquin', 'Casares', 3451878], ['Joaquin', 'Joaquin', 9345879], ['Joaquin', 'Joaquin', 5123789], ['Joaquin', 'Guadalupe', 8845748]]
[['Phil', 'Cannata', 7735647], ['Matthew', 'Clarkson', 9875643], ['Joaquin', 'Joaquin', 9345879], ['Joaquin', 'Guadalupe', 8845748]]
[['Matthew', 'Clarkson', 9875643], ['Joaquin', 'Casares', 3451878], ['Joaquin', 'Joaquin', 9345879], ['Joaquin', 'Joaquin', 5123789], ['Joaquin', 'Guadalupe', 8845748]]
print '----------------------------------------------------------------------------'

print
print 'Customers:'
print '|---------------------------------------------------'
print '|  name          |  last          |  phone         |'
print '|---------------------------------------------------'
print '|  Joaquin       |  Casares       |  3451878       |'
print '|  Joaquin       |  Joaquin       |  9345879       |'
print '|  Joaquin       |  Joaquin       |  5123789       |'
print '|  Joaquin       |  Guadalupe     |  8845748       |'
print '|  Matthew       |  Clarkson      |  9875643       |'
print '|  Phil          |  Cannata       |  7735647       |'
print '|---------------------------------------------------'

print

print
print 'Customers:'
print '|---------------------------------------------------'
print '|  name          |  last          |  phone         |'
print '|---------------------------------------------------'
print '|  Joaquin       |  Joaquin       |  5123789       |'
print '|  Joaquin       |  Joaquin       |  9345879       |'
print '|  Joaquin       |  Guadalupe     |  8845748       |'
print '|  Matthew       |  Clarkson      |  9875643       |'
print '|  Joaquin       |  Casares       |  3451878       |'
print '|  Phil          |  Cannata       |  7735647       |'
print '|---------------------------------------------------'

print

print 'All rows: '
for a in [['Phil', 'Cannata', 7735647], ['Matthew', 'Clarkson', 9875643], ['Joaquin', 'Casares', 3451878], ['Joaquin', 'Joaquin', 9345879], ['Joaquin', 'Joaquin', 5123789], ['Joaquin', 'Guadalupe', 8845748]] :
  print a,
print '\n'

print 'All phone numbers: '
for a in [[7735647], [9875643], [3451878], [9345879], [5123789], [8845748]] :
  print a,
print '\n'

print 7735647 in [7735647, 9875643, 3451878, 9345879, 5123789, 8845748]
print 7735647 in ['Phil', 'Cannata', 7735647, 'Matthew', 'Clarkson', 9875643, 'Joaquin', 'Casares', 3451878, 'Joaquin', 'Joaquin', 9345879, 'Joaquin', 'Joaquin', 5123789, 'Joaquin', 'Guadalupe', 8845748]
print

for i in ['Phil', 'Cannata', 7735647, 'Matthew', 'Clarkson', 9875643, 'Joaquin', 'Casares', 3451878, 'Joaquin', 'Joaquin', 9345879, 'Joaquin', 'Joaquin', 5123789, 'Joaquin', 'Guadalupe', 8845748]:
  print i,
print '\n'

print "Database:"
print "Customers:[1, 2, 3, 4, 5, 6]"
print "Customers_fields:['name', 'last', 'phone']"
print "current_record:6"
print "datatypes:{'Customers': {'phone': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}}"
print "triples:[(1, 'name', 'Phil'), (1, 'last', 'Cannata'), (1, 'phone', 7735647), (2, 'name', 'Matthew'), (2, 'last', 'Clarkson'), (2, 'phone', 9875643), (3, 'name', 'Joaquin'), (3, 'last', 'Casares'), (3, 'phone', 3451878), (4, 'name', 'Joaquin'), (4, 'last', 'Joaquin'), (4, 'phone', 9345879), (5, 'name', 'Joaquin'), (5, 'last', 'Joaquin'), (5, 'phone', 5123789), (6, 'name', 'Joaquin'), (6, 'last', 'Guadalupe'), (6, 'phone', 8845748)]"
print "valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']"
print


print 'Customers:'
print '|---------------------------------------------------'
print '|  name          |  last          |  phone         |'
print '|---------------------------------------------------'
print '|  Phil          |  Cannata       |  7735647       |'
print '|  Matthew       |  Clarkson      |  9875643       |'
print '|  Joaquin       |  Casares       |  3451878       |'
print '|  Joaquin       |  Joaquin       |  9345879       |'
print '|  Joaquin       |  Joaquin       |  5123789       |'
print '|  Joaquin       |  Guadalupe     |  8845748       |'
print '|---------------------------------------------------'


=======================================================
### Console Output:

0 1 2 3 4 5 6 7 8 9
What follows gets sent to the actual python code.
Not the output window.
----------------------------------------------------------------------------

Customers:
|---------------------------------------------------
|  name          |  last          |  phone         |
|---------------------------------------------------
|  Joaquin       |  Casares       |  3451878       |
|  Joaquin       |  Joaquin       |  9345879       |
|  Joaquin       |  Joaquin       |  5123789       |
|  Joaquin       |  Guadalupe     |  8845748       |
|  Matthew       |  Clarkson      |  9875643       |
|  Phil          |  Cannata       |  7735647       |
|---------------------------------------------------


Customers:
|---------------------------------------------------
|  name          |  last          |  phone         |
|---------------------------------------------------
|  Joaquin       |  Joaquin       |  5123789       |
|  Joaquin       |  Joaquin       |  9345879       |
|  Joaquin       |  Guadalupe     |  8845748       |
|  Matthew       |  Clarkson      |  9875643       |
|  Joaquin       |  Casares       |  3451878       |
|  Phil          |  Cannata       |  7735647       |
|---------------------------------------------------

All rows: 
['Phil', 'Cannata', 7735647] ['Matthew', 'Clarkson', 9875643] ['Joaquin', 'Casares', 3451878] ['Joaquin', 'Joaquin', 9345879] ['Joaquin', 'Joaquin', 5123789] ['Joaquin', 'Guadalupe', 8845748] 

All phone numbers: 
[7735647] [9875643] [3451878] [9345879] [5123789] [8845748] 

True
True

Phil Cannata 7735647 Matthew Clarkson 9875643 Joaquin Casares 3451878 Joaquin Joaquin 9345879 Joaquin Joaquin 5123789 Joaquin Guadalupe 8845748 

Database:
Customers:[1, 2, 3, 4, 5, 6]
Customers_fields:['name', 'last', 'phone']
current_record:6
datatypes:{'Customers': {'phone': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}}
triples:[(1, 'name', 'Phil'), (1, 'last', 'Cannata'), (1, 'phone', 7735647), (2, 'name', 'Matthew'), (2, 'last', 'Clarkson'), (2, 'phone', 9875643), (3, 'name', 'Joaquin'), (3, 'last', 'Casares'), (3, 'phone', 3451878), (4, 'name', 'Joaquin'), (4, 'last', 'Joaquin'), (4, 'phone', 9345879), (5, 'name', 'Joaquin'), (5, 'last', 'Joaquin'), (5, 'phone', 5123789), (6, 'name', 'Joaquin'), (6, 'last', 'Guadalupe'), (6, 'phone', 8845748)]
valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

Customers:
|---------------------------------------------------
|  name          |  last          |  phone         |
|---------------------------------------------------
|  Phil          |  Cannata       |  7735647       |
|  Matthew       |  Clarkson      |  9875643       |
|  Joaquin       |  Casares       |  3451878       |
|  Joaquin       |  Joaquin       |  9345879       |
|  Joaquin       |  Joaquin       |  5123789       |
|  Joaquin       |  Guadalupe     |  8845748       |
|---------------------------------------------------
