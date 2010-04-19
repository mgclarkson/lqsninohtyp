=======================================================
#####################
### Original Python2 File:
### drop.py  
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
  PRINT SELECT * FROM Customers
  
  DROP INDEX name ON Customers 
  PRINT SELECT * FROM Customers
  
  DROP INDEX blah ON Customers 

  DROP TABLE Nope
  
  DROP TABLE Customers
  DATABASEPRINT
:sql

=======================================================
### Converted Python File:

#!/usr/bin/env python2.py

for i in range(10):
  print i,
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
print 'Customers:'
print '|----------------------------------'
print '|  last          |  phone         |'
print '|----------------------------------'
print '|  Cannata       |  7735647       |'
print '|  Clarkson      |  9875643       |'
print '|  Casares       |  3451878       |'
print '|  Joaquin       |  9345879       |'
print '|  Joaquin       |  5123789       |'
print '|  Guadalupe     |  8845748       |'
print '|----------------------------------'
print "Database:"
print "current_record:6"
print "datatypes:{}"
print "triples:[]"
print "valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']"
print


=======================================================
### Console Output:

Field: blah does not exist. Table unchanged.
Table: Nope does not exist. Database unchanged.
0 1 2 3 4 5 6 7 8 9
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
Customers:
|----------------------------------
|  last          |  phone         |
|----------------------------------
|  Cannata       |  7735647       |
|  Clarkson      |  9875643       |
|  Casares       |  3451878       |
|  Joaquin       |  9345879       |
|  Joaquin       |  5123789       |
|  Guadalupe     |  8845748       |
|----------------------------------
Database:
current_record:6
datatypes:{}
triples:[]
valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

