"""
This is a powerful snippit, it is a mockery of how python should work, and i am
asshamed of having used this, but it works well, and allows a user to load a
module from a variable name, in this case, it loads the test.py script, and
the sub function printme, this can allow a user to send a module to a running
program via a command config
"""


name = "test"
func = "printme"
module = getattr(__import__(name, fromlist=[func]), func)
module()

'''
this is a variation which is more simple, it allows for a standardised function
name to be used, in which case it would be less work on the user, only needing
a script to be given to it, then the script needs a common function name for this
to execute
'''

module = __import__(name, None)
module.launch()
