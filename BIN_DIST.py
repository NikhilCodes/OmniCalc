from cx_Freeze import setup,Executable
import sys
import os

includes = {'packages':['tkinter', 'sympy', 'matplotlib', 'numpy', 'PyQt5', 'Calculus', 'Scalc', 'Graph']}
os.environ['TCL_LIBRARY']='D:\\Python3.5\\tcl\\tcl8.6'
os.environ['TK_LIBRARY']='D:\\Python3.5\\tcl\\tk8.6'
include_files=[r'D:\\Python3.5\\DLLs\\tcl86t.dll',r'D:\\Python3.5\\DLLs\\tk86t.dll']
exe=Executable(script='GUI.py',base='Console',)

setup(name='Omni Calulator',
      version='0.54.2',
      options={'build_exe':includes},
      description="""!Professional Calculator!""",
      executables=[exe]
      )
