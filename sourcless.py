import importlib
import importlib.machinery

"""
the file something.cpython-37.pyc, can be any .pyc file
"""
pycFile = "something.cpython-37.pyc"
pyFilePath = "relitive/path/to/something.cpython-37.pyc" # include the .pyc in the path

common = importlib.machinery.SourcelessFileLoader(pycFile, pycFilePath)

common.load_module()
"""
once load_module() has been called, whatever functions are within the pyc can now be called as
common.func()
common.func1()
and so on, the functions will remain their original names, func() and func1() are simply examples
"""

"""
This method allows a python file to be somewhat like a shared object (.so) from C or CPP, the
contents can still be extracted with some effort, but this allows you to have some way to not so
much "hide" the source data, but to protect it, or ensure it does not change
"""
