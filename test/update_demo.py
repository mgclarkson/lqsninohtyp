=======================================================
#####################
### Original Python2 File:
### update.py2  
#####################  
  
#!/usr/bin/env python2.py

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
  INSERT INTO new_Customers VALUES ('Burbple', 'Durple', 124967, 7)
  INSERT INTO new_Customers VALUES ('Hes', 'ABob', 8675309, 2)
  INSERT INTO new_Customers VALUES ('See', 'Mee', 302740, 1)
  INSERT INTO new_Customers VALUES ('Jose', 'Nosey', 911, 2)
  INSERT INTO new_Customers VALUES ('Miggh', 'Tyfine', 124967, 2)
  PRINT SELECT * FROM new_Customers
  
  UPDATE new_Customers SET last='Bosey', name='Bob' WHERE last='Jose' AND name='Nosey'
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET last='Bopey', name='PopBob' WHERE last='Mee' AND name='Absente'
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET last='Groth', name='Henry' WHERE phone=302740 AND last='Mee'
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET phone=3994542, birthday=8 WHERE name='Henry' AND last='Groth'
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET phone=3994542, birthday=9 WHERE name='Henry' AND birthday=8
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET last='Less', name='Job' WHERE phone=124967
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET last='Hesty', name='Testme', birthday=5 WHERE last='Less'
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET phone=911
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET gender=0
  PRINT SELECT * FROM new_Customers
  UPDATE new_Customers SET last='Iven', name='oCond', phone=9343, birthday=6
  PRINT SELECT * FROM new_Customers

:sql

=======================================================
### Converted Python File:

#!/usr/bin/env python2.py

for i in range(10):
  print i,
print

print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  Absente       |  Mee           |  302740        |  8             |'
print '|  Burbple       |  Durple        |  124967        |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  See           |  Mee           |  302740        |  1             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Miggh         |  Tyfine        |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  Absente       |  Mee           |  302740        |  8             |'
print '|  Burbple       |  Durple        |  124967        |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  See           |  Mee           |  302740        |  1             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Miggh         |  Tyfine        |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  PopBob        |  Bopey         |  302740        |  8             |'
print '|  Burbple       |  Durple        |  124967        |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  See           |  Mee           |  302740        |  1             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Miggh         |  Tyfine        |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  PopBob        |  Bopey         |  302740        |  8             |'
print '|  Burbple       |  Durple        |  124967        |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  Henry         |  Groth         |  302740        |  1             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Miggh         |  Tyfine        |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  PopBob        |  Bopey         |  302740        |  8             |'
print '|  Burbple       |  Durple        |  124967        |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  Henry         |  Groth         |  3994542       |  8             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Miggh         |  Tyfine        |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  PopBob        |  Bopey         |  302740        |  8             |'
print '|  Burbple       |  Durple        |  124967        |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  Henry         |  Groth         |  3994542       |  9             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Miggh         |  Tyfine        |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  PopBob        |  Bopey         |  302740        |  8             |'
print '|  Job           |  Less          |  124967        |  7             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  Henry         |  Groth         |  3994542       |  9             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Job           |  Less          |  124967        |  2             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  PopBob        |  Bopey         |  302740        |  8             |'
print '|  Testme        |  Hesty         |  124967        |  5             |'
print '|  Hes           |  ABob          |  8675309       |  2             |'
print '|  Henry         |  Groth         |  3994542       |  9             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Testme        |  Hesty         |  124967        |  5             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  PopBob        |  Bopey         |  911           |  8             |'
print '|  Testme        |  Hesty         |  911           |  5             |'
print '|  Hes           |  ABob          |  911           |  2             |'
print '|  Henry         |  Groth         |  911           |  9             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Testme        |  Hesty         |  911           |  5             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  Lake          |  Travis        |  911           |  1             |'
print '|  PopBob        |  Bopey         |  911           |  8             |'
print '|  Testme        |  Hesty         |  911           |  5             |'
print '|  Hes           |  ABob          |  911           |  2             |'
print '|  Henry         |  Groth         |  911           |  9             |'
print '|  Jose          |  Nosey         |  911           |  2             |'
print '|  Testme        |  Hesty         |  911           |  5             |'
print '|--------------------------------------------------------------------'
print 'new_Customers:'
print '|--------------------------------------------------------------------'
print '|  name          |  last          |  phone         |  birthday      |'
print '|--------------------------------------------------------------------'
print '|  oCond         |  Iven          |  9343          |  6             |'
print '|  oCond         |  Iven          |  9343          |  6             |'
print '|  oCond         |  Iven          |  9343          |  6             |'
print '|  oCond         |  Iven          |  9343          |  6             |'
print '|  oCond         |  Iven          |  9343          |  6             |'
print '|  oCond         |  Iven          |  9343          |  6             |'
print '|  oCond         |  Iven          |  9343          |  6             |'
print '|--------------------------------------------------------------------'


=======================================================
### Console Output:

Column: gender does not exist.
0 1 2 3 4 5 6 7 8 9
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  Absente       |  Mee           |  302740        |  8             |
|  Burbple       |  Durple        |  124967        |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  See           |  Mee           |  302740        |  1             |
|  Jose          |  Nosey         |  911           |  2             |
|  Miggh         |  Tyfine        |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  Absente       |  Mee           |  302740        |  8             |
|  Burbple       |  Durple        |  124967        |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  See           |  Mee           |  302740        |  1             |
|  Jose          |  Nosey         |  911           |  2             |
|  Miggh         |  Tyfine        |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  PopBob        |  Bopey         |  302740        |  8             |
|  Burbple       |  Durple        |  124967        |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  See           |  Mee           |  302740        |  1             |
|  Jose          |  Nosey         |  911           |  2             |
|  Miggh         |  Tyfine        |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  PopBob        |  Bopey         |  302740        |  8             |
|  Burbple       |  Durple        |  124967        |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  Henry         |  Groth         |  302740        |  1             |
|  Jose          |  Nosey         |  911           |  2             |
|  Miggh         |  Tyfine        |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  PopBob        |  Bopey         |  302740        |  8             |
|  Burbple       |  Durple        |  124967        |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  Henry         |  Groth         |  3994542       |  8             |
|  Jose          |  Nosey         |  911           |  2             |
|  Miggh         |  Tyfine        |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  PopBob        |  Bopey         |  302740        |  8             |
|  Burbple       |  Durple        |  124967        |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  Henry         |  Groth         |  3994542       |  9             |
|  Jose          |  Nosey         |  911           |  2             |
|  Miggh         |  Tyfine        |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  PopBob        |  Bopey         |  302740        |  8             |
|  Job           |  Less          |  124967        |  7             |
|  Hes           |  ABob          |  8675309       |  2             |
|  Henry         |  Groth         |  3994542       |  9             |
|  Jose          |  Nosey         |  911           |  2             |
|  Job           |  Less          |  124967        |  2             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  PopBob        |  Bopey         |  302740        |  8             |
|  Testme        |  Hesty         |  124967        |  5             |
|  Hes           |  ABob          |  8675309       |  2             |
|  Henry         |  Groth         |  3994542       |  9             |
|  Jose          |  Nosey         |  911           |  2             |
|  Testme        |  Hesty         |  124967        |  5             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  PopBob        |  Bopey         |  911           |  8             |
|  Testme        |  Hesty         |  911           |  5             |
|  Hes           |  ABob          |  911           |  2             |
|  Henry         |  Groth         |  911           |  9             |
|  Jose          |  Nosey         |  911           |  2             |
|  Testme        |  Hesty         |  911           |  5             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  Lake          |  Travis        |  911           |  1             |
|  PopBob        |  Bopey         |  911           |  8             |
|  Testme        |  Hesty         |  911           |  5             |
|  Hes           |  ABob          |  911           |  2             |
|  Henry         |  Groth         |  911           |  9             |
|  Jose          |  Nosey         |  911           |  2             |
|  Testme        |  Hesty         |  911           |  5             |
|--------------------------------------------------------------------
new_Customers:
|--------------------------------------------------------------------
|  name          |  last          |  phone         |  birthday      |
|--------------------------------------------------------------------
|  oCond         |  Iven          |  9343          |  6             |
|  oCond         |  Iven          |  9343          |  6             |
|  oCond         |  Iven          |  9343          |  6             |
|  oCond         |  Iven          |  9343          |  6             |
|  oCond         |  Iven          |  9343          |  6             |
|  oCond         |  Iven          |  9343          |  6             |
|  oCond         |  Iven          |  9343          |  6             |
|--------------------------------------------------------------------
