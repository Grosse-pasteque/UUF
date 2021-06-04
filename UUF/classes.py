### class error ###
class LenghtError(Exception): pass
class InvalidConfigError(Exception): pass
class CharError(Exception): pass
class IntValueError(Exception): pass
class TooBigValueError(Exception): pass

### class custom ###
class ErrorData:
    def __init__(self, Errors: dict):
        if isinstance(Errors, dict):
            self.Errors = Errors.copy()
    def __getitem__(self, item):
        if item in list(self.Errors.keys()):
            return str(self.Errors[item])
        raise AttributeError(
            f"{error} doesn't exist in error data !")