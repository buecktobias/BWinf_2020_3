from src.paths.PathFinder import PathFinder
from src.IO import Input
"""

UserInterface is responsible for the users input.
And program output.
So its responsible for input and output of the program.

IPO:
Input -> Process -> Output
"""


class UserInterface:
    def __init__(self):
        self.start_node = None
        self.target_node = None
        self.graph = None
        while True:
            self._input()
            self._process()
            self._output()
            # TODO safe results!

    def _check_percentage_extension(self):
        return self.percentage_extension > 0

    # INPUT
    def _input(self):
        file_prompt = "Bitte geben Sie den Dateinamen ein, welchen Sie einlesen wollen!"

        file_name = str(input(file_prompt))
        file_input = Input.Input()
        start_node, target_node = file_input.create_graph(file_name)
        self.start_node = start_node
        self.target_node = target_node
        self.graph = file_input.graph

        input_prompt = "Bitte geben sie die maximale prozentuale Verlängerung ein!"
        self.percentage_extension = int(input(input_prompt))
        if not self._check_percentage_extension():
            self._input()

    # PROCESS
    def _process(self):
        pf = PathFinder(self.start_node, self.target_node)
        pf.start()
        self.result = pf.get_path_least_turn_offs(self.percentage_extension)

    # OUTPUT
    def _output(self):
        print(self.result)