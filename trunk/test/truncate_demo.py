=======================================================
#####################
### Original Python2 File:
### truncate.py2  
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
  DATABASEPRINT
  TRUNCATE TABLE Firsts
  TRUNCATE TABLE Customers
  DATABASEPRINT
:sql

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
print "Database:"
print "Customers:[]"
print "Customers_fields:[]"
print "current_record:6"
print "datatypes:{}"
print "triples:[]"
print "valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']"
print


=======================================================
### Console Output:

Table: Firsts does not exist. Database unchanged.
0 1 2 3 4 5 6 7 8 9
Database:
Customers:[1, 2, 3, 4, 5, 6]
Customers_fields:['name', 'last', 'phone']
current_record:6
datatypes:{'Customers': {'phone': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}}
triples:[(1, 'name', 'Phil'), (1, 'last', 'Cannata'), (1, 'phone', 7735647), (2, 'name', 'Matthew'), (2, 'last', 'Clarkson'), (2, 'phone', 9875643), (3, 'name', 'Joaquin'), (3, 'last', 'Casares'), (3, 'phone', 3451878), (4, 'name', 'Joaquin'), (4, 'last', 'Joaquin'), (4, 'phone', 9345879), (5, 'name', 'Joaquin'), (5, 'last', 'Joaquin'), (5, 'phone', 5123789), (6, 'name', 'Joaquin'), (6, 'last', 'Guadalupe'), (6, 'phone', 8845748)]
valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

Database:
Customers:[]
Customers_fields:[]
current_record:6
datatypes:{}
triples:[]
valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

