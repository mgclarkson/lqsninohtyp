=======================================================
#####################
### Original Python2 File:
### insert.py  
#####################  
  
#!/usr/bin/env python2.py

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

sql: DATABASEPRINT :sql

sql:PRINT SELECT * FROM Customers:sql

list = sql:TRIPLES:sql

print 'Here are the triples!'
for i in list:
  print i,
print

=======================================================
### Converted Python File:

#!/usr/bin/env python2.py

for i in range(10):
  print i,
print



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


list = (1, 'name', 'Phil'), (1, 'last', 'Cannata'), (1, 'phone', 7735647), (2, 'name', 'Matthew'), (2, 'last', 'Clarkson'), (2, 'phone', 9875643), (3, 'name', 'Joaquin'), (3, 'last', 'Casares'), (3, 'phone', 3451878), (4, 'name', 'Joaquin'), (4, 'last', 'Joaquin'), (4, 'phone', 9345879), (5, 'name', 'Joaquin'), (5, 'last', 'Joaquin'), (5, 'phone', 5123789), (6, 'name', 'Joaquin'), (6, 'last', 'Guadalupe'), (6, 'phone', 8845748)

print 'Here are the triples!'
for i in list:
  print i,
print

=======================================================
### Console Output:

0 1 2 3 4 5 6 7 8 9
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
Here are the triples!
(1, 'name', 'Phil') (1, 'last', 'Cannata') (1, 'phone', 7735647) (2, 'name', 'Matthew') (2, 'last', 'Clarkson') (2, 'phone', 9875643) (3, 'name', 'Joaquin') (3, 'last', 'Casares') (3, 'phone', 3451878) (4, 'name', 'Joaquin') (4, 'last', 'Joaquin') (4, 'phone', 9345879) (5, 'name', 'Joaquin') (5, 'last', 'Joaquin') (5, 'phone', 5123789) (6, 'name', 'Joaquin') (6, 'last', 'Guadalupe') (6, 'phone', 8845748)
