from argparse import ArgumentParser

from ..BaseCommand import Command


class TestCommand(Command):
    _name = "test"
    _description = "Test command"
    @staticmethod
    def _finc(): print("Test command")


class DevCommand(Command):
    _name = "dev"
    _description = "Provide development commands"

    @classmethod
    def init_parser(self, parser: ArgumentParser):
        subparsers = parser.add_subparsers(title="commands")

        # command_parser = subparsers.add_parser(
        #     "test", help="Test command", description="Prints test message")
        command_parser = subparsers.add_parser(**TestCommand().parser_schema)
        command_parser.set_defaults(func=TestCommand)
