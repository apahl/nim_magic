"""
nim_magic.py
Nim cell magic for JupyterLab or Juypter Python Notebooks.

Write Nim modules and use the compiled code directly in the Notebook as extension modules for the Python kernel (similar to e.g. %%cython, but for your favorite language :-P ). It builds on @yglukhov 's awesome [nimpy](https://github.com/yglukhov/nimpy) library.

## Requirements
* A [Nim](https://nim-lang.org) compiler in your path
* [nimpy](https://github.com/yglukhov/nimpy) package (`nimble install nimpy`)

## Installation
Just put the file nim_magic.py somewhere in Python's import path.

## Example
In a JupyterLab or Jupyter Notebook:

```Python
# In [1]:
%load_ext nim_magic


# In [2]:
%%nim -d:release
proc greet(name: string): string {.exportpy.} =
    return "Hello, " & name & "!"


# In [3]:
greet("World")


# Out [3]:
'Hello, World!'


# In [4] (this will remove temporary dirs created by nim_magic):
%nim_clear
```
"""

import os
import shutil
import sys
import time
import subprocess as sp
from IPython.core.magic import (Magics, magics_class,
                                line_magic, cell_magic)


@magics_class
class NimMagics(Magics):

    @line_magic
    def nim_clear(self, cmd):
        """%nim_clear
        will remove the temporary dirs used by nim_magic."""
        shutil.rmtree('nimmagic', ignore_errors=True)
        print("Removed temporary files used by nim_magic.")

    @cell_magic
    def nim(self, options, code):
        """`options` can be left empty or contain further compile options, e.g. "-d:release"
        (separated by space).

        Example:

        %%nim -d:release
        <code to compile in release mode>"""
        if not os.path.isdir("nimmagic"):
            os.mkdir("nimmagic")

        glbls = self.shell.user_ns
        name = time.strftime("nim%y%m%d%H%M%S")
        code = "import nimpy\n\n" + code
        ext = "pyd" if sys.platform.startswith('win') else "so"
        open("nimmagic/{}.nim".format(name), "w").write(code)
        cmd = "nim {1} --hints:off --app:lib --out:nimmagic/{0}.{2} c nimmagic/{0}.nim".format(name, options, ext)
        cp = sp.run(cmd, shell=True, check=False, encoding="utf8", stdout=sp.PIPE, stderr=sp.PIPE)
        print(cp.stderr)
        if cp.returncode == 0:
            import_exec = "from nimmagic.{} import *".format(name)
            exec(import_exec, glbls)


def load_ipython_extension(ipython):
    ipython.register_magics(NimMagics)
