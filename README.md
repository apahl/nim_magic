# nim_magic

Nim cell magic for JupyterLab or Jupyter Python Notebooks.

Write Nim modules and use the compiled code directly in the Notebook as extension modules for the Python kernel (similar to e.g. %%cython, but for your favorite language :P ). It builds on @yglukhov 's awesome [nimpy](https://github.com/yglukhov/nimpy) library. 

## Requirements
* A [Nim](https://nim-lang.org) compiler in your path
* [nimpy](https://github.com/yglukhov/nimpy) package (`nimble install nimpy`)

## Installation
Just put the file `nim_magic.py` somewhere in Python's import path, e.g. in one of the dirs that is printed by: `python3 -c "import sys; print(sys.path)"`.

## Example
In a JupyterLab or Jupyter Notebook running a Python3 kernel:

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

Further examples can be found [here](examples.ipynb).

And there are some gists, too:
* [Accelerating Pearson](https://gist.github.com/apahl/d673b0033794cc5f9514de639285592b): Directly accessing Numpy arrays.
