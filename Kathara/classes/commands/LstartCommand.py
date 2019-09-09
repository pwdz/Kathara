import argparse

from classes.commands.Command import Command
from classes.parser.LabParser import LabParser
from classes.deployer.Deployer import Deployer


class LstartCommand(Command):
    __slots__ = []

    def __init__(self):
        Command.__init__(self)

        parser = argparse.ArgumentParser(
            prog='kathara lstart',
            description='Starts a Kathara Lab.'
        )

        group = parser.add_mutually_exclusive_group(required=False)

        group.add_argument(
            "-n", "--noterminals",
            action="store_const",
            dest="terminals",
            const=False,
            default=True,
            help='Start the lab without opening terminal windows.'
        )
        group.add_argument(
            "-t", "--terminals",
            action="store_const",
            dest="terminals",
            const=True,
            help='Start the lab opening terminal windows.'
        )
        parser.add_argument(
            '-d', '--directory',
            required=False,
            help='Specify the folder contining the lab.'
        )
        parser.add_argument(
            '-F', '--force-lab',
            dest='force_lab',
            required=False,
            action='store_true',
            help='Force the lab to start without a lab.conf or lab.dep file.'
        )
        parser.add_argument(
            '-l', '--list',
            required=False,
            action='store_true',
            help='Show a list of running container after the lab has been started.'
        )
        parser.add_argument(
            '-o', '--pass',
            dest='options',
            nargs='*',
            required=False,
            help="Pass options to vstart. Options should be a list of double quoted strings, "
                 "like '--pass \"mem=64m\" \"eth=0:A\"'."
        )
        parser.add_argument(
            '--xterm',
            required=False,
            help='Set a different terminal emulator application (Unix only).'
        )
        parser.add_argument(
            '--print',
            dest="print_only",
            required=False,
            action='store_true',
            help='Print commands used to start the containers to stderr (dry run).'
        )
        parser.add_argument(
            '-c', '--counter',
            required=False,
            help='Start from a specific network counter '
                 '(overrides whatever was previously initialized, using 0 will prompt the default behavior).'
        )
        parser.add_argument(
            "--execbash",
            required=False,
            action="store_true",
            help=argparse.SUPPRESS
        )

        self.parser = parser

    def run(self, current_path, argv):
        # TODO ma su netkit non si poteva fare "lstart pc1" e startava solo pc1 del lab?
        args = self.parser.parse_args(argv)

        lab_path = args.directory.replace('"', '').replace("'", '') if args.directory else current_path

        # Call the parser
        lab = LabParser.get_instance().lab_parse(lab_path)

        Deployer.get_instance().deploy(lab)
