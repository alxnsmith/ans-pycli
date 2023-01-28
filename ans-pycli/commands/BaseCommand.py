from argparse import ArgumentParser

from ..helpers import no_function


class Command:
    _name: str = None
    _description: str = None
    _help = None
    _func: callable = None

    def __init__(self,
                 name: str = None,
                 description: str = None,
                 help: str = None,
                 func: callable = None):
        self.set_val("_name", name)
        self.set_val("_description", description, self._help, help)
        self.set_val("_help", help, self._description, description)
        self.set_val("_func", func, no_function)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @classmethod
    def get_val(cls, name: str, *defaults):
        cls_val = getattr(cls, name)
        if cls_val is not None:
            return cls_val
        for default in defaults:
            if default is not None:
                return default
        return None

    def set_val(self, name: str, *defaults):
        setattr(self, name, self.get_val(name, *defaults))

    def init_parser(self, parser: ArgumentParser):
        pass

    @property
    def parser_schema(self):
        return {
            "name": self.name,
            "description": self.description,
            "help": self.help,
        }

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def help(self):
        return self._help

    @property
    def func(self):
        return self._func
