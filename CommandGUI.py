from SQLinjection import *

class CommandGUI:
  def __init__(self):
    print 'Python 2: The SQL (r100:39, Apr 26 2010, 14:00:00)'
    print 'Type "help()", "copyright()", "credits()", or "license()" for more information.'
    app = SQLinjection()
    while True:
      # python_code = '\
# def copyright():\n\
  # copyright()\n\
  # print \'\\nCopyright (c) 2010 Matthew Clarkson and Joaquin Casares.\'\n\
  # print \'All Rights Reserved.\'\n\
# def credits():\n\
  # credits()\n\
  # print \'\\n    SQL implementation by Matthew Clarkson and Joaquin Casares.\'\n'
      try:
        temp = raw_input('>>> ')
        if temp.strip()[-1:] == ':':
          looppython_code = 'spacer'
          temp += '\n'
          while not looppython_code.strip() == '':
            looppython_code = raw_input('... ')
            temp += looppython_code + '\n'
        try:
          python_code = app.run(temp)
          exec python_code
        except Exception as e:
          print type(e).__name__ + ':',
          print e
      except KeyboardInterrupt:
        print '\nGoodbye.\n'
        return
      except EOFError:
        print 'Goodbye.\n'
        return
