from Levenshtein import distance
from functools import partial

class BotCommands(list):

    def __init__(self):
        self.commands = dict()

    def processCommand(self, command, *args):

        if command not in self.commands:

            dist = partia(distance, command)
            list(self.commands.keys).sort(dist)