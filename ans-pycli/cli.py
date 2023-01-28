import argparse

from .commands import (
    DevCommand,
)


class CLI:
    _DEBUG = False
    _description = "PyCli is a CLI for your Python project"
    __commands = [
        DevCommand(),
    ]

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self._description)
        self.subparsers = self.parser.add_subparsers(title="commands")

        self.parser.add_argument(
            "args", nargs="*", help="Arguments for the command")
        self.init_commands()

    def init_commands(self):
        for cmd in self.__commands:
            command_parser = self.subparsers.add_parser(**cmd.parser_schema)
            cmd.init_parser(command_parser)

    def run(self):
        args = self.parser.parse_args()
        res = args.func()
        if self._DEBUG:
            print('Args: \n', args)
            print('Result: \n', res)
