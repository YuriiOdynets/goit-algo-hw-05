#input decorator for all functions in processing.py file
def input_error(add_contact):
    def inner(*args, **kwargs):
        try:
            return add_contact(*args, **kwargs)
        except ValueError:
            return 'Enter the argument for the command (ValueError)'
        except IndexError:
            return 'Enter the argument for the command (IndexError)'
        except KeyError:
            return 'Enter the argument for the command (KeyError)'
    return inner