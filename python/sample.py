#Load data and parse date columnPython

import pandas as pd
import json
import json_maker

class sample(object):
    def __init__(self):
        self.cli = json_maker.json_maker()

    def analyze(self, temp, stateName, countyName, cropName):
        acres_harvested = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & temp['data_item'].str.contains('ACRES HARVESTED')]
        acres_planted = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & temp['data_item'].str.contains('ACRES PLANTED')]
        production = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & temp['data_item'].str.contains('PRODUCTION')]
        yield_measured = temp[ (temp.commodity == cropName) & (temp.state == stateName) & (temp.county == countyName) & temp['data_item'].str.contains('YIELD')]
        list = {}
        list.update({'acres_harvested': acres_harvested.value.mean()})
        list.update({'acres_planted': acres_planted.value.mean()})
        list.update({'production': production.value.mean()})
        list.update({'yield': yield_measured.value.mean()})
        a = self.cli.prepare(list, cropName)
        return a