import inspect
import sys
import traceback
import os

DEBUG = True
INFO = True
TRACE = False

class Log(object):
    """
    super intelligent logger, can be used as a class as well as a decorator.
    """

    @staticmethod
    def get_caller_module():
        """
        Get the module object of whoever called the logger.
        """
        mod = None
        for i in range(10):
            frame = inspect.stack()[i]
            mod = inspect.getmodule(frame[0])
            if not mod.__name__ == __name__: 
                break
        return mod
    
    @staticmethod
    def print_message(message, message_type):
        if message_type == "DEBUG":
            if not DEBUG: return
        elif message_type == "INFO":
            if not INFO: return
        elif message_type == "TRACE":
            if not TRACE: return

        caller = Log.get_caller_info()
        print "[{mod}] {message}".format(mod=caller["filename"], message=message)

    @staticmethod
    def info(message):
        """
        Used everywhere, to log every event thats interesting
        """
        Log.print_message(message, "INFO")

    @staticmethod
    def trace(message):
        """
        Used everywhere, to log every event thats interesting
        """
        Log.print_message(message, "TRACE")

    @staticmethod
    def warning(message):
        """
        Used when an event might cause problems later:
        Ex. Disk 85% full
        """
        Log.print_message(message, "WARNING")

    @staticmethod
    def debug(message):
        """
        Used very sparingly, only when trying to debug
        """
        Log.print_message(message, "DEBUG")

    @staticmethod
    def error(message):
        """
        Used to log an error. optionally, you can directly send 
        an Exception instance as the message
        """

        # if message is an exception, get the full traceback as string!!
        if isinstance(message, Exception):
            exc_info = sys.exc_info()
            lines = traceback.format_exception(exc_info[0], exc_info[1], exc_info[2])
            tb_message = "".join(lines)
            message = "%s:\n%s" %(str(message), str(tb_message))

        Log.print_message(message, "ERROR")

    @staticmethod
    def get_caller_info():
        """
        Stalk your caller, and know everything about it
        """
        caller = {}
        mod = Log.get_caller_module()
        
        filepath = mod.__file__
        dirname, filename = os.path.split(filepath)
        # import IPython; IPython.embed()
        filename = filename.split(".")[0]

        caller["module_name"] = mod.__name__
        caller["filepath"] = filepath
        caller["filename"] = filename
        caller["dirname"] = dirname
        return caller
