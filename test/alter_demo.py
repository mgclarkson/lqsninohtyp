=======================================================
#####################
### Original Python2 File:
### alter.py  
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

