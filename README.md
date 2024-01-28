# Loguru Logging Intercept

[![PyPI - Version](https://img.shields.io/pypi/v/loguru-logging-intercept)](https://pypi.org/project/loguru-logging-intercept) [![PyPI - Downloads](https://img.shields.io/pypi/dm/loguru-logging-intercept)](https://pypi.org/project/loguru-logging-intercept)

*Code to integrate [Loguru](https://github.com/Delgan/loguru) with Python's standard
[logging](https://docs.python.org/3/howto/logging.html) module*

[Loguru](https://github.com/Delgan/loguru) is a great alternative logging library for
Python. However, if you use (potentially external) code that already integrates with
Python's default logger, you'll get a combination of the two logging styles. This code
provides a function that sets up an intercept handler to route calls to Python's
default `logging` module to Loguru.

## Usage

Before calls that use Python's default `logging` module, call the provided
`setup_loguru_logging_intercept()` as shown below:

```python
import logging
from loguru_logging_intercept import setup_loguru_logging_intercept


def main():
    setup_loguru_logging_intercept(
        level=logging.DEBUG,
        modules=("foo", "foo.bar", "foo.baz")
    )
    # Can now call functions from foo that use getLogger(__name__)

...
```

## Installation

Install via `pip`:

```bash
pip3 install loguru-logging-intercept
```
