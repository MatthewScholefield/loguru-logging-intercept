"""Capture Python's stdlib logging messages and route them to loguru"""

import logging
from itertools import chain
from types import FrameType
from typing import cast

from loguru import logger


class InterceptHandler(logging.Handler):
    """Logs to loguru from Python logging module"""

    def emit(self, record: logging.LogRecord) -> None:
        """Route a record to loguru."""
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message...
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1
        logger_with_opts = logger.opt(depth=depth, exception=record.exc_info)
        try:
            logger_with_opts.log(level, "{}", record.getMessage())
        except Exception as e:
            safe_msg = getattr(record, "msg", None) or str(record)
            logger_with_opts.warning(
                "Exception logging the following native logger message: {}, {!r}",
                safe_msg,
                e,
            )


def setup_loguru_logging_intercept(level: int = logging.DEBUG, modules: tuple[str, ...] = ()) -> None:
    """Set up an interceptor routing messages from the root logger and those specified in modules to Loguru.

    Parameters
    ----------
    level : int, optional
        The log level (as defined by Python's standard `logging`). Messages with this
        level or above will be forwarded to Loguru. By default `logging.DEBUG`.
    modules : tuple, optional
        A list of module names whose `logging` messages should be intercepted, by
        default an empty tuple.

    Example
    -------
    >>> setup_loguru_interceptor(modules=("my_module", "your_module.config"))
    """
    logging.basicConfig(handlers=[InterceptHandler()], level=level)  # noqa
    for logger_name in chain(("",), modules):
        if logger_name:
            # undocumented way of getting a logger without creating it:
            mod_logger = logging.Logger.manager.loggerDict.get(logger_name)
        else:
            # root logger is not contained in loggerDict
            mod_logger = logging.getLogger()
        if (mod_logger) and (isinstance(mod_logger, logging.Logger)):
            mod_logger.handlers = [InterceptHandler(level=level)]
            mod_logger.propagate = False
            logger.trace(f"InterceptHandler in place for logger {logger_name}")
        else:
            logger.debug(f"No logger found named {logger_name}")
