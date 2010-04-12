Quick Reference: I named it a *.py for IDE color coding reasons.

* self.NAME refers to a private variable kinda thing.
* Also declaring takes place on the fly.
* Also there are no needed return types for this reason. All methods are unrequired "voids".
* Each "tab" is really 2 spaces.
* Strings can be like 'this' or "this". I tend to stick toward using 'single' quotes in the code just a personal
    standard but either way since it's interchangeable.
* string.split(', ') returns a list where the string is parsed where every comma+space are seperators.

Data Structure (Initialization):
  self.database = {} # A database is a dictionary.
  self.database['current_record'] = 0
  self.database['constraints'] = {}
  self.database['triples'] = []

sql:
CREATE TABLE Firsts ( name VARCHAR(5) ) 
INSERT INTO Firsts VALUES ('Phil') 
INSERT INTO Firsts VALUES ('Matthew') 
INSERT INTO Firsts VALUES ('Joaquin')
:sql

Database after above code:
  self.database['current_record'] : 3
  self.database['constraints'] : {'Firsts': {'name': {'VARCHAR': '5'}}}
  self.database['triples'] : [(1, 'name', 'Phil'), (2, 'name', 'Matth'), (3, 'name', 'Joaqu')]
  self.database['Firsts'] : [1, 2, 3]
  self.database['Firsts_fields'] : ['name']

http://docs.python.org/tutorial/controlflow.html

Read 4.1 through 4.4. Breaks haven't been used yet.  
  
  
http://docs.python.org/tutorial/datastructures.html

Read 5.1 on Lists. 
  The holders for the triples and tables and table_fields (lists inside a dictionary).
Read 5.3 on Tuples. 
  How are triples are stored in the 'triples' list (a list of tuples inside a dictionary).
Read 5.5 on Dicationaries. 
  The main database is a dictionary. Also, the constraints key in the database dictionary, is another
  dictionary (a dictionary housed in another dictionary).

  But also note that the constraints dictionary has multiple dictionary layers.
  These are accessed much like 2D arrays like so:
  
  if table in self.database['constraints'] and column in self.database['constraints'][table]:
    type = self.database['constraints'][table][column].keys()[0]  # i.e. VARCHAR
    type_val = self.database['constraints'][table][column][type]  # i.e. 5

Read 5.6 on Looping. I haven't implemented this yet in our code, but it would be good to know.

Again the sites that I've been using:
## Sources: http://www.w3schools.com/sql/default.asp
## Sources: http://www.mckoi.com/database/SQLSyntax.html
## Sources: http://txt2re.com/index-python.php3
## Sources: http://gskinner.com/RegExr
## Sources: http://gskinner.com/RegExr/desktop

I usually get the text from w3 schools. Read up if I need to off mckoi. Copy the w3 text into txt2re.
Edit that. Toss it into a test.py file. Run the code changing the text for multiple commands. Edit the 
end pieces to be match only one command by using gskinner if I need help. Then insert the code into 
the method followed by this line:

self.sql_insert = self.sql_insert[len(m.group(0)):].strip()

to eliminate what was recognized from the sql_insert string (the collection of all the current commands
that are to be processed) and leave only the commands that need to be processed in sql_insert.



END NOTE:

Keep a lookup at the top of the sqlpython.py file. There I make a note of all that needs to be done.
Lets keep that updated kind of as an in-line SVN bug tracker?