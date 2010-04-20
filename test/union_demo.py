=======================================================
#####################
### Original Python2 File:
### union.py  
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
  
  CREATE TABLE new_Customers ( 
    name VARCHAR(100) ,
    last VARCHAR(15),
    phone int,
    birthday int
  )
  INSERT INTO new_Customers VALUES ('Lake', 'Travis', 911, 1)
  INSERT INTO new_Customers VALUES ('Absente', 'Mee', 302740, 8)
  INSERT INTO new_Customers VALUES ('Burbple', 'Durple', 8837232, 7)
  INSERT INTO new_Customers VALUES ('Hes', 'ABob', 8675309, 2)
  INSERT INTO new_Customers VALUES ('See', 'Mee', 302740, 1)
  INSERT INTO new_Customers VALUES ('Jose', 'Nosey', 928223, 2)
  INSERT INTO new_Customers VALUES ('Miggh', 'Tyfine', 124967, 2)
  
  SELECT * FROM Customers
  UNION
  SELECT * FROM new_Customers
  
:sql


=======================================================
### Converted Python File:

#!/usr/bin/env python2.py

for i in range(10):
  print i,
print

[['Lake', 'Travis', 911, 1], ['Absente', 'Mee', 302740, 8], ['Burbple', 'Durple', 8837232, 7], ['Hes', 'ABob', 8675309, 2], ['See', 'Mee', 302740, 1], ['Jose', 'Nosey', 928223, 2], ['Miggh', 'Tyfine', 124967, 2]]


=======================================================
### Console Output:

[['Phil', 'Cannata', 7735647], ['Matthew', 'Clarkson', 9875643], ['Joaquin', 'Casares', 3451878], ['Joaquin', 'Joaquin', 9345879], ['Joaquin', 'Joaquin', 5123789], ['Joaquin', 'Guadalupe', 8845748]] 
[['Lake', 'Travis', 911, 1], ['Absente', 'Mee', 302740, 8], ['Burbple', 'Durple', 8837232, 7], ['Hes', 'ABob', 8675309, 2], ['See', 'Mee', 302740, 1], ['Jose', 'Nosey', 928223, 2], ['Miggh', 'Tyfine', 124967, 2]] 1111111111111111
0 1 2 3 4 5 6 7 8 9
