import json
import sample
import pandas as pd
from pandas import DataFrame

class request_json(object):

    def __init__(self):
        self.cli = sample.sample()
        self.df = pd.read_csv('Texas.csv')
        self.df.columns = [c.lower().replace(' ', '_') for c in self.df.columns]
        self.df['value'] = self.df['value'].apply(pd.to_numeric, errors='coerce')
        

    def analyze(self,st,ct):
        temp=self.df.groupby(['state', 'county']).get_group((st,ct))
        crops = temp.commodity.unique()
        tempjson = {}
        columns = []
        options = []
        columns.append({'key':'yield', 'full_name':'Yield', 'type':'numeric', 'goal':'max'})
        columns.append({'key':'production', 'full_name':'Production', 'type':'numeric', 'goal':'max'})
        columns.append({'key':'acres_harvested', 'full_name':'Acres Harvested', 'type':'numeric', 'goal':'max'})
        columns.append({'key':'acres_planted', 'full_name':'Acres Planted', 'type':'numeric', 'goal':'max'})
        tempjson.update({'subject': 'Plantaplan'})
        tempjson.update({'columns': columns})
        for crop in crops:
            options.append(self.cli.analyze(temp, st, ct, crop.upper()))
        tempjson.update({'options': options})
        return json.dumps(tempjson)

