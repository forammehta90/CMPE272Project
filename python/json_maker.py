import json
from random import randint

class json_maker(object):
    def __init__(self):
        self.i = 0

    def prepare(self, dict, cropType):
        options_list = {}
        options_list.update({'key': str(self.i+1)})
        options_list.update({'name': cropType})
        options_list.update({'values': dict})
        self.i += 1
        return options_list