=======================================================
#####################
### Original Python2 File:
### create.py  
#####################  
  
for i in range(10):
  print i,
print

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

for i in range(10):
  print i,
print



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

