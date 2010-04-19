=======================================================
#####################
### Original Python2 File:
### update.py  
#####################  
  
for i in range(10):
  print i,
print

sql:
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
  UPDATE new_Customers SET last='Bosey', name='Bob' WHERE last='Jose' AND name='Nosey'
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET last='Bosey', name='Bob' WHERE last='Jose'
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET last='Bosey', name='Bob', phone=9343
  PRINT SELECT * FROM new_Customers

:sql

=======================================================
### Converted Python File:

for i in range(10):
  print i,
print

print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  Absente       |  Mee           |  302740        |  8             |'
print '|  Burbple       |  Durple        |  8837232       |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  See           |  Mee           |  302740        |  1             |'
print '|  Jose          |  Nosey         |  928223        |  2             |'
print '|  Miggh         |  Tyfine        |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  Absente       |  Mee           |  302740        |  8             |'
print '|  Burbple       |  Durple        |  8837232       |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  See           |  Mee           |  302740        |  1             |'
print '|  Jose          |  Nosey         |  928223        |  2             |'
print '|  Miggh         |  Tyfine        |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Bob           |  Bosey         |  9343          |  1             |'
print '|  Bob           |  Bosey         |  9343          |  8             |'
print '|  Bob           |  Bosey         |  9343          |  7             |'
print '|  Bob           |  Bosey         |  9343          |  2             |'
print '|  Bob           |  Bosey         |  9343          |  1             |'
print '|  Bob           |  Bosey         |  9343          |  2             |'
print '|  Bob           |  Bosey         |  9343          |  2             |'
print '|--------------------------------------------------------------------'


=======================================================
### Console Output:

0 1 2 3 4 5 6 7 8 9
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  Absente       |  Mee           |  302740        |  8             |
|  Burbple       |  Durple        |  8837232       |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  See           |  Mee           |  302740        |  1             |
|  Jose          |  Nosey         |  928223        |  2             |
|  Miggh         |  Tyfine        |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  Absente       |  Mee           |  302740        |  8             |
|  Burbple       |  Durple        |  8837232       |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  See           |  Mee           |  302740        |  1             |
|  Jose          |  Nosey         |  928223        |  2             |
|  Miggh         |  Tyfine        |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Bob           |  Bosey         |  9343          |  1             |
|  Bob           |  Bosey         |  9343          |  8             |
|  Bob           |  Bosey         |  9343          |  7             |
|  Bob           |  Bosey         |  9343          |  2             |
|  Bob           |  Bosey         |  9343          |  1             |
|  Bob           |  Bosey         |  9343          |  2             |
|  Bob           |  Bosey         |  9343          |  2             |
|--------------------------------------------------------------------
