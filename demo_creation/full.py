  =======================================================
  #####################
  ### Original Python2 File:
  ### alter.py  
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
    DATABASEPRINT
    
    ALTER TABLE new_Customers ADD gender VARCHAR(1)
    DATABASEPRINT
    
    ALTER TABLE new_Customers ALTER COLUMN gender INT
    DATABASEPRINT
    
    ALTER TABLE new_Customers DROP COLUMN birthday
    DATABASEPRINT
  :sql

  =======================================================
  ### Converted Python File:

  #!/usr/bin/env python2.py

  for i in range(10):
    print i,
  print

  print "Database:"
  print "current_record:0"
  print "datatypes:{'new_Customers': {'phone': {'INT': -1}, 'birthday': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}}"
  print "new_Customers:[]"
  print "new_Customers_fields:['name', 'last', 'phone', 'birthday']"
  print "triples:[]"
  print "valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']"
  print
  print "Database:"
  print "current_record:0"
  print "datatypes:{'new_Customers': {'phone': {'INT': -1}, 'birthday': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}, 'gender': {'VARCHAR': '1'}}}"
  print "new_Customers:[]"
  print "new_Customers_fields:['name', 'last', 'phone', 'birthday', 'gender']"
  print "triples:[]"
  print "valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']"
  print
  print "Database:"
  print "current_record:0"
  print "datatypes:{'new_Customers': {'phone': {'INT': -1}, 'birthday': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}, 'gender': {'INT': -1}}}"
  print "new_Customers:[]"
  print "new_Customers_fields:['name', 'last', 'phone', 'birthday', 'gender']"
  print "triples:[]"
  print "valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']"
  print
  print "Database:"
  print "current_record:0"
  print "datatypes:{'new_Customers': {'phone': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}, 'gender': {'INT': -1}}}"
  print "new_Customers:[]"
  print "new_Customers_fields:['name', 'last', 'phone', 'gender']"
  print "triples:[]"
  print "valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']"
  print


  =======================================================
  ### Console Output:

  0 1 2 3 4 5 6 7 8 9
  Database:
  current_record:0
  datatypes:{'new_Customers': {'phone': {'INT': -1}, 'birthday': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}}
  new_Customers:[]
  new_Customers_fields:['name', 'last', 'phone', 'birthday']
  triples:[]
  valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

  Database:
  current_record:0
  datatypes:{'new_Customers': {'phone': {'INT': -1}, 'birthday': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}, 'gender': {'VARCHAR': '1'}}}
  new_Customers:[]
  new_Customers_fields:['name', 'last', 'phone', 'birthday', 'gender']
  triples:[]
  valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

  Database:
  current_record:0
  datatypes:{'new_Customers': {'phone': {'INT': -1}, 'birthday': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}, 'gender': {'INT': -1}}}
  new_Customers:[]
  new_Customers_fields:['name', 'last', 'phone', 'birthday', 'gender']
  triples:[]
  valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

  Database:
  current_record:0
  datatypes:{'new_Customers': {'phone': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}, 'gender': {'INT': -1}}}
  new_Customers:[]
  new_Customers_fields:['name', 'last', 'phone', 'gender']
  triples:[]
  valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

  =======================================================
  #####################
  ### Original Python2 File:
  ### create.py  
  #####################  
    
  #!/usr/bin/env python2.py

  for i in range(10):
    print i,
  print

  #sql:
    CREATE TABLE neverBuild ( blah VARCHAR(5) )
    INSERT INTO neverBuild VALUES ('NOPE')
  :sql

  sql:
    CREATE TABLE Customers ( 
      name VARCHAR(100) ,
      last VARCHAR(15),
      phone int,
      birthday VARCHAR(20)
    )
    CREATE TABLE Noncustomers ( 
      name VARCHAR(100) ,
      last VARCHAR(15),
      phone int
    )
    CREATE TABLE Housing ( 
      person VARCHAR(100) ,
      floor int,
      room VARCHAR(4),
      phone int
    )
  :sql

  sql: DATABASEPRINT :sql

  =======================================================
  ### Converted Python File:

  #!/usr/bin/env python2.py

  for i in range(10):
    print i,
  print

  #



  print "Database:"
  print "Customers:[]"
  print "Customers_fields:['name', 'last', 'phone', 'birthday']"
  print "Housing:[]"
  print "Housing_fields:['person', 'floor', 'room', 'phone']"
  print "Noncustomers:[]"
  print "Noncustomers_fields:['name', 'last', 'phone']"
  print "current_record:0"
  print "datatypes:{'Noncustomers': {'phone': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}, 'Customers': {'phone': {'INT': -1}, 'birthday': {'VARCHAR': '20'}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}, 'Housing': {'person': {'VARCHAR': '100'}, 'room': {'VARCHAR': '4'}, 'phone': {'INT': -1}, 'floor': {'INT': -1}}}"
  print "triples:[]"
  print "valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']"
  print


  =======================================================
  ### Console Output:

  0 1 2 3 4 5 6 7 8 9
  Database:
  Customers:[]
  Customers_fields:['name', 'last', 'phone', 'birthday']
  Housing:[]
  Housing_fields:['person', 'floor', 'room', 'phone']
  Noncustomers:[]
  Noncustomers_fields:['name', 'last', 'phone']
  current_record:0
  datatypes:{'Noncustomers': {'phone': {'INT': -1}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}, 'Customers': {'phone': {'INT': -1}, 'birthday': {'VARCHAR': '20'}, 'last': {'VARCHAR': '15'}, 'name': {'VARCHAR': '100'}}, 'Housing': {'person': {'VARCHAR': '100'}, 'room': {'VARCHAR': '4'}, 'phone': {'INT': -1}, 'floor': {'INT': -1}}}
  triples:[]
  valid_datatypes:['VARCHAR', 'INT', 'CHAR', 'TEXT', 'BIT', 'BIGINT', 'REAL']

  =======================================================
  #####################
  ### Original Python2 File:
  ### delete.py  
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
    INSERT INTO new_Customers VALUES ('Burbple', 'Durple', 8837232, 7)
    INSERT INTO new_Customers VALUES ('Hes', 'ABob', 8675309, 2)
    INSERT INTO new_Customers VALUES ('See', 'Mee', 302740, 1)
    INSERT INTO new_Customers VALUES ('Jose', 'Nosey', 928223, 2)
    INSERT INTO new_Customers VALUES ('Miggh', 'Tyfine', 124967, 2)
    PRINT SELECT * FROM new_Customers
    
    DELETE FROM new_Customers WHERE last='Nope'
    PRINT SELECT * FROM new_Customers
    
    DELETE FROM new_Customers WHERE phone='ABob'
    PRINT SELECT * FROM new_Customers
    
    DELETE FROM new_Customers WHERE phone=8837232
    PRINT SELECT * FROM new_Customers
    
    DELETE FROM new_Customers WHERE last='ABob'
  :sql
  sql:
    PRINT SELECT * FROM new_Customers

    DELETE FROM new_Customers WHERE last='Mee' AND phone=98478
    PRINT SELECT * FROM new_Customers
    
    DELETE FROM new_Customers WHERE last='Knee' AND phone=302740
    PRINT SELECT * FROM new_Customers
    
    DELETE FROM new_Customers WHERE last='Mee' AND phone=302740
    PRINT SELECT * FROM new_Customers
    
    DELETE FROM new_Customers
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
  print '|  See           |  Mee           |  302740        |  1             |'
  print '|  Jose          |  Nosey         |  928223        |  2             |'
  print '|  Miggh         |  Tyfine        |  124967        |  2             |'
  print '|--------------------------------------------------------------------'
  print 'new_Customers:'
  print '|--------------------------------------------------------------------'
  print '|  name          |  last          |  phone         |  birthday      |'
  print '|--------------------------------------------------------------------'
  print '|  Lake          |  Travis        |  911           |  1             |'
  print '|  Jose          |  Nosey         |  928223        |  2             |'
  print '|  Miggh         |  Tyfine        |  124967        |  2             |'
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
  |  See           |  Mee           |  302740        |  1             |
  |  Jose          |  Nosey         |  928223        |  2             |
  |  Miggh         |  Tyfine        |  124967        |  2             |
  |--------------------------------------------------------------------
  new_Customers:
  |--------------------------------------------------------------------
  |  name          |  last          |  phone         |  birthday      |
  |--------------------------------------------------------------------
  |  Lake          |  Travis        |  911           |  1             |
  |  Jose          |  Nosey         |  928223        |  2             |
  |  Miggh         |  Tyfine        |  124967        |  2             |
  |--------------------------------------------------------------------
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
  =======================================================
  #####################
  ### Original Python2 File:
  ### joins.py  
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
  =======================================================
  #####################
  ### Original Python2 File:
  ### select.py  
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

  #!/usr/bin/env python2.py

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
  =======================================================
  #####################
  ### Original Python2 File:
  ### truncate.py  
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
  :sql

  sql: DATABASEPRINT :sql

  sql:PRINT SELECT * FROM Customers:sql

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
  =======================================================
  #####################
  ### Original Python2 File:
  ### update.py  
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
