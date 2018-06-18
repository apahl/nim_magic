# nim_magic

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

Have a look at the [example](example.ipynb) for further examples.
