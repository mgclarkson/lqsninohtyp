=======================================================
#####################
### Original Python2 File:
### union.py2  
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
  INSERT INTO Customers VALUES ('Miggh', 'Tyfine', 124967)
  INSERT INTO Customers VALUES ('Joaquin', 'Joaquin', 5123789)
  INSERT INTO Customers VALUES ('Joaquin', 'Guadalupe', 8845748)
  
  CREATE TABLE new_Customers ( 
    name VARCHAR(100),
    last VARCHAR(15),
    phone int,
    birthday int
  )
  INSERT INTO new_Customers VALUES ('Lake', 'Travis', 911, 1)
  INSERT INTO new_Customers VALUES ('Absente', 'Mee', 302740, 8)
  INSERT INTO new_Customers VALUES ('Burbple', 'Durple', 8837232, 7)
  INSERT INTO new_Customers VALUES ('Hes', 'ABob', 8675309, 2)
  INSERT INTO new_Customers VALUES ('See', 'Mee', 302740, 1)
  INSERT INTO new_Customers VALUES ('Matthew', 'Clarkson', 9875643, 5)
  INSERT INTO new_Customers VALUES ('Jose', 'Nosey', 928223, 2)
  INSERT INTO new_Customers VALUES ('Miggh', 'Tyfine', 124967, 2)
  
  SELECT * FROM Customers
  UNION
  SELECT * FROM new_Customers
  
  SELECT name, last FROM Customers
  UNION
  SELECT name, last, phone FROM new_Customers
  
  SELECT name, last, phone FROM Customers
  UNION
  SELECT name, last FROM new_Customers
  
  SELECT name, phone FROM Customers
  UNION
  SELECT name, last FROM new_Customers
  
  SELECT name, last FROM Customers
  UNION
  SELECT birthday, last FROM new_Customers
  
  SELECT name, last FROM Customers
  UNION
  SELECT name, last FROM new_Customers
:sql

list = sql:
  SELECT name, last, phone FROM Customers
  UNION
  SELECT name, last, phone FROM new_Customers
:sql
print list
#sql:  
  SELECT last, name FROM Customers
  UNION
  SELECT last, name FROM new_Customers
  
:sql

=======================================================
### Converted Python File:

#!/usr/bin/env python2.py

for i in range(10):
  print i,
print

[['Phil', 'Cannata'], ['Matthew', 'Clarkson'], ['Joaquin', 'Casares'], ['Joaquin', 'Joaquin'], ['Miggh', 'Tyfine'], ['Joaquin', 'Joaquin'], ['Joaquin', 'Guadalupe'], ['Lake', 'Travis'], ['Absente', 'Mee'], ['Burbple', 'Durple'], ['Hes', 'ABob'], ['See', 'Mee'], ['Jose', 'Nosey']]

list = [['Phil', 'Cannata', 7735647], ['Matthew', 'Clarkson', 9875643], ['Joaquin', 'Casares', 3451878], ['Joaquin', 'Joaquin', 9345879], ['Miggh', 'Tyfine', 124967], ['Joaquin', 'Joaquin', 5123789], ['Joaquin', 'Guadalupe', 8845748], ['Lake', 'Travis', 911], ['Absente', 'Mee', 302740], ['Burbple', 'Durple', 8837232], ['Hes', 'ABob', 8675309], ['See', 'Mee', 302740], ['Jose', 'Nosey', 928223]]
print list
#

=======================================================
### Console Output:

SQL: each SELECT statement within the UNION must have the same number of columns.
SQL: each SELECT statement within the UNION must have the same number of columns.
SQL: each SELECT statement within the UNION must have the same number of columns.
SQL: each SELECT statement within the UNION must have columns of the same data types in the same order.
SQL: each SELECT statement within the UNION must have columns of the same data types in the same order.
0 1 2 3 4 5 6 7 8 9
[['Phil', 'Cannata', 7735647], ['Matthew', 'Clarkson', 9875643], ['Joaquin', 'Casares', 3451878], ['Joaquin', 'Joaquin', 9345879], ['Miggh', 'Tyfine', 124967], ['Joaquin', 'Joaquin', 5123789], ['Joaquin', 'Guadalupe', 8845748], ['Lake', 'Travis', 911], ['Absente', 'Mee', 302740], ['Burbple', 'Durple', 8837232], ['Hes', 'ABob', 8675309], ['See', 'Mee', 302740], ['Jose', 'Nosey', 928223]]
