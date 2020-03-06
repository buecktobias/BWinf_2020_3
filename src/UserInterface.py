from src.PathFinder import PathFinder


class UserInterface:
    def __init__(self, start_node, end_node):
        self.percentage_extension = int(input("Bitte geben sie die maximale prozentuale Verlängerung ein!"))
        pf = PathFinder(start_node, end_node)
        pf._start()
        print(pf.get_path_least_turn_offs(self.percentage_extension))
