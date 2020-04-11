from src.PathFinder import PathFinder

"""

UserInterface is responsible for the users input.
And program output.
So its responsible for input and output of the program.

IPO:
Input -> Process -> Output
"""


class UserInterface:
    def __init__(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node
        while True:
            self._input()
            self._process()
            self._output()
            # TODO safe results!

    def _check_percentage_extension(self):
        return self.percentage_extension > 0

    # INPUT
    def _input(self):
        input_prompt = "Bitte geben sie die maximale prozentuale Verlängerung ein!"
        self.percentage_extension = int(input(input_prompt))
        if not self._check_percentage_extension():
            self._input()

    # PROCESS
    def _process(self):
        pf = PathFinder(self.start_node, self.end_node)
        pf.start()
        self.result = pf.get_path_least_turn_offs(self.percentage_extension)

    # OUTPUT
    def _output(self):
        print(self.result)