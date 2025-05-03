<div align = "center">

# Python Useful Wrappers/Decorators

```{eval-rst}
.. attention::
  Source Code: `GH/pydry <https://gist.github.com/ZenithClown/df4391a8b0313eb808e9a0f4ef5c78ad>`_
```

</div>

<br>

<div align = "justify">

**PyDRY** (Python's "Don't Repeat Yourself" Tools) is a software development principle that encourages developers (like
me) to avoid duplication of code in a system. To effectively understand and use this principle in python coding context
one might need the use of advanced powerful tools that makes the code cleaner, more resuable and easier to manage. The
**`pydry`** is module is developed to simulate such a scenario. Below are some of the use cases that were designed to
be simple and efficient and provide extensions to other developed functions and code-blocks.

## Python Decorators

A decorator in python is a powerful tool that allows to modify the behavior of a function or a class by wrapping another
method that extends its behavior without permanently modifying it.

### Time Decorators

```{eval-rst}
.. automodule:: timer_decorator
  :members:
  :undoc-members:
  :show-inheritance:
```

## Context Managers

An advanced python tool - a context manager defines the runtime context (or behavior) for executing a code within a
**`with`** statement. Typical example of a context manager is:

```python
with open(filename, "r") as f:
  ... # do something
```

In the above statement, we use the context manager `open` to interact with a file and auto close the file without the
need of explicit `.close()` method on the open file [(more information)](https://stackoverflow.com/q/3012488/6623589).

### Time Context Manegers

```{eval-rst}
.. automodule:: context_managers
  :members:
  :undoc-members:
  :show-inheritance:
```

</div>
