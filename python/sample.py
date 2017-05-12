#Load data and parse date columnPython

import numpy as np
import pandas as pd
import json
import json_maker

class sample(object):
    def __init__(self):
        self.data = pd.read_csv('barley_data.csv')
        self.data['Value'] = self.data.Value.str.replace(',','').astype(float)
        self.cli = json_maker.json_maker()

    def analyze(self, countyName, cropName):
        self.data.columns = [c.lower().replace(' ', '_') for c in self.data.columns]
        acres_harvested = self.data[ (self.data.commodity == cropName) & (self.data.county == countyName) & ('ACRES HARVESTED' in str(self.data.data_item))]
        acres_planted = self.data[ (self.data.commodity == cropName) & (self.data.county == countyName) & ('ACRES PLANTED' in str(self.data.data_item))]
        production = self.data[ (self.data.commodity == cropName) & (self.data.county == countyName) & ('PRODUCTION, MEASURED IN BU' in str( self.data.data_item))]
        yield_measured = self.data[ (self.data.commodity == cropName) & (self.data.county == countyName) & ('YIELD, MEASURED IN BU / ACRE' in str(self.data.data_item))]
        list = {}
        list.update({'acres_harvested': acres_harvested.value.mean()})
        list.update({'acres_planted': acres_planted.value.mean()})
        list.update({'production': production.value.mean()})
        list.update({'yield': yield_measured.value.mean()})
        a = self.cli.prepare(list, cropName)
        return a