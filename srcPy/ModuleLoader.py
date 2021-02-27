import os
import importlib
from importlib import import_module
from inspect import getmembers, isfunction
from inspect import signature

from dotenv import load_dotenv

load_dotenv()

MODULE_PATH = os.getenv('MODULES')

class ModuleLoader:

    _modules = dict()
    _functions = dict()

    def __init__(self):
        pass

    def reload_all(self):
        for mod in self._modules:
            self._modules[mod.key] = reload(mod.key)
            self._functions[mod.key].clear()
            self._functions[mod.key] = load_funcs(self._modules[mod.key])

    def reload_mod(self, module):
        if module in self._modules:
            try:
                self._modules[module] = importlib.reload(self._modules[module])
            except:
                print(f"Error reloading: {module}")
                return False
        else:
            try:
                self._modules[module] = import_module(MODULE_PATH + module)
            except:
                print(f"Error loading: {module}")
                return False

        # Load in all module functions -- can be dangerous since it does this blindly
        self._functions[module] = self.load_funcs(self._modules[module])
        return True

    def load_funcs(self, module):
        funcs = dict()

        for fun in getmembers(module, isfunction):
            funcs[fun[0]] = fun[1]

        return funcs


    def correctNumArgs(self, func, *args):
        return len(args[0]) == len(signature(func).parameters) -1

    def func_work(self, module, func):
        if module in self._functions:
            if func in self._functions[module]:
                # Get the function described
                return self._functions[module][func]
            else:
                print("No such function {func} in module {module} exists")
        else:
            print(f"Module {module} not found")