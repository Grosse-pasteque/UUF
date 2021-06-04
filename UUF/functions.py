from .constants import function, alltypes
from .classes import LenghtError
from string import printable
from re import fullmatch
from random import randint, uniform
import os


# function used by other function who are imported those can't be used ! and are not imported.
def CheckTypeError():
    raise TypeError(
        f"type(variables and types) need to be list and type(reseerror): bool !")
def CheckLenghtError(var1, var2):
    raise LenghtError(
        f"len({var1}) need to be == to len({var2}) !")

def randfloat(a, b, c):
    return round(uniform(a, b), c)

def dicttreeview(path: str):
    treeview = {}
    base = ""
    for root, dirs, files in os.walk(path):
        root = root.replace(path, '')
        if root != '':
            root = root[1:]
            for i in root.split(os.sep): base += f"['{i}']"
            exec("treeview%s = {}"%base)
            exec(f"treeview{base}['files'] = {files}")
            base = ""
    return treeview

# type checking function
def CheckType(variables: list, types: list, raiseerror=True):
    if isinstance(variables, list) and isinstance(types, list) and isinstance(raiseerror, bool):
        if len(variables) == len(types):
            for key in range(len(variables)):
                if str(type(variables[key])) not in str(types[key]):
                    if raiseerror:
                        raise TypeError(
                            "type of: {}, need to be: {}".format(variables[key], str(types[key]).replace("<class '", '').replace("'>", '')))
                    return False
            return True
        CheckLenghtError('variables', 'types')
    CheckTypeError()

# format checking function
class _Pattern:
    def __init__(self): pass
    def __call__(self, variables: list, patterns: list, maxseprange=999, raiseerror=True):
        if isinstance(variables, list) and type(patterns) == list and isinstance(raiseerror, bool):
            if len(variables) == len(patterns):
                for key in range(len(variables)):
                    # pattern and variable type() compiler
                    pattern = ReCompile(str(patterns[key])).replace(str(int), r'.[0-9]{0,%d}' % maxseprange).replace(str(float), r'.[0-9]{0,%d}\.[0-9]{0,%d}' % (maxseprange, maxseprange)).replace(str(str), r'(.*){0,%d}' % maxseprange).replace(str(list), r'\[(.*){0,%d}\]' % maxseprange).replace(str(dict), r'\{(.*){0,%d}\}' % maxseprange).replace(str(tuple), r'\((.*){0,%d}\)' % maxseprange)
                    for i in alltypes: pattern = pattern.replace(str(i), r'(.*){0,%d}' % maxseprange)
                    pattern = fr"^{pattern.replace(' ', '')}$"
                    variable = str(variables[key]).replace(' ', '')

                    if not fullmatch(pattern, variable):
                        if raiseerror:
                            raise TypeError(
                                "pattern of: {}, need to fullmatch: {}".format(
                                    variables[key], patterns[key].replace("<class '", '').replace("'>", '')))
                        return False
                return True
            CheckLenghtError('variables', 'patterns')
        CheckTypeError()
Pattern = _Pattern()


# unpacking all elements of variable
def Unpack(variable):
    if not '{' in str(variable) or not '}' in str(variable):
        return str(variable).replace('[', '').replace('(', '').replace(']', '').replace(')', '').replace('"', '').replace("'", '').split(', ')
    raise KeyError(
        "dict aren't supported in this function !")

# change all things that can compromise re.fullmatch from running: with \{char}, (\=escape character)
def ReCompile(value: str):
    return r"{}".format(value.replace('[', '\[').replace('(', '\(').replace('{', '\{').replace(']', '\]').replace(')', '\)').replace('}', '\}').replace('.', '\.').replace('+', '\+').replace('*', '\*').replace('$', '\$').replace('?', '\?').replace('^', '\^').replace('|', '\|'))


# function to make error raising easier
def LineNumberError(error):
    return error.__traceback__.tb_lineno

def LineTextError(error, file):
    with open(file, 'r') as f: lines = f.readlines()
    return lines[LineNumberError(error) - 1].replace('\n', '').replace(' '*4, '')

def BasicErrorMessage(error, file):
    return f'''\n  File "{file}", line {LineNumberError(error)}\n  \t{LineTextError(error, file)}'''